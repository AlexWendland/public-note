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

>[!important] Euclid's rule
>For integers $x,y \in \mathbb{Z}$ where $x \geq y > 0$ we have
>$$gcd(x,y) = gcd(x \ mod \ y, y).$$

# Proof

We prove more generally that
$$gcd(x,y) = gcd(x + c\cdot y, y).$$
which will give the desired result from the definition of [[Modular arithmetic|modular arithmetic]].

Note that if $d \vert x$ ($x = d \cdot \overline{x}$) and $d \vert y$ ($y = d \overline{y}$) then $d \vert x + c \cdot y$ ($x + c \cdot y = d(\overline{x} + c \cdot \overline{y})$).

Also if $d \vert y$ ($y = d \overline{y}$) and $d \vert x + c \cdot y$ ($x + c \cdot y = d \overline{z}$) then $d \vert x$ ($x = d(\overline{z} - c \cdot \overline{y}$)).

Therefore both sides share divisors and so the [[Greatest common divisor|greatest common divisor]].
