---
aliases:
  - VC dimension
created: 2024-02-16
date_checked:
draft: false
last_edited: 2026-02-05
tags:
  - machine-learning
title: Vapnik-Chervonenkis dimension
type: definition
---
>[!definition] Vapnik-Chervonenkis dimension
>Suppose we are in the [modelling framework](modelling_framework.md) with feature space $A$, domain $B$, and we have [hypothesis space](modelling_paradigm.md) $H$. The *VC-dimension* of $H$ is the size of the largest set $S \subset A$ such that for all $l: S \rightarrow B$ there exists $h_l \in H$ such that $h_l(s) = l(s)$ for all $s \in S$.

