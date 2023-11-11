---
aliases: null
checked: false
course: '[[CS6200 Introduction to Graduate Algorithms]]'
created: 2023-09-30
last_edited: 2023-11-11
publish: false
tags:
  - OMSCS
type: exercise
week: 7
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

## **Part a)**

The [[Flow|flow]] is in red below.

![[ex_7_17_flow]]

A minimum cut is $\{S, A, B\}$ $\{C, D, T\}$ with another one being $\{S, A, B, D\}$ $\{C, T\}$.

## **Part b)**

This has [[Residual Network (flow)|residual network]] as follows. It has purple nodes that are reachable from $S$ and orange nodes with can reach $T$.

![[ex_7_17_res]]

## **Part c)**

The Bottleneck edges are $(A,C)$ and $(B,C)$.

## **Part d)**

![[ex_7_17_bottleneck_counter_example]]

The max [[Flow|flow]] is 1. If we increase the value of $(S,A)$ or $(A,T)$ then the max flow is still only 1.

## **Part e)**

### **Algorithm**

```Pseudocode
1. Find a maxflow f using Edmond's-Karp algorithm.
2. Calculate the resuide graph G^f.
3. Run BFS on G^f starting at s to find all the vertices accessible from s call these A.
4. Calculate the reverse of resuide graph G^f called (G^f)^R.
5. Run BFS on (G^f)^R starting at t to find all vertices that can access t call these B.
6. Return edges (a,b) in G with a in A and B in B.
```

### **Correctness**

We know $(A, V \backslash A =: \overline{A})$ and $(B, V \backslash B =: \overline{B})$ are both [[Min st-cut problem|min st-cuts]]. From [[Week 7 - Homework 5#Claim 1|Claim 1]] any bottleneck edge must lie in $cut(A, \overline{A}) \cap cut(B, \overline{B})$. Therefore our algorithm returns all bottleneck edges.

Suppose our algorithm returns an edge $(a,b)$.

By the definition of $A$ we have a $s-a$ path in $G^f$. By the definition of $B$ we have a $b-t$ path in $G^f$ by increasing the capacity at $(a,b)$ this gives us a graph $\tilde{G}$ with an $(a,b)$ edge in $\tilde{G}^f$. Therefore we can augment $f$ along this $s-t$ path to increase the flow in $\tilde{G}$.

Therefore by definition $(a,b)$ is a bottleneck edge.

So our algorithm returns the correct result.

#### Claim 1

>[!important] Claim 1
>The bottleneck edges are exactly
>$$\bigcap_{(S,T) \ min \ st-cut} cut(S,T).$$

#### Proof of Claim 1

By the [[Max-flow min-cut Theorem]] we know that $value(f) = capacity(S,T)$ for any $(S,T)$ a [[Min st-cut problem|min st-cut]].

If $e$ is a bottleneck edge then increasing $c(e)$ increases the max flow in the [[Flow network|flow network]]. Therefore $capacity(S,T)$ must increase for each $(S,T)$ a [[Min st-cut problem|min st-cut]] in the original graph. For e to effect $capacity(S,T)$ it must lie in $cut(S,T)$.

This gives all bottleneck edges must lie in every [[Min st-cut problem|min st-cut]].

If $e$ lies in $cut(S,T)$ for every [[Min st-cut problem|min st-cut]] if I increase $c(e)$ the $capacity(S,T)$ rises for every [[Min st-cut problem|min st-cut]]. By the [[Max-flow min-cut Theorem]] this must increase the [[Max flow problem|max flow]] of the [[Flow network|flow network]].

Therefore any edge that lies in every [[Min st-cut problem|min st-cut]] is a bottleneck edge.

This gives the equality in claim 1.

### **Run Time**

The overall run time is limited by that of [[Edmonds-Karp algorithm]] $O(\vert E \vert^2 \cdot \vert V \vert)$ as I show below.

Step 1 takes the time of [[Edmonds-Karp algorithm]] $O(\vert E \vert^2 \cdot \vert V \vert)$ to produce the [[Max flow problem|max flow]] $f$.

Step 2 takes $O(\vert E \vert)$ as we need to go through all the edges of $G$ which are in $f$ to create $G^f$.

Step 3 and 5 runs the [[Breath-first search (BFS)|BFS]] algorithm which takes $O(\vert V \vert + \vert E \vert) = O(\vert E \vert)$ as $G$ is connected (note this is ran on $G^f$ or $(G^f)^R$ but that has at most $2 \vert E \vert$ edges).

Step 4 takes $O(\vert E \vert)$ as we need to invert each edge of $G^f$ (of which there is at most $2 \vert E \vert$ edges.

Step 5 takes $O(\vert E \vert \cdot \vert V \vert)$ as for each edge we need to check if its start vertex lies in $A$ and its end vertex lies in $\vert B \vert$. As $A$ and $B$ are disjoin we know this will take at most $\vert V \vert$ checks.

All together this takes $O(\vert E \vert^2 \cdot \vert V \vert) + 4 O(\vert E \vert) + O(\vert E \vert \cdot \vert V \vert) = O(\vert E \vert^2 \cdot \vert V \vert)$.


>[!question] Problem 7.19 verify max-flow
>Suppose someone presents you with a solution to a max-flow problem on some network. Give a linear time algorithm to determine whether the solution does indeed give a maximum flow.

## Algorithm

Do the following steps:

1. Build the [[Residual Network (flow)|residual network]] for [[Flow|flow]] $f$, $G^f$.
2. Run [[BFS]] on $G^f$ starting at $s$.
3. If $t$ is accessible then it is not a maximum flow otherwise return true.

## Correctness

Note our algorithm is just one step of the [[Ford-Fulkerson Algorithm]]. If it terminates with no path then starting [[Ford-Fulkerson Algorithm]] at $f$ would return $f$ which we have proven is a [[Max flow problem|max flow]].

If there is an augmenting path in $G^f$ then we can increase value of $f$.

Therefore either state returns correctly.

## Run time

The run time of this is $O(\vert E \vert)$.

As we have a [[Flow network|flow network]] the graph is connected so we can assume $\vert V \vert = O(\vert E \vert)$.

Step one takes $O(\vert E \vert)$ steps.

Step two takes $O(\vert V \vert + \vert E \vert) = O(\vert E \vert)$

Step three takes $O(1)$ as it is just checking a single value in a dictionary.

This gives $2O(\vert E \vert) + O(1) = O(\vert E \vert)$.
