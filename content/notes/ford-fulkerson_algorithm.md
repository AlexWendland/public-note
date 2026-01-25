---
aliases:
created: 2023-10-03
date_checked:
draft: false
last_edited: 2023-11-11
tags:
  - programming
title: Ford-Fulkerson Algorithm
type: algorithm
---

This is the naïve solution to the [Max flow problem](max_flow_problem.md). It runs in [pseudo-polynomial time](pseudo-polynomial_time.md) depending on the size of the solution. A more developed algorithm that uses the same design is the [Edmonds-Karp algorithm](edmonds-karp_algorithm.md).

Their main difference is that [Edmonds-Karp algorithm](edmonds-karp_algorithm.md) must use [BFS](breath-first_search_(bfs).md) whereas [Ford-Fulkerson Algorithm](ford-fulkerson_algorithm.md) can use [DFS](depth-first_search_(dfs).md) also. For a runtime bound we require [Ford-Fulkerson Algorithm](ford-fulkerson_algorithm.md) to use integer capacities.

# Algorithm

```pseudocode
ford_fulkerson(G, c, s, t)
	Input: A flow network with integer capacities.
	Output: A max flow on the network.
1. Set f(e) = 0 for all e in E.
2. Build the residual network G^f for the current flow f.
3. Check for any s-t paths p in G^f using BFS (or DFS).
	1. If no such path then output f.
4. Given p let c(p) = min_{e in p} c^f(e).
5. Augment f by c(p) units along p.
	1. f(e) = f(e) + c(p) for forward edges.
	2. f(e) = f(e) - c(p) for backward edges.
6. Repeat from step 2.
```

# Correctness

This is proven as [flows are maximal if there is no augmenting path in the residual graph](flows_are_maximal_if_there_is_no_augmenting_path.md). The proof of this follows from the [Max-flow min-cut Theorem](max-flow_min-cut_theorem.md).

# Run time

If we assume $c(e) \in \mathbb{Z}$ are integers, then each iteration we will increase the flow by 1. Therefore we can have at most the max flow iterations $C$.

To run each iteration we need need to update the path length number of edges in the graph $G^f$ which takes $O(\vert V \vert)$ time. We need to run [BFS](breath-first_search_(bfs).md) which takes $O(\vert V \vert + \vert E \vert) = O(\vert E \vert)$ if we assume $G$ is connected. Then calculating $c(p)$ and updating the weights also takes $O(\vert V \vert)$ time. So all together a single iteration takes $O(\vert E \vert)$ time.

Therefore altogether the runtime is $O(C\vert E \vert)$.
