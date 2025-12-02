---
aliases:
checked: false
created: 2023-10-04
draft: false
last_edited: 2023-11-11
tags:
  - programming
title: Image Segmentation
type: problem
---
# Statement

>[!tldr] Image Segmentation
>Given an undirected graph $G = (V,E)$ with weights:
>- for each $v \in V$, $f(v), b(v) \geq 0$, and
>- for each $e \in E$, $p(e) \geq 0$.
>We we find [cut](cut_(graph).md) $V = F \cup B$ that maximises
>$$w(F,B) = \sum_{v \in F} f(v) + \sum_{u \in B} b(u) - \sum_{(v,u) \in cut(F,B)} p(u,v).$$

# Solutions
- [Image segmentation by max flow](image_segmentation_by_max_flow.md)
	- This runs as fast as your solution to [min st-cut](min_st-cut_problem.md)
