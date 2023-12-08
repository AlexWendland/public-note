---
aliases:
  - max-Ek-SAT
checked: false
created: 2023-11-12
last_edited: 2023-11-13
publish: true
tags:
  - programming
type: problem
---
# Statement

>[!tldr] Max-$k$-exact-satisfiability problem
>Provided with a [[Boolean function|boolean function]] $f$ in [[Conjunctive normal form (CNF)|CNF]] with $n$ variables and $m$ clauses, where each variable only appears in a single literal in each clause and each clause has exactly $k$ litterals. What is an assignment maximising the number of satisfied clauses?

# Solutions

- [[Max-SAT random approximation algorithm]]
	- Runs in $O(nm)$ time.
	- Is an $(1-2^{-k})$-approximation algorithm.

# Theory

# Related problems

- [[Max-Satisfiability Problem|Max-SAT]]
