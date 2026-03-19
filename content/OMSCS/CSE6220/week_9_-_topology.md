---
aliases:
course_code: CSE6220
course_name: Introduction to High Performance Computing
created: '2026-03-19'
date_checked:
draft: true
last_edited: '2026-03-19'
tags:
  - OMSCS
title: Week 9 - Topology
type: lecture
week: 9
---

In the distributed machine model we said the algorithm running time depended on the underlying network.
However, in that lecture we mainly used a linear network to develop algorithms.
At the start of HPC the design of these networks were an important area of study - however as computers got faster it dropped in importance.

# Network properties

A network $N = (V, E)$ is a graph where each node can contain a processor (but does not have to in the case of routers).
More complex networks may have a bandwidth associated to each edge $b: E \rightarrow \mathbb{R}$.
There are multiple properties we care about:

- Number of nodes: $\vert V \vert$, this is the compute capacity.

- Number of links: $\vert E \vert$, this is the cost of setting this network up.

- Diameter: the longest shortest path between two nodes, this is the furthest a message may have to pass.

- Bisection width: the minimum number of edges the separate two halves of the graph.

- Bisection bandwidth: (in the case where edges have different bandwidth) the minimum size cut the separates two halves of the graph.

There are certain classes of graphs people care about in HPC:

- Linear (1d): This is just a path of length $P$.

- Mesh (d-dimensional): This is a d-dimensional grid of a given size where each node is connected to its immediate neighbours.

- Torus: Same as a mesh but you connect vertices at the sides so all nodes have the same amount of connections.
High-end systems tend to use low dimensional torii as their architecture.

- Fully connected: A complete graph with a connection between every pair of nodes.

- Hypercube dimension $d$: Consider vertices in $\{0,1\}^d$ and connect two vertices if they differ by only 1 bit.

- Tree: Here all the nodes are on the leaves with a router connecting groups of them up.
We sometimes increase the size of the bandwidth on the branches closer to the root of the node - this is called a 'fat tree'.

These graphs have the following properties:

| Family | Vertices | Links | Diameter | Bisection |
| ------ | -------- | ----- | -------- | --------- |
| Linear | P        | P - 1 | P - 1    | 1         |
| Mesh (2d)   | P        | $2(\sqrt{P} - 1)\sqrt{P}$ | $2(\sqrt{P} - 1)$ | $\sqrt{P}$ |
| Torus (d) | P         | $dP$ | $d P^{1/d}/2$ | $2P^{d-1/d}$ |
| Complete | P      | $P(P-1)/2$ | 1 | $P(P/2 - 1)/4$ |
| Hypercube (d) | $2^d$ | $d2^{d-1}$ | $d$ | $2^{d-1}$ |

# Mappings and congestion

We may have the case where we design algorithms for one particular kind of network but functionally the network architecture is different.
Here we say the network we designed for is the 'logical network' and the real network is the physical network.
We then will map our logical network to the physical one $m: L \rightarrow P$.
This is a mapping to the vertices that maps any edges in $L$ to the shortest paths in $P$.

If the logical network is more sparse than the physical one (in terms of edges) then the algorithm will run even more efficiently in the physical network.
However, if the logical network is denser than the physical one then the algorithm will run more slowly in the physical network.
We measure this difference by calculating the congestion of a mapping.
The congestion of the mapping $m$ is the maximum number of logical edges that map to a single physical edge.
Intuitively, this is a measure of the maximum amount of serialisation that can occur when we translate algorithms.

> [!example] Congestion
> Consider the mapping from the 2-d torus to a ring network as given below:
> ![Congestion example](../../../static/images/congestion_example.png)
> In this example each 2 consecutive rows provide $\sqrt{P} + 2$ congestion on the vertical edges.
> That is all the edges connecting the two edges project onto the horizontal edge at the end of the two rows (close to the connecting vertical edge) as well as the 2 wrap around edges.
> This gives us our $\sqrt{P} + 2$ congestion.

Manually computing congestion is normally pretty tricky but there are easy lower bounds that help with our understanding.

> [!lemma] Congestion lower bound
> Suppose we have a mapping $m: L \rightarrow P$, and let $B_L$ and $B_P$ be the graphs bisection widths respectively.
> Then the congestion must be atleast $B_L/B_P$.

This is because we can map the cut of $L$ onto a cut of $P$ that cut of $P$ could have atleast $B_P$ edges due to the definition.
Then the $B_L$ edges will need to be mapped onto the $B_P$ edges - of which the maximum such mapping would have to be at least $B_L/B_P$ by the pigeon hole principle.

Applying this to the example above we have $B_L = 2P^{1/2}$ and $B_P = 2$ giving us the bound $\sqrt{P}$ - which is fairly tight to the real answer.

# Exploiting topology

We can use the topology of a particular network to speed up algorithms.
Consider `allGather` which on a linear network we showed could either be efficient in the $\alpha$ term using a tree-algorithm $O((\alpha + n\beta)\log(P))$.
Otherwise we could use bucketing to get it efficient in the $\beta$ term $O(P\alpha + n \beta)$.
Here we had to choose a payoff.
Lets instead consider the same on a 2d-grid network.
Here lets do the allGather in two stages - first gather along the rows using the linear bucket algorithm then allGather along the columns.
Assuming the 2d grid of $\sqrt{P}$ size then we get this algorithm runs in $O(\alpha \sqrt{P} + \beta m \sqrt{P}) + O(\alpha \sqrt{P} + \beta n) = O(\alpha \sqrt{P} + \beta m(P + \sqrt{P}))$.
This is basically optimal in $\beta$ with a much more competitive $\alpha$ term than the bucket algorithm alone.

## All to all

In a all-to-all communication each node needs to send a personalised message to each other node.
This is a toy problem that demonstrates the worst case scenario.
One real-world example of this would be matrix transpose where each node is storing one column of the matrix data.
