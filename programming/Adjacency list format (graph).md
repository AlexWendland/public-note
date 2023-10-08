---
aliases:
  - Adjacency list
  - adjacency list
type: data structure
publish: true
created: 2023-10-08
last_edited: 2023-10-08
tags:
  - programming
chatgpt: false
---
>[!tldr] Adjacency list
>For a [[Graph|graph]] $G = (V,E)$ (that can be a [[Directed graph|directed graph]] or [[Graph|undirected graph]]) the *adjacency list format* is a list of [[Neighbourhood (graph)|neighbourhoods]] $N_v = \{u \in V \vert (v,u) \in E\}$ for $v \in V$.
>

- This takes up $O(\vert V \vert + \vert E \vert)$ space as you need to store the vertices $V$ and lists of edges taking up $2\vert E \vert$ space.
- To check if two vertices are connected takes $O(\vert N_v \vert)$ time.
- Finding neighbours takes $O(\vert N_v \vert)$.