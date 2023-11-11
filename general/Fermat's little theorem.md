---
aliases: null
checked: false
created: 2023-10-09
last_edited: 2023-10-09
publish: true
tags:
  - maths
type: lemma
---
# Statement

>[!important] Fermat's little theorem
>For any prime number $p$ and $a \in \mathbb{Z}$ we have
>$$a^p = a \ (mod \ p).$$

# Proof

Note if $a$ is a multiple of $p$ the statement is true as both sides are zero. It suffices to prove this for $0 < a < p$ as all other integers are congruent to one of these mod $p$. Moreover, we only need to show $a^{p-1} = 1$ (mod $p$).

Consider the set $S = \{a \cdot i \ (mod \ p) \vert 0 < i < p\}$. From the proof of [[Modular multiplicative inverse existence]] we know $S = \{i \vert 0 < i < p\}$.

Therefore by multiplying the entries in $S$ together we have
$$ (p-1)! = z^{p-1} (p-1)! \ (mod \ p).$$
However as $i$ for $0 < i < p$ is coprime to $p$ from [[Modular multiplicative inverse existence|modular multiplicative inverse existence lemma]]. We know $(p-1)!$ therefore has a multiplicative inverse mod $p$. So we have
$$ 1 = z^{p-1} \ (mod \ p)$$
as desired.

# Theory

This is generalised by [[Euler's theorem (modular arithmetic)]].
