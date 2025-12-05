---
aliases:
checked: false
created: 2023-09-26
draft: false
last_edited: 2025-12-05
tags:
  - maths
title: Vertex degree sum in a graph
type: lemma
---
> [!lemma] Lemma
> Let $G = (V, E)$ represents a [undirected simple graph](graph.md). Let $\mbox{deg}(v)$ be the [degree](degree_(graph).md) of vertex $v \in V$. Then
> $$ \sum_{v \in V} \mbox{deg}(v) = 2 \vert E \vert.$$

## Proof

Lets prove this by induction on the number $\vert E \vert$ within a graph.

Suppose a graph has no edges. Therefore $\deg(v) = 0$ for all $v \in V$ as there are no edges to be incident to $v$. Thus
$$\sum_{v \in V} \mbox{deg}(v) = 0 = 2 \vert E \vert.$$
Suppose we have shown the statement true for all graphs where $\vert E \vert < k$ and suppose we have a graph with $\vert E \vert = k$. Pick any edge $e = (x,y)$ and remove it from the graph to get $G^{\ast} = (V, E^{\ast})$ . From the induction hypothesis we have
$$ \sum_{v \in V} \mbox{deg}_{G^{\ast}}(v) = 2 (\vert E \vert - 1)$$
Where $\mbox{deg}_{G^{\ast}}$ is the degree in $G^{\ast}$. Note that $\mbox{deg}_{G}(v) = \mbox{deg}_{G^{\ast}}(v)$ for all $v \in V \backslash \{x, y\}$. Whereas, $\mbox{deg}_{G^{\ast}}(v) + 1 = \mbox{deg}_{G}(v)$ for $v \in \{x,y\}$ (as it is incident to $e = (x,y)$ as well as all the edges in $E^{\ast}$). Therefore
$$\begin{align*}
\sum_{v \in V} \mbox{deg}_{G}(v) & = \sum_{v \in V \backslash \{x,y\}} \mbox{deg}_{G^{\ast}}(v) + \sum_{v \in \{x,y\}} (\mbox{deg}_{G}(v) + 1)\\
& = 2 + \sum_{v \in V} \mbox{deg}_{G^{\ast}}(v) \\
& = 2 + 2 (\vert E \vert - 1)\\
& = 2 \vert E \vert. \end{align*}$$
This shows the inductive case and proves the statement.
