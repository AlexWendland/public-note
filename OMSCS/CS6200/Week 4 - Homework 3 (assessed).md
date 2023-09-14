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
> $$S_0 = \{s \in S \vert s \leq s_1'\}, \ S_j = \{s \in S \vert s_{j-1}' < s \leq s_j'\}, \mbox{ and } S_k = \{s \in S \vert s_{k-1} < s\}$$
> 
> are the same (i.e. these numbers split the set into $k$ subsets of equal size). Design a divide and conquer algorithm to find the $k$-th quantiles of a given set $S$ of $n$ numbers. You may assume that $k$ is a power of $2$ and that you can split the set $S$ into $k$ subsets of the same size. Your input is the set $S$, and the value of $k$. Note that $S$ is not sorted. 
>
> **Example**: $S=\{-1, 2, 4, 1, 3, 0, 18, -3\}$ and $k=2$, your algorithm should output $1$ (i.e.: the $2$-th quantile is the median).
>
> **Example**: $S=\{-1, 2, 4, 1, 3, 0, 18, -3\}$ and $k=4$ your algorithm should output $\{-1,1,3\}$.
>
>$$S = \{-3, -1, 0, 1, 2, 3, 4, 18\}$$
>
>Design a Divide & Conquer algorithm to solve this problem.  Describe your algorithm in words (no pseudocode!) and justify its correctness. State and justify its runtime.  Faster (and correct) in asymptotic Big O notation is worth more credit.

## Algorithm

>[!Note] We can assume $k$ is a power of 2.
>Let $k = 2^a$. As $S$ can be divided into $2^a$ pieces we can also assume $\vert S \vert = 2^a \cdot b$. 

Broadly the algorithm will follow these steps. First calculate the median $m$ of $S$. If $k = 2$ return $m$. Otherwise partition the set into
$$S_{\leq m} = \{s \in S \vert s \leq m\} \mbox{ and } S_{>m} = \{s \in S \vert s > m\}.$$
then run the algorithm again on $S_{\leq m}$ and $S_{>m}$ looking for the $k/2 = 2^{a-1}$-quartiles. Let $s_1', \ldots, s_{k/2-1}'$ be returned from $S_{\leq m}$ and $s_{k/2 + 1}', \ldots, s_{k-1}'$ be returned from $S_{>m}$. Then set $s_{k/2}' = m$ and return $s_1', \ldots, s_{k/2-1}', s_{k/2}', s_{k/2 + 1}', \ldots, s_{k-1}'$.

## Run time

Let $T(n, k)$ be the runtime of our algorithm.

To calculate the median costs us $O(n)$ using the fast median algorithm.

To partition the set into $S_{\leq m}$ and $S_{> m}$ takes $O(n)$ as we need to go through the list once.

Lastly the other t
