---
aliases:
created: 2023-10-01
date_checked:
draft: false
last_edited: 2023-11-11
tags:
  - programming
  - maths
title: Cut property
type: lemma
---
>[!important] Cut property
>Let $G = (V,E)$ be an [undirected graph](graph.md) with an edge weight $w: E \rightarrow \mathbb{R}$. Suppose $X \subset E$ is part of an [MST](minimum_spanning_tree_problem_(mst).md) $T$. Let $S \subset V$ be a [cut](cut_(graph).md) where no edge of $X$ is in the [cut edges](cut_(graph).md) $cut(S, \overline{S})$. Then for $e^{\ast} \in cut(S, \overline{S})$ of minimum weight - $X \cup \{e^{\ast}\}$ is part of an [MST](minimum_spanning_tree_problem_(mst).md) $T^{\ast}$.

## Proof

If $e^{\ast} \in T$ then $X \cup \{e^{\ast}\} \subset T$ and we are done.

Assume $e^{\ast} \not \in T$.

Let $e^{\ast} = (a,b)$. As $T$ is an [MST](minimum_spanning_tree_problem_(mst).md) it contains a path $p$ from $a$ to $b$. As $a \in S$ and $b \in \overline{S}$ the path $p$ contains an edge $e' \in cut(S, \overline{S})$.

Let $T^{\ast} = T \cup \{e^{\ast}\} \backslash \{e'\}$.

We have the size of $T^{\ast}$ is
$$\vert T^{\ast} \vert = \vert T \vert + 1 - 1 = \vert T \vert = \vert V \vert - 1$$
as $T$ is a tree.

Consider the cycle $p e^{\ast}$ - rewrite this cycle as $e' \overline{p}$. We will use this to show $T^{\ast}$ is connected.

Let $a, b \in V$. As $T$ is connected there must a path $p'$ in $T$ connecting $a$ to $b$.

If $p'$ uses $e'$ replace $e'$ by $\overline{p}$ to form $p^{\ast}$ which only uses edges in $T^{\ast}$. As $p^{\ast}$ connects $a$ to $b$ we have $T^{\ast}$ is connected.

As $T^{\ast}$ is connected on $V$ and has $\vert V \vert - 1$ edges it has to be a [spanning](spanning_subgraph.md) [tree](tree_(graph).md) of $G$.

Note as $e^{\ast}$ is the minimum weight edge in $cut(S,\overline{S})$ we have $w(e^{\ast}) \leq w(e')$ and moreover
$$w(T^{\ast}) = w(T) + w(e^{\ast}) - w(e') \leq w(T).$$
This gives that $T^{\ast}$ is of minimum weight as $T$ was a [MST](mst.md).

All together this gives us that $T^{\ast}$ is an [MST](minimum_spanning_tree_problem_(mst).md) where $X \cup \{e^{\ast}\} \subset T^{\ast}$, proving the statement.
