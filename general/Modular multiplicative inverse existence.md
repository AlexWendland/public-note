---
aliases: null
checked: false
created: 2023-10-09
last_edited: 2023-11-11
draft: false
tags:
  - maths
type: lemma
---
# Statement

>[!important] Lemma
>For $x, N \in \mathbb{Z}$ there exists $y \in \mathbb{Z}$ where $0 < y < N$ such that $x \cdot y = 1$ (mod $N$) if and only if $gcd(x,N) = 1$.

# Proof

## $\Rightarrow$

Let the [[Greatest common divisor|greatest common divisor]] be $gcd(x, N) = y$, so $y \cdot \overline{x} = x$ and $y \cdot \overline{N} = N$ where $0 < \overline{N} \leq N$. Therefore consider the following [[Modular arithmetic|modular arithmetic]]
$$x \cdot \overline{N} = \overline{x} \cdot y \cdot \overline{N} = 0 \ (mod \ N).$$
As $x$ has an inverse $x^{-1}$ consider
$$
\overline{N} = \overline{N} \cdot 1 = \overline{N} \cdot x \cdot x^{-1} = 0 \cdot x^{-1} = 0 \ (mod \ N).$$
Therefore $\overline{N} = N$ and $gcd(x, N) = 1$.

## $\Leftarrow$

Consider the set of numbers $S = \{ i \cdot x \ mod \ N \vert 0 \leq i < N\}$. We know $\vert S \vert = N$ and for $s \in S$ we have $0 \leq s < N$. Suppose
$$ i \cdot x = j \cdot x \ (mod \ N).$$
for $0 \leq i \leq j < N$. This gives us
$$ (j - i) \cdot x = 0 \ (mod \ N).$$
Set $j-i := k$ where $0 \leq k < N$ now we have $k \cdot x = c \cdot N$. However as $gcd(x, N) = 1$ we have $N \vert k \cdot x$ giving $N \vert k$ making $k = 0$.

Therefore all of $S$ are unique, so $1 \in S$ and we have a multiplicative inverse.
