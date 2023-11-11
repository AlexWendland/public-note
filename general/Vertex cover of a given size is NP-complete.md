---
aliases: null
chatgpt: false
created: 2023-11-03
last_edited: 2023-11-03
publish: true
tags:
  - graph-theory
  - programming
type: lemma
---
# Statement

> [!important] Lemma
> [[Vertex cover of a given size]] is [[NP-Complete|NP-complete]].

# Proof

As [[Vertex cover of a given size is NP]] we only need to show the problem is [[NP-hard]].

We will show that the [[Independent set of a given size]] has a [[Many-one reduction (problem)|many-one reduction]] to the [[Vertex cover of a given size]].

Suppose we have a [[Graph|undirected graph]] $G = (V,E)$ and $g > 0$ a positive integer and we are looking for a [[Independent set (graph)|independent set]] of size $g$.

Provide $G$ and $\vert V \vert - g$ to the [[Vertex cover of a given size]] problem. This takes $O(1)$ as we are doing no manipulation to the graph.

If we are provided a [[Vertex cover|vertex cover]] $C$ of size at most $\vert V \vert - g$ return the set $I := V \backslash C$  as the solution to the [[Independent set of a given size]] problem. This takes $O(\vert V \vert)$ to run so is [[Polynomial time|polynomial time]] in the input size. (Here $\vert I \vert = \vert V \vert - \vert I \vert \geq \vert V \vert - (\vert V \vert - g) \geq g$ so is of the correct size.)

If there is a solution to the [[Independent set of a given size]] with the size of at least $g$ then the compliment is a [[Vertex cover|vertex cover]] of size at most $\vert V \vert - g$ from [[Vertex cover if and only if the complement is an independent set]].

Similarly if there is a solution to the [[Vertex cover of a given size]] with size of at most $\vert V \vert - g$ then the compliment is a [[Independent set (graph)|independent set]] of size at least $g$ from [[Vertex cover if and only if the complement is an independent set]].

Therefore as [[Independent set of a given size is NP-complete]] we have [[Vertex cover of a given size]] is [[NP-hard]], which from above gives us it is [[NP-Complete|NP-complete]].



