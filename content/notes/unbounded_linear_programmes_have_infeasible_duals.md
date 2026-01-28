---
aliases:
created: 2023-11-09
date_checked: 2026-01-28
draft: false
last_edited: 2026-01-28
tags:
  - maths
title: Unbounded linear programmes have infeasible duals
type: lemma
---
# Statement

> [!lemma] Lemma
> If a [linear programme](linear_programme.md) is [unbounded](unbounded_linear_programme.md) then its [dual linear programme](dual_linear_programme.md) is [infeasible](infeasible_linear_programme.md).

# Proof

If we have a [linear programme](linear_programme.md) given by $A$, $b$, and $c$, then from the [weak duality theorem](weak_duality_theorem_(linear_programme).md) we have
$$
c^Tx \leq b^Ty$$
for all feasible $x$ in the original [linear programme](linear_programme.md) and $y$ in the [dual linear programme](dual_linear_programme.md). Therefore, if the original [linear programme](linear_programme.md) is [unbounded](unbounded_linear_programme.md), then no feasible $y$ exists, making the [dual linear programme](dual_linear_programme.md) [infeasible](infeasible_linear_programme.md).
