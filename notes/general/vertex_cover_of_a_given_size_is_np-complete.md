---
aliases:
checked: false
created: 2023-11-03
draft: false
last_edited: 2023-11-11
tags:
  - graph-theory
  - programming
title: Vertex cover of a given size is NP-complete
type: lemma
---
# Statement

> [!important] Lemma
> [Vertex cover of a given size](vertex_cover_of_a_given_size.md) is [NP-complete](np-complete.md).

# Proof

As [Vertex cover of a given size is NP](vertex_cover_of_a_given_size_is_np.md) we only need to show the problem is [NP-hard](np-hard.md).

We will show that the [Independent set of a given size](independent_set_of_a_given_size.md) has a [many-one reduction](many-one_reduction_(problem).md) to the [Vertex cover of a given size](vertex_cover_of_a_given_size.md).

Suppose we have a [undirected graph](graph.md) $G = (V,E)$ and $g > 0$ a positive integer and we are looking for a [independent set](independent_set_(graph).md) of size $g$.

Provide $G$ and $\vert V \vert - g$ to the [Vertex cover of a given size](vertex_cover_of_a_given_size.md) problem. This takes $O(1)$ as we are doing no manipulation to the graph.

If we are provided a [vertex cover](vertex_cover.md) $C$ of size at most $\vert V \vert - g$ return the set $I := V \backslash C$  as the solution to the [Independent set of a given size](independent_set_of_a_given_size.md) problem. This takes $O(\vert V \vert)$ to run so is [polynomial time](polynomial_time.md) in the input size. (Here $\vert I \vert = \vert V \vert - \vert I \vert \geq \vert V \vert - (\vert V \vert - g) \geq g$ so is of the correct size.)

If there is a solution to the [Independent set of a given size](independent_set_of_a_given_size.md) with the size of at least $g$ then the compliment is a [vertex cover](vertex_cover.md) of size at most $\vert V \vert - g$ from [Vertex cover if and only if the complement is an independent set](vertex_cover_if_and_only_if_the_complement_is_an_independent_set.md).

Similarly if there is a solution to the [Vertex cover of a given size](vertex_cover_of_a_given_size.md) with size of at most $\vert V \vert - g$ then the compliment is a [independent set](independent_set_(graph).md) of size at least $g$ from [Vertex cover if and only if the complement is an independent set](vertex_cover_if_and_only_if_the_complement_is_an_independent_set.md).

Therefore as [Independent set of a given size is NP-complete](independent_set_of_a_given_size_is_np-complete.md) we have [Vertex cover of a given size](vertex_cover_of_a_given_size.md) is [NP-hard](np-hard.md), which from above gives us it is [NP-complete](np-complete.md).



