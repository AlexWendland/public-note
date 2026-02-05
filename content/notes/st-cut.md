---
aliases:
  - st-cuts
created: 2023-10-03
date_checked: 2026-02-05
draft: false
last_edited: 2026-02-05
tags:
  - programming
title: st-cut
type: definition
---
>[!definition] st-cut
>Given a [flow network](flow_network.md) $(G, c, s, t)$, an *st-cut* is a [cut](cut_(graph).md) $(L, R)$ of $G$ where $s \in L$ and $t \in R$. The *capacity* of this cut is
>$$capacity(L,R) = \sum_{\substack{(v,w) \in E\\ v \in L, w \in R}} c(v,w).$$
