---
aliases:
checked: false
created: 2023-09-28
draft: false
last_edited: 2023-11-11
tags:
  - programming
type: problem
---
# Statement

> [!tldr] Find [[Path (graph)|path]] between vertices in an [[Directed graph|directed graph]]
> Given an [[Directed graph|directed graph]] $G = (V,E)$ and two vertices $a,b \in V$. How can we find a [[Path (graph)|path]] in $G$ between them. Sometime we will also have a weighting $W: E \rightarrow D$ and we want to minimise the path length.

## Solutions

- [[DFS to find path in a directed graph]]
	- Runs in $O(\vert V \vert \cdot \vert E \vert)$
	- Unweighted.
