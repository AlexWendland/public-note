---
aliases:
course_code: CS6215
course_name: Introduction to Graduate Algorithms
created: 2023-10-03
date_checked:
draft: false
last_edited: 2023-11-11
tags:
  - OMSCS
title: Week 7 - Max-Flow Min-Cut
type: lecture
week: 7
---
# Week 6 - Homework 4 (assessed)
# Week 7 - Max-Flow Min-Cut

This lecture we want to show correctness of [Ford-Fulkerson Algorithm](../../notes/ford-fulkerson_algorithm.md).

To do this we will prove the following Theorem.
[Statement](../../notes/max-flow_min-cut_theorem.md#statement)
To do this lets first look at [cuts](../../notes/cut_(graph).md) of this graph in particular [st-cuts](../../notes/st-cut.md).
[st-cut](../../notes/st-cut.md)
There is a related problem to [Max flow problem](../../notes/max_flow_problem.md) called the [Min st-cut problem](../../notes/min_st-cut_problem.md).
[Statement](../../notes/min_st-cut_problem.md#statement)

## Proof of the [Max-flow min-cut Theorem](../../notes/max-flow_min-cut_theorem.md)
[Max-flow min-cut Theorem](../../notes/max-flow_min-cut_theorem.md)
Note this gives us that $size(f^{\ast})$ for a [flow](../../notes/flow.md) from the [Ford-Fulkerson Algorithm](../../notes/ford-fulkerson_algorithm.md) is maximal. Therefore [Ford-Fulkerson Algorithm](../../notes/ford-fulkerson_algorithm.md) is correct and we have proven the following lemma.
[Flows are maximal if there is no augmenting path](../../notes/flows_are_maximal_if_there_is_no_augmenting_path.md)
