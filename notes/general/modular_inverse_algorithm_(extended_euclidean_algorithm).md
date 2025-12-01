---
aliases:
checked: false
created: 2023-10-09
draft: false
last_edited: 2023-11-11
name: Modular inverse algorithm (extended Euclidean algorithm)
tags:
  - programming
type: algorithm
---
# Modular inverse algorithm (extended Euclidean algorithm)

This algorithm solves the [Modular inverse problem](modular_inverse_problem.md) and uses the [Extended Euclidean algorithm](extended_euclidean_algorithm.md) to do it.

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

As the [Extended Euclidean algorithm](extended_euclidean_algorithm.md) takes $O(n^3)$ so does this algorithm.

# Correctness

From the [Modular multiplicative inverse existence](modular_multiplicative_inverse_existence.md) lemma we know the inverse only exists if the [Greatest common divisor](greatest_common_divisor.md) between $x$ and $N$ is 1.

As $1 = d = a \cdot x + N \cdot b$ looking at this all mod $N$ we have $a \cdot x = 1$ (mod $N$).
