---
aliases:
  - min st-cut
checked: false
created: 2023-10-03
draft: false
last_edited: 2023-11-11
name: Min st-cut problem
tags:
  - programming
type: problem
---
# Statement

>[!tldr] Min st-cut
>Given a [flow network](flow_network.md) $(G, c, s, t)$ what is the [st-cut](st-cut.md) $(L, R)$ with minimum capacity.

# Solutions

- [Ford-Fulkerson Algorithm](ford-fulkerson_algorithm.md)
	- $O(C \vert E \vert)$ where $C$ is the min cut.
	- This is only guaranteed to terminate for integer flows.
-

# Theory

- [Max-flow min-cut Theorem](max-flow_min-cut_theorem.md)
	- This says the solutions are the same as the [max flow](max_flow_problem.md) problems.
