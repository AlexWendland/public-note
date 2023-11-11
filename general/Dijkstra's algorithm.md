---
aliases: null
checked: false
created: 2023-09-05
last_edited: 2023-11-11
publish: true
tags:
  - programming
type: algorithm
---
# Dijkstra's algorithm

This is an algorithm to solve the [[Find path in undirected graph|shortest path problem]] in [[Graph|undirected graphs]] or [[Directed graph|directed graphs]] $G = (V,E)$. It is based on [[Breath-first search (BFS)|Breath-first search]] but uses a [[Priority queue|priority queue]] instead of just a [[Queue|queue]]. It requires positive edge lengths $w: E \rightarrow \mathbb{R}_{>0}$.

```pseudocode
Dijkstra(G,w,s):
	Input: graph G=(V,E) with weights w(e) and a start vertex s.
	Output: For all vertices reachable from s a shortest path length dist
1. for all u in V
	1.1 dist(u) = inf
	1.2 prev(u) = nil
2. dist(s) = 0
3. H = makequeue(V)
4. while H is not empty:
	4.1 v = deletemin(H)
	4.2 for each {v,z} in E:
		4.2.1 if dist(z) > dist(v) + w(v,z):
			4.2.1.1 dist(z) = dist(v) + w(v,z)
			4.2.1.2 prev(z) = v
			4.2.1.3 decreasekey(H,z)
5. output dist
```

## Correctness


## Run time

To initialise $dist$ and $prev$ takes $O(\vert V \vert)$ time.

To fetch the key $v$ takes $O(\log(\vert V \vert))$ time from [[Priority queue]] data structure. This is executed $\vert V \vert$ times so takes $O(\vert V \vert \log(\vert V \vert))$.

We iterate over each edge twice and for each iteration we might have to call decreasekey which takes $O(\log(\vert V \vert))$ time from [[Priority queue]] implementation. So this takes $O(\vert E \vert \log(\vert V \vert))$.

All together this takes $O(\vert V \vert) + O(\vert V \vert \log(\vert V \vert)) + O(\vert E \vert \log(\vert V \vert)) = O((\vert V \vert + \vert E \vert) \log(\vert V \vert))$.
