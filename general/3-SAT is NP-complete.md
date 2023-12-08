---
aliases: null
checked: false
created: 2023-11-03
last_edited: 2023-11-12
publish: true
tags:
  - programming
type: lemma
---
# Statement

> [!important] Lemma
> [[k-satisfiability problem (k-SAT problem)|3-SAT]] is [[NP-Complete|NP-complete]].

# Proof

We already know [[k-satisfiability problem (k-SAT problem)|3-SAT]] is in [[Nondeterministic Polynomial time (NP)|NP]], as shown in [[k-SAT is in NP]].

So, we need to demonstrate that [[k-satisfiability problem (k-SAT problem)|3-SAT]] is [[NP-hard]]. This will be done by establishing a [[Many-one reduction (problem)|many-one reduction]] to the [[Satisfiability problem (SAT problem)|SAT problem]], which is [[NP-Complete|NP-complete]] (see [[SAT is NP-complete]]). Specifically, we will show the following:

A [[Satisfiability problem (SAT problem)|SAT problem]] instance can be transformed into a [[k-satisfiability problem (k-SAT problem)|3-SAT]] problem instance in polynomial time.
The solution to the [[k-satisfiability problem (k-SAT problem)|3-SAT]] problem can be used to solve the [[Satisfiability problem (SAT problem)|SAT problem]].
A solution for the [[k-satisfiability problem (k-SAT problem)|3-SAT]] problem exists if and only if a solution for the [[Satisfiability problem (SAT problem)|SAT problem]] exists.
Let $f$ be a [[Conjunctive normal form (CNF)|CNF]] formula using $n$ variables with $m$ clauses. Our goal is to construct $f'$, a [[Conjunctive normal form (CNF)|CNF]] formula that falls under [[k-satisfiability problem (k-SAT problem)|3-SAT]].

For each clause $C$ in $f$, we proceed as follows:

If the clause contains 3 or fewer literals, we keep the formula unchanged, letting $C' = C$.
Otherwise, we apply [[3-SAT is NP-complete#Clause reduction|clause reduction]] to obtain $C'$.
Then, we add $C'$ to $f'$.
Since every clause in $f'$ has at most 3 literals, $f'$ belongs to [[k-satisfiability problem (k-SAT problem)|3-SAT]].

The [[3-SAT is NP-complete#Clause reduction|clause reduction]] process takes $O(n)$ time, as each clause can be at most $n$ literals long. Applying [[3-SAT is NP-complete#Clause reduction|clause reduction]] up to $m$ times, the reduction is done in $O(nm)$, a polynomial time.

We then solve $f'$ using [[k-satisfiability problem (k-SAT problem)|3-SAT]]. If no solution is found, we conclude the same for the original; otherwise, we use the solution for the original $n$ variables. This step takes $O(1)$ time.

From [[3-SAT is NP-complete#Claim 1|Claim 1]], each clause $C$ of $f$ is satisfiable if and only if its [[3-SAT is NP-complete#Clause reduction|clause reduction]] $C'$ is satisfiable. Therefore, since $f'$ consists of [[3-SAT is NP-complete#Clause reduction|clause reductions]] of $f$'s clauses, $f'$ is satisfiable if and only if $f$ is.

Hence, $f'$ has a solution if and only if $f$ does, establishing a valid reduction of the [[Satisfiability problem (SAT problem)|SAT problem]] to [[k-satisfiability problem (k-SAT problem)|3-SAT]].

This proves that [[k-satisfiability problem (k-SAT problem)|3-SAT]] is [[NP-Complete|NP-complete]], as initially stated.

## Clause reduction

>[!tldr] Clause reduction
> Given a clause
> $$ C = \bigvee_{i = 1}^k l_i$$
> with literals $l_i$ in our $n$ variables. We define the reduction
> $$ C' = (l_1 \lor l_2 \lor y_1) \land \left ( \bigwedge_{i=1}^{k-4} ( \overline{y_i} \ \lor l_{i+2} \lor y_{i+1}) \right ) \land (\overline{y_{k-3}} \ \lor l_{k-1} \lor l_k)$$
> where $y_i$ are some new variables.

## Claim 1

> [!important] Claim 1
> A clause $C$ is satisfiable if and only if it's [[3-SAT is NP-complete#Clause reduction|clause reduction]] $C'$ is satisfiable.

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
