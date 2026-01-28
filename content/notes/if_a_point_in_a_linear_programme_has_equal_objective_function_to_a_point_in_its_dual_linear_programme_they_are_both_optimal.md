---
aliases:
created: 2023-11-09
date_checked: 2026-01-28
draft: false
last_edited: 2026-01-28
tags:
  - maths
title: If a point in a linear programme has equal objective function to a point in
  its dual linear programme they are both optimal
type: lemma
---
# Statement

> [!lemma] Lemma
> For a [linear programme](linear_programme.md) given by $A$, $b$, and $c$ if there is a feasible point $x \in \mathbb{R}^n$ and a feasible point $y \in \mathbb{R}^m$ in the [dual linear programme](dual_linear_programme.md) such that
> $$ c^Tx = b^Ty$$
> then they are both optimal points in their respective [linear programmes](linear_programme.md).

# Proof

This follows from the [weak duality theorem](weak_duality_theorem_(linear_programme).md) as
$$c^Tx' \leq b^Ty'$$
for all feasible $x'$ and $y'$ then by definition of their objective functions $x$ and $y$ are optimal.
