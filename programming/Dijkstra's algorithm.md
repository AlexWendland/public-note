---
aliases: 
type: algorithm
publish: true
created: 2023-09-05
last_edited: 2023-09-29
tags:
  - programming
chatgpt: false
---
# Dijkstra's algorithm

This is an algorithm to solve the [[Find path in undirected graph|shortest path problem]] in [[Graph|undirected graphs]] or [[Directed graph|directed graphs]] $G = (V,E)$. It is based on [[Breath-first search (BFS)|Breath-first search]] but uses a [[Priority queue|priority queue]] instead of just a [[Queue|queue]]. It requires positive edge lengths $w: E \rightarrow \mathbb{R}_{>0}$.

```pseudocode
dijkstra(G, l, s)
Input: Graph = (V,E) 
```