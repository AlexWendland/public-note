---
aliases:
  - quick sort
type: algorithm
publish: true
created: 2023-09-07
last_edited: 2023-09-07
tags:
  - programming
  - list[str]
chatgpt: false
---
# Quick Sort

This is a [[Recursion|recursive]] algorithm used to solve the [[Sorting problem|sorting problem]] that uses pivots $p$ to sort the list. A very brief guide to how this works is as follow

1. Choose a pivot $p$.
2. Partition $A$ into $A_{<p}$ , $A_{=p}$ , and $A_{>p}$ .
3. Recursively sort $A_{<p}$ and $A_{>p}$.

The issue is how to choose a good piviot $p$ - ideally you would want to pick the [[Median|median]] element. 

## Run time

This runs in $O(n\log(n))$ time.