---
aliases: 
type: exercise
publish: false
created: 2023-09-14
last_edited: 2023-09-14
tags:
  - OMSCS
course: "[[CS6200 Introduction to Graduate Algorithms]]"
week: 4
chatgpt: false
---
# Week 4 - Homework 3 (assessed)

>[!question] Question 
>Let $S = \{s_1, s_2, \ldots, s_n\}$ be a set of distinct real numbers. The $k$-th quantiles of $S$ is a subset of exactly $k-1$ numbers $s_1' < s_2' < \ldots < s_{k-1}'$ such that the cardinality of the sets
> 
> $$S_j = \{s \in S \vert s_{j-1}' < s \leq s_j'\}$$
> 
> are the same (i.e. these numbers split the set into $k$ subsets of equal size). Design a divide and conquer algorithm to find the $k$-th quantiles of a given set $S$ of $n$ numbers. You may assume that $k$ is a power of $2$ and that you can split the set $S$ into $k$ subsets of the same size. Your input is the set $S$, and the value of $k$. Note that $S$ is not sorted. 
>
> **Example**: $S=\{-1, 2, 4, 1, 3, 0, 18, -3\}$ and $k=2$, your algorithm should output $1$ (i.e.: the $2$-th quantile is the median).
>
> **Example**: $S=\{-1, 2, 4, 1, 3, 0, 18, -3\}$ and $k=4$ your algorithm should output $\{-1,1,3\}$.
>
>Design a Divide & Conquer algorithm to solve this problem.  Describe your algorithm in words (no pseudocode!) and justify its correctness. State and justify its runtime.  Faster (and correct) in asymptotic Big O notation is worth more credit.

## Algorithm

