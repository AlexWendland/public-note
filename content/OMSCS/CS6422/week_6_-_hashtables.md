---
aliases:
course_code: CS6422
course_name: Database Systems Implementations
created: '2026-06-16'
date_checked: '2026-06-16'
draft: true
last_edited: '2026-06-16'
tags:
  - OMSCS
title: Week 6 - Hash Tables
type: lecture
week: 6
---

Within our database we will need a way to index data within our tables.
Here we go over the standard C++ implementations of a hash table then cover a manual implementation.

# C++ Implementations

There are two main implementations of a hash table in C++.

## std::map

Map stores items in a balanced binary search tree (red-black tree).

![Ordered map](/images/c++_ordered_map.png)

This has the following run times:

- Look up: $O(\log n)$

- Insert: $O(\log n)$

- Delete: $O(\log n)$

## std::unordered_map

Unordered map stores items in a hash table.
This uses the hash of the key to find the associated value.
We will cover the details of this later.
This has the following run times:

- Look up: $\Theta(1)$ expected, $O(n)$ worst case.

- Insert: $\Theta(1)$ expected, $O(n)$ worst case.

- Delete: $\Theta(1)$ expected, $O(n)$ worst case.

# Custom Implementation

When using the hash table in BuzzDB we will use a `HashIndex`.
This could simply wrap the `std::unordered_map`, like below.

```cpp
class HashIndex {
private:
  std::unordered_map<int, int> index;
public:
  void insertOrUpdate(int key, int value) {
    index[key] = value;
  }

  int getValue(int key) const {
    auto it = index.find(key);
    return it != index.end() ? it->second : -1;
  }
};
```

However, we would like to use a custom structure to understand better how this would work.

## Building a Hash Table

To make a hash table we use a fixed-sized array N and a hash function $hash: D \rightarrow [0,N)$ that takes our key values and outputs a number between 0 and N-1.
The elements of our array are structs such as the following:

```cpp
struct HashEntry {
  Key key;
  Value value;
  int position;
  bool empty;
};
```

The position of that element in our hash table is then $hash(key)$.
To retrieve or insert the value we first hash it to find its position and then check there.

If we have a collision (i.e., $d_1, d_2 \in D$ such that $hash(d_1) = hash(d_2)$), then we use linear probing to find the next empty space.
If $hash(d_2)$ has the struct for $d_1$'s value and we want to insert $d_2$, then we look at $(hash(d_2) + k) \bmod N$ for ever-increasing $k$ until we find a space to insert it.
For retrieval we then do exactly the same walk until we find the slot with the key of the given key.

However, this causes us a problem if we need to delete a key — to preserve all these walks we would need to rehash all the keys again.
To get around this we soft delete the keys by using the empty boolean.

## Improving collisions

The linear scans cause a massive bottleneck within the hash table design.
If multiple keys stack up they block a whole region of the slots, which causes multiple near-linear scans.
There are two solutions to this.

### Quadratic probing

When keys start to stack up they don't only block the key that started the pile up but the keys after.
To alleviate this we change the probing scheme to use the key start point to differentiate keys probing paths.
This is as simple as switching from looking up keys with $(hash(key) + k) \bmod N$ to using $(hash(key) + k^2) \bmod N$.

The issue with Quadratic probing is we can still have a single entry buildup.
I.e. if multiple keys hash to the same value this will still cause a blockage.

### Double hashing

To get around the issue with quadratic probing we use a second hash function.
So let us assume we have two hash functions $hash_1, hash_2: D \rightarrow [0,N)$ that are different from one another.
We use $hash_1$ as above.
However, for probing we instead look at $(hash_1(key) + k \cdot hash_2(key)) \bmod N$.
This use of the double hash means even if elements are the same in the first hash, their probe path will be different due to the use of the second hash.

## Position tracking

For debugging the hash table it is useful to track the position the key ended up in within the struct as well.
Therefore upon insertion we add this as well.

## Putting it all together

Below we use the double hashing implementation and show this all together.

```cpp
int hash_1(Key key);
int hash_2(Key key);

struct HashEntry {
  Key key;
  Value value;
  int position;
  bool empty = true;
};

class HashIndex {
private:
  int size;
  HashEntry* hash_table;
public:
  HashIndex(int size) : size(size), hash_table(new HashEntry[size]) {}

  void insert(Key key, Value value) {
    for (int round = 0; round < size; round++) {
      int position = (hash_1(key) + round * hash_2(key)) % size;
      if (hash_table[position].empty) {
        hash_table[position].key = key;
        hash_table[position].value = value;
        hash_table[position].position = position;
        hash_table[position].empty = false;
        return;
      }
    }
  }

  void remove(Key key) {
    for (int round = 0; round < size; round++) {
      int position = (hash_1(key) + round * hash_2(key)) % size;
      if (hash_table[position].empty)
        break;
      if (hash_table[position].key == key) {
        hash_table[position].empty = true;
        return;
      }
    }
  }

  Value *get(Key key) {
    for (int round = 0; round < size; round++) {
      int position = (hash_1(key) + round * hash_2(key)) % size;
      if (hash_table[position].empty)
        break;
      if (hash_table[position].key == key)
        return &hash_table[position].value;
    }
    return nullptr;
  }
};
```
