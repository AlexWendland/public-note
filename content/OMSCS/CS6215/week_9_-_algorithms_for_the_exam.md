---
aliases:
checked: false
course_code: CS6215
course_name: Introduction to Graduate Algorithms
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
| [DFS to find path in a directed graph](../../notes/dfs_to_find_path_in_a_directed_graph.md)                    | [Find path in a directed graph](../../notes/find_path_in_a_directed_graph.md)                                   | $O(\vert V \vert + \vert E \vert)$                       | Not shortest                                                        |
| [DFS to find path in an undirected graph](../../notes/dfs_to_find_path_in_an_undirected_graph.md)                 | [Find path in undirected graph](../../notes/find_path_in_undirected_graph.md)                                   | $O(\vert V \vert + \vert E \vert)$                       | Not shortest                                                        |
| [DFS to find connected components in an undirected graph](../../notes/dfs_to_find_connected_components_in_an_undirected_graph.md) | [Find connected components in a undirected graph](../../notes/find_connected_components_in_a_undirected_graph.md)                 | $O(\vert V \vert + \vert E \vert)$                       |                                                                     |
| [BFS](breath-first_search_(bfs)\.md)                          | [Find path in undirected graph](../../notes/find_path_in_undirected_graph.md)/[Find path in a directed graph](../../notes/find_path_in_a_directed_graph.md) | $O(\vert V \vert + \vert E \vert)$                       | Shortest unweighted                                                 |
| [Dijkstra's algorithm](../../notes/dijkstra's_algorithm.md)                                    | [Find path in undirected graph](../../notes/find_path_in_undirected_graph.md)/[Find path in a directed graph](../../notes/find_path_in_a_directed_graph.md) | $O((\vert V \vert + \vert E \vert) \log(\vert V \vert))$ | shortest weighted, positive weights only, from source               |
| [Bellman-Ford algorithm](../../notes/bellman-ford_algorithm.md)                                  | [Find path in undirected graph](../../notes/find_path_in_undirected_graph.md)/[Find path in a directed graph](../../notes/find_path_in_a_directed_graph.md) | $O(\vert V \vert \vert E \vert)$                         | shortest weighted, from source, detects negative cycles             |
| [Floyd-Warshall algorithm](../../notes/floyd-warshall_algorithm.md)                                | [Find path in undirected graph](../../notes/find_path_in_undirected_graph.md)/[Find path in a directed graph](../../notes/find_path_in_a_directed_graph.md) | $O(\vert V \vert^3)$                                     | shortest weighted, all nodes, detects negative cycles               |
| [DFS for finding strongly connected components](../../notes/dfs_for_finding_strongly_connected_components.md)           | [Find strongly connected components for an undirected graph](../../notes/find_strongly_connected_components_for_an_undirected_graph.md)      | $O(\vert V \vert + \vert E \vert)$                       | Outputs them with [topologically sort](topological_sorting_(dag)\.md) |
| [Kruskal's algorithm](../../notes/kruskal's_algorithm.md)                                     | [MST](minimum_spanning_tree_problem_(mst)\.md)                        | $O(\vert E \vert \log(\vert V \vert))$                   |                                                                     |
| [Prim's algorithm](../../notes/prim's_algorithm.md)                                        | [MST](minimum_spanning_tree_problem_(mst)\.md)                        | $O(\vert E \vert \log(\vert V \vert))$                   |                                                                     |
| [Ford-Fulkerson Algorithm](../../notes/ford-fulkerson_algorithm.md)                                | [max flow](max_flow_problem\.md)                                      | $O(C \vert E \vert)$ $C$ being the max flow              | Integer weights                                                     |
| [Edmonds-Karp algorithm](../../notes/edmonds-karp_algorithm.md)                                  | [max flow](max_flow_problem\.md)                                      | $O(\vert V \vert \vert E \vert^2)$                       |                                                                     |
| [2-SAT algorithm using SCC](../../notes/2-sat_algorithm_using_scc.md)                               | [2-SAT](k-satisfiability_problem_(k-sat_problem)\.md)                 | $O(\vert V \vert + \vert E \vert)$                       |                                                                     |
