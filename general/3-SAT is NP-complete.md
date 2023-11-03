---
aliases: 
type: lemma
publish: true
created: 2023-11-03
last_edited: 2023-11-03
tags:
  - programming
chatgpt: false
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

Let $f$ be a [[Conjunctive normal form (CNF)|CNF]] using $n$ variables with $m$ clauses.

For each clause we do the following:
- if the clause has 3 or less literals we don't change the formula,
- otherwise we apply [[3-SAT is NP-complete#Clause reduction|clause reduction]] to it.



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

Suppose we have some assignment to the variables $n$ variables such that $C$ is satisfied. Then we know at least one literal $l_a$ is true.

To make a satisfying assignment for $C'$ first keep the assignment the same for the original $n$ variables and 
- set $y_i$ to be true for all $i \leq a - 2$, and
- set $y_i$ to be false for all $i \geq a - 1$.

For the first $a - 2$ clauses (in the case of $a = k$ the first $k-3$ clauses) in $C'$ they all contain $y_i$ for some $i \leq a - 2$. Therefore they are satisfied in this allocation as $y_i$ is true for all $i \leq a - 2$.

For the $a - 1$'th clause (in the case of $a = 1$ the first clause and in the case of $a = k$ the $k-2$'th clause) it contains $l_a$. Therefore this clause is satisfied.

For the $a$'th clause and above (in the case of $a = 1$ the 2'nd clause and above) it contains $\overline{y_i}$ for some $i \geq a - 1$. Therefore they are satisfied in this allocation as $y_i$ is false for $i \geq a - 1$.

This makes $C'$ satisfiable.

Suppose instead $C'$ is satisfiable. Therefore we have some assignment to the $n$ variables 