---
aliases:
checked: false
created: 2023-11-09
draft: false
last_edited: 2023-11-11
title: The dual dual linear programme is the original linear programme
tags:
  - maths
type: lemma
---
# Statement

> [!important] Lemma
> For a [linear programme](linear_programme.md) given by $A, b,$ and $c$ if we take the [dual linear programme](dual_linear_programme.md) and then the [dual linear programme](dual_linear_programme.md) of that we get back to the original [linear programme](linear_programme.md).

# Proof

Just following the definition the [dual linear programme](dual_linear_programme.md) is defined by $-A^T$, $-c$ and $-b$. Then the [dual linear programme](dual_linear_programme.md) of that is given by $-(-A^T)^T$, $-(-b)$ and $-(-c)$ which by laws of [linear algebra](linear_algebra.md) give us $A$, $b$ and $c$ back.
