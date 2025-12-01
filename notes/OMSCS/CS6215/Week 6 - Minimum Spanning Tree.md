---
aliases:
checked: false
course: '[[CS6215 Introduction to Graduate Algorithms]]'
created: 2023-10-01
draft: false
last_edited: 2023-11-11
tags:
  - OMSCS
type: lecture
week: 6
---
# Week 6 - Minimum Spanning Tree

![[Minimum Spanning Tree problem (MST)#Statement]]

## Tree properties

It is useful to remind ourselves of some [[Tree (graph)|tree]] properties:

1. Tree on $n$ vertices has $n-1$ edges.
2. In a tree, there is exactly one path between every pair of vertices.
3. Any connected $G = (V,E)$ with $\vert E \vert = \vert V \vert - 1$ is a tree.

These are all proved by the [[Equivalent tree definitions|equivalent tree definitions]].

## Greed is good ... in this case

The greedy approach of just starting with an empty graph and keep adding valid edges of minimum weight, solves the [[Minimum Spanning Tree problem (MST)|MST]] problem.

The only problem is keeping track of the edges that are valid to include.

## Kruskal's Algorithm

![[Kruskal's algorithm#Pseudocode]]

![[Kruskal's algorithm#Run time]]

![[Kruskal's algorithm#Correctness]]

So the only think left to prove [[Kruskal's algorithm]] is correct is the proof of the cut property.

![[Cut property]]

## Prim's algorithm

![[Prim's algorithm#Algorithm]]

![[Prim's algorithm#Correctness]]
