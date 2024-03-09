---
aliases: 
checked: false
created: 2024-03-09
last_edited: 2024-03-09
publish: true
tags:
  - machine-learning
type: definition
---
>[!tldr] Consistent clustering
>Suppose we are in the [[Clustering problem|clustering problem]] set up. A clustering algorithm $C$ is considered *consistent* if for distance $d$ on $T$ we get clustering $C(d) = f$ then any distance $d'$ such that 
>- $d'(a,b) \leq d(a,b)$ for any $a,b \in T$ where $f(a) = f(b)$ , and
>- $d'(a,b) \geq d(a,b)$ for any $a,b \in T$ where $f(a) \not = f(b)$
>
>then $C(d') = f$.





