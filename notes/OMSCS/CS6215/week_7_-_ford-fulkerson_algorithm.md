---
aliases:
checked: false
course_code: CS6215
course_name: Introduction to Graduate Algorithms
created: 2023-10-02
draft: false
last_edited: 2023-11-11
tags:
  - OMSCS
title: Week 7 - Ford-Fulkerson Algorithm
type: lecture
week: 7
---

This lecture will focus on the [Max flow problem](../../general/max_flow_problem.md). To define this we need some other definitions.

[Flow network](../../general/flow_network.md)

[Flow](../../general/flow.md)

[Statement](../../general/max_flow_problem.md#statement)

# Assume we have no parallel edges

If we are in the case where there are parallel edges, we can split one edge into two by putting a vertex in the middle of it.

We will assume from now on we have no parallel edges.

# Algorithm idea

We want to build a flow by finding paths from $s$ to $t$ in a [flow network](../../general/flow_network.md). However, if we greedily pick paths we do not get an optimal solution.

We may have to backtrack on previous chosen paths if it means we can increase the net flow. So lets define the [residual network](../../general/residual_network_(flow).md) for a [flow](../../general/flow.md) $f$.

[Residual Network (flow)](../../general/residual_network_(flow).md)

This allows us to define the idea for the algorithm.

[Algorithm](../../general/ford-fulkerson_algorithm.md#algorithm)
[Run time](../../general/ford-fulkerson_algorithm.md#run-time)
