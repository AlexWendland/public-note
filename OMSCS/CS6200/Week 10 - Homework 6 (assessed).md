---
aliases: 
type: exercise
publish: false
created: 2023-10-27
last_edited: 2023-10-27
tags:
  - OMSCS
course: "[[CS6200 Introduction to Graduate Algorithms]]"
week: 10
chatgpt: false
---
# Week 10 - Homework 6 (assessed)

>[!question] Question
>A star of size $N$ is a graph with exactly $N+1$ vertices such that one vertex is connected to all other vertices and no other edges exists in the graph. Consider the star-search problem:
> 
> Input: [[Graph|Undirected graph]] $G = (V,E)$ and a natural number $k > 0$.
> Output: A set $X$ of $k+1$ vertices such that the [[Induced subgraph|induced subgraph]] on $X$ is a star, or report NO if such a set does not exist.
> 
> Show the star-search problem is [[NP-Complete]].

To show that star-search problem is [[NP-Complete]] I will do the following:

1. Demonstrate that the star search problem is in the class of [[Nondeterministic Polynomial time (NP)|NP]] problems. 
	1. Show the star search problem is of the correct form to be a [[Search problems|search problem]]. 
	2. Given a candidate solution to an instance of our star search problem, we show that you can validate that solution in [[Polynomial time|polynomial time]].
2. Then demonstrate that the star search problem is at least as hard as the independent set problem - which is known to be [[NP-Complete]]. The specific steps are as follows:
	1. Show how an instance of the independent set problem is converted to an instance of the star search problem, in polynomial time.
	2. Show how a solution the star problem can be converted to a solution for the independent set problem, again in polynomial time.
	3. Show that a solution for the independent set problem exists if and only if a solution to the star problem exists.

## Star search problem has [[Nondeterministic Polynomial time (NP)|NP]] complexity

### Correct form

The set up of the star search problem we either get a solution or it returns that there is no solution. This is of the required form to be a [[Search problems|search problem]].

### Validation in [[Polynomial time|polynomial time]]

For $G = (V,E)$ and $k$  we need to check we can validate a solution $X$ in polynomial time. The algorithm below validates a solution in $O(\vert V \vert \vert E \vert)$ time providing such an algorithm.

#### Algorithm

