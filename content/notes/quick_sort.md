---
aliases:
  - quick sort
checked: false
created: 2023-09-07
draft: false
last_edited: 2023-11-11
tags:
  - programming
title: Quick sort
type: algorithm
---

This is a [recursive](recursion.md) algorithm used to solve the [sorting problem](sorting_problem.md) that uses pivots $p$ to sort the list. A very brief guide to how this works is as follow

1. Choose a pivot $p$.
2. Partition $A$ into $A_{<p}$ , $A_{=p}$ , and $A_{>p}$ .
3. Recursively sort $A_{<p}$ and $A_{>p}$.

The issue is how to choose a good piviot $p$ - ideally you would want to pick the [median](median.md) element.

# Run time

This runs in $O(n\log(n))$ time.
