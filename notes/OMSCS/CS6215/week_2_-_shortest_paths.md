---
aliases: []
checked: false
course_code: CS6215
course_name: Introduction to Graduate Algorithms
created: 2023-09-05
draft: false
last_edited: 2023-11-11
tags:
  - OMSCS
title: Week 2 - Shortest Paths
type: lecture
week: '2'
---

> [!tldr] Shortest path problem
> Given a [directed graph](../../general/directed_graph.md) $(V, E)$ with [edge weights](../../general/edge_weights.md) $w: E \rightarrow \mathbb{R}$ and a start vertex $s \in V$ - the shortest path problem is to find the shortest distance between $s \in V$ and $z \in V$ for every $x$. This is called $\mbox{dist}(z)$ with the formal definition
> $$\mbox{dist}_s(z) = \min_{\substack{p \mbox{ path}\\ s \mbox{ to } z}} \sum_{e \in p} w(e)$$
> where $p$ is a [path](../../general/path_(graph).md) that starts at $s$ and ends at $z$.

The classic solution to this is [Dijkstra's algorithm](../../general/dijkstra's_algorithm.md) which runs in $O((\vert V \vert + \vert E \vert)\log(\vert V \vert))$ time - however this requires that $w(e) > 0$ for all $e \in E$. We are looking at a more generic problem.

# Negative weight cycles

If there is a [cycle](../../general/cycle_(graph).md) that has negative total weight then the problem is not well defined as you can always extend you path with another loop of the cycle to reduce your weight.

The first step of our algorithm will be looking up if there is such a cycle.

# Case 1: No negative weight cycles

In this case you can guarantee that paths will only visit each vertex at most once. So they will use at most $\vert V \vert - 1$ edges. So it is enough to solve the subproblem.

Let $D(i,z)$ be the length of the shortest path between $s$ and $z$ that use at most $0 \leq i \leq n-1$ edges.

Base case: $D(0,s) = 0$ with $D(0,z) = \infty$ for $z \in V \backslash \{s\}$.

[Recursion](../../general/recursion.md): Let $D(i,z) = \min\{D(i-1,z), \min_{y \in V, (y,z) \in E} \{D(i-1, y) + w(y,z)\}\}$.

Solution: $D(\vert V \vert - 1, \cdot)$

This algorithm is called the [Bellman-Ford algorithm](../../general/bellman-ford_algorithm.md) and has the following pseudo code. For this let $n = \vert V \vert$

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

# Case 2: Negative weight cycles

If we run to the $\vert V \vert$ case (note before we stopped at $\vert V \vert - 1$) if any weights decrease then there was a shorter path visiting a vertex twice. This implies there is a negative weight cycle.

# All-pairs shortest path

> [!tldr] Shortest path problem (all pairs)
> Given a [directed graph](../../general/directed_graph.md) $(V, E)$ with [edge weights](../../general/edge_weights.md) $w: E \rightarrow \mathbb{R}$  - the shortest path problem is to find the shortest distance between $y,z \in V$ for every $y,z$. This is called $\mbox{dist}(y,z)$ with the formal definition
> $$\mbox{dist}(y,z) = \min_{\substack{p \mbox{ path}\\ y \mbox{ to } z}} \sum_{e \in p} w(e)$$
> where $p$ is a [path](../../general/path_(graph).md) that starts at $y$ and ends at $z$.

If you used the [Bellman-Ford algorithm](../../general/bellman-ford_algorithm.md) for each vertex this would take $O(\vert V \vert^2 \vert E \vert)$. Instead we will define the [Floyd-Warshall algorithm](../../general/floyd-warshall_algorithm.md) which takes $O(\vert V \vert^3)$ run time - which at worst the same as the [Bellman-Ford algorithm](../../general/bellman-ford_algorithm.md) as $\vert V \vert - 1 \leq \vert E \vert \leq \vert V \vert^2$ if it is connected without any double edges.

Let $V = \{x_1, \ldots, x_n\}$ in the set up of a new subproblem.

