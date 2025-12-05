---
aliases:
checked: false
created: 2023-11-03
draft: false
last_edited: 2025-12-05
tags:
  - programming
title: Independent set of a given size is in NP
type: lemma
---
# Statement

> [!lemma] Lemma
> [Independent set of a given size](independent_set_of_a_given_size.md) is in [NP](nondeterministic_polynomial_time_(np).md).

# Proof

This problem is in the form of a [search problem](search_problems.md) as either you provide an [independent set](independent_set_(graph).md) of the required size or you say no such set exists.

For a [undirected graph](graph.md) $G = (V,E)$, positive integer $g > 0$, and supposed solution $S$ to the [Independent set of a given size](independent_set_of_a_given_size.md). It takes $O(\vert E \vert + \vert V \vert)$ to check this solution. We have to do two steps:
- Check $\vert S \vert \geq g$.
- Check for all $(u,v) \in E$ that $u \not \in S$ or $v \not \in S$.
The first step takes $O(\vert V \vert)$ and the second $O(\vert E \vert)$.

Therefore this problem is in [NP](nondeterministic_polynomial_time_(np).md).
