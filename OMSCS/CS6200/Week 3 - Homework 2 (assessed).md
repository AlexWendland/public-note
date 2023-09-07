---
aliases: []
type: exercise
publish: false
created: 2023-09-07
last_edited: 2023-09-07
tags:
  - OMSCS
course: "[[CS6200 Introduction to Graduate Algorithms]]"
week: 3
chatgpt: false
---
# Week 2 - Homework 1 (assessed)

>[!question] Question 
>Brito's youngest kid is learning the natural numbers. To practice, he writes a list of natural numbers, starting from the number $1$. In doing so, he repeats exactly one, resulting in a list $A$ of $N$ numbers, such that there is exactly one repeated, and $A$ is non decreasingly sorted. Help Brito figure out which number is repeated.
> 
> Design a divide and conquer algorithm that takes as input a sorted array $A$, of length $N$, containing all the integers from $1$ to $N-1$ exactly once, except for one which appears twice. Your algorithm should find the value of the only repeated element.
>  
>  Describe your algorithm in words (no pseudocode!) and justify its correctness. State and justify its runtime.  Faster (and correct) in asymptotic Big O notation is worth more credit.

**Subproblem:** Consider the subproblem that we are given $S$ a monotonically non-decreasing list of natural numbers of size $k > 1$ with a single duplicate that uses the numbers from $a$ to $a + k - 2$. 

Our algorithm will take list $S$ and look at the $\left \lceil \frac{k}{2} \right \rceil$ element. Given the set up to the sub-problem this will either be $a + \left \lfloor \frac{k}{2} \right \rfloor - 3$ or $a + \left \lfloor \frac{k}{2} \right \rfloor - 2$ 