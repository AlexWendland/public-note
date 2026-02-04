---
aliases:
course_code: CS6215
course_name: Introduction to Graduate Algorithms
created: 2023-11-10
date_checked:
draft: false
last_edited: 2023-11-19
tags:
  - OMSCS
title: Week 12 - Max-SAT approximation algorithm
type: lecture
week: 12
---

In this lecture we consider the a similar problem to the [SAT problem](../../notes/satisfiability_problem_(sat_problem).md).

[Max-SAT](../../notes/max-satisfiability_problem.md#statement)

This is [NP-hard](../../notes/np-hard.md).

[Max-SAT is NP-hard](../../notes/max-sat_is_np-hard.md)

Therefore it is unlikely to find any algorithm that will solve the problem quickly. However we will look at using [linear programming](../../notes/linear_programme.md) to approximate a solution.

# Approximate algorithms

Let $f$ be a [boolean function](../../notes/boolean_function.md) in [CNF](../../notes/conjunctive_normal_form_(cnf).md) with $m$ clauses. Let $m^{\ast}$ denote the solution to the [max-SAT](../../notes/max-satisfiability_problem.md) problem for $f$.

We want to construct an algorithm the on an input $f$ outputs $l$ where $l \geq m^{\ast}d$, this will be referred to as a $d$-approximation algorithm.

# Simple half-approximation algorithm

Suppose we have $f$ with variables $x_i$ for $1 \leq i \leq n$ and clauses $c_i$ for $1 \leq i \leq m$.

Make random assignment
$$
x_i = \begin{cases} T & \mbox{with probability } 1/2\\ F & \mbox{with probability } 1/2\end{cases}
$$
lets look at how many clauses this satisfies $w$. We have expectation
$$
\mathbb{E}[w] = \sum_{l=0}^m l \ \mathbb{P}(w = l)
$$
however it will be easier to break it down further. Let
$$
w_j = \begin{cases} 1 & \mbox{if } c_j \mbox{ is satisfied}\\ 0 & \mbox{otherwise}\end{cases}
$$
so we have
$$
w = \sum_{j=1}^m w_j, \mbox{ therefore } \mathbb{E}[w] = \mathbb{E}[\sum_{j=1}^m w_j] = \sum_{j=1}^m \mathbb{E}[w_j].
$$
Suppose $c_j$ has $k_j$ literals that use distinct variables. For any literal, given our assignment, its probability of being true is $1/2$. For $c_j$ to be true we just need one of these literals to be true. We have,
$$
\mathbb{E}[w_j] = 1 \cdot \mathbb{P}[w_j = 1] + 0 \cdot \mathbb{P}[w_j = 0] = \left( 1 - \frac{1}{2^{k_j}}\right) \geq \frac{1}{2}.
$$
In summary we have
$$
\mathbb{E}[w] = \sum_{j=1}^m E[w_j] \geq \frac{m}{2} \geq \frac{m^{\ast}}{2}
$$
though this is in expectation - which means there is an assignment that has more than $m/2$ clauses satisfied.

We can in fact find this pretty easily.

[Pseudocode](../../notes/max-sat_random_approximation_algorithm.md#pseudocode)

A version of this algorithm works even better on the following problem.

[Statement](../../notes/max-k-exact-satisfiability_problem.md#statement)

If we calculate this expectation more exactly we can get $m(1-2^{-k})$ clauses are satisfied.

For the case of $k=3$ it has been shown that doing any better than a $7/8$-approximation algorithm is [NP-hard](../../notes/np-hard.md).

# Integer linear programming

[Statement](../../notes/integer_linear_programming_problem.md#statement)

We can use [Max-SAT](../../notes/max-satisfiability_problem.md) to show this version of [linear programming](../../notes/linear_programme.md) is [NP-hard](../../notes/np-hard.md).

[Integer linear programming is NP-hard](../../notes/integer_linear_programming_is_np-hard.md)

However, what if we run the constructed [ILP](../../notes/integer_linear_programming_problem.md) in the proof but don't require the points to be integers? We know [Linear programming problem](../../notes/linear_programming_problem.md) can be solved in [polynomial time](../../notes/polynomial_time.md) can we use this to get an approximate solution to the [max-SAT](../../notes/max-satisfiability_problem.md) problem?

# LP relaxation for max-SAT

Let $y_i^{\ast}$ and $z_j^{\ast}$ be optimal solutions to the constructed [ILP](../../notes/integer_linear_programming_problem.md) for [max-SAT](../../notes/max-satisfiability_problem.md). Whereas let $\hat{y_i^{\ast}}$ and $\hat{z_j^{\ast}}$ be optimal solutions to the constructed [ILP](../../notes/integer_linear_programming_problem.md) for [max-SAT](../../notes/max-satisfiability_problem.md) where we drop the need to be an [Integer](../../notes/integer.md) solution.

Note as $\hat{y_i^{\ast}}$ and $\hat{z_j^{\ast}}$ are less constrained we have
$$ \sum_{j=1}^m \hat{z_j^{\ast}} \geq \sum_{j=1}^m z_j^{\ast}.$$
Next we are going to transform the point $\hat{y_i^{\ast}}$ and $\hat{z_j^{\ast}}$ into an integer point by using a random algorithm again. Set
$$
y_i = a(x_i) = \begin{cases} 1 & \mbox{with probability } \hat{y_i^{\ast}}\\ 0 & \mbox{with probability } 1 - \hat{y_i^{\ast}} \end{cases}
$$
we call this randomized rounding.

Let $w = \sum_{j=1}^m w_j$ be the number of satisfied clauses in this assignment, with $w_j = a(c_j)$. We want to look at the expectation of $w$ for this we will need the following lemma.

>[!important] Lemma 1
> $$\mathbb{P}(w_j = 1) \geq \left ( 1 - \frac{1}{e} \right )\hat{z_j^{\ast}}$$

Then we can look at the expectation of $w$
$$
\mathbb{E}[w] = \sum_{j=1}^m \mathbb{E}[w_j] = \sum_{j=1}^m \mathbb{P}(w_j = 1) \geq \left ( 1 - \frac{1}{e} \right ) \sum_{j=1}^m \hat{z_j^{\ast}} \geq  \left ( 1 - \frac{1}{e} \right ) m^{\ast}.
$$
Giving us a $\left ( 1 - \frac{1}{e} \right )$-approximation algorithm to the problem - in expectation.

# Proof of Lemma 1

For this we are going to use the [AM-GM inequality](../../notes/arithmetic_mean_is_greater_than_or_equal_to_the_geometric_mean.md). Break down the clause $c_j$ by its positive and negative literals
$$
c_j = \left ( \bigvee_{i \in c_j^+} x_i \right ) \lor \left ( \bigvee_{i \in c_j^-} \overline{x_i} \right).
$$
Then lets look at
$$
\begin{aligned}
\mathbb{P}(w_j = 1) & = 1 - \mathbb{P}(w_j = 0)\\
& = 1 - \left [ \prod_{i \in c_j^+} (1 - \hat{y_i^{\ast}}) \cdot \prod_{i \in c_j^-} \hat{y_i^{\ast}} \right ]\\
& \geq 1 - \left [\frac{1}{k} \left( \sum_{i \in c_j^+} (1 - \hat{y_i^{\ast}}) + \sum_{i \in c_j^-} \hat{y_i^{\ast}}  \right ) \right ]^k & \mbox{by the AM-GM inequality} \\
& \geq 1 - \left [ 1 - \frac{1}{k} \left ( \sum_{i \in c_j^+} \hat{y_i^{\ast}} + \sum_{i \in c_j^-} (1 - \hat{y_i^{\ast}}) \right ) \right ]\\
& \geq 1 - \left [ 1 - \frac{\hat{z_j^{\ast}}}{k} \right ]^k & \mbox{as } \sum_{i \in c_j^+} \hat{y_i^{\ast}} + \sum_{i \in c_j^-} (1 - \hat{y_i^{\ast}}) \geq \hat{z_j^{\ast}}\\
\end{aligned}
$$
Here comes a little bit of horrible functional analysis. For a fixed $k \in \mathbb{N}$ we claim
$$
1 - \left [ 1 - \frac{a}{k} \right ]^k \geq \left ( 1 - \left [ 1 - \frac{1}{k} \right ]^k \right ) a
$$
for $0 \leq a \leq 1$.

First if $k = 1$ both sides equate to $a$ and we are done. So assume $k \geq 2$.

Note for $a = 0, 1$ they are equal.

With respect to $a$ we have the second derivative of left hand side is
$$
- \frac{k-1}{k} \left [1 - \frac{a}{k} \right ]^{k-2} < 0, \mbox{ for } 0 \leq a \leq 1.
$$
Whereas the right hand side is linear with respect to $a$. Therefore we have the inequality we desire.

So we can continue

$$
\begin{aligned}
\mathbb{P}(w_j = 1) & \geq 1 - \left [ 1 - \frac{\hat{z_j^{\ast}}}{k} \right ]^k\\
& \geq \left ( 1 - \left [ 1 - \frac{1}{k} \right ]^k \right ) \hat{z_j^{\ast}}\\
& \geq \left ( 1 - \frac{1}{e} \right )\hat{z_j^{\ast}}
\end{aligned}
$$
where this last step comes from the [Taylor expansion](../../notes/taylor_expansion.md) for $e^{-x}$
$$
e^{-x} = 1 - x + \frac{x^2} + \ldots \geq 1 - x
$$
with $x = \frac{1}{k}$ gives us the inequality above.

This completes the proof of the lemma.

$\square$

# Summary of the approach

In abstract we did the following.
- Take an [NP-hard](../../notes/np-hard.md) problem,
- Reduce it to [ILP](../../notes/integer_linear_programming_problem.md),
- Relax to [linear programming](../../notes/linear_programme.md) and solve, and
- Randomize round that solution.

This is a general approach we can take to finding approximation algorithms for [NP-hard](../../notes/np-hard.md) problems.

# Comparison of approaches for [max-Ek-SAT](../../notes/max-k-exact-satisfiability_problem.md)

  | k   | Simple     | LP-based                    |
  | --- | ---------- | --------------------------- |
  | 1   | $1/2$      | $1$                         |
  | 2   | $3/4$      | $3/4$                       |
  | 3   | $7/8$      | $1 - (\frac{2}{3})^3 \approx 0.704$ |
  | k   | $1 - 2^{-k}$ | $1 - (1 - \frac{1}{k})^k$                            |

The thing to note here is that each row is at least $3/4$, so by taking the max of both algorithms we achieve a $3/4$-approximation algorithm in expectation.
