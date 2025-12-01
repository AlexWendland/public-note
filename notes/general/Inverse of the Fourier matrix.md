---
aliases:
checked: false
created: 2023-09-19
draft: false
last_edited: 2023-11-11
tags:
  - maths
type: lemma
---

>[!important] Lemma
>Let $F_n(\omega)$ be a [[Fourier Matrix]] then we have
> $$F_n(\omega)^{-1} = \frac{1}{n} F_n(\omega^{-1}).$$
### Proof
Lets examine
$$F_n(\omega^{-1}) F_n(\omega) := \{m_{i,j}\}.$$
For these terms we have
$$ \begin{align*} m_{j,k} & = \left( 1, \omega^{-j}, \omega^{-2j}, \ldots, \omega^{-(n-1)j} \right ) \cdot \left( 1, \omega^{k}, \omega^{2k}, \ldots, \omega^{(n-1)k} \right )\\
& = \sum_{i=0}^{n-1} \omega^{i(j-k)}\\
& = \sum_{i=0}^{n-1} \left ( \omega^{j-k} \right )^n
\end{align*}$$
Which splits into cases if $j = k$ then $\omega^{j-k} = 1$ and we have this sum is $n$. Whereas if $j \not = k$ from the [[Sum of roots of unity|sum of roots of unity]] we have this sum is 0. Therefore
$$ F_n(\omega^{-1}) F_n(\omega) = n I_n$$
giving us the desired result.
