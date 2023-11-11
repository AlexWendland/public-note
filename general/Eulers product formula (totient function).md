---
aliases: null
chatgpt: false
created: 2023-10-10
last_edited: 2023-10-10
publish: true
tags:
  - maths
type: lemma
---
# Statement

>[!important] Euler's product formula
>Given some $n \in \mathbb{N}$ with [[Prime decomposition|prime decomposition]] $n = \prod_{i=1}^k p_i^{e_i}$ with $p_i \in \mathbb{N}$ distinct [[Prime|primes]] and $e_i \in \mathbb{N}$. Then the [[Euler's totient function]] of $n$ is
>$$\phi(n) = \prod_{i=1}^k (p_i - 1)p_i^{e_i-1} = n \cdot \prod_{i=1}^k \left ( 1 - \frac{1}{p} \right ).$$

# Proof

For $1 \leq j < k$, $p_j^{e_j}$ is [[Coprime|coprime]] to $\prod_{i=j+1}^k p_i^{e_i}$. So by repeated application of [[Eulers product formula (totient function)#Claim 1|Claim 1]] we have
$$\phi(n) = \prod_{i=1}^k \phi(p_i^{e_i}).$$
Which from [[Eulers product formula (totient function)#Claim 2|Claim 2]] we get the result
$$\phi(n) = \prod_{i=1}^k (p_i - 1)p_i^{e_i-1} = n \cdot \prod_{i=1}^k \left ( 1 - \frac{1}{p} \right ).$$

## Claim 1

>[!important] Claim 1
>Let $m, n \in \mathbb{N}$ be [[Coprime|coprime]] then
>$$\phi(mn) = \phi(m) \phi(n).$$

## Proof of Claim 1

As $m$ and $n$ are coprime the [[Chinese remainder theorem]] gives has a bijection
$$b: \{i \vert 0 \leq i < m\} \times \{i \vert 0 \leq i < n\} \rightarrow \{i \vert 0 \leq i < mn\}$$
where $b(x,y) = x$ (mod $m$) and $b(x,y) = y$ (mod $n$).

Note if $gcd(b(x,y),mn) = 1$ if and only if $gcd(x,m) = 1$ and $gcd(y,n) = 1$ as $m$ and $n$ are [[Coprime|coprime]]. Therefore
$$b: \begin{array}\ \{ x \in \mathbb{N} \ \vert \ 0 < x \leq m, \ gcd(x,m) = 1 \} \times \\
\ \{y \in \mathbb{N} \ \vert \ 0 < x \leq n, \ gcd(x,n) = 1 \} \end{array} \mapsto \left \{b(x,y) \in \mathbb{N} \ \Bigg \vert \begin{array} \ 0 < b(x,y) \leq mn, \\ \ gcd(b(x,y),mn) = 1 \end{array} \right \}$$
and we have
$$\phi(mn) = \phi(m) \phi(n).$$

## Claim 2

>[!important] Claim 1
>If $p$ is prime and $k \geq 1$, then
>$$\phi(p^k) = p^k - p^{k-1} = p^{k-1}(p - 1) = p^k\left ( 1 - \frac{1}{p} \right ).$$

## Proof of Claim 2

As $p$ is [[Prime|prime]] we know the positive divisors of $p^k$ are powers of $p^i$ for $0 \leq i \leq k$.

Therefore of $gcd(p^k, x) > 1$ we know $x$ will have to be a multiple of $p$.

So $x = mp$ with $m \in \mathbb{Z}_{\not = 0}$ and for $0 < x < p^k$ we have $0 < m \leq p^{k-1}$.

So
$$\phi(p^k) = \big \vert \left \{x \in \mathbb{N} \ \vert \ 0 < x \leq p^k, \ gcd(x,p^k) = 1 \right \} \   \big \vert = p^k - p^{k-1}$$
giving the desired result.
