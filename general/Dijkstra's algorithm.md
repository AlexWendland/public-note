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
Dijkstra(G,w,s):
	Input: graph G=(V,E) with weights w(e) and a start vertex s.
	Output: For all vertices reachable from s a shortest path length dist
for all u in V
	dist(u) = inf
	prev(u) = nil
dist(s) = 0

H = makequeue(V)
while H is not empty:
	v = deletemin(H)
	for each {v,z} in E:
		if dist(z) > dist(v) + w(v,z):
			dist(z) = dist(v) + w(v,z)
			prev(z) = v
			decreasekey(H,z)
output dist
```

## Correctness


## Run time

To initialise $dist$ and $prev$ takes $O(\vert V \vert)$ time.

To fetch the key $v$ takes $O(\log(\vert V \vert))$ time from [[Priority queue]] data structure. This is executed $\vert V \vert$ times so takes $O(\vert V \vert \log(\vert V \vert))$.

We iterate over each edge twice and for each iteration we might have to call decreasekey which takes $O(\log(\vert V \vert))$ time from [[Priority queue]] implementation. So this takes $O(\vert E \vert \log(\vert V \vert))$. 

All together this takes $O(\vert V \vert) + O(\vert V \vert \log(\vert V \vert)) + O(\vert E \vert \log(\vert V \vert)) = O((\vert V \vert + \vert E \vert) \log(\vert V \vert))$.