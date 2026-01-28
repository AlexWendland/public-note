---
aliases:
created: 2023-11-09
date_checked: 2026-01-28
draft: false
last_edited: 2026-01-28
tags:
  - maths
title: The dual dual linear programme is the original linear programme
type: lemma
---
# Statement

> [!lemma] Lemma
> For a [linear programme](linear_programme.md) given by $A, b,$ and $c$ if we take the [dual linear programme](dual_linear_programme.md) and then the dual of that, we get back to the original [linear programme](linear_programme.md).

# Proof

Just following the definition, the [dual linear programme](dual_linear_programme.md) is defined by $-A^T$, $-c$ and $-b$. Then the dual of that is given by $-(-A^T)^T$, $-(-b)$ and $-(-c)$ which by the laws of [linear algebra](linear_algebra.md) gives us $A$, $b$ and $c$ back.
