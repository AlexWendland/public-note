---
aliases:
  - Bellman-Ford
  - Bellman-Ford equation
checked: false
created: 2023-09-05
last_edited: 2023-11-11
draft: false
tags:
  - programming
type: algorithm
---
# Bellman-Ford algorithm

Suppose we are trying to solve the problem of how to [[Find path in undirected graph]] where we have no negative weight cycles.

In this case you can guarantee that paths will only visit each vertex at most once. So they will use at most $\vert V \vert - 1$ edges. So it is enough to solve the subproblem.

Let $D(i,z)$ be the length of the shortest path between $s$ and $z$ that use at most $0 \leq i \leq n-1$ edges.

Base case: $D(0,s) = 0$ with $D(0,z) = \infty$ for $z \in V \backslash \{s\}$.

[[Recursion]]: Let $D(i,z) = \min\{D(i-1,z), \min_{y \in V, (y,z) \in E} \{D(i-1, y) + w(y,z)\}\}$.

Solution: $D(\vert V \vert - 1, \cdot)$

## Pseudocode

For this let $n = \vert V \vert$

```pseudo
D(0,s) = 0
D(0,z) = inf for all z /= s
for i=1 -> n-1
	for all z in V
		D(i,z) = D(i-1,z)
		for (y,z) in E:
			D(i,z) = min(D(i,z), w(y,z) + D(i-1,y))
return D(n-1, . )
```

The update equation used in the pseudocode is called the *Bellman-Ford equation*. This has applications in distributed path finding algorithms.

## Run time

This takes $O(\vert V \vert \vert E \vert)$ as you could rewrite this psudo-code like this:

```pseudo
D(0,s) = 0
D(0,z) = inf for all z /= s
for i=1 -> n-1
	D(i,z) = D(i-1,z) for all z
	for all (x,y) in E
		D(i,y) = min(D(i,y), w(x,y) + D(i-1,x))
return D(n-1, . )
```
