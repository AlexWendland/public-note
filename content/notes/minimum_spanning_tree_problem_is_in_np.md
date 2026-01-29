---
aliases:
created: 2023-11-02
date_checked: 2026-01-29
draft: false
last_edited: 2025-12-05
tags:
  - maths
title: Minimum Spanning Tree problem is in NP
type: lemma
---
# Statement

> [!lemma] Lemma
> [Minimum Spanning Tree problem (MST)](minimum_spanning_tree_problem_(mst).md) is in [NP](nondeterministic_polynomial_time_(np).md)

# Proof

The problem is in the correct form for a [search problem](search_problems.md). It outputs a [MST](minimum_spanning_tree_problem_(mst).md) always as one always exists from the definition.

To verify a solution, we can first check it is a spanning tree by running [BFS](breadth-first_search_(bfs).md) to verify it is connected and checking the size of the edge set is $|V| - 1$ to check it is a tree. To check it is minimal, we can find a solution in polynomial time using [Kruskal's algorithm](kruskal's_algorithm.md). We can then check its weight versus the weight of the proposed solution to verify they match.

