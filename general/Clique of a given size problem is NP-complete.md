---
aliases: 
type: lemma
publish: true
created: 2023-11-03
last_edited: 2023-11-03
tags:
  - maths
chatgpt: false
---
# Statement

> [!important] Lemma
> [[Clique of a given size problem]] is [[NP-Complete]].

# Proof

We have already shown that [[Clique of a given size problem is in NP]].

We will show that [[Independent set of a given size]] has a [[Many-one reduction (problem)|many-one reduction]] to [[Clique of a given size problem]].

Suppose we have an [[Graph|undirected graph]] $G = (V,E)$ and $g > 0$ a positive integer. If we are looking for an [[Independent set (graph)|independent set]] of size $g$, we will pass $G^C$ the [[Complement graph|complement graph]] and $g$ to the [[Clique of a given size problem]].

Calculating the [[Complement graph|complement graph]] takes $O(\vert V \vert^2)$, therefore this reduction is in [[Polynomial time|polynomial time]].

Then if a [[Clique (graph)|clique]] $S$ is returned in $G^C$ then we return this as our [[Independent set (graph)|independent set]] in $G$.

This takes $O(1)$ as we are doing no transformations to the output. 

As [[Cliques in G are independent sets in the complement]] we have a solution to the [[Independent set of a given size]] if and only if we have a solution to the [[Clique of a given size problem]]. 

This gives [[Clique of a given size problem]] is [[NP-hard]] making it [[NP-Complete|NP-complete]].
