---
aliases:
checked: false
course: CS6215 Introduction to Graduate Algorithms
created: 2023-10-21
draft: false
last_edited: 2023-11-11
tags:
  - OMSCS
title: Week 9 - Algorithms for the exam
type: revision
week: 9
---
| algorithm                                                   | problem                                                             | runtime                                                  | Notes                                                               |
| ----------------------------------------------------------- | ------------------------------------------------------------------- | -------------------------------------------------------- | ------------------------------------------------------------------- |
| [DFS to find path in a directed graph](../../general/dfs_to_find_path_in_a_directed_graph.md)                    | [Find path in a directed graph](../../general/find_path_in_a_directed_graph.md)                                   | $O(\vert V \vert + \vert E \vert)$                       | Not shortest                                                        |
| [DFS to find path in an undirected graph](../../general/dfs_to_find_path_in_an_undirected_graph.md)                 | [Find path in undirected graph](../../general/find_path_in_undirected_graph.md)                                   | $O(\vert V \vert + \vert E \vert)$                       | Not shortest                                                        |
| [DFS to find connected components in an undirected graph](../../general/dfs_to_find_connected_components_in_an_undirected_graph.md) | [Find connected components in a undirected graph](../../general/find_connected_components_in_a_undirected_graph.md)                 | $O(\vert V \vert + \vert E \vert)$                       |                                                                     |
| [BFS](breath-first_search_(bfs)\.md)                          | [Find path in undirected graph](../../general/find_path_in_undirected_graph.md)/[Find path in a directed graph](../../general/find_path_in_a_directed_graph.md) | $O(\vert V \vert + \vert E \vert)$                       | Shortest unweighted                                                 |
| [Dijkstra's algorithm](../../general/dijkstra's_algorithm.md)                                    | [Find path in undirected graph](../../general/find_path_in_undirected_graph.md)/[Find path in a directed graph](../../general/find_path_in_a_directed_graph.md) | $O((\vert V \vert + \vert E \vert) \log(\vert V \vert))$ | shortest weighted, positive weights only, from source               |
| [Bellman-Ford algorithm](../../general/bellman-ford_algorithm.md)                                  | [Find path in undirected graph](../../general/find_path_in_undirected_graph.md)/[Find path in a directed graph](../../general/find_path_in_a_directed_graph.md) | $O(\vert V \vert \vert E \vert)$                         | shortest weighted, from source, detects negative cycles             |
| [Floyd-Warshall algorithm](../../general/floyd-warshall_algorithm.md)                                | [Find path in undirected graph](../../general/find_path_in_undirected_graph.md)/[Find path in a directed graph](../../general/find_path_in_a_directed_graph.md) | $O(\vert V \vert^3)$                                     | shortest weighted, all nodes, detects negative cycles               |
| [DFS for finding strongly connected components](../../general/dfs_for_finding_strongly_connected_components.md)           | [Find strongly connected components for an undirected graph](../../general/find_strongly_connected_components_for_an_undirected_graph.md)      | $O(\vert V \vert + \vert E \vert)$                       | Outputs them with [topologically sort](topological_sorting_(dag)\.md) |
| [Kruskal's algorithm](../../general/kruskal's_algorithm.md)                                     | [MST](minimum_spanning_tree_problem_(mst)\.md)                        | $O(\vert E \vert \log(\vert V \vert))$                   |                                                                     |
| [Prim's algorithm](../../general/prim's_algorithm.md)                                        | [MST](minimum_spanning_tree_problem_(mst)\.md)                        | $O(\vert E \vert \log(\vert V \vert))$                   |                                                                     |
| [Ford-Fulkerson Algorithm](../../general/ford-fulkerson_algorithm.md)                                | [max flow](max_flow_problem\.md)                                      | $O(C \vert E \vert)$ $C$ being the max flow              | Integer weights                                                     |
| [Edmonds-Karp algorithm](../../general/edmonds-karp_algorithm.md)                                  | [max flow](max_flow_problem\.md)                                      | $O(\vert V \vert \vert E \vert^2)$                       |                                                                     |
| [2-SAT algorithm using SCC](../../general/2-sat_algorithm_using_scc.md)                               | [2-SAT](k-satisfiability_problem_(k-sat_problem)\.md)                 | $O(\vert V \vert + \vert E \vert)$                       |                                                                     |
