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

[[Recursion]]: Let $D(i,z) = \min_{y \in V, (y,z) \in E} \{ D(i-1, y) + w(y,z)\}