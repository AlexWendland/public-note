---
aliases: []
type: lecture
publish: true
created: 2023-09-05
last_edited: 2023-09-05
tags:
  - OMSCS
course: "[[CS6200 Introduction to Graduate Algorithms]]"
week: "3"
chatgpt: false
---
# Week 3 - Fast Integer multiplication

> [!tldr] Multiplying $n$-bit integers problem
> Given $n$-bit integers $x$ and $Y$ what is $z = xy$? 

Naïve approaches will do this in $O(n^2)$ time but you can do it faster with divide and conquer.

