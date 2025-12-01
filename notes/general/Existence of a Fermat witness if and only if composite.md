---
aliases:
checked: false
created: 2023-10-10
draft: false
last_edited: 2023-11-11
tags:
  - maths
type: lemma
---
# Statement

>[!important] Lemma
>A number $r$ has a [[Fermat witness]] if and only if $r$ is not [[Prime|prime]].

# Proof

## $\Rightarrow$

If $r$ is [[Prime|prime]] from [[Fermat's little theorem]] we know no [[Fermat witness]] exists.

## $\Leftarrow$

If $r = nm$ for $n,m \in \mathbb{N}_{>1}$ then $gcd(r,n) = n > 1$.

Suppose
$$n^{r-1} = 1 \ (mod \ r)$$
then we would have
$$n^{r-1} = n n^{r-2} = 1 \ (mod \ r)$$
so $n^{r-2}$ is the inverse of $n$.

Though by the [[Modular multiplicative inverse existence|existence modular multiplicative inverse lemma]] we know no such inverse exists for $n$ and therefore $n^{r-1} \not = 1$ (mod $r$). So $n$ is a [[Fermat witness]] for $r$.
