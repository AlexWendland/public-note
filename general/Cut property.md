---
aliases: 
type: lemma
publish: true
created: 2023-10-01
last_edited: 2023-10-01
tags:
  - programming
  - maths
chatgpt: false
---
>[!important] Cut property
>Let $G = (V,E)$ be an [[Graph|undirected graph]] with an edge weight $w: E \rightarrow \mathbb{R}$. Suppose $X \subset E$ is part of an [[Minimum Spanning Tree problem (MST)|MST]] $T$. Let $S \subset V$ be a [[Cut (graph)|cut]] where no edge of $X$ is in the [[Cut (graph)|cut edges]] $cut(S, \overline{S})$. Then for $e^{\ast} \in cut(S, \overline{S})$ of minimum weight - $X \cup \{e^{\ast}\}$ is part of an [[Minimum Spanning Tree problem (MST)|MST]] $T^{\ast}$.

## Proof

If $e^{\ast} \in T$ then $X \cup \{e^{\ast}\} \subset T$ and we are done.

Assume $e^{\ast} \not \in T$.

Let $e^{\ast} = (a,b)$. As $T$ is an [[Minimum Spanning Tree problem (MST)|MST]] it contains a path $p$ from $a$ to $b$. As $a \in S$ and $b \in \overline{S}$ the path $p$ contains an edge $e' \in cut(S, \overline{S})$. 

Let $T^{\ast} = T \cup \{e^{\ast}\} \backslash \{e'\}$.

We have the size of $T^{\ast}$ is 
$$\vert T^{\ast} \vert = \vert T \vert + 1 - 1 = \vert T \vert = \vert V \vert - 1$$
as $T$ is a tree.

Consider the cycle $p e^{\ast}$ - rewrite this cycle as $e' \overline{p}$. We will use this to show $T^{\ast}$ is connected. 

Let $a, b \in V$. As $T$ is connected there must a path $p'$ in $T$ connecting $a$ to $b$. 

If $p'$ uses $e'$ replace $e'$ by $\overline{p}$ to form $p^{\ast}$ which only uses edges in $T^{\ast}$. As $p^{\ast}$ connects $a$ to $b$ we have $T^{\ast}$ is connected.

As $T^{\ast}$ is connected on $V$ and has $\vert V \vert - 1$ edges it has to be a [[Spanning subgraph|spanning]] [[Tree (graph)|tree]] of $G$.

Note as $e^{\ast}$ is the minimum weight edge in $cut(S,\overline{S})$ we have $w(e^{\ast}) \leq w(e')$ and moreover
$$w(T^{\ast}) = w(T) + w(e^{\ast}) - w(e') \leq w(T).$$
This gives that $T^{\ast}$ is of minimum weight as $T$ was a [[MST]].

All together this gives us that $T^{\ast}$ is an [[Minimum Spanning Tree problem (MST)|MST]] where $X \cup \{e^{\ast}\} \subset T^{\ast}$, proving the statement.
