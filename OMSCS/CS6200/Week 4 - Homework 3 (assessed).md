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
> $$S_1 = \{s \in S \vert s \leq s_1'\}, \ S_j = \{s \in S \vert s_{j-1}' < s \leq s_j'\}, \mbox{ and } S_k = \{s \in S \vert s_{k-1}' < s\}$$
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

The algorithm will follow these steps. First calculate the median $m$ of $S$ using the median of medians approach laid out in the lectures.

**Base Case:** If $k = 2$ return $m$. 

**Induction Case:** Otherwise partition the set into
$$S_{\leq m} = \{s \in S \vert s \leq m\} \mbox{ and } S_{>m} = \{s \in S \vert s > m\}.$$
then run the algorithm again on $S_{\leq m}$ and $S_{>m}$ looking for the $k/2 = 2^{a-1}$-quartiles. Let $s_1', \ldots, s_{k/2-1}'$ be returned from $S_{\leq m}$ and $s_{k/2 + 1}', \ldots, s_{k-1}'$ be returned from $S_{>m}$. Then set $s_{k/2}' = m$ and return $s_1', \ldots, s_{k/2-1}', s_{k/2}', s_{k/2 + 1}', \ldots, s_{k-1}'$.

## Correctness

Let $k = 2^i$ and we prove by induction on $i$.

**Base case:** If $i = 1$ then $k = 2$. We need to return $s_1'$ such that
$$S_1 = \{s \in S \vert s \leq s_1'\}, \mbox{ and } S_2 = \{s \in S \vert s > s_1'\}$$
have equal size. In this case $s_1' = m$ the median of this set, which gives the desired result by definition of the median.

**Induction case:** Suppose we have shown it for all $i < a$ and we want to show it for $a$.

In this case we have $\vert S \vert = 2^a b$. First we find the median $m$ of $S$ which gives us that
$$S_{\leq m} = \{s \in S \vert s \leq m\} \mbox{ and } S_{>m} = \{s \in S \vert s > m\}$$
have the same size which in this case would be $\vert S_{\leq m} \vert = \vert S_{>m} \vert = 2^{a-1}b$. As $a-1 < a$ we can solve the $2^{a-1}$-quartile problem correctly on both $S_{\leq m}$ and $S_{>m}$. 

This gives us $t_1', \ldots, t_{2^{a-1} - 1}'$ such that
$$T_1 = \{t \in S_{\leq m} \vert t \leq t_1'\}, \ T_j = \{t \in S_{\leq m} \vert t_{j-1}' < t \leq t_j'\}, \mbox{ and } T_{2^{a-1}} = \{s \in S_{\leq m} \vert t_{2^{a-1} - 1}' < t\}$$
all have the same size $\vert T_j \vert = \vert S_{\leq m} \vert / 2^{a-1} = b$. 

Similarly it gives us $v_1', \ldots v_{2^{a-1} - 1}'$ such that
$$V_1 = \{v \in S_{> m} \vert v \leq v_1'\}, \ V_j = \{v \in S_{> m} \vert v_{j-1}' < v \leq v_j'\}, \mbox{ and } V_{2^{a-1}} = \{v \in S_{> m} \vert v_{2^{a-1} - 1}' < v\}$$
all have the same size $\vert V_j \vert = \vert V_{> m} \vert / 2^{a-1} = b$.

Though substituting in the definition for $S_{\leq m}$ and $S_{> m}$ we have
$$\begin{align*}
T_1 = \{t \in S_{\leq m} \vert t \leq t_1'\} & = \{s \in S \vert t \leq t_1', t \leq m\} = \{s \in S \vert s \leq t_1'\}\\
T_j = \{t \in S_{\leq m} \vert t_{j-1}' < t \leq t_j'\} & = \{s \in S \vert t_{j-1}' < s \leq t_j', s \leq m\} = \{s \in S \vert t_{j-1}' < s \leq t_j'\}\\
T_{2^{a-1}} = \{s \in S_{\leq m} \vert t_{2^{a-1} - 1}' < t\} & = \{s \in S \vert t_{2^{a-1} - 1}' < t, t \leq m\} = \{s \in S \vert t_{2^{a-1} - 1}' < s \leq m\}\\
V_1 = \{v \in S_{> m} \vert v \leq v_1'\} & = \{s \in S \vert s \leq v_1', s > m\} = \{s \in S \vert m < s \leq v_1'\}\\ 
V_j = \{v \in S_{> m} \vert v_{j-1}' < v \leq v_j'\} & = \{s \in S \vert v_{j-1}' < s \leq v_j', s > m\} = \{s \in S \vert v_{j-1}' < s \leq v_j'\}\\ 
V_{2^{a-1}} = \{v \in S_{> m} \vert v_{2^{a-1} - 1}' < v\} & = \{s \in S \vert v_{2^{a-1} - 1}' < s, s > m\} = \{s \in S \vert v_{2^{a-1} - 1}' < s\}
\end{align*}$$
as $t_i' \leq m$ and $v_i > m$. 

These sets are exactly $S_i$ for a $k$-quartile using $t_1', \ldots t_{2^{a-1} - 1}', m, v_1', \ldots , v_{2^{a-1} - 1}'$ which all have the same size from above.

Therefore the output from the algorithm for $k = 2^a$ is correct and by induction works for all powers of $2$. 

## Run time

Let $T(n, k)$ be the runtime of our algorithm.

To calculate the median takes $O(n)$ using the median of medians algorithm.

>[!note] If $k = 2$ then $T(n,2) = O(n)$ as we only run the median of medians algorithm. 

To partition the set into $S_{\leq m}$ and $S_{> m}$ takes $O(n)$ as we need to go through the list once.

Lastly running our algorithm on $S_{\leq m}$ and $S_{> m}$ takes $2T\left (\frac{n}{2}, \frac{k}{2}\right )$ giving us running time
$$T(n,k) = 2T\left (\frac{n}{2}, \frac{k}{2}\right ) + O(n).$$
Lets replace $O(n)$ with its definition then we have
$$T(n,k) \leq 2 \ T\left (\frac{n}{2}, \frac{k}{2}\right ) + cn.$$
As $k = 2^a$ lets keep reapplying this inequality $a = \log_2(k)$ times.
$$\begin{align*}T(n,k) & \leq 2\left [2T\left (\frac{n}{2^2}, \frac{k}{2^2}\right ) + \frac{cn}{2}\right ] + cn\\ & \leq 2^2 \ T\left (\frac{n}{2^2}, \frac{k}{2^2}\right ) + 2cn\\
& \leq 2^2\left [ 2T\left (\frac{n}{2^3}, \frac{k}{2^3}\right ) + \frac{cn}{2^2} \right ] + 2cn\\
& \leq 2^3 \ T \left (\frac{n}{2^3}, \frac{k}{2^3}\right ) + 3cn\\
& \cdots\\
& \leq 2^{a - 1} \ T(2b, 2) \ + \ (a-1)cn\\
& \leq 2^{a} b + (a - 1)cn & \mbox{from the base case}\\
& \leq c\log(k)n + n - c n & \mbox{as } b = \frac{n}{2^a} \mbox{ with } a = \log_2(k)\end{align*}$$
which is dominated by $\log(k)n$ giving $T(n,k) = O(\log(k)n)$.
