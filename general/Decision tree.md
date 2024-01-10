---
aliases: 
checked: false
created: 2024-01-10
last_edited: 2024-01-10
publish: true
tags:
  - maths
  - algorithms
type: definition
---
>[!tldr] Decision tree
>Suppose you have two sets $A$ and $B$. A *decision tree* is a representation of a function $f: A \rightarrow B$, it is comprised of,
>- a [[Rooted tree|rooted tree]] $(T = (P \cup L,E), r)$,
>- for each parent $p \in P$ mapping $f_p : A \rightarrow Child(p)$, and
>- a mapping $r: L \rightarrow B$.
>
>To evaluate $f(a)$ compute the path with $p_1 = r$, then if $p_i \in P$ compute $p_{i+1} = f_{p_i}(a)$ with $f(a) = r(p_k)$ with $p_k \in L$.

