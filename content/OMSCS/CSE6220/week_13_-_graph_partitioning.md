---
aliases:
course_code: CSE6220
course_name: Introduction to High Performance Computing
created: '2026-04-28'
date_checked: '2026-04-28'
draft: false
last_edited: '2026-04-28'
tags:
  - OMSCS
title: Week 13 - Graph partitioning
type: lecture
week: 13
---

In some distributed algorithms we need to partition a graph into subgraphs to break the computation across processes - for example breadth first search.
When partitioning this graph any edge that crosses a partition boundary represents some information that will need to pass between two processes.
Therefore, it would be good to partition the graph in a way to minimise the number of edges crossing between the partitions whilst being roughly equal.

> [!problem] Graph Partitioning
> Given a graph $G = (V, E)$ and a number of partitions $k$.
> Compute a vertex partition $P$ of $V$ into $P_1, P_2, \dots, P_k$ such that:
> 1. $\vert P_i \vert \approx \vert P_j \vert$, all partitions are roughly the same size.
> 2. $E_{cut} = \{ (u,v) \in E \vert u \in V_i, v \in V_j, i \neq j \}$ is minimised.

This problem is NP-complete, so we are looking for good heuristics to solve the problem rather than a complete solution.

# Bisection and planar graphs

An easy first approach to this is work out a way to roughly cut the graph in half - then iteratively do this until you are down to your desired number of partitions.
For planar graphs (ones that can be drawn on a plane) there is a theorem with a polynomial algorithm to do this:

> [!lemma] Lipton & Tarjan's Theorem
> A planar graph G = (V,E) with $\vert V \vert = n$ vertices has a disjoint partition $V = A \cup S \cup B$ such that:
> 1. $S$ separates $A$ and $B$.
> 2. $\vert A \vert$, $\vert B \vert \leq \frac{2}{3} n$.
> 3. $\vert S \vert \leq 2 \sqrt{2} \sqrt{n} = O(\sqrt{n})$.

Included within the paper for this theorem is a polynomial time algorithm to find such a partition.

# Kernighan-Lin algorithm

The idea behind this algorithm is to start with any cut of the graph and greedily improve it until it is maximal in terms of edge cuts.
To know how to improve it we define the concept of 'gain' of switching two vertices.

Let $G$ be partitioned into $V_1$ and $V_2$.
Then let $a \in V_1$ and $b \in V_2$.
Next define internal and external weight of a vertex.

> [!definition] Internal/External Weight
> If $a \in V_i$ then the weight is $W_i(a) := \vert \{ (a,v) \in E \vert v \in V_i\} \vert$.
> If $a \in V_1$ then $I_1(a) := W_1(a)$ is called the internal and $E_1(a) := W_2(a)$ is called the external weight.

Let $\tilde{V_1} = V_1 \cup \{b\} \backslash \{a\}$ and $\tilde{V_2} = V \backslash \tilde{V_1}$.
Let $Cost(X, Y)$ be the number of edges between $X$ and $Y$.
Then we can state the gain.

> [!definition] Gain
> Note we can restate the cost of the partitions $V_1, V_2$ and $\tilde{V_1}, \tilde{V_2}$ as follows:
> $$
> Cost(V_1, V_2) = Cost(V_1 - \{a\}, V_2 - \{b\}) + W_2(a) + W_1(b) - c_{a,b}
> $$
> and
> $$
> Cost(\tilde{V_1}, \tilde{V_2}) = Cost(\tilde{V_1} - \{a\}, \tilde{V_2} - \{b\}) + W_1(a) + W_2(b) + c_{a,b}
> $$
> where $c_{a,b}$ is the cost of the edge $(a,b)$ if it exists.
> Then we define the gain to be the difference in these costs:
> $$
> Gain(a, b) := Cost(V_1, V_2) - Cost(\tilde{V_1}, \tilde{V_2}) = W_2(a) + W_1(b) - W_1(a) - W_2(b) - 2c_{a,b}
> $$

Given the partition $V_1$ and $V_2$ with candidates $a, b$ then it takes $O(d)$ (where $d$ is the maximum degree of any vertex in the graph) time to compute the gain - as we just need to visit all the neighbours of $a$ and $b$ to determine which term they contribute to.
We now have all the definitions to write down the algorithm.

