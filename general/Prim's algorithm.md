---
aliases: null
checked: false
created: 2023-10-02
last_edited: 2023-11-11
draft: false
tags:
  - programming
type: algorithm
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

# Correctness

Note that functionally Prim's algorithm is slowly building a tree $X$ using the closes vertex to the currently constructed tree $X$ that is not already in it.

We prove by induction on the size of $X$ that this must be a subset of some [[Minimum Spanning Tree problem (MST)|MST]].

**Base case**

$X = \emptyset$.

Note there must be an [[Minimum Spanning Tree problem (MST)|MST]] $T$ and $\emptyset \subset T$. Therefore $X \subset T$ and we have shown it true for the base case.

**Induction case**

Suppose $X \subset T$ for some [[Minimum Spanning Tree problem (MST)|MST]] $T$.

Suppose we find the next closest vertex $v \in V \backslash X$. I.e. There is some minimum weight edge $(x,v) \in cut(X,\overline{X})$ the [[Cut (graph)|cut edges]] of $X$.

Therefore by the [[Cut property|cut property]] $X \cup \{e\}$ is contained in some [[MST]] $T^{\ast}$.

This proves the induction case and we have that $X$ is always a subset of some [[MST]].

**Conclusion**

As the algorithm runs until each vertex is added to the tree $X$. $X$ is a [[Spanning subgraph|spanning]] [[Tree (graph)|tree]] which is a subset of a [[Minimum Spanning Tree problem (MST)|MST]]. Therefore is an [[Minimum Spanning Tree problem (MST)|MST]] in its own right.

# Run time

Initialisation takes $O(V)$ steps.

To fetch the key $v$ takes $O(\log(\vert V \vert))$ time from [[Priority queue]] data structure. This is executed $\vert V \vert$ times so takes $O(\vert V \vert \log(\vert V \vert))$.

We iterate over each edge twice and for each iteration we might have to call decreasekey which takes $O(\log(\vert V \vert))$ time from [[Priority queue]] implementation. So this takes $O(\vert E \vert \log(\vert V \vert))$.

All together this takes $O(\vert V \vert) + O(\vert V \vert \log(\vert V \vert)) + O(\vert E \vert \log(\vert V \vert)) = O((\vert V \vert + \vert E \vert) \log(\vert V \vert))$.

