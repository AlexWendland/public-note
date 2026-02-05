---
aliases:
  - min st-cut
created: 2023-10-03
date_checked:
draft: false
last_edited: 2026-02-05
tags:
  - programming
title: Min st-cut problem
type: problem
---
# Statement

>[!definition] Min st-cut
>Given a [flow network](flow_network.md) $(G, c, s, t)$ what is the [st-cut](st-cut.md) $(L, R)$ with minimum capacity.

# Solutions

- [Ford-Fulkerson Algorithm](ford-fulkerson_algorithm.md)
	- $O(C \vert E \vert)$ where $C$ is the min cut.
	- This is only guaranteed to terminate for integer flows.
-

# Theory

- [Max-flow min-cut Theorem](max-flow_min-cut_theorem.md)
	- This says the solutions are the same as the [max flow](max_flow_problem.md) problems.
