---
aliases:
  - B-tree
created: 2026-01-21
date_checked: 2026-01-25
draft: false
last_edited: 2026-01-21
tags:
  - computer science
title: B-tree
type: definition
---

A B-tree is a self-balancing tree data structure that maintains sorted data.
(Note: The B here is for balanced, not for binary - B-trees can have more than two children per node.)
A B-tree of order $m$ is a tree that satisfies the following properties:

- Every node has at most $m$ children.

- Every node other than the root and leaves has at least $\lceil m/2 \rceil$ children.

- The root has at least two children unless it is a leaf.

- All leaves appear on the same level.

- A non-leaf node with $k$ children contains $k-1$ keys.

Each leaf node contains one or more keys (the actual data being stored).
Internal nodes contain separator keys that guide the search: they partition the key space among their child subtrees.
For example, if an internal node has separator key $k$, its left subtree contains keys less than $k$, and its right subtree contains keys greater than or equal to $k$.

# Operations

## Search

Cost: $O(\log_m(n))$ where the tree height is $O(\log_m(n))$.

Search works like any search tree: starting from the root, compare your search value with the separator keys in each internal node to determine which child subtree to descend into, until you reach a leaf.

## Insert

Cost: $O(\log_m(n))$

To insert an element into the B-tree, first find the appropriate leaf node by searching from the root (just like search).
Then what happens depends on the state of that leaf node:

1. If the leaf node contains fewer than the maximum number of keys (m-1): insert the new key into this leaf.

2. Otherwise, the node is full and we need to split it into two nodes:

   - Pick the median key from this node and split the keys into two nodes around it.

   - Promote the median key up to the parent node as a new separator.

   - If the parent now has too many children (more than $m$), split the parent recursively following the same process.

   - If splitting propagates to the root, create a new root with two children (this increases the tree height by 1).

## Delete

Cost: $O(\log_m(n))$

First, search for and remove the key from its leaf node.
After removal, we may need to rebalance if the node has too few keys:

1. **If the key being deleted is used as a separator in an internal node**: Replace it with the predecessor or successor key from an adjacent leaf node.

2. **If deletion causes a node to have fewer than $\lceil m/2 \rceil - 1$ keys** (violating the minimum), we must rebalance:

   - **Try borrowing from siblings**: Check if a sibling node (sharing the same parent) has more than the minimum number of keys. If so, rotate keys through the parent to redistribute them.

   - **Otherwise, merge nodes**: If siblings are at minimum capacity, merge this node with a sibling. This removes a separator key from the parent.

   - **Propagate upward**: If the parent now has too few children (fewer than $\lceil m/2 \rceil$), recursively apply the same rebalancing logic to the parent.

   - **Handle root underflow**: If the root ends up with only one child after merging, remove the root and promote its single child to become the new root (this decreases tree height by 1).
