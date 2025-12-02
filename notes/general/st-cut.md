---
aliases:
  - st-cuts
checked: false
created: 2023-10-03
draft: false
last_edited: 2023-11-11
title: st-cut
tags:
  - programming
type: definition
---
>[!tldr] st-cut
>Given a [flow network](flow_network.md) $(G, c, s, t)$ an *st-cut* is a [cut](cut_(graph).md) $(L, R)$ of $G$ where $s \in L$ and $t \in R$. The *capacity* of this cut is
>$$capacity(L,R) = \sum_{\substack{(v,w) \in E\\ v \in L, w \in R}} c(v,w).$$
>
