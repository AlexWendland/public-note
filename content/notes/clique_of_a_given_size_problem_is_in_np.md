---
aliases:
created: 2023-11-03
date_checked: 2026-01-28
draft: false
last_edited: 2026-01-28
tags:
  - programming
  - graph-theory
title: Clique of a given size problem is in NP
type: lemma
---
# Statement

> [!lemma] Lemma
> [Clique of a given size problem](clique_of_a_given_size_problem.md) is in [NP](nondeterministic_polynomial_time_(np).md).

# Proof

This problem is in the form of a [search problem](search_problems.md) as either you provide a [clique](clique_(graph).md) of the required size or you say no such set exists.

For an [undirected graph](graph.md) $G = (V,E)$, positive integer $g > 0$, and supposed solution $S$ to the [Clique of a given size problem](clique_of_a_given_size_problem.md). It takes $O(\vert V \vert^2)$ to check this solution. We have to do two steps:
- Check $\vert S \vert \geq g$.
- Check that for all $u,v \in S$, $(u,v) \in E$.
The first step takes $O(\vert V \vert)$ and the second $O(\vert V \vert^2)$.

Therefore this problem is in [NP](nondeterministic_polynomial_time_(np).md).
