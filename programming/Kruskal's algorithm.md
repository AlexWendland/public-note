---
aliases: 
type: algorithm
publish: true
created: 2023-10-01
last_edited: 2023-10-01
tags:
  - programming
chatgpt: false
---
# Kruskal's algorithm

This is an algorithm to solve the [[Minimum Spanning Tree problem (MST)|MST]] problem. It uses the [[Disjoint set|union-find]] data structure to help it identify cycles.

## Pseudocode

```pseudocode
Kruskal's(G):
	Input: undirected graph G=(V,E) with weights w(e).
	Output: MST edges X
1. Sort E by weights, smallest to largest
2. Set X to be empty
3. For e = (v,w) in E (ordered)
	1. If X U e does't have a cycle then X = X U e.
4. Output X
```

## Run time

For step 1, we use [[Merge sort|merge sort]] so this takes $O(\vert E \vert \log(\vert E \vert))$ time. Though as $\vert E \vert \leq \vert V \vert^2$, we can think of this as $O(\vert E \vert \log(\vert V \vert))$.

Step 3, has $\vert E \vert$ steps in each one we run two operations in the [[Disjoint set|union-find]] data structure both of which take $\log(\vert V \vert)$ time. So this is $O(\vert E \vert \log(\vert V \vert))$.

So in total this takes $O(\vert E \vert \log(\vert V \vert))$.

## Correctness

