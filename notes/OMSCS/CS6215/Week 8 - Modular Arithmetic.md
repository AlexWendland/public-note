---
aliases: 
checked: false
course: "[[CS6215 Introduction to Graduate Algorithms]]"
created: 2023-10-09
last_edited: 2023-11-11
draft: false
tags:
  - OMSCS
type: lecture
week: 8
---
# Week 8 - Modular Arithmetic

First lets remind ourselves of the definition of [[Modular arithmetic|modular arithmetic]].

![[Modular arithmetic]]

Within a computers architecture as numbers are stored in [[Binary|binary]] calculating mod $2^k$ is simple as taking the $k$ least significant bits. Therefore it is quite cheap. However, when the value is not $2^k$ it can get harder.

## Exponent problem

![[Modular exponent problem#Statement]]

This is the problem we want to solve in the next step. We would like an algorithm that is linear in $n$ which would be the input size. Note that $x$, $y$ and $N$ are all bounded by $2^n$ so if this appears in our bound we will be exponential.

It is quite easy to calculate $x^{2k}$ (mod $N$) as you recursively calculate $(x^{2i})^2$ (mod $N$). Using this idea we get a first attempt at solving the above problem.

![[Modular exponent algorithm]]

## Multiplicative inverse problem

>[!tldr] Modular multiplicative inverses
>The multiplicative inverse of $z$ mod $N$ is $0 \leq x < N$ such that $x \cdot z = 1$.

This may not exist if $N$ is not prime.

![[Modular multiplicative inverse existence]]

Though knowing an inverse exists isn't helpful algorithmically.

![[Modular inverse problem#Statement]]

Let's first look at a helpful rule for finding this.

![[Euclid's rule]]

We can use this rule to calculate [[Greatest common divisor|greatest common divisors]].

![[Euclidean algorithm]]

Moreover we can extend this to calculate the inverse.

![[Extended Euclidean algorithm]]

## Example

To compute $7^{-1}$ mod $360$  we run the [[Extended Euclidean algorithm]] on $7$ and $360$.

| x   | y   | c    | a   | b   |
| --- | --- | ---- | --- | --- |
| 360 | 7   | 51   | -2   | 103 |
| 7   | 3   | 2    | 1   | -2   |
| 3   | 1   | 3    | 0   | 1   |
| 1   | 0   | -    | 1   | 0   |

First calculate the $x$, $y$ and $c$ columns going downwards. Where $x_i = y_i \cdot c_i + y_{i+1}$ with $x_{i+1} = y_i$.

Second calculate $a_i$ and $b_i$ starting form the bottom where $a_{i-1} = b_i$ and $b_{i-1} = a_{i} - c_{i-1} \cdot b_i$. Note $d = min_i \ x_i$.

Then as $1 = -2 \cdot 360 + 103 \cdot 7$ we have that $103 = 7^{-1}$ mod $360$.
