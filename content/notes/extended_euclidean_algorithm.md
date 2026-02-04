---
aliases:
  - extended Euclidean algorithm
created: 2023-10-09
date_checked:
draft: false
last_edited: 2023-11-11
tags:
  - maths
title: Extended Euclidean algorithm
type: algorithm
---

This algorithm extends the [Euclidean algorithm](euclidean_algorithm.md) to be able to calculate the [greatest common divisor](greatest_common_divisor.md) of two integers.

# Algorithm

```pseudocode
extended_euclidean(x,y):
	Input: integers x, y where x >= y >= 0
	Output: integers d, a, b where d = gcd(x,y) and d = xa + yb
1. if y = 0, return (x,1,0)
2. (d, a', b') = extended_euclidean(y,x mod y)
3. return (d, b', a' - floor(x/y)b')
```

# Runtime

Notice this is functionally the same as [Euclidean algorithm](euclidean_algorithm.md). So if $x, y$ are $n$-bit integers then this takes $O(n^3)$.

# Correctness

The fact that $d$ is correct follows from [Euclid's rule](euclid's_rule.md).

We proceed by induction on $y$.

If $y = 0$ then $x = 1 \cdot x$ and we are done.

Suppose we have it true for all $y < k$ and we want to check it is correct for $y = k$.

We run `extended_euclidean(y,x mod y)` lets set $x = z$ mod $y$ as $z < y$ we get back correct $d, a', b'$ such that $d = gcd(y,z)$ and $d = a'y + b'z$.

Now write
$$x = c \cdot y + z$$
where $c = floor(x/y)$. Then calculate
$$\begin{aligned} b' x + (a' - cb')y & = b'(c \cdot y + z) + (a' - cb')y\\
& = b' c y + b' z + a' y - c b' y\\
& = b' z + a' y\\
& = d \end{aligned}$$
giving what is required.

Thus we get the result by induction.


