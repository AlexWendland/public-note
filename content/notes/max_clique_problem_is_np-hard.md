---
aliases:
created: 2023-11-03
date_checked:
draft: false
last_edited: 2025-12-05
tags:
  - maths
title: Max clique problem is NP-hard
type: lemma
---
# Statement

> [!lemma] Lemma
> [Max clique problem](max_clique_problem_(graph).md) is [NP-hard](np-hard.md).

# Proof

We know the [Clique of a given size problem is NP-complete](clique_of_a_given_size_problem_is_np-complete.md), therefore it is [NP-hard](np-hard.md). We can reduce the [Clique of a given size problem](clique_of_a_given_size_problem.md) to [Max clique problem](max_clique_problem_(graph).md) using the straight forward [Many-one reduction](many-one_reduction_(problem).md).

Suppose we have a graph $G$ and integer $g \geq 1$. Pass this graph $G$ to the [Max clique problem](max_clique_problem_(graph).md). This step is $O(1)$ as we need to do no manipulation.

The solution provides $C$ a max [clique](clique_(graph).md). If $\vert C \vert \geq g$ then return $C$, otherwise return no. This step takes $O(\vert V \vert)$ so it is polynomial in the input size.

If the [graph](graph.md) $G$ has a [clique](clique_(graph).md) of size at least $g$ then its max [clique](clique_(graph).md) is of size $\geq g$, so we return true in the case.

If the [graph](graph.md) $G$ has a max [clique](clique_(graph).md) of size greater than $g$ then it has an [clique](clique_(graph).md) of size $\geq g$ by definition.
