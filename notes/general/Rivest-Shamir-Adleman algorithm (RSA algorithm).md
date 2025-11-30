---
aliases:
  - RSA
checked: false
created: 2023-10-09
last_edited: 2023-11-11
draft: false
tags:
  - programming
type: algorithm
---
# Rivest-Shamir-Adleman algorithm (RSA algorithm)

To set up the [[Rivest-Shamir-Adleman algorithm (RSA algorithm)|RSA]] algorithm you do the following:

1. You pick 2 n-bit random primes $p$ and $q$.
3. You choose $e$ relatively prime to $(p-1)(q-1)$.
4. You let $N = pq$ and you publish the public key $(N,e)$.
5. You compute your private key $d = e^{-1}$ (mod $(p-1)(q-1)$).

Then to encrypt a message $m \in \mathbb{Z}$ someone else does the following:

1. Take a public key $(N,e)$.
2. You compute $y = m^e$ (mod $N$).
3. Then you send message $y$.

Lastly to decipher the message using the private key you do the following.

1. You receive the message $y$.
2. You calculate $y^d = m^{ed} = m$ (mod $pq$).
3. Revel in your secrete knowledge.

Note this works from [[Euler's theorem (modular arithmetic)]] as $ed = 1 + k(p-1)(q-1)$ so
$$ y^d = m^{ed} = m \cdot (m^{(p-1)(q-1)})^k = m \cdot 1^k = m \ (mod \ pq)$$
as $\phi(pq) = (p-1)(q-1)$.

## Limitations

1. gcd(m,N) = 1
	1. Otherwise the encrypted message $y^e$ and $N$ share a common factor $p$ or $q$ and they can work out $p$ and $q$ using the [[Extended Euclidean algorithm|extended Euclidean algorithm]] and work out $e$.
2. $m < N < 2^n$
	1. Otherwise looking at the message mod $N$ gives the wrong message.
	2. This is normally gotten around by breaking the message up and giving it in little chunks.
3. $m^e > N$
	1. Otherwise they can just calculate the $e$'th root to understand the message.
	2. If $m$ is too small then you normally augment it by a factor $r$ and encrypt $m + r$ sending $r$ afterwards to let the person know they need to subtract it.
4. Can't send the same $m$ and $e$ out multiple times.
	1. If you have 3 public keys $(N_1, 3)$, $(N_2, 3)$ and $(N_3,3)$ then using the [[Chinese remainder theorem]] you can recover the original message $m$.
5. We assume factoring $N = qp$ is hard.
	1. If it was not other people would be able to recover $(p-1)(q-1)$ and calculate $d$.
