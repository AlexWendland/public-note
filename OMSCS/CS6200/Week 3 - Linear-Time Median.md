---
aliases: []
type: lecture
publish: true
created: 2023-09-07
last_edited: 2023-09-07
tags:
  - OMSCS
course: "[[CS6200 Introduction to Graduate Algorithms]]"
week: "3"
chatgpt: false
---
# Week 3 - Linear-Time Median

> [!tldr] Median list problem
> Given an unsorted list $A = [a_1, \ldots, a_n]$ of $n$ numbers - you want to find the [[Median|median]] ($\lceil \frac{n}{2} \rceil$) element.

> [!Note] Not usual [[Median]] definition
> This isn't the usual definition of median, which in the case of odd $n$ would return the mean of the $\lceil \frac{n}{2} \rceil$ and $\lfloor \frac{n}{2} \rfloor$ elements.

Though we can solve a more generic problem.

> [!tldr] $k$th smallest element
> Given an unsorted list $A = [a_1, \ldots, a_n]$ of $n$ numbers - you want to find the $k$'th smallest element.

## Using [[Merge sort]]

A basic algorithm would be to use [[Merge sort]] on $A$ then output the $k$-th element of that list which would take $O(n\log(n))$. Though is it possible to do this without sorting $A$?

## Using [[Divide and conquer algorithms|divide and conquer]] better

>[!Note] [[Quick sort]]
>We are going to use ideas from [[Quick sort|quick sort]] algorithm.

The basic idea is summed up in following [[Pseudocode|pseudocode]]

```pseudo
Select(A, k):
1. Choose a piviot p.
2. Partition A into A_{<p}, A_{=p}, and A_{>p}.
3. If k <= |A_{<p}| then return Select(A_{<p}, k)
4. If |A_{<p}| < k <= |A_{<p}| + |A_{=p}| then retrun p.
5. Otherwise return Select(A_{>p}, k - (|A_{<p}| + |A_{=p}|))
```

Though we have skipped how we choose a pivot.