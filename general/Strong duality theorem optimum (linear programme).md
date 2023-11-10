---
aliases: 
type: lemma
publish: true
created: 2023-11-10
last_edited: 2023-11-10
tags:
  - maths
chatgpt: false
---
# Statement

> [!important] Lemma
> A [[Linear programme|linear programme]] (given by $A$, $b$ and $c$) has an optimal point $x^{\ast}$ if and only if its [[Dual linear programme|dual linear programme]] has an optimal point $y^{\ast}$. These relate by
> $$c^Tx^{\ast} = b^Ty^{\ast}.$$

# Proof

From the [[Strong duality theorem (linear programme)]] we know the original [[Linear programme|linear programme]] is feasible and bounded if and only if the [[Dual linear programme|dual linear programme]] is feasible and bounded.

However, a [[Linear programme|linear programme]] has a solution if and only if it is feasible and bounded therefore providing the equivalence above.

The relationship between the points is given by the [[Weak duality theorem (linear programme)|weak duality theorem]].
