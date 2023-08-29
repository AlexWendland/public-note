---
aliases: []
type: lecture
publish: true
created: 2023-08-29
last_edited: 2023-08-29
tags: OMSCS
course: [[CS6200 Introduction to Graduate Algorithms]]
week: 1
chatgpt: false
---
# Week 1 - Knapsack Problem

> [!tldr] The knapsack problem
> Given $n$ objects $o_i$ with weight $w_i$ and value $v_i$ how do we maximise the value of a bag that can carry weight $B$. The solution to this is a subset of objects $S \subset \{1, 2, \ldots, n\}$ such that:
> - $\sum_{i \in S} w_i \leq B$, and
> - it maximises its value $\sum_{i \in S} v_i$.

There are different versions of this problem:
- Where you can have at most one version of each object,
- Where you can have at most a given number of each object, and
- Where you can have an infinite amount of each object.

We will focus on the first problem for the next sections.

## Greedy solution

> [!example] Greed's downfall
> Suppose we have the following objects $o_i = (w_i, v_i)$
> $$O = \{(15,15), (12,10), (10,8), (5,1)\},$$
> with a max capacity of $B=22$.

Here a greedy algorithm would notice that the first object $(15,15)$ has the best value to weight ratio, so would fit one of those in the bag first. With 7 (=22-15) capacity left it would fit a single copy of the 4th object $(5,1)$ making the bag full. 

This solution has a value of 16.

However, consider the solution using objects 2 and 3. This has weight 22, so in capacity but has value 18. This is 2 value higher than the greedy solution.

In summary greedy algorithm will not work for this problem.

## Dynamic programming approach

Lets define a [[Dynamic programming|dynamic program]] for the single copy Knapsack problem.

Let $K(i, b)$ be the max value using the first $0 \leq i \leq n$ objects with a bag of capacity $0 \leq b \leq B$. 

The solution to the knapsack problem will then be $K(n,B)$.

To define the [[Recursion|recursion]] for this problem first set the base case $K(0,b) = K(i,0) = 0$. More generically define,
$$K(i,b) = \begin{cases} K(i-1,b) & \mbox{if } w_i > b\\ \max\{v_i + K(i-1,b-w_i), K(i-1,b)\} & \mbox{otherwise.} \end{cases}$$
The code for this program would look as follows.

```python

```




