---
aliases:
  - max-Ek-SAT
created: 2023-11-12
date_checked:
draft: false
last_edited: 2023-11-13
tags:
  - programming
title: Max-k-exact-satisfiability problem
type: problem
---
# Statement

>[!tldr] Max-$k$-exact-satisfiability problem
>Provided with a [boolean function](boolean_function.md) $f$ in [CNF](conjunctive_normal_form_(cnf).md) with $n$ variables and $m$ clauses, where each variable only appears in a single literal in each clause and each clause has exactly $k$ litterals. What is an assignment maximising the number of satisfied clauses?

# Solutions

- [Max-SAT random approximation algorithm](max-sat_random_approximation_algorithm.md)
	- Runs in $O(nm)$ time.
	- Is an $(1-2^{-k})$-approximation algorithm.

# Theory

# Related problems

- [Max-SAT](max-satisfiability_problem.md)
