---
aliases: 
type: lecture
publish: true
created: 2023-10-24
last_edited: 2023-10-24
tags:
  - OMSCS
course: "[[CS6200 Introduction to Graduate Algorithms]]"
week: 10
chatgpt: false
---
# Week 10 - NP-complete overview

## Complexity classes

![[Nondeterministic Polynomial time (NP)]]

In this class we use the [[Search problems|search problem]] definition.

![[Search problems]]

Note here we have.

![[Polynomial time is a subset of NP-complete#Statement]]

There is an open problem.

![[P equals NP or P not equals NP#P equals NP or P not equals NP]]

## Satisfiability

![[Satisfiability problem (SAT problem)#Statement|SAT problem]]

![[The Satisfiability problem is in NP]]

## k-colourings problem

![[k-colourings problem (graphs)#Statement]]

![[The k-colourings problem is in NP]]

## [[Minimum Spanning Tree problem (MST)|MST]]

![[Minimum Spanning Tree problem (MST)#Statement|MST]]

![[Minimum Spanning Tree problem is in NP]]

This proof was relatively easy as [[Minimum Spanning Tree problem (MST)|MST]] is a [[Polynomial time|polynomial time]] problem. This is shown by what is above and [[Kruskal's algorithm]].

## Knapsack problem

![[Knapsack problem (without repetition)#Statement]]

Whilst the [[Knapsack problem (without repetition)|Knapsack problem]] is of the correct form to be a [[Search problems|search problem]] we can't currently check if a solution is correct in polynomial time. Therefore the [[Knapsack problem (without repetition)|Knapsack problem]] isn't known to be in [[Nondeterministic Polynomial time (NP)|NP]].

Similarly we say that the [[Knapsack problem (without repetition)|Knapsack problem]] isn't known to be in [[Polynomial time|polynomial time]] either.

We say it isn't known to be as there might be a super clever algorithm that happens to solve the [[Knapsack problem (without repetition)|Knapsack problem]] in polynomial time.

However, there is a variant of the problem that is in [[Nondeterministic Polynomial time (NP)|NP]].

![[Knapsack-search (without replacement)#Statement]]

Here instead of having to check if a solution is maximal we can instead just check if it has enough value.

![[Knapsack-search is NP]]

## Revisit [[P equals NP or P not equals NP]]




