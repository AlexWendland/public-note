---
aliases: null
chatgpt: false
created: 2023-10-09
last_edited: 2023-10-09
publish: true
tags:
  - maths
type: lemma
---
>[!important] Lemma
>Suppose we have some set $X$ and [[associative]] [[Binary operation|binary operation]] $\cdot$  with a unit $1$ such that $x \cdot 1 = 1 \cdot x = x$ then two-sided inverses if they exists are unique.

## Proof

Suppose for some element $x \in X$ and let $x_1^{-1}$ and $x_2^{-1}$ be two-sided inverses. Then observe
$$
x_1^{-1} = x_1^{-1} \cdot 1 = x_1^{-1} \cdot ( x \cdot x_2^{-1}) = (x_1^{-1} \cdot x) \cdot x_2^{-1} = 1 \cdot x_2^{-1} = x_2^{-1}
$$
giving equality.
