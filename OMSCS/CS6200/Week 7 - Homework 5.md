---
aliases: 
type: exercise
publish: false
created: 2023-09-30
last_edited: 2023-09-30
tags:
  - OMSCS
course: "[[CS6200 Introduction to Graduate Algorithms]]"
week: 7
chatgpt: false
---
# Week 7 - Homework 5 (unassessed) 

From [Algorithms](http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf) by S. Dasgupta, C. Papadimitriou, and U. Vazirani.

> [!question] Problem 7.10 max-flow = min-cut example
> For the following network, with edge capacities as shown, find the maximum flow from $S$ to $T$, along with a matching cut.

![[ex_7_10]]

Find the below flow in red

![[ex_7_10_flow]]

This has max capacity 13 with the min-cut being $\{S, C, F\}$ with $\{A, B, D, E, G, T\}$.

>[!question] Problem 7.17 Bottleneck edges
>Consider the following network (the numbers are edge capacities).
>(a) Find the maximum flow $f$ and a minimum cut. 
>(b) Draw the residual graph $G^f$ (along with its edge capacities). In this residual network, mark the vertices reachable from $S$ and the vertices from which $T$ is reachable. 
>(c) An edge of a network is called a bottleneck edge if increasing its capacity results in an increase in the maximum flow. List all bottleneck edges in the above network. 
>(d) Give a very simple example (containing at most four nodes) of a network which has no bottleneck edges. 
>(e) Give an efficient algorithm to identify all bottleneck edges in a network. (Hint: Start by running the usual network flow algorithm, and then examine the residual graph.)

![[ex_7_17]]

**Part a)**

The [[Flow|flow]] is in red below.

![[ex_7_17_flow]]

A minimum cut is $\{S, A, B\}$ $\{C, D, T\}$ with another one being $\{S, A, B, D\}$ $\{C, T\}$.

**Part b)**

This has [[Residual Network (flow)|residual network]] as follows. It has purple nodes that are reachable from $S$ and orange nodes with can reach $T$.

![[ex_7_17_res]]

**Part c)**

The Bottleneck edges are $(A,C)$ and $(B,C)$.

**Part d)**

![[ex_7_17_bottleneck_counter_example]]

The max [[Flow|flow]] is 1. If we increase the value of $(S,A)$ or $(A,T)$ then the max flow is still only 1.

**Part e)**

**Algorithm**

```Pseudocode
1. Find a maxflow f using Edmond's-Karp algorithm.
2. Calculate the resuide graph G^f.
3. Run BFS on G^f starting at S to find all the vertices accessible from S call these A.
4. Calculate the reverse of resuide graph G^f called (G^f)^R.
5. Run BFS on (G^f)^R starting at T to find all vertices that can access T call these B.
6. Return edges (a,b) with a in A and B in B.
```

**Correctness**



**Run Time**

The overall run time is limited by that of [[Edmonds-Karp algorithm]] $O(\vert E \vert^2 \cdot \vert V \vert)$ as I show below.

Step 1 takes the time of [[Edmonds-Karp algorithm]] $O(\vert E \vert^2 \cdot \vert V \vert)$ to produce the [[Max flow problem|max flow]] $f$.

Step 2 takes $O(\vert E \vert)$ as we need to go through all the edges of $G$ which are in $f$ to create $G^f$.

Step 3 and 5 runs the [[Breath-first search (BFS)|BFS]] algorithm which takes $O(\vert V \vert + \vert E \vert) = O(\vert E \vert)$ as $G$ is connected (note this is ran on $G^f$ or $(G^f)^R$ but that has at most $2 \vert E \vert$ edges).

Step 4 takes $O(\vert E \vert)$ as we need to invert each edge of $G^f$ (of which there is at most $2 \vert E \vert$ edges.

Step 5 takes $O(\vert E \vert \cdot \vert V \vert)$ as for each edge we need to check if its start vertex lies in $A$ and its end vertex lies in $\vert B \vert$. As $A$ and $B$ are disjoin we know this will take at most $\vert V \vert$ checks. 

All together this takes $O(\vert E \vert^2 \cdot \vert V \vert) + 4 O(\vert E \vert) + O(\vert E \vert \cdot \vert V \vert) = O(\vert E \vert^2 \cdot \vert V \vert)$. 


>[!question] Problem 7.19 verify max-flow
>Suppose someone presents you with a solution to a max-flow problem on some network. Give a linear time algorithm to determine whether the solution does indeed give a maximum flow.
