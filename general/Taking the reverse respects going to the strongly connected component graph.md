---
aliases: null
checked: false
created: 2023-09-28
last_edited: 2023-09-28
publish: true
tags:
  - maths
type: lemma
---
> [!important] Lemma
> Let $G = (V,E)$ be a [[Directed graph|directed graph]] and $G^R= (V,E^R)$ be its [[Reverse directed graph|reverse]]. Then if $S_G$ is [[Strongly connected component graph (directed graph)|strongly connected component graph]] of $G$ then the [[Reverse directed graph|reverse]] of $S_G$ is equal the [[Strongly connected component graph (directed graph)|strongly connected component graph]] of $G^R$ called $S_{G^R}$. I.e. $S_G^R = S_{G^R}$.

## Proof

As [[The strongly connected components are the same in a directed graph and its reverse|the strongly connected components are the same in a directed graph and its reverse]] we know $S_G$ and $S_{G^R}$ have the same vertex set.

The edge set for $S_G$ is
$$\{(S_i, S_j) \vert \ s_i \in S_i, s_j \in S_j\ \mbox{ with } (s_i, s_j) \in E\}.$$
therefore the edge set for $S_G^R$ is
$$\{(S_j, S_i) \vert \ s_i \in S_i, s_j \in S_j\ \mbox{ with } (s_i, s_j) \in E\}.$$
Which by the definition of [[Reverse directed graph|reverse]] could be rephrased as
$$\{(S_j, S_i) \vert \ s_i \in S_i, s_j \in S_j\ \mbox{ with } (s_j, s_i) \in E^R\}.$$
This is exactly the definition of the edge set for $S_{G^R}$ giving the required statement.
