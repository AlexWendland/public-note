---
aliases: []
chatgpt: false
course: '[[CS6200 Introduction to Graduate Algorithms]]'
created: 2023-08-28
last_edited: 2023-08-28
publish: false
tags: OMSCS
type: exercise
week: 2
---
# Week 2 - Homework 1 (assessed)

>[!tldr] Question setup
>A thief is planning on burglarizing some subset of n consecutive houses in a neighborhood. The houses are labelled $1, 2, \ldots, n$ and the thief will address them sequentially. The thief has an estimate of the profit to be earned from burglarizing each house $p_i$, $i = 1, 2, \ldots, n$, where $p_i > 0$. To avoid detection, he decides that he will never burglarize two adjacent houses, meaning that if he burglarizes house 2, he cannot burglarize house 1 or house 3. Design a dynamic programming algorithm to determine the maximum total profit he can achieve.
>
> Example: In each of the following two neighborhoods, the maximum achievable profit is $100:
>
> Case 1: p = [$20, $100, $30].
> Case 2: p = [$40, $30, $10, $60].
>
> Your input is the table $p = [p_1, p_2, \ldots , p_n]$. Your output should be the maximum profit the thief can get. You do not have to return the subset of houses the thief has to burglarize to achieve the maximum.

> [!question] Part 1
> Define the entries of your table in words. E.g. T(i) or T(i, j) is ...

Let $T(i)$ = the maximum profit from burgling houses $1, 2, \ldots, i$ where you must burgle house $i$.

> [!question] Part 2
> State a recurrence for the entries of your table in terms of smaller subproblems.  Don't forget your base case(s).

Base: Set $T(-2) = T(-1) = T(0) = 0$

Recursion: Set $T(i) = \max\{T(i-3), T(i-2)\} + p_i$ for $1 \leq i \leq n$.

Solution: Return $\max\{T(n-1), T(n)\}$.

## Correctness of $T(i)$

Proof by induction.

For $i = 1$, given $p_1 > 0$ the correct solution is $p_1$. When calculating
$$\begin{align*}T(1)& = \max\{T(-2), T(-1)\} + p_1\\ & = \max\{0, 0\} + p_1\\ & = 0 + p_1\\ & = p_1.\end{align*}$$
For $i=2$, as we have to use house $2$ by the definition of $T_i$ we can't use house $1$ - therefore the correct answer is $p_2$. When calculating
$$\begin{align*}T(2)& = \max\{T(-1), T(0)\} + p_2\\ & = \max\{0, 0\} + p_2\\ & = 0 + p_2\\ & = p_2.\end{align*}$$
For $i = 3$, as we have to use house $3$ by the definition of $T_i$ we can't use house $2$ and given $p_1 > 0$ we should use house $1$. So the correct answer is $p_1 + p_3$. When calculating
$$\begin{align*} T(3)& = \max\{T(0), T(1)\} + p_3\\ & = \max\{0, p_1\} + p_3\\ & = p_1 + p_3 & \mbox{as } p_1 > 0.\end{align*}$$

Assume the subproblem is correct for all $i < k$ with $k > 3$.

For $i = k$, assume we have an optimum solution $s$. By the definition of $T_i$ $s$ must include house $k$ therefore not include house $k-1$.

Let $s^{\ast}$ be an optimal solution to this problem using house $k-3$ or $k-2$ (which are houses as $k > 3$) so
$$s^{\ast} = \max\{T(k-3), T(k-2)\}.$$
By appending house $k$ to $s^{\ast}$ have a solution to $T(k)$ and we have that
$$s^{\ast} + p_k = \max\{T(k-3), T(k-2)\} + p_k \leq s.$$

Suppose $s$ did not include house $k-2$ or $k-3$. Then I could append house $k-2$ to $s$ to get an profit of $s + p_{k-2} > s$ as we have assumed $p_{k-2} > 0$. This contradicts the maximality of $s$ therefore $s$ includes house $k-2$ or $k-3$. So $s$ without house $k$ is a solution to either $T(k-3)$ or $T(k-2)$ so we have
$$ s - p_k \leq \max\{T(k-3), T(k-2)\}.$$

Combining these inequalities we have that
$$s = \max\{T(k-3), T(k-2)\} + p_k,$$
and the algorithm returns the correct solution to $T(k)$.

Thus by induction the solution to $T(i)$ is always correct.

## Correctness of the solution

Let $s$ be an optimal solution to this problem.

Note that any solution $s^{\ast}$ to $T(n)$ or $T(n-1)$ is a potential solution to the whole problem. Therefore $s^{\ast} \leq s$, as $s$ is the optimal solution. This gives
$$\max\{T(n-1), T(n)\} \leq s.$$

If $s$ did not include house $n$ or $n-1$ then we could append house $n$ to $s$ to get solution with profit $s + p_n$ however as $p_n > 0$ we have $s < s + p_n$ and $s$ would not be maximal. Therefore $s$ must use house $n$ or $n-1$. So $s$ is a solution to either $T(n-1)$ or $T(n)$, giving
$$s \leq \max\{T(n-1), T(n)\}.$$
Combining these we have that
$$s = \max\{T(n-1), T(n)\},$$
so solves the whole problem correctly.

> [!question] Part 3
> Write pseudocode for your algorithm to solve this problem.

```psudocode
Burgle(p_1, ..., p_n):
	T(-2), T(-1), T(0) = 0
	for i = 1 -> n:
		T(i) = max(T(i-3), T(i-2)) + p_i
	return max(T(n-1), T(n))
```

> [!question] Part 4
> State and analyze the running time of your algorithm.

The run time is $O(n)$.

We do the following steps
- initialisation of the base case: $O(1)$,
- the for loop has $n$ steps calculating a max of 2 variables and doing 1 addition which is $O(1)$ therefore overall this is: $O(n)$, and
- calculating the solution is a max of 2 values which is: $O(1)$.

So the run time of the algorithm is $O(1) + O(n) + O(1) = O(n)$.
