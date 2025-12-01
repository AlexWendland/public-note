---
aliases:
checked: false
created: 2023-10-10
draft: false
last_edited: 2023-11-11
name: Chinese remainder theorem
tags:
  - maths
type: lemma
---
# Statement

>[!important] Chinese remainder theorem
>Let $n_i \in \mathbb{Z}$ be positive non-zero, non-unit elements for $1 \leq i \leq k$ where $n_i$ are [pairwise coprime](pairwise_coprime.md) and set $N = \prod_{i=1}^k n_i$. Then for any $a_i \in \mathbb{Z}$ with $0 \leq a_i < n_i$ and $1 \leq i \leq k$ there exists a unique $x \in \mathbb{Z}$ where $0 \leq x < N$ such that
>$$x = a_i \ (mod \ n_i).$$
>

# Proof

## Existence

We proceed by induction.

If $i = 2$ then from the [extended Euclidean algorithm](extended_euclidean_algorithm.md) we could construct $x_1$ and $x_2$ such that $x_1 n_1 + x_2 n_2 = 1$.

Note this gives $x_1n_1 = 1$ (mod $n_2)$ and $x_2n_2 = 1$ (mod $n_1$).

Then consider $x = a_2 x_1 n_1 + a_1 x_2 n_2$
$$x = a_2 x_1 n_1 + a_1 x_2 n_2 = a_1 \left ( x_2 n_2 \right ) = a_1 \ (mod \ n_1)$$
similarly
$$x = a_2 x_1 n_1 + a_1 x_2 n_2 = a_2 \left ( x_1 n_1 \right ) = a_2 \ (mod \ n_2).$$
Suppose we have now solved it for $i < k$ with $k > 2$.

Note that first we can solve the case with 2 variables for $n_{k-1}$ and $n_k$. So we get an $0 \leq x_{k-1,k} < n_{k-1}n_k$ such that
$$ x_{k-1,k} = a_{k-1} \ (mod \ n_{k-1}), \mbox{ and } x_{k-1,k} = a_k \ (mod \ n_k).$$
Now solve the $i = k-1$ problem using the induction assumption with $n_i$ for $i < k-1$ and $n_{k-1}n_k$ with $a_i$ for $i < k-1$ and $x_{k-1,k}$. Giving $0 \leq x < N$ where
$$ x = a_{i} \ (mod \ n_{i}), \mbox{ for } i < k-1, \mbox{ and } x = x_{k-1,k} \ (mod \ n_{k-1}n_k).$$
which by construction gives
$$ x = x_{k-1,k} = a_{k-1} \ (mod \ n_{k-1}), \mbox{ and } x = x_{k-1,k} = a_k \ (mod \ n_k).$$
Thus by induction we have show existence.

## Uniqueness

Suppose $0 \leq x \leq y < N$ were two such solutions then $n_i \vert y - x$ for all $1 \leq i \leq k$.

As the $n_i$ are [coprime](coprime.md) we have that $N \vert y-x$.

As $0 \leq y-x < N$ the only possible solution is $y = x$ and we have uniqueness.
