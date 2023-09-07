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

## Algorithm

### Subproblem 

Consider the subproblem that we are given $S$ a monotonically non-decreasing list of natural numbers of size $k > 1$ with a single duplicate that uses the numbers from $a$ to $a + k - 2$. 

**Base case:** If $k$ = 2 or 3 return the second value in the array.

**Recurrence step**: Set a pivot $p = \left \lceil \frac{k}{2} \right \rceil$. Split the list up into two overlapping sublists $S_L$ being the first $p$ elements (starting from the $1$'st to the $p$'th element) and $S_R$ the last $k + 1 - p$ elements (starting from the $p$'th element to the $k$'th). If the $p$'th element is $a + p - 2$ then return the result of solving the subproblem on $S_R$ otherwise return the result of solving the subproblem on $S_L$.

### Full algorithm

We are given a list of $k := N$ elements that starts with $a := 1$ and $A$ is a monotonically non-decreasing list of natural numbers from $a = 1$ to $a + k - 2 = 1 + N - 2 = N - 1$ with a single duplicate. Therefore the original problem fits the definition of our sub problem and we solve the subproblem on it as described above.

## Correctness

Proof by induction on the size of the list $k$.

### Base case

If $k = 2$, then both elements are the duplicate elements so either of them is the correct solution, giving that the second element is the correct solution.

If $k = 3$, then either the first two entries are the duplicates or the last two are. In either case the second entry is the duplicate - therefore it suffices to return the second element.

### Induction step
Let $k > 3$ and suppose we have the subproblem returns the correct answer for all lists of size $i$ with $1 < i < k$ and we want to prove for a list $S$ of size $k$.

Given the lists $S_L$ and $S_R$ are overlapping by only the $p = \left \lceil \frac{k}{2} \right \rceil$'th element we know the duplicate adjacent entries are either both in exactly one of $S_L$ or $S_R$. (If they were in both the lists would overlap by two elements.)

If $S_L$ **does contain duplicates** then it has $p-1$ different elements making the $p$'th term $a + p - 2$. (The algorithm applies itself to the subproblem to $S_L$.) So $S_L$ is a monotonically non-decreasing list of natural numbers of size $p = \left \lceil \frac{k}{2} \right \rceil \geq \left \lceil \frac{4}{2} \right \rceil > 1$ with a single duplicate that uses the numbers from $a$ to $a + p - 2$. Therefore $S_L$ fits our subproblem and has size $p = \left \lceil \frac{k}{2} \right \rceil < k$ which our algorithm finishes correctly on. Therefore the algorithm on $S$ in this case returns the correct answer.

If $S_L$ **does not contain duplicates** then it has $p$ different elements making the $p$'th term $a + p - 1$. (The algorithm applies itself to the subproblem $S_R$.) So $S_R$ is a monotonically non-decreasing list of natural numbers of size $k + 1 - p = \left \lceil \frac{2k + 2 - k}{2} \right \rceil \geq \left \lceil \frac{4 + 2}{2} \right \rceil > 1$ with a single duplicate that uses the numbers from $(a + p - 1)$ to $a + k - 1 = (a + p - 1) + (k + 1 - p) - 1$. There $S_R$ fits into our subproblem and has size $k + 1 - p < k$ as $k \geq 4$ so $p \geq 2$ so our subproblem solves correctly on $S_R$. Therefore the the algorithm on $S$ in this case returns the correct answer.

This proves that the algorithm returns correctly on list of size $k$. Therefore by induction our algorithm returns correctly for all cases.

## Run time




