---
aliases: null
chatgpt: false
created: 2023-11-03
last_edited: 2023-11-03
publish: true
tags:
  - programming
  - graph-theory
type: lemma
---
# Statement

> [!important] Lemma
> [[Vertex cover of a given size]] is [[Nondeterministic Polynomial time (NP)|NP]].

# Proof

First note that this problem is of the correct form to be a [[Search problems|search problem]]. Either there is a [[Vertex cover|vertex cover]] of the required size and we return it or we say no such cover exists.

For a [[Graph|undirected graph]] $G = (V,E)$ if we are provided with a purposed solution $C$ to the problem there are two steps to checking it:
- Check that $\vert C \vert \geq g$, this takes $O(\vert V \vert)$.
- Check for every edge $(u,v) \in E$ that $u \in S$ or $v \in S$, that takes $O(\vert E \vert \cdot \vert V \vert)$.
Therefore checking a solution takes [[Polynomial time|polynomial time]] in the input size.

This gives that the [[Vertex cover of a given size]] is in [[Nondeterministic Polynomial time (NP)|NP]].
