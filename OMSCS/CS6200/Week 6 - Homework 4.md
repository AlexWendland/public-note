---
aliases: null
chatgpt: false
course: '[[CS6200 Introduction to Graduate Algorithms]]'
created: 2023-09-30
last_edited: 2023-09-30
publish: false
tags:
  - OMSCS
type: exercise
week: 6
---
# Week 6 - Homework 4 (unassessed)

From [Algorithms](http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf) by S. Dasgupta, C. Papadimitriou, and U. Vazirani.

> [!question] Problem 3.3 Topological ordering example
> Run the [[Depth-first search (DFS)|DFS]]-based [[Topological sorting (DAG)|topologically sort]] algorithm on the following graph. Whenever you have a choice of vertices to explore always pick the one that is alphabetically first.
> ![[ex_3_3]]
> 1. Indicate the pre and post numbers of the nodes
> 2. What are the source and sinks of the graph?
> 3. What is the topological ordering found by the algorithm?
> 4. How many topological orderings does this graph have?

## Part 1

| Vertex | pre | post |
| ------ | --- | ---- |
| A      | 1   | 14   |
| B      | 15  | 16   |
| C      | 2   | 13   |
| D      | 3   | 10   |
| E      | 11  | 12   |
| F      | 4   | 9    |
| G      | 5   | 6    |
| H      | 7   | 8    |

## Part 2

The sources are $A$ and $B$. The sinks are $G$ and $H$.

## Part 3

The ordering is:

$G, H, F, D, E, C, A, B$

## Part 4

There are 8 orderings where you can switch the positions of $G$ and $H$, $D$ and $E$, and $A$ and $B$.

>[!question] Problem 3.4 SCC algorithm example
>Run the [[Strongly connected components (directed graphs)|strongly connected components]] algorithm on the following directed graphs $G$. When doing [[Depth-first search (DFS)|DFS]] on $G^R$: whenever there is a choice of vertices to explore, always pick the one that is alphabetically first.
>In each case answer the following questions:
>1. In what order are the strongly connected components found?
>2. Which are the source SCCs and which are the sink SCCs?
>3. Draw the metagraph.
>4. What is the minimum number of edges you must add to this graph to make it strongly connected?

We are running the [[DFS for finding strongly connected components]].

```pseudocode
SCC(G):
	Input: directed graph G = (V,E) in adjacency list
	Output: labeling of V by strongly connected component
		1. Construct G^R
		2. Run DFS on G^R
		3. Order V by decreasing post order number.
		4. Run directed DFS on G using the vertex ordering from before and
		   label the connected components we reach.
```

## Example 1

![[ex_3_4_1]]

## Step 1 & 2

| Vertex | pre | post |
| ------ | --- | ---- |
| A      | 1   | 6    |
| B      | 2   | 3    |
| C      | 7   | 20   |
| D      | 10  | 11   |
| E      | 4   | 5    |
| F      | 9   | 18   |
| G      | 14  | 15   |
| H      | 12  | 17    |
| I      | 13   | 16   |
| J      | 8   | 19   |

## Step 3

C, J, F, H, I, G, D, A, E, B

## Step 4

| Vertex | pre | post | Strongly connected component |
| ------ | --- | ---- | ---------------------------- |
| A      | 15  | 16   | 3                            |
| B      | 19  | 20   | 5                            |
| C      | 1   | 8    | 1                            |
| D      | 2   | 7    | 1                            |
| E      | 17  | 18   | 4                            |
| F      | 3   | 6    | 1                            |
| G      | 10  | 13   | 2                            |
| H      | 9   | 14   | 2                            |
| I      | 11  | 12   | 2                            |
| J      | 4   | 5    | 1                            |

Source SCC's are B, E and the sink is the SCC containing C

The meta graph is

![[meta_3_4_1]]

We would need to add 2 edges to make it [[Strongly connected (directed graphs)|strongly connected]] $(c,b)$ and $(c,e)$.

## Example 2

![[ex_3_4_2]]

## Step 1 & 2

| Vertex | pre | post |
| ------ | --- | ---- |
| A      | 1   | 6    |
| B      | 3   | 4    |
| C      | 7   | 8    |
| D      | 9   | 18   |
| E      | 2   | 5    |
| F      | 13  | 14   |
| G      | 10  | 17   |
| H      | 11  | 16   |
| I      | 12  | 15   |

