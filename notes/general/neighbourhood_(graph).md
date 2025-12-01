---
aliases:
  - neighbourhood
checked: false
created: 2023-10-08
draft: false
last_edited: 2023-11-11
name: Neighbourhood (graph)
tags:
  - programming
  - graph-theory
type: definition
---
>[!tldr] Neighbourhood
>For a [undirected graph](graph.md) $G = (V,E)$ the *neighbourhood* of $X \subset V$ is $N_G(X) = \{u \in V \vert (x,u) \in E, x \in X\}$ ($\backslash X$, $\cup X$). Sometimes this will be defined to include $X$ or exclude $X$ - this is called open and closed neighbourhoods.

## Directed graph

In a directed this would normally be specified inbound or outbound neighbourhoods.

>[!tldr] Inbound / outbound neighbourhood
>For a [directed graph](directed_graph.md) $G = (V,E)$ and $X \subset V$ we define:
>- the *inbound neighbourhood* of $X$ to be $N^{in}_G(X) = \{u \in V \vert (u,x) \in E, x \in X\}$, and
>- the *outbound neighbourhood* of $X$ to be $N^{out}_G(X) = \{u \in V \vert (x,u) \in E, x \in X\}$, and
>- the *neighbourhood* of $X$ to be $N_G(X) = N^{in}_G(X) \cup N^{out}_G(X)$.

