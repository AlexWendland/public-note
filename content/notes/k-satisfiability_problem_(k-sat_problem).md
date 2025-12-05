---
aliases:
  - k-satisfiability problem
  - k-SAT
  - 2-SAT
  - k-SAT problem
  - 2-SAT problem
  - 3-SAT
checked: false
created: 2023-09-30
draft: false
last_edited: 2023-11-11
tags:
  - programming
title: k-satisfiability problem (k-SAT problem)
type: problem
---
# Statement

>[!tldr] k-SAT Problem
>Given a [boolean function](boolean_function.md) $f$ in [CNF](conjunctive_normal_form_(cnf).md) with $n$ variables and $m$ clauses of size at most $k$. Is there a true/false assignment to the $n$ variables that satisfies $f$. If yes then output it, otherwise say no.

# Solutions
 - [2-SAT algorithm using SCC](2-sat_algorithm_using_scc.md)
	 - This runs in $O(n + m)$.
	 - Only solves problems with clauses of size at most 2.
-

# Related
- [SAT problem](satisfiability_problem_(sat_problem).md)
	- The more general form of this problem

# Theory
- [2-SAT](k-satisfiability_problem_(k-sat_problem).md) runs in [polynomial time](polynomial_time.md).
- [k-SAT is in NP](k-sat_is_in_np.md)
- [3-SAT is NP-complete](3-sat_is_np-complete.md)
- [k-SAT is NP-complete for k greater than or equal to 3](k-sat_is_np-complete_for_k_greater_than_or_equal_to_3.md)
