---
aliases:
checked: false
course: '[[CS6215 Introduction to Graduate Algorithms]]'
created: 2023-10-21
draft: false
last_edited: 2023-11-11
tags:
  - OMSCS
type: revision
week: 9
---
| algorithm                                                   | problem                                                             | runtime                                                  | Notes                                                               |
| ----------------------------------------------------------- | ------------------------------------------------------------------- | -------------------------------------------------------- | ------------------------------------------------------------------- |
| [[DFS to find path in a directed graph]]                    | [[Find path in a directed graph]]                                   | $O(\vert V \vert + \vert E \vert)$                       | Not shortest                                                        |
| [[DFS to find path in an undirected graph]]                 | [[Find path in undirected graph]]                                   | $O(\vert V \vert + \vert E \vert)$                       | Not shortest                                                        |
| [[DFS to find connected components in an undirected graph]] | [[Find connected components in a undirected graph]]                 | $O(\vert V \vert + \vert E \vert)$                       |                                                                     |
| [[Breath-first search (BFS)\|BFS]]                          | [[Find path in undirected graph]]/[[Find path in a directed graph]] | $O(\vert V \vert + \vert E \vert)$                       | Shortest unweighted                                                 |
| [[Dijkstra's algorithm]]                                    | [[Find path in undirected graph]]/[[Find path in a directed graph]] | $O((\vert V \vert + \vert E \vert) \log(\vert V \vert))$ | shortest weighted, positive weights only, from source               |
| [[Bellman-Ford algorithm]]                                  | [[Find path in undirected graph]]/[[Find path in a directed graph]] | $O(\vert V \vert \vert E \vert)$                         | shortest weighted, from source, detects negative cycles             |
| [[Floyd-Warshall algorithm]]                                | [[Find path in undirected graph]]/[[Find path in a directed graph]] | $O(\vert V \vert^3)$                                     | shortest weighted, all nodes, detects negative cycles               |
| [[DFS for finding strongly connected components]]           | [[Find strongly connected components for an undirected graph]]      | $O(\vert V \vert + \vert E \vert)$                       | Outputs them with [[Topological sorting (DAG)\|topologically sort]] |
| [[Kruskal's algorithm]]                                     | [[Minimum Spanning Tree problem (MST)\|MST]]                        | $O(\vert E \vert \log(\vert V \vert))$                   |                                                                     |
| [[Prim's algorithm]]                                        | [[Minimum Spanning Tree problem (MST)\|MST]]                        | $O(\vert E \vert \log(\vert V \vert))$                   |                                                                     |
| [[Ford-Fulkerson Algorithm]]                                | [[Max flow problem\|max flow]]                                      | $O(C \vert E \vert)$ $C$ being the max flow              | Integer weights                                                     |
| [[Edmonds-Karp algorithm]]                                  | [[Max flow problem\|max flow]]                                      | $O(\vert V \vert \vert E \vert^2)$                       |                                                                     |
| [[2-SAT algorithm using SCC]]                               | [[k-satisfiability problem (k-SAT problem)\|2-SAT]]                 | $O(\vert V \vert + \vert E \vert)$                       |                                                                     |
