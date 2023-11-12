---
aliases: 
checked: false
created: 2023-11-12
last_edited: 2023-11-12
publish: true
tags:
  - maths
type: lemma
---
# Statement

> [!important] Lemma
> [[Integer linear programming problem|integer linear programming]] is [[NP-hard]].

# Proof

We are going to find a [[Many-one reduction (problem)|Many-one reduction]] of [[Max-Satisfiability Problem|Max-SAT]] to [[Integer linear programming problem|integer linear programming (ILP)]]. Which as [[Max-SAT is NP-hard]] will give us [[Integer linear programming problem|integer linear programming]] is too.

Suppose we have an instance of the [[Max-Satisfiability Problem|Max-SAT]] problem given by $f$. Design an [[Integer linear programming problem|ILP]] with the variables $y_i$ for each $x_i$ variable in $f$ (with $1 \leq i \leq n$) and $z_j$ for each $c_j$ clause in $f$ (with $1 \leq j \leq m$).

Now add the following constraints,
$$
0 \leq y_i \leq 1, \mbox{ and } 0 \leq z_j \leq 1
$$
this will relate to the variables $x_i$ and clauses $c_j$ being true or false.

To add constraints to reflect the clauses $c_j$ suppose $c_j$ contains positive literals involving variables $c_j^+ := \{i \vert x_i \in c_j\}$ and negative literals $c_j^- = \{i \vert \overline{x_i} \in c_j\}$. So we have the clause
$$
c_j = \left ( \bigvee_{i \in c_j^+} x_i \right ) \lor \left ( \bigvee_{i \in c_j^-} \overline{x_i} \right).
$$
For each clause $c_j$ add the following constraint
$$
\sum_{i \in c_j^+} y_i + \sum_{i \in c_j^-} (1 - y_i) \geq z_j
$$
this guarantees for integer points $z_j$ can only be 1 if $x_i = 1$ for some $i \in c^+_j$ or $x_i = 0$ for some $i \in c^-_j$. 

Lastly to define the reduction, we need to define the objective function
$$\max \sum_{j=1}^m z_j.$$
This reduction takes time $O(mn)$, as we need to go through each clause to convert them into functionals. So this takes [[Polynomial time|polynomial time]].

When provided with a solution to the [[Integer linear programming problem|ILP]] return the solution to the [[Max-Satisfiability Problem|Max-SAT]] problem with $x_i$ true for all $y_i = 1$ and $x_i$ false for all $y_i = 0$. This takes $O(n)$ time so takes [[Polynomial time|polynomial time]].

Let $v$ be the max value of the constructed [[Integer linear programming problem|ILP]] and $w$ be the max value of [[Max-Satisfiability Problem|Max-SAT]]. From [[Integer linear programming is NP-hard#Claim 1|Claim 1]] we have $w \leq v$. Equally [[Integer linear programming is NP-hard#Claim 2|Claim 2]] gives us $v \leq w$. This provides that $v = w$ and we have the solution of the contracted [[Integer linear programming problem|ILP]] if and only if we have a solution to the [[Max-Satisfiability Problem|Max-SAT]] problem. 

## Claim 1

>[!important] Claim 1
>An assignment to the variables of $f$ is reversed transformed into a feasible point in the contracted [[Integer linear programming problem|ILP]] and the value of its objective function is the number of satisfied clauses.

## Proof of Claim 1

Set $y_i = a(x_i)$ and $z_j = a(c_j)$, 1 if true and 0 if false. This satisfies the bounds on the variables and they are integers. The clause constraint
$$
\sum_{i \in c_j^+} y_i + \sum_{i \in c_j^-} (1 - y_i) \geq z_j
$$
is satisfied as if there is a literal making $c_j$ true the corresponding value of $y_i$ or $(1-y_i)$ is 1 allowing $z_j$ to be 1.

The objective function
$$\sum_{j=1}^m z_j$$
is the number of satisfied clauses by definition.

## Claim 2

>[!important] Claim 2
>A feasible point in the constructed [[Integer linear programming problem|ILP]] is transformed into a valid assignment of the variables and the value of the objective function is less than or equal to the number of satisfied clauses.
>

## Proof of Claim 2

We set $a(x_i) = y_1$ with $1$ being True and $0$ being False. The clause constraint
$$
\sum_{i \in c_j^+} y_i + \sum_{i \in c_j^-} (1 - y_i) \geq z_j
$$
guarantees that if this assignment doesn't satisfy $c_j$ then $z_j = 0$ as $0 \leq z_j \leq 1$ and 
$$
\sum_{i \in c_j^+} y_i + \sum_{i \in c_j^-} (1 - y_i) = \sum_{i \in c_j^+} 0 + \sum_{i \in c_j^-} (1 - 1) = 0 \geq z_j.
$$
Therefore
$$
\sum_{j = 1}^m z_j \leq \sum_{j=1}^m a(c_j)
$$
and we get the required statement.
