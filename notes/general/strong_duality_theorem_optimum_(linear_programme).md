---
aliases:
checked: false
created: 2023-11-10
draft: false
last_edited: 2025-12-05
tags:
  - maths
  - todo
title: Strong duality theorem optimum (linear programme)
type: lemma
---
# Statement

> [!lemma] Lemma
> A [linear programme](linear_programme.md) (given by $A$, $b$ and $c$) has an optimal point $x^{\ast}$ if and only if its [dual linear programme](dual_linear_programme.md) has an optimal point $y^{\ast}$. These relate by
> $$c^Tx^{\ast} = b^Ty^{\ast}.$$

# Proof

From the [Strong duality theorem (linear programme)](strong_duality_theorem_(linear_programme).md) we know the original [linear programme](linear_programme.md) is feasible and bounded if and only if the [dual linear programme](dual_linear_programme.md) is feasible and bounded.

However, a [linear programme](linear_programme.md) has a solution if and only if it is feasible and bounded therefore providing the equivalence above.

The relationship between the points is given by the [weak duality theorem](weak_duality_theorem_(linear_programme).md). **This is not finished**
