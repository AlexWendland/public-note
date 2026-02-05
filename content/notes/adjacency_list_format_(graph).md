---
aliases:
  - Adjacency list
  - adjacency list
created: 2023-10-08
date_checked:
draft: false
last_edited: 2026-02-05
tags:
  - programming
title: Adjacency list format (graph)
type: data structure
---
>[!definition] Adjacency list
>For a [graph](graph.md) $G = (V,E)$ (that can be a [directed graph](directed_graph.md) or [undirected graph](graph.md)) the *adjacency list format* is a list of [neighbourhoods](neighbourhood_(graph).md) $N_v = \{u \in V \vert (v,u) \in E\}$ for $v \in V$.
>

- This takes up $O(\vert V \vert + \vert E \vert)$ space as you need to store the vertices $V$ and lists of edges taking up $2\vert E \vert$ space.
- To check if two vertices are connected takes $O(\vert N_v \vert)$ time.
- Finding neighbours takes $O(\vert N_v \vert)$.
