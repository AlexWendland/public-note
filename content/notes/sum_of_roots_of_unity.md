---
aliases:
  - sum of roots of unity
created: 2023-09-19
date_checked:
draft: false
last_edited: 2023-11-11
tags:
  - maths
title: Sum of roots of unity
type: lemma
---
>[!important] Lemma
>For any $n$th root of unity $\omega$ where $\omega \not = 1$ we have
>$$ \sum_{i=0}^{n-1} \omega^i = 0.$$
## Proof

For any number $z$ we have
$$(z - 1)(1 + z + z^2 + \ldots + z^{n-1}) = z^n - 1.$$
Therefore
$$ (\omega - 1) \cdot \left ( \sum_{i=0}^{n-1} \omega^i \right ) = \omega^n - 1 = 0$$
however as $\omega \not = 1$ we have $\omega - 1 \not = 0$ giving the desired result.
