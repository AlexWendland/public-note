---
aliases:
checked: false
created: 2023-09-28
draft: false
last_edited: 2023-11-11
name: Taking the reverse respects going to the strongly connected component graph
tags:
  - maths
type: lemma
---
> [!important] Lemma
> Let $G = (V,E)$ be a [directed graph](directed_graph.md) and $G^R= (V,E^R)$ be its [reverse](reverse_directed_graph.md). Then if $S_G$ is [strongly connected component graph](strongly_connected_component_graph_(directed_graph).md) of $G$ then the [reverse](reverse_directed_graph.md) of $S_G$ is equal the [strongly connected component graph](strongly_connected_component_graph_(directed_graph).md) of $G^R$ called $S_{G^R}$. I.e. $S_G^R = S_{G^R}$.

## Proof

As [the strongly connected components are the same in a directed graph and its reverse](the_strongly_connected_components_are_the_same_in_a_directed_graph_and_its_reverse.md) we know $S_G$ and $S_{G^R}$ have the same vertex set.

The edge set for $S_G$ is
$$\{(S_i, S_j) \vert \ s_i \in S_i, s_j \in S_j\ \mbox{ with } (s_i, s_j) \in E\}.$$
therefore the edge set for $S_G^R$ is
$$\{(S_j, S_i) \vert \ s_i \in S_i, s_j \in S_j\ \mbox{ with } (s_i, s_j) \in E\}.$$
Which by the definition of [reverse](reverse_directed_graph.md) could be rephrased as
$$\{(S_j, S_i) \vert \ s_i \in S_i, s_j \in S_j\ \mbox{ with } (s_j, s_i) \in E^R\}.$$
This is exactly the definition of the edge set for $S_{G^R}$ giving the required statement.
