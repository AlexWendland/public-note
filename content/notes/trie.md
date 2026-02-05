---
aliases:
  - trie
  - prefix tree
  - tries
created: 2024-06-13
date_checked:
draft: false
last_edited: 2026-02-05
tags:
  - programming
title: Trie
type: data structure
---
>[!definition] Trie
>A *trie* or *prefix tree* is used for associating words in a given alphabet $A$ to some values in $X$.
>- This is given by a directed rooted [tree](tree_(graph).md) $(T = (V, E), r)$.
>- An edge letter map $a: E \rightarrow A$, where $a(v,u) = a(v,w) \Rightarrow u = v$.
>- A node key map $k: V \rightarrow X \cup \{ - \}$ where $-$ is a null value.
>
>Then every word $w = w_1 w_2 \ldots w_{n-1} w_n$ in $A$ has a [path](path_(graph).md) in $T$ $p = v_0 v_1 v_2 \ldots v_t$ where $v_0 = r$ and $a(v_{i-1}, v_i) = w_i$. Then either $n = t$ or $v_t$ has no edge labelled $w_{t+1}$. We then can use this to associate a value to $w$ it is the last non-null value in the sequence $k(v_i)$ or it is null.