Let $D(i,s,t)$ be the length of the shortest path $s$ to $t$ only using $\{x_1, \ldots, x_i\}$ as intermediate vertices.

Base case,
$$D(0,s,t) = \begin{cases} w(s,t) & \mbox{if } (s,y) \in E\\ \infty & \mbox{otherwise}\end{cases}.$$
The recursion set then is:
$$D(i,s,t) = \min\{D(i-1,s,t), D(i-1,s,i) + D(i-1,i,t)\}.$$
> [!question] Why do you only visit $i$ once?

The pseudo code is as follows:

```pseudo
for s= 1 -> n:
	for t= 1 -> n:
		D(0,s,t) = inf
for (x, y) in E:
	D(0,x,y) = w(x,y)
for i = 1 -> n:
	for s = 1 -> n:
		for t = 1 -> n:
			D(i,s,t) = min(D(i-1,s,t), D(i-1, s, i) + D(i-1, i, t))
return D(n, . , . )
```

The run time of this algorithm is $O(n^2) + O(\vert E \vert) + O(n^3)$ as $\vert E \vert \leq n^2$ we have that the run time is $O(n^3)$.

# Negative weight cycles

Within the [Floyd-Warshall algorithm](../../general/floyd-warshall_algorithm.md) you detect negative weight cycles by looking at the values $D(n,x,x)$ if a negative weight cycle exists - this diagonal will have negative values.

> [!warning] [Bellman-Ford algorithm](../../general/bellman-ford_algorithm.md) vs [Floyd-Warshall algorithm](../../general/floyd-warshall_algorithm.md)
> [Bellman-Ford algorithm](../../general/bellman-ford_algorithm.md) only finds negative weight cycles reachable from that start vertex. Whereas [Floyd-Warshall algorithm](../../general/floyd-warshall_algorithm.md) will find any negative weight cycle in the graph.

# Further questions

From [Algorithms](http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf) by S. Dasgupta, C. Papadimitriou, and U. Vazirani.

>[!question] 4.21 Currency exchange
>Shortest path algorithms can be applied in currency trading. Let $c_1, c_2, \ldots , c_n$ be various currencies; for instance, $c_1$ might be dollars, $c_2$ pounds, and $c_3$ lire. For any two currencies $c_i$ and $c_j$ , there is an exchange rate $r_{i,j}$ ; this means that you can purchase $r_{i,j}$ units of currency $c_j$ in exchange for one unit of $c_i$. These exchange rates satisfy the condition that $r_{i,j} \cdot r_{j,i} < 1$, so that if you start with a unit of currency $c_i$, change it into currency $c_j$ and then convert back to currency $c_i$, you end up with less than one unit of currency $c_i$ (the difference is the cost of the transaction).
>
>(a) Give an efficient algorithm for the following problem: Given a set of exchange rates $r_{i,j}$, and two currencies $s$ and $t$, find the most advantageous sequence of currency exchanges for converting currency $s$ into currency $t$. Toward this goal, you should represent the currencies and rates by a graph whose edge lengths are real numbers.
>
>The exchange rates are updated frequently, reflecting the demand and supply of the various currencies. Occasionally the exchange rates satisfy the following property: there is a sequence of currencies $c_{i_1} , c_{i_2} , \ldots , c_{i_k}$ such that $r_{i_1,i_2} \cdot r_{i_2,i_3} \ldots r_{i_{k−1},i_k} \cdot r_{i_k,i_1} > 1$. This means that by starting with a unit of currency $c_{i_1}$ and then successively converting it to currencies $c_{i_2} , c_{i_3} , \ldots , c_{i_k}$ , and finally back to $c_{i_1}$ , you would end up with more than one unit of currency $c_{i_1}$. Such anomalies last only a fraction of a minute on the currency exchange, but they provide an opportunity for risk-free profits.
>
>(b) Give an efficient algorithm for detecting the presence of such an anomaly. Use the graph representation you found above.

