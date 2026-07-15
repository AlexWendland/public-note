---
aliases:
course_code: CS6422
course_name: Database Systems Implementations
created: '2026-06-19'
date_checked:
draft: false
last_edited: '2026-06-19'
tags:
  - OMSCS
title: Week 8 - B+tree
type: lecture
week: 8
---

With a database there are two kinds of queries.

- Point queries - 'Get me person named Alex'

- Range queries - 'Get me all the children between 10 and 18 years old'

Hash tables for indexes work great for point queries.
The execute in $\Theta(1)$ time as we just look for the key Alex.
However, they struggle at 'range queries'.
Here, there is nothing we can really do other than iterate through the keys.
The solution to this is to use an ordered index - which in this course we implement as a B+ tree.

# B+ tree

A B+ tree is a balanced tree where each node can have at most some fixed number $F$ of children - called the fan out.
This means the hight of the tree is always $\ciel \log_F(n) \ciel$.
The keys for the values in the nodes must be linearly order.
The tree has two kinds of nodes - internal nodes and leaf nodes.

The internal nodes hold two data structures, $F$ pointers to other nodes and $F-1$ 'dividers'.
If you are querying for value $v$ the dividers tell you which next node to follow by checking $d_{i-1} < v \leq d_i$ then go to node $i$.

The leaf nodes hold the actual values.
This means that they contain two data structures, the first holding the key and the second a pointer to the tuple.
The leaf nodes also contains a reference to the next right (increase) leaf node.
This is so range queries can find the lower bound and then progress up through the index until the hit the upper bound.

> [!note] Normal fanout values
> Normally, the number of children is about 500 meaning that by a hight of 3 we can already support more than 100 million keys.

## Point query

Given a key $k$ we can recursively find it.
Starting at the root node:

1. Iterate through the dividers, if we find $d_i$ such that $d_{i-1} < k \leq d_{i}$ then iterate on node $n_i$.

2. Else, we go to node $n_{max}$.

This can be followed on all internal nodes.
When we reach a leaf node then we find the key and return the associated value.

## Range query

Given we want to find all keys between $k_{low}$ and $k_{high}$ then we:

1. Run a point query on $k_{low}$.

2. Iterate through the keys from $k_{low}$ using the next node pointer.

3. We stop when we hit $k_{high}$.

## Node splitting

We may find a leaf/internal node gets full - in this case we break it into two nodes.
For a leaf node we split it along the middle key value.
Once we have done the split we add a divider (the middle key value) to the internal node above for the splitting value and add the new node to the children.
Note that for leaf splits the middle key is **copied up** - it remains in the leaf node as actual data still needs to be accessible there.

We perform a similar pattern with internal nodes.
If we need to add a divider but we are already at the max fanout then we split ourselves into two nodes along the middle divider.
Attaching the new node to the parent and making it add a new divider as well.
For internal node splits the middle divider is **pushed up** - it moves to the parent and is not kept in either child, since internal nodes only hold routing information.

If we need to split the root node, then we just create two new children and hand off the children of the old root node between them.
With replacing the dividers and children of the old root with these two children and the divider being the max value in the lower child.

## Inserting/updating key-value

We can use node splitting to insert a key-value pair.

1. We run a point query on the key and update the entry with the new value if the key is found.

2. If the key is not found then we insert this key-value pair into the node that was located.

3. If the node is full then we split it, and propagate that change.

4. This can increase the depth of the tree if the fullness goes all the way to the root.

> [!note] Bulk loading
> This can be inefficient if we bulk insert sorted data, so it can be more efficient to manually implement bulk insertion to get the tree more saturated.

## Deleting a key-value

We can remove a key-value pair by finding the node that contains the key and then removing the key-value pair from the node.

If we delete the last entry in a leaf node, the node becomes empty and must be removed entirely.
We remove it from the linked list of leaf nodes by updating its left sibling's next pointer.
We also remove the corresponding divider and child pointer from the parent internal node.
If this in turn empties the parent, the same process applies recursively up the tree.
If the root ends up with only one child, that child becomes the new root and the tree shrinks in height.

## Aside: Templates in C++

Templates in C++ allow the use of generic types, for example:

```cpp
template <typename T> T add(T a, T b) { return a + b; }

int result = add<int>(1, 2);
float result = add<float>(1.0, 2.0);
```

This defines a generic function `add` which can be given a type `T` which then can run on any type `T`.

We use it for B+tress by providing a generic `Key` and `Value` type.


```cpp
template <typename Key, typename Value> class BPlusTree {
  ...
}
```

In the case of B+tree we can support various indexing methods by using custom structs with overloaded comparison operators.

```cpp
struct CustomKey {
  int field1;
  int field2;

  bool operator<(const CustomKey& other) const {
    // field1 is the primary key, with secondary key field2
    if (field1 == other.field1) {
     return field2 < other.field2;
    }
    return field1 < other.field1;
  }
};
```

## On disk representation

Building index's within a database can take a long time.
Therefore, without our index being on-disk each time we restart our database application we would need to rebuild all the indices.
So, similarly to pages in our database we implement something similar for our B+ tree.

The main trick to this is:

- Aligning the size of nodes with the disks block size.

- Replacing pointers with offsets within a index file.

Then whenever we would in-memory have a object pointer, replace this with the index of the node on disk.
Then we can write a serialise/deserialise method for these nodes into this file to go at the file offset.

```cpp
struct DiskNode {
  Key keys[MAX_FANOUT]; // Either the divders or the key associated to the value.
  Value values[MAX_FANOUT]; // For leaf nodes
  uint32_t children[MAX_FANOUT]; // For internal nodes
  uint32_t next;
  bool is_leaf;
  uint32_t key_count; // Helps with serialisation
};

std::vector<uint8_t> serializeNodeToBytes(const DiskNode &node);
void deserializeNodeFromBytes(const std::vector<uint8_t> &buffer, DiskNode &node);
```

To align the `DiskNode` with a disk block we need to calculate the size of the node:

- Keys: This is determined by the type of key.

- Values: This is determined by the type of value.

- Children: 4 bytes per child.

- Next Pointer: 4 bytes.

- Is Leaf: 1 byte.

- Key Count: 4 bytes.

This case then give us our fanout size.
For example if the Key/Value are 4 byes each with a 4kB page then the nodes will have max size:

$$
4m + 4m + 4 + 1 + 4 = 8m + 9 (= 4 \cdot 2^10)
$$

That gives around $2^9 - 2 = 510$ nodes.
However, using larger SSD pages of 16kB gives us larger values - around 2046 nodes.



