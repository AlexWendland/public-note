---
aliases:
checked: false
created: 2023-11-10
draft: false
last_edited: 2023-11-11
title: Strong duality theorem (linear programme)
tags:
  - maths
type: lemma
---
# Statement

> [!important] Lemma
> A [linear programme](linear_programme.md) is feasible and bounded if and only if the [dual linear programme](dual_linear_programme.md) is feasible and bounded.

# Proof

This follows as [the dual of the dual linear programme is the original linear programme](the_dual_dual_linear_programme_is_the_original_linear_programme.md) and [unbounded linear programmes have infeasible duals](unbounded_linear_programmes_have_infeasible_duals.md).

Note a linear programme is feasible and bounded if it is feasible and the [dual linear programme](dual_linear_programme.md) is feasible. However, this gives that the [dual linear programme](dual_linear_programme.md) is feasible and its dual (the original linear programme) is feasible therefore the [dual linear programme](dual_linear_programme.md) is feasible and bounded.

Similarly if the [dual linear programme](dual_linear_programme.md) is feasible and bounded then it is feasible and its dual (the original linear programme) is feasible. However, this gives that the original linear programme and its dual are feasible, making the original linear programme feasible and bounded.