## Step 3

D, G, H, I, F, C, A, E, B

## Step 4

| Vertex | pre | post | Strongly connected component |
| ------ | --- | ---- | ---------------------------- |
| A      | 13  | 18   | 3                             |
| B      | 14  | 17   | 3                             |
| C      | 11  | 12   | 2                            |
| D      | 1   | 10   | 1                            |
| E      | 15  | 16   | 3                             |
| F      | 3   | 6    | 1                            |
| G      | 7   | 8    | 1                            |
| H      | 2   | 9    | 1                            |
| I      | 4   | 5    | 1                            |

Soruce is $A$, sink is $D$.

![[meta_3_4_2]]

We only need to add 1 edge $(D,A)$.

>[!question] Problem 3.5 Reverse of graphs
>The [[Reverse directed graph|reverse]] of a [[Directed graph|directed graph]] $G = (V,E)$ is another directed graph $G^R = (V, E^R)$ on the same vertex set, but with all edges revered; that is $E^R = \{(v,u) \vert (u,v \in E\}$.
>Give a linear-time algorithm for computing the reverse of a graph in [[Adjacency list format (graph)|adjacency list]] format?

```pseudocode
reverse(V, E):
	Input: A graph G = (V,E) in adacency list format E(v).
	Ouput: The graph G^R = (V, E^R) in adacency list format.
1. Intialise lists E^R(v) for v in V
2. For each vertex v in V
	2.1. for each u in E(v)
		2.1.1 add v to E^R(u)
3. Output E^R(v)
```

Initialising the lists takes $O(\vert V \vert)$ time. As there are $\vert E \vert$ edges represented in $E(v)$, going through all of them takes $O(\vert E \vert)$ time. Giving the run time is $O(\vert V \vert + \vert E \vert$).

>[!question] Problem 3.15 Computopia
>The police department in the city of Computopia has made all streets one-way. The mayor contends that there is still a way to drive legally from any intersection in the city to any other intersection, but the opposition is not convinced. A computer program is needed to determine whether the mayor is right. However, the city elections are coming up soon, and there is just enough time to run a linear-time algorithm.
>
>(a) Formulate this problem graph-theoretically, and explain why it can indeed be solved in linear time.
>
>(b) Suppose it now turns out that the mayor’s original claim is false. She next claims something weaker: if you start driving from town hall, navigating one-way streets, then no matter where you reach, there is always a way to drive legally back to the town hall. Formulate this weaker property as a graph-theoretic problem, and carefully show how it too can be checked in linear time.

**Part a**

>[!note] Formulation
>Given a [[Directed graph|directed graph]] $G = (V,E)$, do the vertices form a single strongly connected component?

Run the [[DFS for finding strongly connected components]] to check if all vertices are in a single strongly connected component.

**Part b**

>[!note] Formulation
>Given a [[Directed graph|directed graph]] $G = (V, E)$ and a vertex $x \in V$ is $x$ in a sink vertex of the [[Strongly connected component graph (directed graph)|strongly connected component graph]].

Run the [[DFS for finding strongly connected components]] to form the meta graph and then see if $x$ belongs to a sink vertex.

>[!question] Problem 4.14 Shortest path through a given vertex
>You are given a strongly connected directed graph $G = (V,E)$ with positive edge weights along with a particular node $v_0 \in V$ . Give an efficient algorithm for finding shortest paths between all pairs of nodes, with the one restriction that these paths must all pass through $v_0$.

**Algorithm**

Run [[Dijkstra's algorithm]] on $G$ starting a $v_0 \in V$ and return not only the shortest path lengths but also the `prev` array. This gives us paths $p^{out}_y$ from $v_0$ to $y \in V$ for every $y \in V$ as the graph is strongly connected. Then take the [[Reverse directed graph|reverse directed graph]] $G^R$ and run [[Dijkstra's algorithm]] again starting at $v_0 \in V$. This gives us paths in $G$ $p^{in}_x$ from $x \in V$ to $v_0$ for every $x \in V$ by inverting the paths we got in $G^R$. For any two points $x,y \in V$ the shortest path to get from $x$ to $y$ via $v_0$ is then $p^{in}_xp^{out}_y$.

**Correctness**

Note $p^{in}_xp^{out}_y$ is a path from $x$ to $y$ via $v_0$. Suppose we have another path $p$ from $x$ to $y$ via $v_0$ so we can separate it into $p_xp_y$ where $p_x$ is a path from $x$ to $v_0$ and $p_y$ is a path from $v_0$ to $y$. Due to the definition of $p^{in}_x$ and $p^{out}_y$ we have $dist(p^{in}_x) \leq dist(p_x)$ and $dist(p^{out}_y) \leq dist(p_y)$ therefore
$$dist(p^{in}_xp^{out}_y) = dist(p^{in}_x) + dist(p^{out}_y) \leq dist(p_x) + dist(p_y) = dist(p).$$
This gives it is the shortest such path.

**Runtime**

The both runs of [[Dijkstra's algorithm]] takes $O(\vert E \vert \log(\vert V \vert))$.

Calculating the reverse graph takes $O(\vert E \vert)$.

Concatenating the paths together takes $O(\vert V \vert^2)$ time.

Therefore the run time takes $O(\vert V \vert^2 + \vert E \vert \log(\vert V \vert))$.


>[!question] Problem 5.1 MST design
>Consider the following graph.
>
>(a) What is the cost of its minimum spanning tree?
>
>(b) How many minimum spanning trees does it have?
>
>(c) Suppose [[Kruskal's algorithm]] is run on this graph. In what order are the edges added to the MST? For each edge in this sequence, give a cut that justifies its addition.

![[ex_5_1]]

**Part a**

The MST is given by

![[ex_5_1_mst]]

which has weight 19.

**Part b**

It has 2, with the second replacing $(E,B)$ by $(B,F)$.

**Part c**

| edge  | cutset              |
| ----- | ------------------- |
| (A,E) | A                   |
| (E,F) | A, E                |
| (E,B) | A, E, F             |
| (F,G) | A, B, E, F          |
| (G,H) | A, B, E, F, G       |
| (C,G) | A, B, E, F, G, H    |
| (D,G) | A, B, C, E, F, G, H |

>[!question] Problem 5.2 MST design
>Suppose we want to find the minimum spanning tree of the following graph.
>
>(a) Run [[Prim's algorithm]]; whenever there is a choice of nodes, always use alphabetic ordering (e.g., start from node A). Draw a table showing the intermediate values of the cost array.
>
>(b) Run [[Kruskal's algorithm]] on the same graph. Show how the disjoint-sets data structure looks at every intermediate stage (including the structure of the directed trees), assuming path compression is used.

![[ex_5_2]]

**part a)**

| Iteration | A      | B      | C      | D      | E      | F      | G      | H      |
| --------- | ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| 0         | 0      | inf    | inf    | inf    | inf    | inf    | inf    | inf    |
| 1         | - (\*) | 1 (A)  | inf    | inf    | 4 (A)  | 8 (A)  | inf    | inf    |
| 2         | -      | A (\*) | 2 (B)  | inf    | 4 (A)  | 6 (B)  | 6 (B)  | inf    |
| 3         | -      | A      | B (\*) | 3 (C)  | 4 (A)  | 6 (B)  | 2 (C)  | inf    |
| 4         | -      | A      | B      | 1 (G)  | 4 (A)  | 1 (G)  | C (\*) | 1 (G)  |
| 5         | -      | A      | B      | G (\*) | 4 (A)  | 1 (G)  | C      | 1 (G)  |
| 6         | -      | A      | B      | G      | 4 (A)  | G (\*) | C      | 1 (G)  |
| 7         | -      | A      | B      | G      | 4 (A)  | G      | C      | G (\*) |
| 8         | -      | A      | B      | G      | A (\*) | G      | C      | G      |
| 9         | -      | A      | B      | G      | A      | G      | C      | G      |

This gives the following MST

![[ex_5_2_mst]]

**part b)**

| Iteration    | A     | B     | C     | D     | E     | F     | G     | H     |
| ------------ | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| -            | A (1) | B (1) | C (1) | D (1) | E (1) | F (1) | G (1) | H (1) |
| (A,B) 1 (\*) | A (2) | A (1) | C (1) | D (1) | E (1) | F (1) | G (1) | H (1) |
| (D,G) 1 (\*) | A (2) | A (1) | C (1) | D (2) | E (1) | F (1) | D (1) | H (1) |
| (F,G) 1 (\*) | A (2) | A (1) | C (1) | D (2) | E (1) | D (1) | D (1) | G (1) |
| (G,H) 1 (\*) | A (2) | A (1) | C (1) | D (2) | E (1) | D (1) | D (1) | D (1) |
| (B,C) 2 (\*) | A (2) | A (1) | A (1) | D (2) | E (1) | D (1) | D (1) | D (1) |
| (C,G) 2 (\*) | A (3) | A (1) | A (1) | A (2) | E (1) | D (1) | A (1) | D (1) |
| (C,D) 3      | A (3) | A (1) | A (1) | A (2) | E (1) | D (1) | A (1) | D (1) |
| (A,E) 4 (\*) | A (3) | A (1) | A (1) | A (2) | A (1) | D (1) | A (1) | D (1) |
| (D,H) 4      | A (3) | A (1) | A (1) | A (2) | A (1) | D (1) | A (1) | A (1) |
| (E,F) 5      | A (3) | A (1) | A (1) | A (2) | A (1) | A (1) | A (1) | A (1) |


>[!question] Problem 5.9 MST statements
>The following statements may or may not be correct. In each case, either prove it (if it is correct) or give a counterexample (if it isn’t correct). Always assume that the graph $G = (V, E)$ is undirected. Do not assume that edge weights are distinct unless this is specifically stated.
>(a) If graph $G$ has more than $\vert V \vert − 1$ edges, and there is a unique heaviest edge, then this edge cannot be part of a [[Minimum Spanning Tree problem (MST)|MST]].
>(b) If $G$ has a cycle with a unique heaviest edge $e$, then $e$ cannot be part of any [[Minimum Spanning Tree problem (MST)|MST]].
>(c) Let $e$ be any edge of minimum weight in $G$. Then $e$ must be part of some [[Minimum Spanning Tree problem (MST)|MST]].
>(d) If the lightest edge in a graph is unique, then it must be part of every [[Minimum Spanning Tree problem (MST)|MST]].
>(e) If $e$ is part of some [[Minimum Spanning Tree problem (MST)|MST]] of $G$, then it must be a lightest edge across some cut of $G$.
>(f) If $G$ has a cycle with a unique lightest edge $e$, then $e$ must be part of every [[Minimum Spanning Tree problem (MST)|MST]].
>(g) The shortest-path tree computed by [[Dijkstra's algorithm]] is necessarily an [[Minimum Spanning Tree problem (MST)|MST]].
>(h) The shortest path between two nodes is necessarily part of some [[Minimum Spanning Tree problem (MST)|MST]].
>(i) [[Prim's algorithm]] works correctly when there are negative edges.
>(j) (For any $r > 0$, define an $r$-path to be a path whose edges all have weight $< r$.) If $G$ contains an $r$-path from node $s$ to $t$, then every [[Minimum Spanning Tree problem (MST)|MST]] of $G$ must also contain an $r$-path from node $s$ to node $t$.
>

a) False
![[5_9_a]]

b) True

In [[Kruskal's algorithm]] by the time it got to that edge it would have considered if all the rest of the cycle were in connected components and if not joined them. At this point they are all part of the same connected component.

C) True

It could always be the first edge we consider in [[Kruskal's algorithm]].

D) True

By the [[Cut property]].

E) True

By the [[Cut property]]

F) False

Consider the blue cycle in the graph below.

![[5_9_f]]

G) False,

Starting at $v$ below you will construct the blue tree as these edges minimise the distance to $v$.

![[5_9_g]]

H) False,

Consider the two vertices connected by the edge of weight 3 below

![[5_9_f]]

I) True,

There is no restriction on the edge weights for [[Prim's algorithm]].

J) True,

If not there must be some path between $s$ and $t$ remove one of the edges of weight greater than $r$ then you could add one of the edges in the $r$-path between $s$ and $t$ to reconnect the tree. This would reduce the weight of the path.
