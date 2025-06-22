---
aliases:
  - st-cuts
checked: false
created: 2023-10-03
last_edited: 2023-11-11
draft: false
tags:
  - programming
type: definition
---
>[!tldr] st-cut
>Given a [[Flow network|flow network]] $(G, c, s, t)$ an *st-cut* is a [[Cut (graph)|cut]] $(L, R)$ of $G$ where $s \in L$ and $t \in R$. The *capacity* of this cut is
>$$capacity(L,R) = \sum_{\substack{(v,w) \in E\\ v \in L, w \in R}} c(v,w).$$
>
