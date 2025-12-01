---
aliases:
checked: false
created: 2023-11-03
draft: false
last_edited: 2023-11-11
tags:
  - programming
type: lemma
---
# Statement

> [!important] Lemma
> [[Independent set of a given size]] is in [[Nondeterministic Polynomial time (NP)|NP]].

# Proof

This problem is in the form of a [[Search problems|search problem]] as either you provide an [[Independent set (graph)|independent set]] of the required size or you say no such set exists.

For a [[Graph|undirected graph]] $G = (V,E)$, positive integer $g > 0$, and supposed solution $S$ to the [[Independent set of a given size]]. It takes $O(\vert E \vert + \vert V \vert)$ to check this solution. We have to do two steps:
- Check $\vert S \vert \geq g$.
- Check for all $(u,v) \in E$ that $u \not \in S$ or $v \not \in S$.
The first step takes $O(\vert V \vert)$ and the second $O(\vert E \vert)$.

Therefore this problem is in [[Nondeterministic Polynomial time (NP)|NP]].
