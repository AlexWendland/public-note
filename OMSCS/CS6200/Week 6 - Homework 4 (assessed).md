---
aliases: null
checked: false
course: '[[CS6200 Introduction to Graduate Algorithms]]'
created: 2023-09-30
last_edited: 2023-09-30
publish: false
tags:
  - OMSCS
type: exercise
week: 6
---
# Week 6 - Homework 4 (assessed)

>[!question] Pre-ramble
>Let $G = (V,E)$ be an undirected graph, and let $s,t \in V$, $s \not = t$ be distinct vertices of $G$. Each edge in $G$ is assigned one of two colors, white or gold.

For my answer I will represent this colouring as a map $c: E \rightarrow \{white, gold\}$.

>[!question] Part a
>Design an algorithm that determines if there is a path from $s$ to $t$ with edges of only one color (that is, a path containing either white edges only or gold edges only).

## Algorithm

My algorithm is defined by the following steps.

1. Divide the edges up into two sets the white edges $E_{white} = \{ e \in E \vert\ c(e) = \ white\}$ and the gold edges $E_{gold} = \{e \in E \vert \ c(e) = \ gold\}$. (Using the definition of $c$ in my pre-ramble.)
2. Run Breath-first search on $G_{white} = (V, E_{white})$ starting at $s$ returning $dist_{white}$.
3. If $dist_{white}(t) < \infty$ output that there is a path.
4. Run Breath-first search on $G_{gold} = (V, E_{gold})$ starting at $s$ returning $dist_{gold}$.
5. If $dist_{gold}(t) < \infty$ output that there is a path.
6. Otherwise output that no path exists using only one vertex.

## Correctness

Suppose there is a path between $s$ and $t$ that uses edges $p$. If this uses only one $colour \in \{white, gold\}$ then for all $e \in p$ $c(e) = colour$. Therefore $p \subset E_{colour}$ giving $dist_{colour}(t) \leq \vert p \vert$. Therefore my algorithm will return true in this case.

Suppose no path exists between $s$ and $t$ that uses edges from one colour. As $G_{colour}$ only has edges from one colour no path can exists between $s$ and $t$ in it. Therefore $dist_{colour}(t) = \infty$ and my algorithm will return that no path exists.

## Run time

The run time is $O(\vert V \vert + \vert E \vert)$, with the explanation below.

Dividing the edges up takes $O(\vert E \vert)$ time, as we require to run through each edge.

As BFS takes $O(\vert V \vert + \vert E \vert)$ running BFS on $G_{white}$ takes $O(\vert V \vert + \vert E_{gold} \vert) = O(\vert V \vert + \vert E \vert)$ time.

I assume checking in an array is constant time O(1).

Similarly the second run of BFS and checking an array value takes $O(\vert V \vert + \vert E \vert)$ and $O(1)$ respectively.

In summary this is $O(\vert E \vert) + 2O(\vert V \vert + \vert E \vert) + 2O(1) = O(\vert V \vert + \vert E \vert)$.

>[!question] Part b
>Design an algorithm that determines if there is a path from $s$ to $t$ such that all white edges appear before all gold edges in the path.

## Algorithm

My algorithm is defined by the following steps.

1. Divide the edges up into two sets the white edges $E_{white} = \{ e \in E \vert\ c(e) = \ white\}$ and the gold edges $E_{gold} = \{e \in E \vert \ c(e) = \ gold\}$. (Using the definition of $c$ in my pre-ramble.)
2. Run Breath-first search on $G_{white} = (V, E_{white})$ starting at $s$ returning $dist_{white}$.
4. Run Breath-first search on $G_{gold} = (V, E_{gold})$ starting at $t$ returning $dist_{gold}$.
5. Run through each vertex $v \in V$
	1. if $dist_{white}(v) < \infty$ and $dist_{gold}(v) < \infty$ output that such a path does exist.
6. If no such $v$ matches that condition return that no such path exists.

## Correctness

Suppose there exists a path $p = e_1 e_2 \ldots e_n$ in $G$ from $s$ to $t$ such that there exists a $0 \leq k \leq n$ with $c(e_i) = white$ for $i \leq k$ and $c(e_{i}) = gold$ for $i >k$. Let $v \in V$ be the vertex the subpath $e_1 e_2 \ldots e_k$ terminates at (if $k=0$ this will be $s$).

Then $dist_{white}(v) \leq k$ as $e_1e_2 \ldots e_k$ is a path in $G_{white}$ from $s$ to $v$.

Also as $e_n, e_{n-1}, \ldots e_{k+1}$ is a path from $t$ to $v$ using only $gold$ edges then $dist_{gold}(v) \leq n - k$.

Therefore our algorithm would return that such a path does exist.

Suppose our algorithm returned that such a path exists.

Therefore there is some $v \in V$ such that $dist_{white}(v) = k < \infty$ so there exists some path $e_1 e_2 \ldots e_k$ between $s$ and $v$ such that $c(e_i) =\ white$.

Equally as $dist_{gold}(v) = n < \infty$ so there exists some path $f_1f_2 \ldots f_n$ between $t$ and $v$ such that $c(f_i) = \ gold$.

As $G$ is undirected, $e_1e_2 \ldots e_kf_n \ldots f_2 f_1$ is a path between $s$ and $t$ where all white edges appear before gold edges.

This gives that our algorithm says there is a path if and only if such a path exists - proving it is correct.

## Run time

The run time is $O(\vert V \vert + \vert E \vert)$, with the explanation below.

Dividing the edges up takes $O(E)$ time, as we require to run through each edge.

As BFS stakes $O(\vert V \vert + \vert E \vert)$ running BFS on $G_{white}$ takes $O(\vert V \vert + \vert E_{gold} \vert) = O(\vert V \vert + \vert E \vert)$ time.

Similarly the second run of BFS takes $O(\vert V \vert + \vert E \vert)$.

Lastly for each vertex we have to check two values which we will assume takes constant time. Therefore these checks take $O(\vert V \vert)$.

In summary this is $O(\vert E \vert) + 2O(\vert V \vert + \vert E \vert) + O(\vert V \vert) = O(\vert V \vert + \vert E \vert)$.
