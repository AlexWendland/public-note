---
aliases:
  - decision tree
  - decision trees
created: 2024-01-10
date_checked:
draft: false
last_edited: 2026-02-05
tags:
  - maths
  - algorithms
title: Decision tree
type: definition
---
>[!definition] Decision tree
>Suppose you have two sets $A$ and $B$. A *decision tree* is a representation of a function $f: A \rightarrow B$, it is comprised of,
>- a [rooted tree](rooted_tree.md) $(T = (P \cup L,E), r)$,
>- for each parent $p \in P$ mapping $f_p : A \rightarrow Child(p)$, and
>- a mapping $r: L \rightarrow B$.
>
>To evaluate $f(a)$ compute the path with $p_1 = r$, then if $p_i \in P$ compute $p_{i+1} = f_{p_i}(a)$ with $f(a) = r(p_k)$ with $p_k \in L$.

