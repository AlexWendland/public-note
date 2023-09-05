---
aliases: []
type: lecture
publish: true
created: 2023-09-05
last_edited: 2023-09-05
tags:
  - OMSCS
course: "[[CS6200 Introduction to Graduate Algorithms]]"
week: "2"
chatgpt: false
---
# Week 2 - Shortest Paths

> [!tldr] Shortest path problem
> Given a [[Directed graph|directed graph]] $(V, E)$ with [[Edge weights|edge weights]] $w: E \rightarrow \mathbb{R}$ and a start vertex $s \in V$ - the shortest path problem is to find the shortest distance between $s \in V$ and $z \in V$ for every $x$. This is called $\mbox{dist}(z)$ with the formal definition
> $$\mbox{dist}_s(z) = \min_{\substack{p \mbox{ path}\\ s \mbox{ to } z}} \sum_{e \in p} w(e)$$ 
> where $p$ is a [[Path (graph)|path]] that starts at $s$ and ends at $z$.

The classic solution to this is [[Dijkstra's algorithm]] which runs in $O((\vert V \vert + \vert E \vert)\log(\vert V \vert))$ time - however this requires that $w(e) > 0$ for all $e \in E$. We are looking at a more generic problem.

## Negative weight cycles

If there is a [[Cycle (graph)|cycle]] that has negative total weight then the problem is not well defined as you can always extend you path with another loop of the cycle to reduce your weight. 

The first step of our algorithm will be looking up if there is such a cycle.

## Case 1: No negative weight cycles

In this case you can guarantee that paths will only visit each vertex at most once. So they will use at most $\vert V \vert - 1$ edges. So it is enough to solve the subproblem.

Let $D(i,z)$ be the length of the shortest path between $s$ and $z$ that use at most $0 \leq i \leq n-1$ edges.

Base case: $D(0,s) = 0$ with $D(0,z) = \infty$ for $z \in V \backslash \{s\}$. 

[[Recursion]]: Let $D(i,z) = \min\{D(i-1,z), \min_{y \in V, (y,z) \in E} \{D(i-1, y) + w(y,z)\}\}$.

Solution: $D(\vert V \vert - 1, \cdot)$

This algorithm is called the [[Bellman-Ford algorithm]] and has the following pseudo code. For this let $n = \vert V \vert$

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

## Case 2: Negative weight cycles 

If we run to the $\vert V \vert$ case (note before we stopped at $\vert V \vert - 1$) if any weights decrease then there was a shorter path visiting a vertex twice. This implies there is a negative weight cycle.

## All-pairs shortest path

> [!tldr] Shortest path problem (all pairs)
> Given a [[Directed graph|directed graph]] $(V, E)$ with [[Edge weights|edge weights]] $w: E \rightarrow \mathbb{R}$  - the shortest path problem is to find the shortest distance between $y,z \in V$ for every $y,z$. This is called $\mbox{dist}(y,z)$ with the formal definition
> $$\mbox{dist}(y,z) = \min_{\substack{p \mbox{ path}\\ y \mbox{ to } z}} \sum_{e \in p} w(e)$$ 
> where $p$ is a [[Path (graph)|path]] that starts at $y$ and ends at $z$.

If you used the [[Bellman-Ford algorithm]] for each vertex this would take $O(\vert V \vert^2 \vert E \vert)$. Instead we will define the [[Floyd-Warshall algorithm]] which takes $O(\vert V \vert^3)$ run time - which is better than this as $\vert V \vert - 1 \leq \vert E \vert \leq \vert V \vert^2$ if it is connected without any double edges. 

Let $V = \{x_1, \ldots, x_n\}$ now set up a new subproblem.

Let $D(i,s,t)$ be the length of the shortest path $s$ to $t$ only using $\{x_1, \ldots, x_i\}$ as intermediate vertices.

Base case,
$$D(0,s,t) = \begin{cases} w(s,t) & \mbox{if } (s,y) \in E\\ \infty & \mbox{otherwise}\end{cases}.$$
The recursion set then is:
$$D(i,s,t) = \min\{D(i,s,t), D(i-1,s,i) + D(i-1,i,t)\}.$$
