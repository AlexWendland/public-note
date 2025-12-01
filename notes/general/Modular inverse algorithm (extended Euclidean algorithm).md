---
aliases:
checked: false
created: 2023-10-09
draft: false
last_edited: 2023-11-11
tags:
  - programming
type: algorithm
---
# Modular inverse algorithm (extended Euclidean algorithm)

This algorithm solves the [[Modular inverse problem]] and uses the [[Extended Euclidean algorithm]] to do it.

# Algorithm

```pseudocode
modular_inverse_algorithm(x, N):
	Input: 2 n-bit integers x, N.
	Output: Either x^{-1} mod N or it says it does not exists.
1. Run extended_euclidean_algorithm(x, N) = (d, a, b)
2. If d != 1 return that no inverse exists.
3. Return a
```

# Runtime

As the [[Extended Euclidean algorithm]] takes $O(n^3)$ so does this algorithm.

# Correctness

From the [[Modular multiplicative inverse existence]] lemma we know the inverse only exists if the [[Greatest common divisor]] between $x$ and $N$ is 1.

As $1 = d = a \cdot x + N \cdot b$ looking at this all mod $N$ we have $a \cdot x = 1$ (mod $N$).
