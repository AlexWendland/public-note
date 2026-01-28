---
aliases:
created: 2023-11-03
date_checked: 2026-01-28
draft: false
last_edited: 2026-01-28
tags:
  - programming
  - graph-theory
title: Vertex cover of a given size is NP
type: lemma
---
# Statement

> [!lemma] Lemma
> [Vertex cover of a given size](vertex_cover_of_a_given_size.md) is [NP](nondeterministic_polynomial_time_(np).md).

# Proof

First note that this problem is of the correct form to be a [search problem](search_problems.md). Either there is a [vertex cover](vertex_cover.md) of the required size and we return it or we say no such cover exists.

For an [undirected graph](graph.md) $G = (V,E)$ if we are provided with a purposed solution $C$ to the problem there are two steps to checking it:
- Check that $|C| \leq g$, this takes $O(|C|)$.
- Check for every edge $(u,v) \in E$ that $u \in C$ or $v \in C$, that takes $O(|E|)$.
Therefore checking a solution takes [polynomial time](polynomial_time.md) in the input size.

This gives that the [Vertex cover of a given size](vertex_cover_of_a_given_size.md) is in [NP](nondeterministic_polynomial_time_(np).md).
