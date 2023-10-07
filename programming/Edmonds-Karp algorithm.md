---
aliases: 
type: algorithm
publish: true
created: 2023-10-07
last_edited: 2023-10-07
tags:
  - programming
chatgpt: false
---
# Edmonds-Karp algorithm

This is an algorithm to solve the [[Max flow problem|max flow]] problem but also solves the [[Min st-cut problem|min st-cut]] problem on a [[Flow network|flow network]] $(G = (V,E), c, s, t)$. This is very similar to the [[Ford-Fulkerson Algorithm]] but with the use of [[Breath-first search (BFS)|BFS]] when picking the s-t path.

## Algorithm

```pseudocode
edmonds_karp(G, c, s, t)
	Input: A flow network.
	Output: A max flow on the network.
1. Set f(e) = 0 for all e in E.
2. Build the residual network G^f for the current flow f.
3. Check for any s-t paths p in G^f using BFS.
	1. If no such path then output f.
4. Given p let c(p) = min_{e in p} c^f(e).
5. Augment f by c(p) units along p.
	1. f(e) = f(e) + c(p) for forward edges.
	2. f(e) = f(e) - c(p) for backward edges.
6. Repeat from step 2.
```

## Correctness

This proof is the same as [[Ford-Fulkerson Algorithm]].

## Run time

This takes $O(\vert E \vert^2 \cdot \vert V \vert)$.

From [[Edmonds-Karp algorithm#Claim 1|Claim 1]] we know we only have to loop $\vert E \vert \cdot \vert V \vert /2$ times. 

To run each iteration we need need to update the path length number of edges in the graph $G^f$ which takes $O(\vert V \vert)$ time. We need to run [[Breath-first search (BFS)|BFS]] which takes $O(\vert V \vert + \vert E \vert) = O(\vert E \vert)$ if we assume $G$ is connected. Then calculating $c(p)$ and updating the weights also takes $O(\vert V \vert)$ time. So all together a single iteration takes $O(\vert E \vert)$ time.

Therefore together this takes $O(\vert E \vert^2 \cdot \vert V \vert)$ times.

## Claim 1

>[!important] Claim 1
>The algorithm has at most $\vert E \vert \cdot \vert V \vert/2$ loops.

### Proof

Note that as we let $c(p) = \min_{e \in p} c^f(e)$ in each round of the algorithm we remove at least one edge of $G^f$. (This isn't to say the number of edges reduces each round - as we may add in more edges to $G^f$ than we have deleted.)

From [[Edmonds-Karp algorithm#Claim 2|Claim 2]] we know each edge gets deleted and reinserted to $G^f$ at most $\vert V \vert/2$ times.

Therefore we can only iterate $\vert E \vert \cdot \vert V \vert / 2$ times. As there has to be an edge to remove. 

## Claim 2

>[!important] Claim 2
>For every edge $e \in E$, $e$ is deleted and reinserted to $G^f$ at most $\vert V \vert/2$ times.

### Proof

## Claim 3

>[!important] Claim 3
>For a vertex $v \in V$ the edge distance between $x$ and $v$ in $G^f$ can only increase as we go to later stages of the algorithm.

### Proof

For a given edge $(v,w) \in E$ we have the following conditions for it to be added or removed from the [[Residual Network (flow)|residual network]]:

- Add $(v,w)$ to $G^f$ if the [[Flow|flow]] was full and reduced.
	- So $(w,v) \in p$.
- Remove $(v,w)$ from $G^f$ if the [[Flow|flow]] is now full.
	- So $(v,w) \in p$.
- Add $(w,v)$ to $G^f$ if the [[Flow|flow]] was empty.
	- So $(v,w) \in p$.
- Remove $(w,v)$ from $G^f$ if the [[Flow|flow]] was positive and is now empty.
	- So $(w,v) \in p$.

So if we add $(y,z)$ to $G^f$ then $(y,z) \in p$. 

Similarly if we remove $(y,z)$ in $G^f$ then $(y,z) \in p$.

To prove this claim we have to show that if an edge is added then 



