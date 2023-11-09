---
aliases: 
type: lemma
publish: true
created: 2023-11-09
last_edited: 2023-11-09
tags:
  - maths
chatgpt: false
---
# Statement

> [!important] Lemma
> Let $x$ be a feasible point for a [[Linear programme|linear programme]] given by $A$, $b$, and $c$. Let $y$ be a feasible point for the [[Dual linear programme|dual linear programme]] then we have the following inequality
> $$c^Tx = \sum_j c_j x_j \leq \sum_i b_i y_i = y^Tb.$$

# Proof

Recall that the [[Dual linear programme|dual linear programme]] was specified by $-A^T$, $-c$ and $-b$. So we have
$$-A^Ty \leq -c, \mbox{ therefore } A^Ty \geq c$$
and so we have
$$c^Tx \leq (A^Ty)^Tx = y^TAx \leq y^Tb.$$

