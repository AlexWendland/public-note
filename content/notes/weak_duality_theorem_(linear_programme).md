---
aliases:
created: 2023-11-09
date_checked:
draft: false
last_edited: 2025-12-05
tags:
  - maths
title: Weak duality theorem (linear programme)
type: lemma
---
# Statement

> [!lemma] Lemma
> Let $x$ be a feasible point for a [linear programme](linear_programme.md) given by $A$, $b$, and $c$. Let $y$ be a feasible point for the [dual linear programme](dual_linear_programme.md) then we have the following inequality
> $$c^Tx = \sum_j c_j x_j \leq \sum_i b_i y_i = y^Tb.$$

# Proof

Recall that the [dual linear programme](dual_linear_programme.md) was specified by $-A^T$, $-c$ and $-b$. So we have
$$-A^Ty \leq -c, \mbox{ therefore } A^Ty \geq c$$
and so we have
$$c^Tx \leq (A^Ty)^Tx = y^TAx \leq y^Tb.$$

