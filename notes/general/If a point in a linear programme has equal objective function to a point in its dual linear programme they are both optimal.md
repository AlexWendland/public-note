---
aliases: null
checked: false
created: 2023-11-09
last_edited: 2023-11-11
draft: false
tags:
  - maths
type: lemma
---
# Statement

> [!important] Lemma
> For a [[Linear programme|linear programme]] given by $A$, $b$, and $c$ if there is feasible point $x \in \mathbb{R}^n$ and $y \in \mathbb{R}^m$ feasible point in the [[Dual linear programme|dual linear programme]] such that
> $$ c^Tx = b^Ty$$
> then they are both optimal points in there respective [[Linear programme|linear programmes]].

# Proof

This follows from the [[Weak duality theorem (linear programme)|weak duality theorem]] as
$$c^Tx' \leq b^ty'$$
for all feasible $x'$ and $y'$ then by definition of their objective functions $x$ and $y$ are optimal.
