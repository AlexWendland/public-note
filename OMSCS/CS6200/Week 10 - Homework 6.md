---
aliases: 
checked: false
course: "[[CS6200 Introduction to Graduate Algorithms]]"
created: 2023-11-15
last_edited: 2023-11-15
publish: false
tags:
  - OMSCS
type: exercise
week: 10
---
# Week 10 - Homework 6 (unassessed)

From [Algorithms](http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf) by S. Dasgupta, C. Papadimitriou, and U. Vazirani.

> [!question] Problem 8.1 TSP optimization versus search
> Recall the traveling salesman problem:
> ![[Traveling salesman problem (search)#Statement]]
> and the optimisation version of the problem:
> ![[Traveling salesman problem#Statement]]
> Show that if [[Traveling salesman problem (search)|TSP search]] can be solved in [[Polynomial time|polynomial time]] then we can solve [[Traveling salesman problem|TSP]] in [[Polynomial time|polynomial time]] also.



>[!question] Problem 8.2 Search problems vs Decision problems
>Suppose you have an [[Polynomial time|polynomial time]] algorithm that tells you if there is a [[Rudrata path]] in a given [[Graph|graph]] $G$. Show that you can use it to develop a [[Polynomial time|polynomial time]] algorithm to solve the [[Rudrata path problem]].



>[!question] Problem 8.3 Stingy SAT
>Stingy SAT: Given a [[Boolean function|boolean function]] $f$ that is in [[Conjunctive normal form (CNF)|CNF]] and an integer $k$, find a satisfying assignment for $f$ with at most $k$ variables are true if it exists. 
>Prove that the stingy SAT problem is [[NP-Complete]].



>[!question] Problem 8.4 Clique-3
>Suppose we reduce the [[Clique of a given size problem]] but on [[Graph|graphs]] with [[Degree (graph)|degree]] at most 3.
>a) Prove that Clique-3 is in [[Nondeterministic Polynomial time (NP)|NP]].
>...
>d) Describe an $O(\vert V \vert^4)$ algorithm for clique-3.

a) Follows as [[Clique of a given size problem is in NP]].

d)

Notice this only has 2 real cases of interest.
- $g = 1$ the answer is true.
- $g = 2$ we just have to check if there is an edge.
- $g = 3$, we are looking for a triangle.
- $g = 4$, we are looking for copy of $k_4$ in the graph (if there are 4 than 4 vertices this will be a disconnected copy)
- $g > 4$ the answer is false as the degree is limited to 3.

```
g_3_algorithm(G)
	Input: suppose we have a graph G = (V,E) in adjacency list form (A_v for v in V) where |A_v| <= 3.
	Output: A triangle in the graph or that no such triangle exists.
1. Let S = V.
2. While S is not empty.
	1. Pop off the next element of v in S.
	2. For w in A_v:
		1. If u in A_v intersect A_w return v, w, u
3. Return no such triangle exists
```

This algorithm takes $O(\vert V \vert)$ as we need to go through each element of $V$ and then do atmost 3 intersections of two sets of size at most 3 which can take $3 \times 9 = 27$ operations. 

```
g_4_algorithm(G)
	Input: suppose we have a graph G = (V,E) in adjacency list form (A_v for v in V) where |A_v| <= 3.
	Output: A copy of K_4 exists in G.
1. For v in V:
	1.1. For w in A_V,
		1.1.1. if A_W /= A_v U {v} \ {w}
			1.1.1.1 continue
	1.2. return v U A_v
2. return no such component exists.
```

Step 1 takes $\vert V \vert$ steps. At worst each step compares 3 sets of size 3 which takes $3 \times 9 = 27$ operations. So this algorithm takes $O(\vert V \vert)$ time.

Therefore to check for cliques it takes $O(\vert V \vert)$ by running the right sub-algorithm given the $g$. 

>[!question] Problem 8.8 Exact 4-SAT
>Exact 4-SAT: Suppose we are given a [[Boolean function|boolean function]] $f$ that is in [[Conjunctive normal form (CNF)|CNF]], each clause has exactly 4 literals, and each variable appears at most once in each clause. The goal is to find a satisfying assignment, if one exists.
>Prove that Exact 4-SAT is [[NP-Complete|NP-complete]]. 



>[!question] Problem 8.10 Subgraph isomorphism
>



>[!question] 8.14 Clique + Independent set (HW 6 assessed)

>[!question] 8.19 Kite
