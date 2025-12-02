---
aliases:
checked: false
created: 2023-11-03
draft: false
last_edited: 2023-11-11
tags:
  - programming
title: k-SAT is NP-complete for k greater than or equal to 3
type: lemma
---
# Statement

> [!important] Lemma
> [k-SAT](k-satisfiability_problem_(k-sat_problem).md) is [NP-complete](np-complete.md) for $k \geq 3$

# Proof

Note that [k-SAT is in NP](k-sat_is_in_np.md).

Separately we have shown [3-SAT is NP-complete](3-sat_is_np-complete.md). In this proof we showed a reduction of the [SAT problem](satisfiability_problem_(sat_problem).md) to [3-SAT](k-satisfiability_problem_(k-sat_problem).md). The [clause reduction](3-sat_is_np-complete.md#clause-reduction) in this takes a [SAT problem](satisfiability_problem_(sat_problem).md) and reduces it to a problem in [3-SAT](k-satisfiability_problem_(k-sat_problem).md). The same reduction can we used to reduce the [SAT problem](satisfiability_problem_(sat_problem).md) to [k-SAT](k-satisfiability_problem_(k-sat_problem).md) for all $k \geq 3$, as a [CNF](conjunctive_normal_form_(cnf).md) with at most $3$ terms has at most $k$ terms for $k \geq 3$.

Therefore [k-SAT](k-satisfiability_problem_(k-sat_problem).md) is [NP-hard](np-hard.md) and in [NP](nondeterministic_polynomial_time_(np).md) so is [NP-complete](np-complete.md).

