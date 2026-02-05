---
aliases:
  - max-SAT problem
  - Max-SAT problem
  - max-SAT
  - Max-SAT
created: 2023-11-12
date_checked:
draft: false
last_edited: 2026-02-05
tags:
  - programming
title: Max-Satisfiability Problem
type: problem
---
# Statement

>[!definition] Max-Satisfiability Problem (Max-SAT problem)
>Provided with a [boolean function](boolean_function.md) $f$ in [CNF](conjunctive_normal_form_(cnf).md) with $n$ variables and $m$ clauses, where each variable only appears in a single literal in each clause. What is an assignment maximising the number of satisfied clauses?

# Solutions

- [Max-SAT random approximation algorithm](max-sat_random_approximation_algorithm.md)
	- Runs in $O(nm)$ and achieves a $1/2$-approximation.

# Theory

- [Max-SAT is NP-hard](max-sat_is_np-hard.md)

# Related problems

- [SAT problem](satisfiability_problem_(sat_problem).md)
