---
aliases:
checked: false
created: 2023-08-28
draft: false
last_edited: 2023-11-11
tags:
  - maths
type: lemma
---
>[!important] Proposition
>A finite [[Graph|graph]] who has more than one vertex that is a [[Tree (graph)|tree]] must have at least two leaf vertex.

## Proof

Proof by contradiction.

Suppose this is not the case, then if it has a single vertex of degree one start a path at this vertex. Otherwise pick a random vertex to start the path at. As the tree is connected and has more than one vertex the [[Degree (graph)|degree]] of the chosen vertex is at least 1. It then has an edge to another vertex or itself.

If it has an edge to itself it is not a tree.

Then it must have an edge to another vertex, include this edge in our path.

Our path now contains 2 vertices.

We will now repeat the following argument for proceeding vertices.

The next vertex then must have another edge incident to it as it has [[Degree (graph)|degree]] at least 2. This edge is either incident to a vertex we have already visited or lead to a vertex we have not visited.

If it is incident to a vertex we have already visited we have a [[Cycle (graph)|cycle]] in our graph and this is not a tree.

If it is incident to a vertex we have not already visited, we include this edge in our path and increase the set of vertices we have visited in our path by 1.

As the graph is finite, the set has a maximum size and therefore we must visit a vertex we have already visited before, creating a cycle.

Therefore there must be a vertex of degree 1.
