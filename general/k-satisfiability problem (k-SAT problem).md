---
aliases:
  - k-satisfiability problem
  - k-SAT
  - 2-SAT
  - k-SAT problem
  - 2-SAT problem
type: problem
publish: true
created: 2023-09-30
last_edited: 2023-09-30
tags:
  - programming
chatgpt: false
---
# Statement

>[!tldr] k-SAT Problem
>Given a [[Boolean function|boolean function]] $f$ in [[Conjunctive normal form (CNF)|CNF]] with $n$ variables and $m$ clauses of size at most $k$. Is there a true/false assignment to the $n$ variables that satisfies $f$. If yes then output it, otherwise say no.

# Solutions
 - [[2-SAT algorithm using SCC]]
	 - This runs in $O(n + m)$.
	 - Only solves problems with clauses of size at most 2.
- 

# Related
- [[Satisfiability problem (SAT problem)|SAT problem]]
	- The more general form of this problem

# Theory
- $k$-SAT for $k \geq 3$ is NP-complete.
- $2-SAT$ runs in polynomial time.