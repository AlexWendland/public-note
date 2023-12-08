---
aliases: null
checked: false
created: 2023-10-08
last_edited: 2023-11-11
publish: true
tags:
  - programming
type: data structure
---
# Graph representations

How we represent a [[Directed graph|directed graph]] or [[Graph|undirected graph]] in an algorithm can effect the run time of an algorithm.

Bellow are some common ways to do this:

| Data structure                                        | Space complexity                   | Time to check connection | Time to find neighbours |
| ----------------------------------------------------- | ---------------------------------- | ------------------------ | ----------------------- |
| [[Adjacency list format (graph)|Adjacency list]]     | $O(\vert V \vert + \vert E \vert)$ | $O(N_v)$                 | $O(N_v)$                |
| [[Adjacency matrix format (graph)|Adjacency matrix]] | $O(\vert V \vert^2)$               | $O(1)$                   | $O(\vert V \vert)$      |
| [[Edge list format (graph)|Edge list]]               | $O(\vert E \vert)$                 | $O(\vert E \vert)$       | $O(\vert E \vert)$      |
