---
aliases:
checked: false
created: 2023-11-03
draft: false
last_edited: 2025-12-05
tags:
  - programming
title: Max independent set problem is NP-hard
type: lemma
---
# Statement

> [!lemma] Lemma
> [Max independent set problem](max_independent_set_problem_(graph).md) is [NP-hard](np-hard.md).

# Proof

We know the [Independent set of a given size is NP-complete](independent_set_of_a_given_size_is_np-complete.md), therefore it is [NP-hard](np-hard.md). We can reduce the [Independent set of a given size](independent_set_of_a_given_size.md) to [max independent set problem](max_independent_set_problem_(graph).md) using the straight forward [Many-one reduction](many-one_reduction_(problem).md).

Suppose we have a graph $G$ and integer $g \geq 1$. Pass this graph $G$ to the [max independent set problem](max_independent_set_problem_(graph).md). This step is $O(1)$ as we need to do no manipulation.

The solution provides $I$ a max [independent set](independent_set_(graph).md). If $\vert I \vert \geq g$ then return $I$, otherwise return no. This step takes $O(\vert V \vert)$ so it is polynomial in the input size.

If the [graph](graph.md) $G$ has an [independent set](independent_set_(graph).md) of size at least $g$ then its max independent set is of size $\geq g$, so we return true in the case.

If the [graph](graph.md) $G$ has a max [independent set](independent_set_(graph).md) of size greater than $g$ then it has an independent set of size $\geq g$ by definition.
