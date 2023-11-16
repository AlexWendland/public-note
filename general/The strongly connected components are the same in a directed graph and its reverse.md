---
aliases: null
checked: false
created: 2023-09-28
last_edited: 2023-11-11
publish: true
tags:
  - maths
type: lemma
---
> [!important] Lemma
> Let $G = (V,E)$ be a [[Directed graph|directed graph]] and $G^R = (V,E^R)$ be its [[Reverse directed graph|reverse]]. Both $G$ and $G^R$ have the same strongly connected components.

## Proof

For any two vertices $x,y \in V$ who are [[Strongly connected (directed graphs)|strongly connected]] in $G$ we need a path $p_{x,y}$ connecting $x$ to $y$ and path $p_{y,x}$ connecting $y$ to $x$.

The reverse of the path $p_{x,y}^R$ connected $y$ to $x$ in $G^R$ and $p_{y,x}^R$ connects $x$ to $y$ in $G^R$.

Therefore if two vertices are [[Strongly connected (directed graphs)|strongly connected]] in $G$ they are strongly connected in $G^R$.

As $G = \left (G^R \right )^R$ this also gives us that if two vertices are [[Strongly connected (directed graphs)|strongly connected]] in $G^R$ they are strongly connected in $G$.

Thus by the definition of [[Strongly connected components (directed graphs)|strongly connected components]] they must be identical in $G$ and $G^R$.
