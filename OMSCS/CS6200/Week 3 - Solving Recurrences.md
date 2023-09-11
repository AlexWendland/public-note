---
aliases: []
type: lecture
publish: true
created: 2023-09-11
last_edited: 2023-09-11
tags:
  - OMSCS
course: "[[CS6200 Introduction to Graduate Algorithms]]"
week: "3"
chatgpt: false
---
# Week 3 - Solving Recurrences

## $T(n) = 4T\left (\frac{n}{2}\right ) + O(n)$

First step is to replace the [[Big-O notation]]. Let $c > 0$ such that 
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
## Geometric Series