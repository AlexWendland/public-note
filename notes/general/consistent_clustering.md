---
aliases:
checked: false
created: 2024-03-09
draft: false
last_edited: 2024-03-09
name: Consistent clustering
tags:
  - machine-learning
type: definition
---
>[!tldr] Consistent clustering
>Suppose we are in the [clustering problem](clustering_problem.md) set up. A clustering algorithm $C$ is considered *consistent* if for distance $d$ on $T$ we get clustering $C(d) = f$ then any distance $d'$ such that
>- $d'(a,b) \leq d(a,b)$ for any $a,b \in T$ where $f(a) = f(b)$ , and
>- $d'(a,b) \geq d(a,b)$ for any $a,b \in T$ where $f(a) \not = f(b)$
>
>then $C(d') = f$.





