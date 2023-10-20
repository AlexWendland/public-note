---
aliases: 
type: lemma
publish: true
created: 2023-10-10
last_edited: 2023-10-10
tags:
  - maths
chatgpt: false
---
# Statement

>[!important] Lemma
>If $r \in \mathbb{N}$ has $\geq 1$ [[Fermat witness|non-trivial Fermat witness]] then atleast 1/2 of $z \in \{1, 2, \ldots, r-1\}$ are [[Fermat witness|Fermat witnesses]].

# Proof

Pick a [[Fermat witness|non-trivial Fermat witness]] $a$. Then for any $b \in \{1, 2, \ldots, r-1\}$ such that
$$b^{r-1} = 1 \ (mod \ r)$$
it has a twin $ab$ where
$$(ab)^{r-1} = a^{r-1}b^{r-1} = a^{r-1} \not = 1 \ (mod \ r).$$
Note as we are just multiplying by $a$ which is a [[Bijection|bijection]] on integers mod $r$ we have that at most half of $\{1, 2, \ldots, r-1\}$ are not [[Fermat witness|Fermat witnesses]].
