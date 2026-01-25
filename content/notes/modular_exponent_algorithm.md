---
aliases:
created: 2023-10-09
date_checked:
draft: false
last_edited: 2023-11-11
tags:
  - programming
title: Modular exponent algorithm
type: algorithm
---

This algorithm has a [polynomial run time](polynomial_time.md) in the size of the input to calculate powers in using [modular arithmetic](modular_arithmetic.md). This has not been sped up using [Euler's theorem (modular arithmetic)](euler's_theorem_(modular_arithmetic).md).

 Algorithm

```pseudocode
resursive_mod_exp(x,y,N):
	Input: n-bit integers x,y,N >= 0
	Ouput: x^y mod N
1. if y = 0, return 1
2. z = resursive_mod_exp(x, floor(y/2), N)
3. if y is even return z^2 mod N
4. if y is off return xz^2 mod N
```

 Run time

The algorithm runs for at most $n$ loops as $y$ is an $n$-bit integer. Calculating multiplication of $n$-bit integers takes $O(n^2)$. Therefore this algorithm runs in $O(n^3)$ time.

 Correctness

This derives from basic properties of [modular arithmetic](modular_arithmetic.md).
