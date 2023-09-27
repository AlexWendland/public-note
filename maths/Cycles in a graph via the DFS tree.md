---
aliases: 
type: lemma
publish: false
created: 2023-09-27
last_edited: 2023-09-27
tags:
  - maths
chatgpt: false
---
> [!important] Lemma
> A [[Directed graph|directed graph]] $G$ has a cycle if and only if its [[DFS tree (algorithm)|DFS tree]] has a back edge.

## Proof

Suppose we have a graph $G = (V,E)$ and some run of a [[Depth-first search (DFS)|DFS]] algorithm $A$ that forms [[DFS tree (algorithm)|DFS tree]] $T = (V, E')$.

### $\Rightarrow$

Suppose it has some cycle $x_1, x_2, \ldots x_n$ where $x_i \in V$ and $(x_i, x_{i+1}), (x_n, x_1) \in E$. Then some vertex $x_k$ must have been discovered first by $A$.

All other vertices $x_i$ must be below $x_k$ and contained in its branch. Therefore $x_{i-1}$ is contained in its branch with edge $(x_{i-1}, x_i)$ giving the desired [[DFS tree (algorithm)|back edge]].

### $\Leftarrow$

Suppose we have some back edge $(a, b) \in E$. By the definition of back edge $(a,b) \not \in E'$ but $a$ and $b$ are in the same branch in $T$.

Therefore there are edges $e_1, \ldots e_n$ connecting $b$ to $a$ in $T$ making $e_1, \ldots, e_n, (a,b)$ a cycle.