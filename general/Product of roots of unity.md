---
aliases: null
chatgpt: false
created: 2023-09-22
last_edited: 2023-09-22
publish: true
tags:
  - maths
type: lemma
---
# Product of roots of unity

>[!important] Lemma
>For any primitive $n$th root of unity $\omega$ we have
>$$ \prod_{i=0}^{n-1} \omega^i = (-1)^{n+1}.$$

## Proof

Note that $\omega^n = 1$, suppose $n = 2k + 1$ then
$$\begin{align} \prod_{i=0}^{2k} \omega^i & = \prod_{i=1}^{2k} \omega^i\\
& = \prod_{i=1}^{k} \omega^i \omega^{2k + 1 - i}\\
& = \prod_{i=1}^k \omega^{2k+1}\\
& = 1\end{align}$$
this proves the case for odd $n$. Now instead suppose $n = 2k$ then
$$\begin{align} \prod_{i=0}^{2k-1} \omega^i & = \prod_{i=1}^{2k -1} \omega^i\\
& = \omega^k \prod_{i=1}^{k-1} \omega^i \omega^{2k - i}\\
& = - \prod_{i=1}^{k-1} \omega^{2k}\\
& = - 1\end{align}$$
which proves the case for even $n$.
