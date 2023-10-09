---
aliases: 
type: lecture
publish: false
created: 2023-10-09
last_edited: 2023-10-09
tags:
  - OMSCS
course: "[[CS6200 Introduction to Graduate Algorithms]]"
week: 
chatgpt: false
---
# Week 8 - Modular Arithmetic

First lets remind ourselves of the definition of [[Modular arithmetic|modular arithmetic]].

![[Modular arithmetic]]

Within a computers architecture as numbers are stored in [[Binary|binary]] calculating mod $2^k$ is simple as taking the $k$ least significant bits. Therefore it is quite cheap. However, when the value is not $2^k$ it can get harder.

## General problem

![[Modular exponent problem#Statement]]

This is the problem we want to solve in the next step. We would like an algorithm that is linear in $n$ which would be the input size. Note that $x$, $y$ and $N$ are all bounded by $2^n$ so if this appears in our bound we will be exponential.

It is quite easy to calculate $x^{2k}$ (mod $N$) as you recursively calculate $(x^{2i})^2$ (mod $N$). Using this idea we get a first attempt at solving the above problem.

```pseudocode
resursive_mod_exp(x,y,N):
	Input: n-bit integers x,y,N >= 0
	Ouput: x^y mod N
1. if y = 0, return 1
2. z = resursive_mod_exp(x, floor(y/2), N)
3. if y is even return z^2 mod N
4. if y is off return xz^2 mod N
```

## Multiplicative inverse

>[!tldr] Modular multiplicative inverses
>The multiplicative inverse of $z$ mod $N$ is $0 \leq x < N$ such that $x \cdot z = 1$.

This may not exist if $N$ is not prime.



