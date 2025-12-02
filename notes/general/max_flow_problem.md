---
aliases:
  - max flow
checked: false
created: 2023-10-02
draft: false
last_edited: 2023-11-11
title: Max flow problem
tags:
  - programming
type: problem
---
# Statement

> [!tldr] Max-flow problem
> Given a [flow network](flow_network.md) $(G, c, s, t)$ what is the max value a [flow](flow.md) on this network can have?

# Solutions
- [Ford-Fulkerson Algorithm](ford-fulkerson_algorithm.md)
	- $O(C \vert E \vert)$ where $C$ is the max flow.
	- This is only guaranteed to terminate for integer flows.
- [Edmonds-Karp algorithm](edmonds-karp_algorithm.md)
	- $O(\vert E \vert^2 \cdot \vert V \vert)$ run time.
	- Assumes positive flow values.

# Theory

- [Max-flow min-cut Theorem](max-flow_min-cut_theorem.md)
	- This says the solutions are the same as the [min st-cut](min_st-cut_problem.md) problems.
