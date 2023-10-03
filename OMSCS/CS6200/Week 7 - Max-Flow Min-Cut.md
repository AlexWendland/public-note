---
aliases: 
type: lecture
publish: true
created: 2023-10-03
last_edited: 2023-10-03
tags:
  - OMSCS
course: "[[CS6200 Introduction to Graduate Algorithms]]"
week: 7
chatgpt: false
---
# Week 7 - Max-Flow Min-Cut

This lecture we want to show correctness of [[Ford-Fulkerson Algorithm]].

To do this we will prove the following lemma.
![[Flows are maximal if there is no augmenting path#Statement]]
To do this lets first look at [[Cut (graph)|cuts]] of this graph in particular [[st-cut|st-cuts]].
![[st-cut]]
There is a related problem to [[Max flow problem]] called the [[Min st-cut problem]].
![[Min st-cut problem#Statement]]
Which we will show the following theorem for.
![[Max-flow min-cut Theorem#Statement]]
