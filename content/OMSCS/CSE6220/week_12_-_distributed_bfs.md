---
aliases:
course_code: CSE6220
course_name: Introduction to High Performance Computing
created: '2026-04-07'
date_checked:
draft: false
last_edited: '2026-04-07'
tags:
  - OMSCS
title: Week 12 - Distributed BFS
type: lecture
week: 12
---

In this lecture, we will look at how we can distribute a BFS algorithm among multiple processors.
This relies on the idea of representing a graph as an [adjacency matrix](/content/notes/adjacency_matrix_format_%28graph%29.md).

# Calculating distances

Take the BFS algorithm to calculate the distance each node is away from a given node.
This has been covered before but can be expressed as below.

```pseudocode
// Input:
//   G: graph we are working on.
//   source: node to start from.
// Output:
//   A |V| array of distances from the source node.
distance(G, source):
  dist = array of size |V| with infinity at all vertices other than the source at 0
  frontier = {source}
  next_frontier = empty set
  frontier_distance = 1
  while frontier is not empty:
    for each vertex current in frontier:
      for each neighbor of current:
        if dist[neighbor] is infinity:
          dist[neighbor] = frontier_distance
          next_frontier.add(neighbor)
    frontier = next_frontier
    next_frontier = empty set
    frontier_distance += 1
  return dist
```

This has clear steps,

1. Find neighbors of the current frontier.

2. Filter the neighbours by who has a distance already.

3. Update the distances of the neighbours and set that to the next frontier.

We do this until the frontier is empty.

The time complexity of this is $O(V + E)$.
To parallelise this, we need each processor to work independently on finding neighbours.
The process of finding neighbours can be expressed as a matrix multiplication problem.
If we express the frontier as a vector of length $\vert V \vert$ where we have a 1 for every element in the frontier - then the neighbours are non-zero elements of $vM$.
We can now cut up this matrix multiplication in a 1d or 2d way.

![1D BFS](../../../static/images/1d_bfs.png)

For the 1d case we cut the adjacency matrix into $p$ sets of columns and distribute them among out processors.
Each processor is then responsible for the nodes associated to the columns it has gotten.
Each processor gets the whole frontier vector and can calculate $vM$ on their set of columns.
It filters using their part of the distance vector and updates the distance vector.
Lastly, we use an all-to-all to distribute the new frontier vector.

```pseudocode
// Input:
//   A: A n/p slice of the adjacency matrix.
//   start: The start node.
//   rank: The rank of this node.
// Output:
//   A distance vector of size n still distributed on the nodes.
1d_bfs(A[1:n/p][1:n], start):
  dist = A 1-d array of size n/p with infinity at all vertices other than the source at 0
  frontier = zero array of size n with start set to 1.
  distance = 1
  while frontier is not zero:
    neighbors = A x frontier
    next_frontier = 2-d zero array of dimension p, n/p
    for index in [1, n/p]:
      if neighbors[index] is not zero and dist[index] is infinity:
        dist[index] = distance
        next_frontier[rank][index] = 1
    for processor in [1, p]:
      all-to-all(next_frontier[processor], next_frontier)
    frontier = flatten(next_frontier)
    distance += 1
  return dist
```

The main computation done in the matrix multiplication - whilst initially this may seem like $n^2/p$ operations on each node this matrix in real world is likely to be sparse which can be sped up.
The communication costs of this algorithm is $O(\alpha p + \beta n)$ which is not bad given the optimal linear cost of the algorithm.

This can be extended to 2D grid with a little more work.

![2D BFS](../../../static/images/2d_bfs.png)

In the 2d case we not only split up the columns but also rows.
This means the knowledge about a given vertex is limited to a column of processors which will all need to update their distance vectors/frontiers before they distribute it with their row.
However, this means we limit the matrix operations to just a $n/p \times n/p$ matrix.
