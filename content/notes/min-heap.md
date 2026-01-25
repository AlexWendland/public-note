---
aliases:
  - max-heap
created: 2023-09-29
date_checked:
draft: false
last_edited: 2026-01-21
tags:
  - programming
title: Min-heap
type: data structure
---

A min-heap is a complete binary tree T (i.e. all layers other than the bottom are full).
Each node $x \in T$ in this tree is associated with a value of your heap $v_x$.
This tree obeys the min-heap property:

- For all nodes $x \in T$ in the tree if they have a parent $p \in T$ then $v_x \geq v_p$.

This means the root node is the smallest value in the heap.

> [!note] Max-heap
> You can use what is above to make a max-heap by just inverting the comparison.
> I.e. the top of the heap is the maximum value.

# Implementation

Heaps are normally implemented as arrays.
Where the tree structure is implied by a value's position within the array.
e.g. [1, 2, 3, 4, 5, 6] would give the following tree.
```
layer 0:      1
             / \
layer 1:   2     3
          / \   /
layer 2: 4   5 6
```
A node on layer $i$ with position $0 \leq j < 2^i$ would be in array position $2^i + j - 1$ (0 indexed).

Alternatively, using 0-indexed positions:
- Parent of node at index $i$: $\lfloor (i-1)/2 \rfloor$
- Left child of node at index $i$: $2i+1$
- Right child of node at index $i$: $2i+2$

# Operations

## Create

Cost: $O(n)$

This takes an array and returns a heap with the given property.
Here we take any array as is and starting from the lowest node with children, work our way up the tree ensuring the heap is sorted correctly.

The key insight for linear time complexity: we process fewer nodes at higher levels (which require more swaps), but many more nodes at lower levels (which need fewer swaps). This balance yields $O(n)$ rather than $O(n \log n)$.

In a tree of depth $d := \lfloor \log_2(n) \rfloor$ each node we consider at layer $l$ we only need to consider $d-l$ swaps - as the new root node gets swapped down to the correct depth.
This takes the following number of operations:
$$
\begin{align*}
\sum_{l=0}^{d-1} 2^l (d-l) & \leq \sum_{l=0}^{d-1} \frac{2^d (d-l)}{2^{d-l}}\\
& \leq \sum_{h=0}^{d-1} n \frac{h}{2^h} & \mbox{where } h = d-l\\
& \leq 2n & \mbox{as } \sum_{h=0}^{\infty} \frac{h}{2^h} = 2
\end{align*}
$$

## Insert

Cost: $O(\log_2(n))$

Append the element to the end of the array and then bubble this element up through the tree.
As the depth of the tree is at most $\log_2(n)$ it takes that many swaps.

## Remove root

Cost: $O(\log_2(n))$

Swap the root element with the last element of the tree and contract its size by 1.
Then bubble that element down through the tree.
