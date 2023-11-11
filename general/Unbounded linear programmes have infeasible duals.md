---
aliases: null
checked: false
created: 2023-11-09
last_edited: 2023-11-09
publish: true
tags:
  - maths
type: lemma
---
# Statement

> [!important] Lemma
> If a [[Linear programme|linear programme]] is [[Unbounded linear programme|unbounded]] then its [[Dual linear programme|dual linear programme]] is [[Infeasible linear programme|infeasible]].

# Proof

If we have a [[Linear programme|linear programme]] given by $A$, $b$, and $c$. From the [[Weak duality theorem (linear programme)|weak duality theorem]] we have
$$
c^Tx \leq b^Ty.$$
for all feasible $x$ in the original [[Linear programme|linear programme]] and $y$ in the [[Dual linear programme|dual linear programme]]. Therefore if the original [[Linear programme|linear programme]] is [[Unbounded linear programme|unbounded]] then no such $y$ can exist making the [[Dual linear programme|dual linear programme]] [[Infeasible linear programme|infeasible]].
