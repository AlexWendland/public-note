---
aliases: null
checked: false
created: 2023-11-03
last_edited: 2023-11-11
publish: true
tags:
  - maths
type: lemma
---
# Statement

> [!important] Lemma
> [[Max clique problem (graph)|Max clique problem]] is [[NP-hard]].

# Proof

We know the [[Clique of a given size problem is NP-complete]], therefore it is [[NP-hard]]. We can reduce the [[Clique of a given size problem]] to [[Max clique problem (graph)|Max clique problem]] using the straight forward [[Many-one reduction (problem)|Many-one reduction]].

Suppose we have a graph $G$ and integer $g \geq 1$. Pass this graph $G$ to the [[Max clique problem (graph)|Max clique problem]]. This step is $O(1)$ as we need to do no manipulation.

The solution provides $C$ a max [[Clique (graph)|clique]]. If $\vert C \vert \geq g$ then return $C$, otherwise return no. This step takes $O(\vert V \vert)$ so it is polynomial in the input size.

If the [[Graph|graph]] $G$ has a [[Clique (graph)|clique]] of size at least $g$ then its max [[Clique (graph)|clique]] is of size $\geq g$, so we return true in the case.

If the [[Graph|graph]] $G$ has a max [[Clique (graph)|clique]] of size greater than $g$ then it has an [[Clique (graph)|clique]] of size $\geq g$ by definition.
