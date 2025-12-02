---
aliases:
checked: false
course_code: CS6215
course_name: Introduction to Graduate Algorithms
created: 2023-10-01
draft: false
last_edited: 2023-11-11
tags:
  - OMSCS
title: Week 6 - Minimum Spanning Tree
type: lecture
week: 6
---

[Statement](../../general/minimum_spanning_tree_problem_(mst).md#statement)

# Tree properties

It is useful to remind ourselves of some [tree](../../general/tree_(graph).md) properties:

1. Tree on $n$ vertices has $n-1$ edges.
2. In a tree, there is exactly one path between every pair of vertices.
3. Any connected $G = (V,E)$ with $\vert E \vert = \vert V \vert - 1$ is a tree.

These are all proved by the [equivalent tree definitions](../../general/equivalent_tree_definitions.md).

# Greed is good ... in this case

The greedy approach of just starting with an empty graph and keep adding valid edges of minimum weight, solves the [MST](../../general/minimum_spanning_tree_problem_(mst).md) problem.

The only problem is keeping track of the edges that are valid to include.

# Kruskal's Algorithm

[Pseudocode](../../general/kruskal's_algorithm.md#pseudocode)

[Run time](../../general/kruskal's_algorithm.md#run-time)

[Correctness](../../general/kruskal's_algorithm.md#correctness)

So the only think left to prove [Kruskal's algorithm](../../general/kruskal's_algorithm.md) is correct is the proof of the cut property.

[Cut property](../../general/cut_property.md)

# Prim's algorithm

[Algorithm](../../general/prim's_algorithm.md#algorithm)

[Correctness](../../general/prim's_algorithm.md#correctness)
