---
aliases:
checked: false
created: 2023-11-03
draft: false
last_edited: 2023-11-11
title: Minimum vertex cover problem is NP-hard
tags:
  - maths
type: lemma
---
# Statement

> [!important] Lemma
> [Minimum vertex cover problem](minimum_vertex_cover_problem.md) is [NP-hard](np-hard.md).

# Proof

We have shown that [Vertex cover of a given size is NP-complete](vertex_cover_of_a_given_size_is_np-complete.md). So we will find a [many-one reduction](many-one_reduction_(problem).md) of [Vertex cover of a given size](vertex_cover_of_a_given_size.md) to [Minimum vertex cover problem](minimum_vertex_cover_problem.md) to show it is [NP-hard](np-hard.md).

Suppose we have an [undirected graph](graph.md) $G = (V,E)$ and a positive integer $g > 0$. If we are looking for a [vertex cover](vertex_cover.md) of size at most $g > 0$, pass $G$ to our solution to the [Minimum vertex cover problem](minimum_vertex_cover_problem.md).

This takes $O(1)$ as we are doing no manipulations.

We get back minimum cover $C$. If $\vert C \vert \leq g$ return $C$ to the [Vertex cover of a given size](vertex_cover_of_a_given_size.md) problem, otherwise return no. This step takes $O(\vert V \vert)$ so is [polynomial time](polynomial_time.md) in the input size.

If there is a [vertex cover](vertex_cover.md) of size less than $g$ then the minimum [vertex cover](vertex_cover.md) will have size less than $g$.

Equally if the minimum [vertex cover](vertex_cover.md) has size less than $g$ then there is a [vertex cover](vertex_cover.md) of size less than $g$.

So we have that [Vertex cover of a given size](vertex_cover_of_a_given_size.md) has a [many-one reduction](many-one_reduction_(problem).md) to [Minimum vertex cover problem](minimum_vertex_cover_problem.md). Giving that [Minimum vertex cover problem](minimum_vertex_cover_problem.md) is [NP-hard](np-hard.md).


