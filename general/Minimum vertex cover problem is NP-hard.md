---
aliases: null
chatgpt: false
created: 2023-11-03
last_edited: 2023-11-03
publish: true
tags:
  - maths
type: lemma
---
# Statement

> [!important] Lemma
> [[Minimum vertex cover problem]] is [[NP-hard]].

# Proof

We have shown that [[Vertex cover of a given size is NP-complete]]. So we will find a [[Many-one reduction (problem)|many-one reduction]] of [[Vertex cover of a given size]] to [[Minimum vertex cover problem]] to show it is [[NP-hard]].

Suppose we have an [[Graph|undirected graph]] $G = (V,E)$ and a positive integer $g > 0$. If we are looking for a [[Vertex cover|vertex cover]] of size at most $g > 0$, pass $G$ to our solution to the [[Minimum vertex cover problem]].

This takes $O(1)$ as we are doing no manipulations.

We get back minimum cover $C$. If $\vert C \vert \leq g$ return $C$ to the [[Vertex cover of a given size]] problem, otherwise return no. This step takes $O(\vert V \vert)$ so is [[Polynomial time|polynomial time]] in the input size.

If there is a [[Vertex cover|vertex cover]] of size less than $g$ then the minimum [[Vertex cover|vertex cover]] will have size less than $g$.

Equally if the minimum [[Vertex cover|vertex cover]] has size less than $g$ then there is a [[Vertex cover|vertex cover]] of size less than $g$.

So we have that [[Vertex cover of a given size]] has a [[Many-one reduction (problem)|many-one reduction]] to [[Minimum vertex cover problem]]. Giving that [[Minimum vertex cover problem]] is [[NP-hard]].


