---
aliases:
checked: false
created: 2023-10-01
draft: false
last_edited: 2023-11-11
title: Kruskal's algorithm
tags:
  - programming
type: algorithm
---
# Kruskal's algorithm

This is an algorithm to solve the [MST](minimum_spanning_tree_problem_(mst).md) problem. It uses the [union-find](disjoint_set.md) data structure to help it identify cycles.

## Pseudocode

```pseudocode
Kruskal's(G,w):
	Input: undirected graph G=(V,E) with weights w(e).
	Output: MST edges X
1. Sort E by weights, smallest to largest
2. Set X to be empty
3. For e = (v,w) in E (ordered)
	1. If X U e does't have a cycle then X = X U e.
4. Output X
```

## Run time

For step 1, we use [merge sort](merge_sort.md) so this takes $O(\vert E \vert \log(\vert E \vert))$ time. Though as $\vert E \vert \leq \vert V \vert^2$, we can think of this as $O(\vert E \vert \log(\vert V \vert))$.

Step 3, has $\vert E \vert$ steps in each one we run two operations in the [union-find](disjoint_set.md) data structure both of which take $\log(\vert V \vert)$ time. So this is $O(\vert E \vert \log(\vert V \vert))$.

So in total this takes $O(\vert E \vert \log(\vert V \vert))$.

## Correctness

We prove by induction on the size of $X$ that this must be a subset of some [MST](minimum_spanning_tree_problem_(mst).md).

**Base case**

$X = \emptyset$.

Note there must be an [MST](minimum_spanning_tree_problem_(mst).md) $T$ and $\emptyset \subset T$. Therefore $X \subset T$ and we have shown it true for the base case.

**Induction case**

Suppose $X \subset T$ for some [MST](minimum_spanning_tree_problem_(mst).md) $T$.

Suppose we want to add some edge $e = (u,v)$. Let $S \subset V$ be the connected component of $X$ containing $u$. Note $v \in \overline{S} := V \backslash S$ as $X \cup \{e\}$ contains no cycles.

This forms [cut](cut_(graph).md) $V = S \cup \overline{S}$ with $e \in cut(S, \overline{S})$. $e$ is of minimum weight otherwise we would have added that edge already.

Therefore by the [cut property](cut_property.md) $X \cup \{e\}$ is contained in some [MST](mst.md) $T^{\ast}$.

This proves the induction case and we have that $X$ is always a subset of some [MST](mst.md).

**Conclusion**

As the algorithm considers adding every edge and adds it if and only if it doesn't add cycle the output is a [spanning](spanning_subgraph.md) [tree](tree_(graph).md). This is also minimal as $X$ is always a subset of an [MST](mst.md) giving the algorithm is correct.
