---
aliases:
created: 2023-11-03
date_checked: 2026-01-28
draft: false
last_edited: 2026-01-28
tags:
  - maths
title: Minimum vertex cover problem is NP-hard
type: lemma
---
# Statement

> [!lemma] Lemma
> [Minimum vertex cover problem](minimum_vertex_cover_problem.md) is [NP-hard](np-hard.md).

# Proof

We have shown that [Vertex cover of a given size is NP-complete](vertex_cover_of_a_given_size_is_np-complete.md). So we will find a [many-one reduction](many-one_reduction_(problem).md) of [Vertex cover of a given size](vertex_cover_of_a_given_size.md) to [Minimum vertex cover problem](minimum_vertex_cover_problem.md) to show it is [NP-hard](np-hard.md).

Suppose we have an [undirected graph](graph.md) $G = (V,E)$ and a positive integer $g > 0$. If we are looking for a [vertex cover](vertex_cover.md) of size at most $g$, we pass $G$ to our solution for the [Minimum vertex cover problem](minimum_vertex_cover_problem.md).

This takes $O(1)$ as we are performing no manipulations.

We get back the minimum cover $C$. If $\vert C \vert \leq g$, we return `true` to the [Vertex cover of a given size](vertex_cover_of_a_given_size.md) problem, otherwise we return `false`. This step takes $O(\vert V \vert)$ and is [polynomial time](polynomial_time.md) in the input size.

If there is a [vertex cover](vertex_cover.md) of size at most $g$, then the minimum [vertex cover](vertex_cover.md) will have size at most $g$.

Conversely, if the minimum [vertex cover](vertex_cover.md) has size at most $g$, then there is a [vertex cover](vertex_cover.md) of size at most $g$.

So we have that [Vertex cover of a given size](vertex_cover_of_a_given_size.md) has a [many-one reduction](many-one_reduction_(problem).md) to [Minimum vertex cover problem](minimum_vertex_cover_problem.md). Giving that [Minimum vertex cover problem](minimum_vertex_cover_problem.md) is [NP-hard](np-hard.md).


