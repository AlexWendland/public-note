---
aliases: null
checked: false
created: 2023-11-03
last_edited: 2023-11-11
publish: true
tags:
  - programming
  - graph-theory
type: lemma
---
# Statement

> [!important] Lemma
> [[Clique of a given size problem]] is in [[Nondeterministic Polynomial time (NP)|NP]].

# Proof

This problem is in the form of a [[Search problems|search problem]] as either you provide a [[Clique (graph)|clique]] of the required size or you say no such set exists.

For a [[Graph|undirected graph]] $G = (V,E)$, positive integer $g > 0$, and supposed solution $S$ to the [[Clique of a given size problem]]. It takes $O(\vert E \vert + \vert V \vert)$ to check this solution. We have to do two steps:
- Check $\vert S \vert \geq g$.
- Check for all $(u,v) \in E$ for all $u,v \in S$.
The first step takes $O(\vert V \vert)$ and the second $O(\vert V \vert^2)$.

Therefore this problem is in [[Nondeterministic Polynomial time (NP)|NP]].
