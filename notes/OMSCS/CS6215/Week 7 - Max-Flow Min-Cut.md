---
aliases:
checked: false
course: '[[CS6215 Introduction to Graduate Algorithms]]'
created: 2023-10-03
draft: false
last_edited: 2023-11-11
tags:
  - OMSCS
type: lecture
week: 7
---
# Week 6 - Homework 4 (assessed)
# Week 7 - Max-Flow Min-Cut

This lecture we want to show correctness of [[Ford-Fulkerson Algorithm]].

To do this we will prove the following Theorem.
![[Max-flow min-cut Theorem#Statement]]
To do this lets first look at [[Cut (graph)|cuts]] of this graph in particular [[st-cut|st-cuts]].
![[st-cut]]
There is a related problem to [[Max flow problem]] called the [[Min st-cut problem]].
![[Min st-cut problem#Statement]]

## Proof of the [[Max-flow min-cut Theorem]]
![[Max-flow min-cut Theorem]]
Note this gives us that $size(f^{\ast})$ for a [[Flow|flow]] from the [[Ford-Fulkerson Algorithm]] is maximal. Therefore [[Ford-Fulkerson Algorithm]] is correct and we have proven the following lemma.
![[Flows are maximal if there is no augmenting path]]
