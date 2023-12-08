---
aliases: null
checked: false
created: 2023-11-02
last_edited: 2023-11-13
publish: true
tags:
  - maths
type: lemma
---
# Statement

> [!important] Lemma
> [[Minimum Spanning Tree problem (MST)]] is in [[Nondeterministic Polynomial time (NP)|NP]]

# Proof

The problem is in the correct form for a [[Search problems|search problem]]. It outputs a [[Minimum Spanning Tree problem (MST)|MST]] always as one always exists from the definition.

To verify a solution as we can first check it is a spanning tree by running [[Breath-first search (BFS)|BFS]] to verify it is connected and checking the size of the edge set is $\vert V \vert - 1$ to check it is a tree. To check it is minimal we can find a solution in polynomial time using [[Kruskal's algorithm]]. We can just check it's weight vs the weight of the proposed solution to check they match.