```pseudocode
// Input:
//  Graph G = (V, E)
//  Initial partition V_1, V_2 (preferably with |V_1| = |V_2|)
// Output: A partition with minimal edge cut whilst keeping the same size partiton.
ker_lin(G, V_1, V_2):
1.  C = cost(V_1, V_2)
2.  while:
3.    visited = map from V to true/false
4.    for-all v in V:
5.      compute V_1(v), V_2(v)
6.      visited(v) = false
7.    let count = 0
8.    while there exists a in V_1 and b in V_2 where visited(a) = visited(b) = false:
9.      choose maximal a_count in V_1, b_count in V_2 with largest gain(a,b) and visited(a_count) = visited(b_count) = false
10.      visited(a_count) = visited(b_count) = true
11.     for v in V such that (v,a) or (v,b) in E:
12.       update V_1(v), V_2(v) to reflect a_count and b_count switching sets.
13.     count++
14.   let cum_gain = 0, max_gain = 0, max_gain_step = -1
15.   for i in 0..count - 1:
16.     let cum_gain += gain(a_i, b_i)
17.     if cum_gain > max_gain:
18.       max_gain = cum_gain
19.       max_gain_step = i
20.   if max_gain_step <= 0:
21.     break
22.   C -= max_gain
23.   A = {a_i | 0 <= i <= max_gain_step}, B = {b_i | 0 <= i <= max_gain_step}
23.   V_1 = V_1 U B - A, V_2 = V_2 U A - B
24. return V_1, V_2
```

This essentially greedily switches vertices until it has to stop.
The algorithm as stated has a run time of $O(d|V|^2)$ however, this can be improved to $O(|E|)$.

# Graph Coarsening

The idea behind the approach is to form smaller graphs that 'represent' the larger graph.
Then by partitioning the smaller graph we get a partition of the larger one - hopefully carrying the optimality between them.

Let $G = (V_G, E_G, w_G^v : V_G \rightarrow \mathbb{R}, w_G^e : E_G \rightarrow \mathbb{R})$ be a weighted graph.
Define a projection $p: G \rightarrow H$ between two weighted graphs to be a surjection $p_V: V_G \rightarrow V_H$ and $p_E: E_G \rightarrow E_H$ such that $p_E(x,y) = (p_V(x), p_V(y))$.
This preserves the weights such that $w_H^V(x') = \sum_{x \in V_G, p_V(x) = x'} w_G^V(x)$ and $w_H^E(x') = \sum_{x \in V_G, p_E(x) = x'} w_G^E(x)$.
Note, if two vertices are collapsed into one vertex the edges between them can disappear.

If you have a projection from $G$ onto $H$ then a partition of $H$ can be brought up to a partition of $G$ by looking at the pre-images of vertices.
Moreover, the weighted cut size also is preserved.

## Graph matching

One easy way to design this projection is to collapse a maximal matching within a graph.

> [!definition] Graph Matching
> A matching $M$ in a graph $G$ is a set of edges $M \subseteq E$ such that no two edges in $M$ share a common vertex.

This is maximal if you can not add another edge to the matching.

To pick a matching, you could just pick edges at random.
However, it seems qualitatively likely that making a 'heaviest edge matching' leads to better partitions.
This is calculated using the following pattern:

1. Pick an unmatched vertex at random.

2. Choose the heaviest edge connected to this vertex.

The intuition behind this is that by collapsing heavy edges you bring down the overall weight of the graph's edges.
This means that the cut set in the smaller graph will be of lower weight as there is less weight to cut.
However, the optimal cut set in the smaller graph may now be the optimal cuts in the larger graph.

# Spectral Graph Partitioning

To understand how we got to spectral graph partitioning we first review a bit of theory.
Suppose we have a directed graph $G$.
Let's represent this in the incidence matrix form.

> [!definition] Incidence Matrix
> Let $G = (V, E)$ be a directed graph.
> Then the incidence matrix $I$ is a $|V| \times |E|$ matrix where:
> $$
> I_{x,e} = \begin{cases}
> 1 & \text{if } (x,y) = e \\
> -1 & \text{if } (y,x) = e \\
> 0 & \text{otherwise}
> \end{cases}
> $$

We can use this representation to define the laplacian of the graph $G$.

> [!definition] Graph Laplacian
> Let $G = (V, E)$ be a directed graph.
> Then we define the graph Laplacian $L(G) = II^T$ where $I$ is the graph incidence matrix.

