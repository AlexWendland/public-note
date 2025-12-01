---
aliases:
checked: false
created: 2023-08-26
draft: false
last_edited: 2023-11-11
name: Euclidean algorithm
tags:
  - maths
  - programming
type: algorithm
---
# Euclidean algorithm

This algorithm is used to calculate the [greatest common divisor](greatest_common_divisor.md) for two positive integers. This uses [Euclid's rule](euclid's_rule.md) and [modular arithmetic](modular_arithmetic.md).

## Algorithm

```pseudocode
Euclid(x,y):
	Input: integers x,y where x >= y >= 0
	Output: gcd(x,y)
1. If y = 0 return x
2. return Eculid(y, x mod y)
```

## Run time

If $x$ and $y$ are $n$-bit integers then calculating $x$ mod $y$ takes $O(n^2)$ time. From [Claim 1](euclidean_algorithm.md#claim-1) we have every 2 rounds $x$ decreases by at least a factor of 2. So there are at most $2n$ rounds giving this algorithm a run time of $O(n^3)$.

### Claim 1

>[!important] Claim 1
>If $x \geq y$ then $x$ mod $y$ < $x/2$.

### Proof

If $y \leq x/2$ then $x$ mod $y$ $\leq y -1 < y \leq x/2$.

If $y > x/2$ then $x$ mod $y$ = $x - y < x - x/2 \leq x/2$.

## Correctness

This follows from [Euclid's rule](euclid's_rule.md).
