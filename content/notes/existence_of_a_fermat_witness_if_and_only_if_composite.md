---
aliases:
created: 2023-10-10
date_checked:
draft: false
last_edited: 2023-11-11
tags:
  - maths
title: Existence of a Fermat witness if and only if composite
type: lemma
---
# Statement

>[!important] Lemma
>A number $r$ has a [Fermat witness](fermat_witness.md) if and only if $r$ is not [prime](prime.md).

# Proof

## $\Rightarrow$

If $r$ is [prime](prime.md) from [Fermat's little theorem](fermat's_little_theorem.md) we know no [Fermat witness](fermat_witness.md) exists.

## $\Leftarrow$

If $r = nm$ for $n,m \in \mathbb{N}_{>1}$ then $gcd(r,n) = n > 1$.

Suppose
$$n^{r-1} = 1 \ (mod \ r)$$
then we would have
$$n^{r-1} = n n^{r-2} = 1 \ (mod \ r)$$
so $n^{r-2}$ is the inverse of $n$.

Though by the [existence modular multiplicative inverse lemma](modular_multiplicative_inverse_existence.md) we know no such inverse exists for $n$ and therefore $n^{r-1} \not = 1$ (mod $r$). So $n$ is a [Fermat witness](fermat_witness.md) for $r$.
