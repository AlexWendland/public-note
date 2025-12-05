---
aliases: []
checked: false
course_code: CS6215
course_name: Introduction to Graduate Algorithms
created: 2023-09-11
draft: false
last_edited: 2023-11-11
tags:
  - OMSCS
title: Week 3 - Solving Recurrences
type: lecture
week: '3'
---
# $T(n) = 4T\left (\frac{n}{2}\right ) + O(n)$

First step is to replace the [Big-O notation](../../notes/big-o_notation.md). Let $c > 0$ such that
$$T(n) \leq 4 T\left ( \frac{n}{2} \right ) + cn, \mbox{ and } T(1) \leq c.$$
Lets keep reapplying this inequality
$$\begin{align*} T(n) \leq & cn + 4T\left ( \frac{n}{2} \right )\\ \leq & cn + 4\left [ 4T\left ( \frac{n}{2^2} \right ) + \frac{cn}{2} \right ]\\
\leq & cn (1 + \frac{4}{2}) + 4^2T\left ( \frac{n}{2^2} \right )\\
\leq & cn (1 + \frac{4}{2}) + 4^2\left[ 4T\left ( \frac{n}{2^3} \right ) + \frac{cn}{2^2} \right ]\\
\leq & cn \left (1 + \frac{4}{2} + \left ( \frac{4}{2} \right )^2 \right) + 4^3T\left ( \frac{n}{2^3} \right )\\
\leq & cn \left ( \sum_{i=0}^{k-1} \left ( \frac{4}{2} \right )^i \right ) + 4^kT\left ( \frac{n}{2^k} \right )  \end{align*}$$
Now lets run this till $k = \log_2(n)$ then $\frac{n}{2^k} = 1$.
$$\begin{align*} T(n) \leq & cn \left ( \sum_{i=0}^{\log_2(n)-1} \left ( \frac{4}{2} \right )^{i} \right ) + 4^{\log_2(n)}T\left ( \frac{n}{2^{\log_2(n)}} \right ) \\
\leq & cn \ O\left ( \left ( \frac{4}{2} \right )^{\log_2(n)} \right ) + n^2c\\
\leq & O(n) O(n) + O(n^2)\\
\leq & O(n^2).\end{align*}$$
# Geometric Series

For constant $\alpha > 0$
$$\sum_{j=0}^k \alpha^k = 1 + \alpha + \alpha^2 + \ldots + \alpha^k = \begin{cases} O(\alpha^k) & \mbox{if } \alpha > 1\\ O(k) & \mbox{if } \alpha = 1\\ O(1) & \mbox{if } \alpha < 1\end{cases}.$$

# General case

Let $a > 0$, $b > 1$, and suppose we have

$$T(n) = a T\left (\frac{n}{b}\right ) + O(n).$$
This expands out to be
$$T(n) = cn\left [ 1 + \left(\frac{a}{b}\right) + \left(\frac{a}{b}\right)^2 + \ldots + \left(\frac{a}{b}\right)^{\log_b(n) - 1}\right] + a^{\log_b(n)}T(1).$$
which we can solve generically as
$$T(n) = \begin{cases} O(n^{\log_b(a)}) & \mbox{if } a>b\\ O(n\log(n)) & \mbox{if } a = b\\ O(n) & \mbox{if } a < b\end{cases}.$$

To generically solve this look into [Masters theorem](../../notes/masters_theorem.md).
