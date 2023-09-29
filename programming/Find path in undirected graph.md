---
aliases: 
type: problem
publish: true
created: 2023-09-28
last_edited: 2023-09-28
tags:
  - programming
chatgpt: false
---
# Statement

> [!tldr] Find [[Path (graph)|path]] between vertices in an [[Graph|undirected graph]]
> Given an [[Graph|undirected graph]] $G = (V,E)$ and two vertices $a,b \in V$. How can we find a [[Path (graph)|path]] in $G$ between them. Sometime we will also have a weighting $W: E \rightarrow D$ and we want to minimise the path length.

## Solutions

- [[DFS to find path in an undirected graph]]
	- This runs in $O(\vert V \vert \cdot \vert E \vert)$
	- This doesn't use weights.