The definition of the graph Laplacian is a bit abstract.
However, when you calculate it out you get a much nicer form.
Let $L(G) = L_{x,y}$ and let's show what each value represents.

Let's look at the central diagonal:
$$
L_{x,x} = \sum_{e \in E} I_{x,e}^2 = \text{degree}(x)
$$
this gives us the degree of each vertex.

Next, let's look at the off-diagonal:
$$
L_{x,y} = \sum_{e \in E} I_{x,e} I_{y,e} = \begin{cases} -1 & \text{if } (x,y) \text{ or } (y,x) \in E \\
0 & \text{otherwise}
\end{cases}
$$
this is exactly the negative of the adjacency matrix.

So we can rewrite the definition of the Laplacian as:

$$L(G) = \text{degree}(G) - \text{adjacency}(G)$$

where $\text{degree}(G)$ is the degree matrix with values as the degree of each vertex and $\text{adjacency}(G)$ is the adjacency matrix.
Both use vertices as their basis.

> [!note] Laplacian is directionless
> As the degree and adjacency matrices are symmetric and do not depend on edge direction, the Laplacian is the same regardless of the direction of the edges.

Below are some additional facts about the Laplacian matrix:

1. The Laplacian matrix is symmetric.

2. The Laplacian matrix has real-valued, non-negative [eigenvalues](../../../notes/eigenvector_and_eigenvalue.md).

3. The Laplacian matrix has real-valued, orthogonal [eigenvectors](../../../notes/eigenvector_and_eigenvalue.md).

4. $G$ has $k$ connected components if and only if the first $k$ eigenvalues are zero with the rest being non-zero.

These all might seem a bit abstract at the moment.
Though this will help us with finding a partition with the following statement.
Suppose we partition the graph into $V_-$ and $V_+$ and let $\vert V \vert$-vector $x$ represent this partition where:
$$
x_v = 1 \text{ if } v \in V_+ else -1.
$$
then the number of cut edges is $1/4 x^T L(G) x$.
We can show this computationally:

$$
\begin{aligned}
x^T L(G) x & = \sum_{u,v \in V} L_{u,v} x_u x_v\\
& = \sum_{v \in V} L_{v,v} x_v x_v + \sum_{u,v \in V_+}L_{u,v} x_u x_v + \sum_{u,v \in V_-} L_{u,v} x_u x_v + 2 \sum_{u \in V_+, v \in V_-} L_{u,v} x_u x_v\\
& = \sum_{v \in V} \text{deg}(v) - \vert \{(u,v) \vert u,v \in V_+\} \vert - \vert \{(u,v) \vert u,v \in V_-\} \vert + 2 \text{cost}(V_+, V_-)\\
& = 2 \vert E \vert - 2( \vert E \vert - \text{cost}(V_+, V_-)) + 2 \text{cost}(V_+, V_-)\\
& = 4 \text{cost}(V_+, V_-)
\end{aligned}
$$

This uses the fact that the Laplacian is symmetric.

Therefore, we can now use this formula to restate the partition problem.

> [!problem] Graph Partitioning
> Find the $\vert V \vert$-vector $x$ that minimises $x^T L(G) x$ such that $\sum_{v \in V} x_v = 0$ and $x_v = \pm 1$ for all $v \in V$.

Whilst this problem we already know is NP-complete, we can simplify it by relaxing the restrictions on $x$ so it can be any real-valued vector.
In this setting there is a theorem that helps us:

> [!lemma] Courant-Fisher Minimax Theorem
> Let $y$ be any real-valued vector.
> Then:
> $$
> \min_{y, y^Ty = n} y^T L(G) y = n q_1^T L(G) q_1 = n\lambda_1
> $$
> Where $\lambda_1$ is the second smallest eigenvalue and $q_1$ its eigenvector.

This gives us a lower bound on the smallest cost partition.
Though another fact from spectral theory gives us a candidate for a partition.
The eigenvector for the second smallest eigenvalue has exactly half its entries greater than zero and the rest less than zero.
So we can use this to make an $x$ by taking the sign of the entries of the second smallest eigenvector.
Putting that all together we get the following pseudo-code:

```pseudocode
// Input: Graph G = (V,E)
// Output: An even partition.
spectral_partition(G):
1. Create L(G) using the vertex degrees and adjacency matrix.
2. Compute the second smallest eigenvalue/vector lambda and q.
3. Choose x_v = sign(q_v).
4. Return x.
```