1. If $X$ is not of size $k+1$ return this is not a solution.
2. Form the [[Induced subgraph]] $I = (X, E' := \{(u,v) \in E \vert u,v \in X \})$.
3. Check $I$ is a star:
	1. Check $\vert E' \vert = k$. 
	2. Take the first two edges in $I$.
		1. If there is not exactly 1 vertex shared between both edges return this is not a solution.
		2. If there is exactly 1 vertex shared between both edges set that vertex to be $v$.
	3. Set $S = \emptyset$ 
	4. For $e \in E'$:
		1. If $v$ isn't in $e$ return that it isn't a star.
		2. If the edge connects $v$ to $v$ return that it isn't a star.
		3. Let $u$ be the vertex that isn't $v$ in $e$.
			1. If $u$ in $S$ return that it isn't a star.
			2. Add $u$ to $S$.
4. Return $X$ is a solution.

#### Correctness

Suppose $X \subset V$ such that the [[Induced subgraph|induced subgraph]] $I$ in $G$ is a star of size $k$.

For $I$ to be a star of size $k$ we have $X$ is of size $k+1$, so it passes step $1$. 

As $I$ is a star of size $k$ it has a vertex $v'$ that is shared in all edges and all edge involve $v'$ and a distinct vertex $u \in X \backslash \{v'\}$. So there is a [[Bijection|bijection]] $b: E' \rightarrow X \backslash \{v'\}$.

Due to the [[Bijection|bijection]] $b$ we know $\vert E' \vert = \vert X \vert - 1 = k$. So this passes step 3.1.

In step 3.2, we find $v := v'$ as it is the only vertex shared between all edged.

In step 3.4 when iterating through $e \in E'$ at each step we inspect $u := b(e)$ which is a distinct element for each $e \in E'$ so we never return this is false.

Therefore the algorithm returns True 

Suppose $X \subset V$ passes the algorithm.

From step 1, $X$ must be of size $k+1$. 

From step 3.1, we know the induced graph $I$ has $k$ edges.

Let $v \in X$ be the vertex found in step $3.2$.

From step 3.4.1 we know $v$ is in every edge and step 3.4.2 guarantees no edge is a loop on $v$.

From step 3.4.3 we know each edge $e \in E$ connects $v$ to a different vertex $u \in X \backslash \{v\}$. However, as $\vert E' \vert = k$ this means for every $u \in X \backslash \{v\}$ there is an edge $(v,u) \in E'$. 

Therefore $X \subset V$ is of size $k+1$ and induces a star of size $k$ by the definition. 

#### Run time

The run time is $O(\vert E \vert \vert V \vert)$.

Step 1 takes $O(\vert V \vert)$ as given that $X$ is a subset of $V$ it can be of size at most $\vert V \vert$.

Step 2 takes $O(\vert E \vert)$ as we have to check all edges to see if they connect two vertices of $X$.

Step 3.1 takes $O(\vert E \vert)$ as we have to check the number of edges that could be size at most $\vert E \vert$.

Step 3.2 takes $O(1)$ time as we select 2 edges and run $4$ checks on the vertices involved.

Step 3.4 iterates through all edges in $E'$ (which can be of size at most $\vert E \vert$).

Step 3.4.1 and 3.4.2 perform 2 checks so it runs in $O(1)$ time.

Step 3.4.3 involves checking set inclusion so takes at most $O(\vert V \vert)$ checks.

All together this takes 
$$\begin{align*}O(\vert V \vert) + O(\vert E \vert) + O(\vert E \vert) + O(1) + O(\vert E \vert)(O(1) + O(\vert V \vert)) & = O(1) + O(\vert V \vert) + 3 O(\vert E \vert) + O(\vert E \vert \vert V \vert)\\ & = O(\vert E \vert \vert V \vert). \end{align*}$$

## Reduction of independent set problem to the star search problem

To reduce the independent set problem to the star search problem we have to show:
1. Show how an instance of the independent set problem is converted to an instance of the star search problem, in polynomial time.
2. Show how a solution the star problem can be converted to a solution for the independent set problem, again in polynomial time.
3. Show that a solution for the independent set problem exists if and only if a solution to the star problem exists.

Below is the statement of the independent set problem.

>[!tldr] Independent set problem
>Input: An [[Graph|undirected graph]] $G = (V,E)$ and an integer $k$.
>
>Output: An independent set $X \subset V$ of size $k$ or reports NO independent set of size $k$ exists in $G$.

### Independent set problem to star search problem

Suppose we are given $G = (V,E)$ and $k$ for the independent set problem. 

Let $x \not \in V$ then define the [[Graph|undirected graph]]  $G' = (V \cup \{x\}, E \cup \{(x,v) \vert v \in V\})$.

Then run the star search algorithm on $G'$ and $k$.

It takes $O(\vert V \vert)$ to produce $G'$ and $G'$ has polynomial size in the size of $G$.

### Star search problem solution to Independent set solution

Suppose we are given a solution $X$ to the star search problem of size $k$.

If $k=1$ $X$ will have 2 vertices - return a single vertex in $\{x \in X \vert x \in V\}$.

If $k \geq 2$ let $v \in X$ be the vertex such that in induced graph $I = (X, \{(a,b) \in E' \vert a,b \in X \}$ the degree of $v$ in $I$ is greater than 1 (the non-leaf node).

Then return the set $X \backslash \{v\}$.

Finding $v \in X$ takes $O(\vert E \vert + \vert V \vert)$ as we have to search all edges in $\vert E' \vert$. So converting the solution of the star problem to the solution of the independent set solution takes polynomial time.

>[!Note] The return set $X \backslash \{v\} \subset V$ is in the correct domain
>We know $\vert X \vert = k + 1 \geq 3$ (as the $k=1$ case is handled differently). 
>Suppose $x \in X$, then there is another two distinct vertices $a,b \in X$ ($a \not = b$) such that $a,b \in V$. From the definition of $G'$ then we have $(x,a), (x,b) \in E'$ meaning the degree of $x$ in the induced graph $I$ is greater than 1. Giving $v := x$ by the definition of $v$.
>This gives $x \not \in X \backslash \{v\}$ and we have $X \backslash \{v\} \subset V$.

### A solution for the independent set problem exists if and only if a solution to the star problem exists

Suppose we are given a graph $G = (V,E)$ and positive integer $k \geq 1$.

#### $\Rightarrow$

Suppose a solution for the independent set problem exists, $Y \subset V$ - where the induced graph on $Y$ is an independent set and $\vert Y \vert = k$.

Then our reduction defines graph 
$$G' = (V \cup \{x\}, E \cup \{(x,v) \vert v \in V\}).$$
Note that $G'$ has a star of size $k$ defined by $X := Y \cup \{x\}$.

As $Y$ is an independent set in $G$ the induced edges of $X$ on $G'$ are $\{(x,y) \vert y \in Y\}$. This gives a star of size $k$ from the definition.

So the star search problem on $G'$ with size $k$ has a solution.

#### $\Leftarrow$

Suppose the star search problem on $G'$ with size $k$ has a solution $X$ - where the induced graph on $X$ is a star of size $k$ with $\vert X \vert = k+1$.

If $k = 1$ then any vertex $v \in V$ is a solution - therefore $v \in X \cap V$ is a solution.

If $k \geq 2$ then let $v \in X$ be non-leaf node in the induced graph $I$ of $X$ in $G'$.

As we showed in the note above if $x \in X$ then $v = x$. Giving $X \backslash \{v\} \subset V$. 

From the definition of a star we know that the induced graph on $X$ is 
$$(X , \{(u,v)  \vert u \in X \backslash \{v\}\}).$$
Therefore the induced graph on $X \backslash \{v\} \subset V$ is an independent set in $G'$ and therefore an independent set in graph $G$. 

We have $\vert X \backslash \{v\} \vert = k$ so $X \backslash \{v\}$ is a solution to the independent set problem of size $k$ in $G$.

## Summary

I have shown that the star search problem has complexity class [[Nondeterministic Polynomial time (NP)|NP]]. Moreover, we can reduce the independent set problem of size $k$ to the star search problem of size $k$. As the independent set problem is [[NP-Complete]] this gives us that the star search problem is also [[NP-Complete]].