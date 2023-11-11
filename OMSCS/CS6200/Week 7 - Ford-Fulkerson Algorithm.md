---
aliases: null
chatgpt: false
course: '[[CS6200 Introduction to Graduate Algorithms]]'
created: 2023-10-02
last_edited: 2023-10-02
publish: true
tags:
  - OMSCS
type: lecture
week: 7
---
# Week 7 - Ford-Fulkerson Algorithm

This lecture will focus on the [[Max flow problem]]. To define this we need some other definitions.

![[Flow network]]

![[Flow]]

![[Max flow problem#Statement]]

## Assume we have no parallel edges

If we are in the case where there are parallel edges, we can split one edge into two by putting a vertex in the middle of it.

We will assume from now on we have no parallel edges.

## Algorithm idea

We want to build a flow by finding paths from $s$ to $t$ in a [[Flow network|flow network]]. However, if we greedily pick paths we do not get an optimal solution.

We may have to backtrack on previous chosen paths if it means we can increase the net flow. So lets define the [[Residual Network (flow)|residual network]] for a [[Flow|flow]] $f$.

![[Residual Network (flow)]]

This allows us to define the idea for the algorithm.

![[Ford-Fulkerson Algorithm#Algorithm]]
![[Ford-Fulkerson Algorithm#Run time]]
