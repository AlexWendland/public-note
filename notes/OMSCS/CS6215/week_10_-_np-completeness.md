---
aliases:
checked: false
course: 'CS6215 Introduction to Graduate Algorithms'
created: 2023-11-03
draft: false
last_edited: 2023-11-11
title: Week 10 - NP-completeness
tags:
  - OMSCS
type: lecture
week: 10
---
# Week 10 - NP-completeness

We are going to assume the following.

[Statement](../../general/sat_is_np-complete.md#statement)

## k-SAT

We are going to show that the [k-SAT](../../general/k-satisfiability_problem_(k-sat_problem).md) problem is [NP-Complete](../../general/np-complete.md) for $k \geq 3$.

[k-SAT](../../general/k-satisfiability_problem_(k-sat_problem).md#statement)

To do this we will show [3-SAT](../../general/k-satisfiability_problem_(k-sat_problem).md) is [NP-complete](../../general/np-complete.md) which as [3-SAT](../../general/k-satisfiability_problem_(k-sat_problem).md) is a subproblem to [k-SAT](../../general/k-satisfiability_problem_(k-sat_problem).md) for $k \geq 3$ this will prove all we need to.

We need to do the following to show this:
- Show that [3-SAT](../../general/k-satisfiability_problem_(k-sat_problem).md) is [NP](../../general/nondeterministic_polynomial_time_(np).md)
- Show there is a reduction from the [SAT problem](../../general/satisfiability_problem_(sat_problem).md) to [3-SAT](../../general/k-satisfiability_problem_(k-sat_problem).md).

## [k-SAT](../../general/k-satisfiability_problem_(k-sat_problem).md) is in [NP](../../general/nondeterministic_polynomial_time_(np).md)

[k-SAT is in NP](../../general/k-sat_is_in_np.md)

## [3-SAT](../../general/k-satisfiability_problem_(k-sat_problem).md) is [NP-Complete](../../general/np-complete.md)

[3-SAT is NP-complete](../../general/3-sat_is_np-complete.md)

Though this has shown us even more than just [3-SAT](../../general/k-satisfiability_problem_(k-sat_problem).md).

[k-SAT is NP-complete for k greater than or equal to 3](../../general/k-sat_is_np-complete_for_k_greater_than_or_equal_to_3.md)

## Practice problems

From [Algorithms](http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf) by S. Dasgupta, C. Papadimitriou, and U. Vazirani.

>[!question] 8.3 Stingy SAT

>[!question] 8.8 Exact 4-SAT

