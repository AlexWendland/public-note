---
aliases: 
type: exercise
publish: false
created: 2023-10-07
last_edited: 2023-10-07
tags:
  - OMSCS
course: "[[CS6200 Introduction to Graduate Algorithms]]"
week: 7
chatgpt: false
---
# Week 7 - Homework 5 (assessed)

>[!question] Question
>You are given a undirected, connected, weighted graph $G = (V,E)$ with positive edge weights $w: E \rightarrow \mathbb{R}_{>0}$. Give a linear time $O(
>\vert E \vert +\vert V \vert)$ algorithm to decide if an input edge $e^{\ast} = (x, y) \in E$, is part of some MST of $G$ or not. You should describe your algorithm in words (a list is okay); no pseudocode. Explain why it is correct and justify its running time.

>[!note] Notation
>I am denoting the given edge as $e^{\ast} = (x,y)$, this differs to the original question. 

## Algorithm

1. Filter through $e \in E$ and select edges $E' = \{e \in E \vert w(e) < w(e^{\ast})\}$.
2. Run [[Breath-first search (BFS)|Breath-first search]] on $G' = (V,E')$ starting at $x$ returning $dist: V \rightarrow \mathbb{R}_{\geq 0}$ (a function telling us the minimum length of a path from $x$ to $v$ with $dist(v) = \infty$ if no such path exists).
3. If $dist(y) < \infty$ output that $e^{\ast}$ is not in an [[MST]].
4. Otherwise output that is it. 

## Correctness

There are two cases if the algorithm returns $e^{\ast}$ is in an [[MST]] or if it does not. If we show correctness in these two cases then we have the algorithm as a whole is correct. 

### Suppose the algorithm returns that $e^{\ast}$ is in an [[Minimum Spanning Tree problem (MST)|MST]]

Suppose we are running [[Kruskal's algorithm]] on $G$ which we recall below.

```pseudocode
Kruskal's(G,w):
	Input: undirected graph G=(V,E) with weights w(e).
	Output: MST edges X
1. Sort E by weights, smallest to largest
2. Set X to be empty
3. For e = (v,w) in E (ordered)
	3.1. If X U e does't have a cycle then X = X U e.
4. Output X
```

When we sort $E$ by weights from the definition of $E' = \{e \in E \vert w(e) < w(e^{\ast})\}$ we can assume that all edges before $e^{\ast}$ are in $E'$. (Note we are assuming edges of equal weight to $e^{\ast}$ appear after it - which is a valid sorting.)

Suppose we are at step 3 and we select $e^{\ast}$. As $G' = (V, E')$ has no path between $x$ and $y$ the same must hold for our $X \subset E'$.

Therefore $X \cup \{e^{\ast}\}$ has no cycle and this is our new $X$. 

From the correctness of [[Kruskal's algorithm]], we know $X \cup \{e^{\ast}\}$ is a subset of some [[MST]] $T$ giving $e^{\ast}$ is in a [[MST]] and our algorithm is correct in this case.

### Suppose the algorithm returns that $e^{\ast}$ is not in an [[Minimum Spanning Tree problem (MST)|MST]]

For a contradiction suppose instead we have an [[Minimum Spanning Tree problem (MST)|MST]] $T^{\ast} = (V, E^{\ast})$ where $e^{\ast} \in E^{\ast}$.

As $T^{\ast}$ is a connected tree we know by removing $e^{\ast}$ this separates $T^{\ast}$ into two connected components $X,Y \subset V$ where $x \in X$ and $y \in Y$. Let $B = E^{\ast} \backslash \{e^{\ast}\}$.    

Now recall the cut property, reworded in our context. 

>[!important] Cut property
>Let $G = (V,E)$ be an [[Graph|undirected graph]] with an edge weight $w: E \rightarrow \mathbb{R}$. Suppose $B \subset E$ is part of an [[Minimum Spanning Tree problem (MST)|MST]] $T^{\ast}$. Let $X \subset V$ be a [[Cut (graph)|cut]] where no edge of $B$ is in the [[Cut (graph)|cut edges]] $cut(X, Y)$. Then for $e' \in cut(X, Y)$ of minimum weight - $B \cup \{e'\}$ is part of an [[Minimum Spanning Tree problem (MST)|MST]] $T$.

As the algorithm returned that $G' = (V, E')$ has a path between $x$ and $y$, then we know that $E' \cap cut(X,Y) \not = \emptyset$.

By the definition $e \in E'$ if $w(e) < w(e^{\ast})$ therefore the minimum weight edge $e' \in cut(X,Y)$ has weight $w(e') < w(e^{\ast})$.

By the [[Cut property]] $B \cup \{e'\}$ is part of a [[Minimum Spanning Tree problem (MST)|MST]] $T$. Note 
$$\vert B \cup \{e'\}\vert = \vert ( E^{\ast} \backslash \{e^{\ast}\} ) \cup \{e'\} \vert = \vert E^{\ast} \vert - 1 + 1 = \vert E^{\ast} \vert = \vert V \vert - 1$$
as $T^{\ast} = (V,E^{\ast})$ is a [[Tree (graph)|tree]]. Giving that $T = (V, B \cup \{e'\})$ as a tree has $\vert V \vert - 1$ edges.

However 
$$w(T) = w(B) + w(e') < w(B) + w(e^{\ast}) = W(T^{\ast})$$
contradicting $T^{\ast}$ was an [[Minimum Spanning Tree problem (MST)|MST]] in the first place. 

Therefore no such $T^{\ast}$ exists and our algorithm is correct. 

## Run time

The overall run time is $O(\vert E \vert + \vert V \vert)$, with explanation below.

Step 1 involves going through the list of edges and checking their weights. This takes $O(\vert E \vert)$ steps.

Step 2 involves running [[Breath-first search (BFS)|Breath-first search]] on a graph with $\vert V \vert$ vertices and $< \vert E \vert$ edges so this takes at most $O(\vert V \vert + \vert E \vert)$ time.

Step 3 and 4 involves checking one value so is $O(1)$.

In total we have a run time of $O(\vert E \vert) + O(\vert V \vert + \vert E \vert) + O(1) = O(\vert E \vert + \vert V \vert)$.