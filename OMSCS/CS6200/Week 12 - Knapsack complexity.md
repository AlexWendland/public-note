---
aliases: 
checked: false
course: "[[CS6200 Introduction to Graduate Algorithms]]"
created: 2023-11-12
last_edited: 2023-11-12
publish: true
tags:
  - OMSCS
type: lecture
week: 12
---
# Week 12 - Knapsack complexity

We are going to prove that the [[Knapsack problem (without repetition)|Knapsack problem]] is [[NP-hard]]. We will do this using the [[k-satisfiability problem (k-SAT problem)|3-SAT]] but first going through the [[Subset-sum problem]].

![[Subset-sum problem#Statement]]

This can be solves using [[Dynamic Programming]] in a similar way to the [[Knapsack problem (without repetition)|Knapsack problem]] in $O(nt)$. However, similar to the [[Knapsack problem (without repetition)|Knapsack problem]] this is not a [[Polynomial time|polynomial time]] algorithm in the length of the input as that is $n\log_2(t)$.

![[Subset-sum problem is in NP]]



