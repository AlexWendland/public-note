---
aliases:
  - polynomial regression
created: 2024-01-17
date_checked:
draft: false
last_edited: 2026-02-05
tags:
  - maths
  - machine-learning
title: Polynomial regression
type: definition
---
>[!definition] Polynomial regression
> In the [modelling framework](modelling_framework.md) saying we are doing *polynomial regression* is saying that we are picking the [modelling paradigm](modelling_paradigm.md) of functions of the form
> $$f(x) = c_0 + \sum_{p \in \Delta_n^k}^n c_{p} x^p$$
> where
> - $x = (x_1, x_2, \ldots, x_n) \in A$,
> - $\Delta_k^n = \{(p_1, \ldots, p_n) \in \mathbb{N}^n \vert \sum_{i=1}^n p_i \leq k\}$, and
> - $x^p = \prod_{i=1}^n x_i^{p_i}$
>
> we say $k$ is the degree of our polynomial.
>
> If $A$ was 1-dimensional this would be:
> $$f(x) = \sum_{i=0}^k c_i x^i.$$

