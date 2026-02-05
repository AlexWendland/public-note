---
aliases:
created: 2024-03-09
date_checked:
draft: false
last_edited: 2026-02-05
tags:
  - machine-learning
title: Consistent clustering
type: definition
---
>[!definition] Consistent clustering
>Suppose we are in the [clustering problem](clustering_problem.md) set up. A clustering algorithm $C$ is considered *consistent* if for distance $d$ on $T$ we get clustering $C(d) = f$ then any distance $d'$ such that
>- $d'(a,b) \leq d(a,b)$ for any $a,b \in T$ where $f(a) = f(b)$ , and
>- $d'(a,b) \geq d(a,b)$ for any $a,b \in T$ where $f(a) \not = f(b)$
>
>then $C(d') = f$.





