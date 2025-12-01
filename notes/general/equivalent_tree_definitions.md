---
aliases:
  - equivalent tree definitions
checked: false
created: 2023-09-26
draft: false
last_edited: 2023-11-11
name: Equivalent tree definitions
tags:
  - maths
type: lemma
---
> [!important] Lemma
> The following conditions are equivalent for a [graph](graph.md) $G = (V,E)$.
> 1. $G$ is a [tree](tree_(graph).md).
> 2. $G$ is [path connected](connected_(graph).md) and $\vert E \vert = \vert V \vert − 1$.
> 3. $G$ has no [cycles](cycle_(graph).md) and $\vert E \vert = \vert V \vert − 1$.

## Proof

### Proof of $(1) \Rightarrow (2)$.

We prove this by induction on the number of vertices.

Suppose $\vert V \vert = 1$ and set $V = \{v\}$ then if $G$ had an edge it must be $(v,v)$. However, we then have a cycle $(v,v)$ so it would not be a tree. So $\vert E \vert = 0 = \vert V \vert - 1$.

Suppose the induction hypothesis is correct on all graphs with $\vert V \vert < k$ and let $G$ be a [graph](graph.md) with $\vert V \vert = k$.

As [a finite tree that has more than one vertex must have at least two leaf vertices](a_finite_tree_that_has_more_than_one_vertex_must_have_at_least_two_leaf_vertices.md) let $v \in V$ be such a leaf vertex with single edge $e \in E$. Remove $v$ to form $G^{\ast} = (V \backslash \{v\}, E \backslash \{e\})$. Note that $G^{\ast}$ has to be a tree as if a [cycle](cycle_(graph).md) existed in $G^{\ast}$ it would exist in $G$ and as $G$ was connected so is $G^{\ast}$ as no path would need to use $e$.

By the induction hypothesis $\vert E \backslash \{e\}\vert = \vert V \backslash \{v\}\vert - 1$. Giving
$$ \vert E \vert = \vert E \backslash \{e\}\vert + \vert \{e\} \vert = \vert V \backslash \{v\}\vert - 1 + 1 =  (\vert V \backslash \{v\}\vert + 1) - 1 = \vert V \vert - 1.$$
Thus proving our statement by induction.

### Proof of $(2) \Rightarrow (3)$.

Suppose we have a graph $G$ that is connected and $\vert E \vert = \vert V \vert - 1$. Though $G$ has a [cycle](cycle_(graph).md) in it.

Take a minimal, in terms of $\vert V \vert$, counter example.

Note that from problem 3(a) we have
$$ \sum_{v \in V} \mbox{deg}(v) = 2 \vert E \vert = 2 \vert V \vert - 2$$
that says one vertex in $V$ must have $\mbox{deg}(v) = 1$ (it has to be at least 1 as it is connected).

As $v$ can't be in the [cycle](cycle_(graph).md) (this would require degree 2), it must be outside. We can now remove this vertex and the remaining graph will still satisfy $(2)$ with the same [cycle](cycle_(graph).md). The new graph will be a smaller example and contradict its minimality.

This proves the claim.

### Proof of $(3) \Rightarrow (1)$.

Note all we need to show is that $G$ is connected.

Lets use proof be contradiction. Suppose $G$ satisfies $(3)$ but is not a tree, let $G$ be a minimal such example.

If $G$ has a vertex of [degree](degree_(graph).md) 1, we can remove it and find a smaller counter example. Therefore $G$ must not have any vertices of degree 1.

Take a connected component of $G$, as it has no vertices of degree 1 they must have vertices of degree $2$ or more. Repeat the argument in [a finite tree that has more than one vertex must have at least two leaf vertices](a_finite_tree_that_has_more_than_one_vertex_must_have_at_least_two_leaf_vertices.md), this shows that this connected component has a cycle it in. This contradicts $(3)$ so no such graph exists.

This proves this claim and the equivalence.
