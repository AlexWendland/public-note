---
aliases: null
chatgpt: false
created: 2023-11-03
last_edited: 2023-11-03
publish: true
tags:
  - programming
type: lemma
---
# Statement

> [!important] Lemma
> [[Max independent set problem (graph)|Max independent set problem]] is [[NP-hard]].

# Proof

We know the [[Independent set of a given size is NP-complete]], therefore it is [[NP-hard]]. We can reduce the [[Independent set of a given size]] to [[Max independent set problem (graph)|max independent set problem]] using the straight forward [[Many-one reduction (problem)|Many-one reduction]].

Suppose we have a graph $G$ and integer $g \geq 1$. Pass this graph $G$ to the [[Max independent set problem (graph)|max independent set problem]]. This step is $O(1)$ as we need to do no manipulation.

The solution provides $I$ a max [[Independent set (graph)|independent set]]. If $\vert I \vert \geq g$ then return $I$, otherwise return no. This step takes $O(\vert V \vert)$ so it is polynomial in the input size.

If the [[Graph|graph]] $G$ has an [[Independent set (graph)|independent set]] of size at least $g$ then its max independent set is of size $\geq g$, so we return true in the case.

If the [[Graph|graph]] $G$ has a max [[Independent set (graph)|independent set]] of size greater than $g$ then it has an independent set of size $\geq g$ by definition.
