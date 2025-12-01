---
aliases:
checked: false
created: 2023-10-03
draft: false
last_edited: 2023-11-11
tags:
  - programming
type: algorithm
---
# Ford-Fulkerson Algorithm

This is the naïve solution to the [[Max flow problem]]. It runs in [[Pseudo-polynomial time|pseudo-polynomial time]] depending on the size of the solution. A more developed algorithm that uses the same design is the [[Edmonds-Karp algorithm]].

Their main difference is that [[Edmonds-Karp algorithm]] must use [[Breath-first search (BFS)|BFS]] whereas [[Ford-Fulkerson Algorithm]] can use [[Depth-first search (DFS)|DFS]] also. For a runtime bound we require [[Ford-Fulkerson Algorithm]] to use integer capacities.

## Algorithm

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

## Correctness

This is proven as [[Flows are maximal if there is no augmenting path|flows are maximal if there is no augmenting path in the residual graph]]. The proof of this follows from the [[Max-flow min-cut Theorem]].

## Run time

If we assume $c(e) \in \mathbb{Z}$ are integers, then each iteration we will increase the flow by 1. Therefore we can have at most the max flow iterations $C$.

To run each iteration we need need to update the path length number of edges in the graph $G^f$ which takes $O(\vert V \vert)$ time. We need to run [[Breath-first search (BFS)|BFS]] which takes $O(\vert V \vert + \vert E \vert) = O(\vert E \vert)$ if we assume $G$ is connected. Then calculating $c(p)$ and updating the weights also takes $O(\vert V \vert)$ time. So all together a single iteration takes $O(\vert E \vert)$ time.

Therefore altogether the runtime is $O(C\vert E \vert)$.
