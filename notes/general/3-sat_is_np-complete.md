---
aliases:
checked: false
created: 2023-11-03
draft: false
last_edited: 2023-11-12
tags:
  - programming
title: 3-SAT is NP-complete
type: lemma
---
# Statement

> [!important] Lemma
> [3-SAT](k-satisfiability_problem_(k-sat_problem).md) is [NP-complete](np-complete.md).

# Proof

We already know [3-SAT](k-satisfiability_problem_(k-sat_problem).md) is in [NP](nondeterministic_polynomial_time_(np).md), as shown in [k-SAT is in NP](k-sat_is_in_np.md).

So, we need to demonstrate that [3-SAT](k-satisfiability_problem_(k-sat_problem).md) is [NP-hard](np-hard.md). This will be done by establishing a [many-one reduction](many-one_reduction_(problem).md) to the [SAT problem](satisfiability_problem_(sat_problem).md), which is [NP-complete](np-complete.md) (see [SAT is NP-complete](sat_is_np-complete.md)). Specifically, we will show the following:

A [SAT problem](satisfiability_problem_(sat_problem).md) instance can be transformed into a [3-SAT](k-satisfiability_problem_(k-sat_problem).md) problem instance in polynomial time.
The solution to the [3-SAT](k-satisfiability_problem_(k-sat_problem).md) problem can be used to solve the [SAT problem](satisfiability_problem_(sat_problem).md).
A solution for the [3-SAT](k-satisfiability_problem_(k-sat_problem).md) problem exists if and only if a solution for the [SAT problem](satisfiability_problem_(sat_problem).md) exists.
Let $f$ be a [CNF](conjunctive_normal_form_(cnf).md) formula using $n$ variables with $m$ clauses. Our goal is to construct $f'$, a [CNF](conjunctive_normal_form_(cnf).md) formula that falls under [3-SAT](k-satisfiability_problem_(k-sat_problem).md).

For each clause $C$ in $f$, we proceed as follows:

If the clause contains 3 or fewer literals, we keep the formula unchanged, letting $C' = C$.
Otherwise, we apply [clause reduction](3-sat_is_np-complete.md#clause-reduction) to obtain $C'$.
Then, we add $C'$ to $f'$.
Since every clause in $f'$ has at most 3 literals, $f'$ belongs to [3-SAT](k-satisfiability_problem_(k-sat_problem).md).

The [clause reduction](3-sat_is_np-complete.md#clause-reduction) process takes $O(n)$ time, as each clause can be at most $n$ literals long. Applying [clause reduction](3-sat_is_np-complete.md#clause-reduction) up to $m$ times, the reduction is done in $O(nm)$, a polynomial time.

We then solve $f'$ using [3-SAT](k-satisfiability_problem_(k-sat_problem).md). If no solution is found, we conclude the same for the original; otherwise, we use the solution for the original $n$ variables. This step takes $O(1)$ time.

From [Claim 1](3-sat_is_np-complete.md#claim-1), each clause $C$ of $f$ is satisfiable if and only if its [clause reduction](3-sat_is_np-complete.md#clause-reduction) $C'$ is satisfiable. Therefore, since $f'$ consists of [clause reductions](3-sat_is_np-complete.md#clause-reduction) of $f$'s clauses, $f'$ is satisfiable if and only if $f$ is.

Hence, $f'$ has a solution if and only if $f$ does, establishing a valid reduction of the [SAT problem](satisfiability_problem_(sat_problem).md) to [3-SAT](k-satisfiability_problem_(k-sat_problem).md).

This proves that [3-SAT](k-satisfiability_problem_(k-sat_problem).md) is [NP-complete](np-complete.md), as initially stated.

## Clause reduction

>[!tldr] Clause reduction
> Given a clause
> $$ C = \bigvee_{i = 1}^k l_i$$
> with literals $l_i$ in our $n$ variables. We define the reduction
> $$ C' = (l_1 \lor l_2 \lor y_1) \land \left ( \bigwedge_{i=1}^{k-4} ( \overline{y_i} \ \lor l_{i+2} \lor y_{i+1}) \right ) \land (\overline{y_{k-3}} \ \lor l_{k-1} \lor l_k)$$
> where $y_i$ are some new variables.

## Claim 1

> [!important] Claim 1
> A clause $C$ is satisfiable if and only if it's [clause reduction](3-sat_is_np-complete.md#clause-reduction) $C'$ is satisfiable.

## Proof of claim 1

### $\Rightarrow$

Suppose we have some assignment to the variables $n$ variables such that $C$ is satisfied. Then we know at least one literal $l_a$ is true.

To make a satisfying assignment for $C'$ first keep the assignment the same for the original $n$ variables and
- set $y_i$ to be true for all $i \leq a - 2$, and
- set $y_i$ to be false for all $i \geq a - 1$.

For the first $a - 2$ clauses (in the case of $a = k$ the first $k-3$ clauses) in $C'$ they all contain $y_i$ for some $i \leq a - 2$. Therefore they are satisfied in this allocation as $y_i$ is true for all $i \leq a - 2$.

For the $a - 1$'th clause (in the case of $a = 1$ the first clause and in the case of $a = k$ the $k-2$'th clause) it contains $l_a$. Therefore this clause is satisfied.

For the $a$'th clause and above (in the case of $a = 1$ the 2'nd clause and above) it contains $\overline{y_i}$ for some $i \geq a - 1$. Therefore they are satisfied in this allocation as $y_i$ is false for $i \geq a - 1$.

This makes $C'$ satisfiable.

### $\Leftarrow$

Suppose instead $C'$ is satisfiable. Therefore we have some assignment to the original $n$ variables and an assignment to $y_i$ for $1 \leq i \leq k-3$ such that $C'$ is satisfied - so every clause in $C'$ is true.

There are 3 cases for $y_i$:
- $y_1$ is false,
- $y_{k-3}$ is true, or
- There exists and $1 \leq i \leq k-2$ such that $y_i$ is true and $y_{i+1}$ is false.

(Note if $y_1$ is true and $y_{k-3}$ is false then there must be $i$ which $y_i$ goes from being true to $y_{i+1}$ being false.)

Note in all these cases as $C'$ is satisfied there is an $l_i$ that is true.
- If $y_1$ is false either $l_1$ or $l_2$ is true.
- If $y_{k-3}$ is true either $l_{k-1}$ or $l_k$ is true.
- If $y_i$ is true and $y_{i+1}$ is false then $l_{i+2}$ is true.

Therefore as $l_i$ is true, assignment to the original $n$ variables satisfies $C$.
