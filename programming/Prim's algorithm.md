---
aliases: 
type: algorithm
publish: true
created: 2023-10-02
last_edited: 2023-10-02
tags:
  - programming
chatgpt: false
---
# Prim's algorithm

This solves the [[Minimum Spanning Tree problem (MST)|MST]] problem using a method similar to [[Dijkstra's algorithm]]. It will use a [[Priority queue]] to do this. 

# Algorithm
```pseudocode
Prim's(G,w):
	Input: undirected graph G=(V,E) with weights w(e).
	Output: MST defined by the array prev
for all u in V
	cost(u) = inf
	prev(u) = nil
Pick any initial node u_0
cost(u_0) = 0

H = makequeue(V)
while H is not empty:
	v = deletemin(H)
	for each {v,z} in E:
		if cost(z) > w(v,z):
			cost(z) = w(v,z)
			prev(z) = v
			decreasekey(H,z)
output prev
```

## Correctness



## Run time

Initialisation takes $O(V)$ steps.

To fetch the key $v$ takes $O(\log(\vert V \vert))$ time from [[Priority queue]] data structure. This is executed $\vert V \vert$ times so takes $O(\vert V \vert \log(\vert V \vert))$.

We iterate over each edge twice and for each iteration we might have to call decreasekey which takes $O(\log(\vert V \vert))$ time from [[Priority queue]] implementation. So this takes $O(\vert E \vert \log(\vert V \vert))$. 

All together this takes $O(\vert V \vert) + O(\vert V \vert \log(\vert V \vert)) + O(\vert E \vert \log(\vert V \vert)) = O((\vert V \vert + \vert E \vert) \log(\vert V \vert))$.

