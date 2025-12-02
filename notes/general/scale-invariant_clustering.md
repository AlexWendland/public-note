---
aliases:
  - scale-invariant clustering
checked: false
created: 2024-03-09
draft: false
last_edited: 2024-03-09
title: Scale-invariant clustering
tags:
  - machine-learning
type: definition
---
>[!tldr] Scale-inverient clustering
>Suppose we are in the [clustering problem](clustering_problem.md) set up. A clustering algorithm $C$ is considered *scale-invariant* if for distance $d$ on $T$ if we scale the distance by some $\alpha$ (i.e. $d_{\alpha}(a, b) = d(a,b) \alpha$) then it still produces the same clustering $C(d) = c(d_{\alpha})$.

