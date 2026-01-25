---
aliases:
created: 2023-09-27
date_checked:
draft: false
last_edited: 2025-12-05
tags:
  - maths
title: Cycles in a graph via the DFS tree
type: lemma
---
> [!lemma] Lemma
> A [directed graph](directed_graph.md) $G$ has a cycle if and only if its [DFS tree](dfs_tree_(algorithm).md) has a back edge.

## Proof

Suppose we have a graph $G = (V,E)$ and some run of a [DFS](depth-first_search_(dfs).md) algorithm $A$ that forms [DFS tree](dfs_tree_(algorithm).md) $T = (V, E')$.

### $\Rightarrow$

Suppose it has some cycle $x_1, x_2, \ldots x_n$ where $x_i \in V$ and $(x_i, x_{i+1}), (x_n, x_1) \in E$. Then some vertex $x_k$ must have been discovered first by $A$.

All other vertices $x_i$ must be below $x_k$ and contained in its branch. Therefore $x_{i-1}$ is contained in its branch with edge $(x_{i-1}, x_i)$ giving the desired [back edge](dfs_tree_(algorithm).md).

### $\Leftarrow$

Suppose we have some back edge $(a, b) \in E$. By the definition of back edge $(a,b) \not \in E'$ but $a$ and $b$ are in the same branch in $T$.

Therefore there are edges $e_1, \ldots e_n$ connecting $b$ to $a$ in $T$ making $e_1, \ldots, e_n, (a,b)$ a cycle.
