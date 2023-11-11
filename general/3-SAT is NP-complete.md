---
aliases: null
checked: false
created: 2023-11-03
last_edited: 2023-11-03
publish: true
tags:
  - programming
type: lemma
---
# Statement

> [!important] Lemma
> [[k-satisfiability problem (k-SAT problem)|3-SAT]] is [[NP-Complete|NP-complete]].

# Proof

We already know [[k-satisfiability problem (k-SAT problem)|3-SAT]] is in [[Nondeterministic Polynomial time (NP)|NP]] as [[k-SAT is in NP]].

So we need to show [[k-satisfiability problem (k-SAT problem)|3-SAT]] is [[NP-hard]]. We will do this by finding a [[Many-one reduction (problem)|many-one reduction]] to the [[Satisfiability problem (SAT problem)|SAT problem]] which is [[NP-Complete|NP-complete]] ([[SAT is NP-complete]]). This will practically involve showing the following:
- We can reformulate a instance of the [[Satisfiability problem (SAT problem)|SAT problem]] into one of the [[k-satisfiability problem (k-SAT problem)|3-SAT]] problem in polynomial time.
- We can use the solution from the [[k-satisfiability problem (k-SAT problem)|3-SAT]] to solve the [[Satisfiability problem (SAT problem)|SAT problem]].
- We show that a solution to the [[k-satisfiability problem (k-SAT problem)|3-SAT]] problem exists if and only if a problem to the [[Satisfiability problem (SAT problem)|SAT problem]] exists.

Let $f$ be a [[Conjunctive normal form (CNF)|CNF]] using $n$ variables with $m$ clauses, we want to make $f'$ a [[Conjunctive normal form (CNF)|CNF]] that is in [[k-satisfiability problem (k-SAT problem)|3-SAT]].

For each clause $C$ in $f$ we do the following:
- if the clause has 3 or less literals we don't change the formula and let $C' = C$,
- otherwise we apply [[3-SAT is NP-complete#Clause reduction|clause reduction]] to it to get $C'$.
Then we add $C'$ to $f'$.

As each clause in $f'$ has at most 3 literals $f'$ is in [[k-satisfiability problem (k-SAT problem)|3-SAT]].

[[3-SAT is NP-complete#Clause reduction|Clause reduction]] takes $O(n)$ as each clause can have length at most $n$ (if it has more it either has repeating terms which can be truncated or contradicting terms which means we can return early saying false). We apply [[3-SAT is NP-complete#Clause reduction|clause reduction]] at most $m$ times so this reduction takes $O(nm)$ polynomial time.

We then solve $f'$ using [[k-satisfiability problem (k-SAT problem)|3-SAT]], if there is no solution we return that otherwise we return whatever assignment there was to the original $n$ variables. This takes $O(1)$ time.

From [[3-SAT is NP-complete#Claim 1|Claim 1]] we know for each clause $C$ of $f$ is satisfiable if its [[3-SAT is NP-complete#Clause reduction|clause reduction]] $C'$ is satisfiable. Therefore as $f'$ is the set of [[3-SAT is NP-complete#Clause reduction|clause reduction]]'s of the clauses of $f$, we have that $f'$ is satisfiable if and only if $f$ is satisfiable.

Therefore $f'$ has a solution if and only if $f$ does and we have a valid reduction of the [[Satisfiability problem (SAT problem)|SAT problem]] to [[k-satisfiability problem (k-SAT problem)|3-SAT]].

All in all this shows that [[k-satisfiability problem (k-SAT problem)|3-SAT]] is [[NP-Complete]] as originally stated.

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
