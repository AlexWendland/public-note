---
aliases:
checked: false
created: 2023-11-09
draft: false
last_edited: 2023-11-11
tags:
  - maths
title: If a point in a linear programme has equal objective function to a point in
  its dual linear programme they are both optimal
type: lemma
---
# Statement

> [!important] Lemma
> For a [linear programme](linear_programme.md) given by $A$, $b$, and $c$ if there is feasible point $x \in \mathbb{R}^n$ and $y \in \mathbb{R}^m$ feasible point in the [dual linear programme](dual_linear_programme.md) such that
> $$ c^Tx = b^Ty$$
> then they are both optimal points in there respective [linear programmes](linear_programme.md).

# Proof

This follows from the [weak duality theorem](weak_duality_theorem_(linear_programme).md) as
$$c^Tx' \leq b^ty'$$
for all feasible $x'$ and $y'$ then by definition of their objective functions $x$ and $y$ are optimal.
