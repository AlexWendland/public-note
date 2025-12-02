---
aliases:
checked: false
created: 2023-10-10
draft: false
last_edited: 2023-11-11
tags:
  - maths
title: Non-trivial Fermat witnesses are dense
type: lemma
---
# Statement

>[!important] Lemma
>If $r \in \mathbb{N}$ has $\geq 1$ [non-trivial Fermat witness](fermat_witness.md) then atleast 1/2 of $z \in \{1, 2, \ldots, r-1\}$ are [Fermat witnesses](fermat_witness.md).

# Proof

Pick a [non-trivial Fermat witness](fermat_witness.md) $a$. Then for any $b \in \{1, 2, \ldots, r-1\}$ such that
$$b^{r-1} = 1 \ (mod \ r)$$
it has a twin $ab$ where
$$(ab)^{r-1} = a^{r-1}b^{r-1} = a^{r-1} \not = 1 \ (mod \ r).$$
Note as we are just multiplying by $a$ which is a [bijection](bijection.md) on integers mod $r$ we have that at most half of $\{1, 2, \ldots, r-1\}$ are not [Fermat witnesses](fermat_witness.md).
