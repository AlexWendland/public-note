---
aliases:
checked: false
created: 2023-10-08
draft: false
last_edited: 2023-11-11
title: Graph representations
tags:
  - programming
type: data structure
---
# Graph representations

How we represent a [directed graph](directed_graph.md) or [undirected graph](graph.md) in an algorithm can effect the run time of an algorithm.

Bellow are some common ways to do this:

| Data structure                                        | Space complexity                   | Time to check connection | Time to find neighbours |
| ----------------------------------------------------- | ---------------------------------- | ------------------------ | ----------------------- |
| [Adjacency list](adjacency_list_format_(graph).md)     | $O(\vert V \vert + \vert E \vert)$ | $O(N_v)$                 | $O(N_v)$                |
| [Adjacency matrix](adjacency_matrix_format_(graph).md) | $O(\vert V \vert^2)$               | $O(1)$                   | $O(\vert V \vert)$      |
| [Edge list](edge_list_format_(graph).md)               | $O(\vert E \vert)$                 | $O(\vert E \vert)$       | $O(\vert E \vert)$      |
