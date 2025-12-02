---
aliases:
checked: false
created: 2023-11-03
draft: false
last_edited: 2023-11-11
title: Clique of a given size problem is in NP
tags:
  - programming
  - graph-theory
type: lemma
---
# Statement

> [!important] Lemma
> [Clique of a given size problem](clique_of_a_given_size_problem.md) is in [NP](nondeterministic_polynomial_time_(np).md).

# Proof

This problem is in the form of a [search problem](search_problems.md) as either you provide a [clique](clique_(graph).md) of the required size or you say no such set exists.

For a [undirected graph](graph.md) $G = (V,E)$, positive integer $g > 0$, and supposed solution $S$ to the [Clique of a given size problem](clique_of_a_given_size_problem.md). It takes $O(\vert E \vert + \vert V \vert)$ to check this solution. We have to do two steps:
- Check $\vert S \vert \geq g$.
- Check for all $(u,v) \in E$ for all $u,v \in S$.
The first step takes $O(\vert V \vert)$ and the second $O(\vert V \vert^2)$.

Therefore this problem is in [NP](nondeterministic_polynomial_time_(np).md).
