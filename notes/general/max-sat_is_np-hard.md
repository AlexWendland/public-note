---
aliases:
checked: false
created: 2023-11-12
draft: false
last_edited: 2023-11-12
tags:
  - maths
title: Max-SAT is NP-hard
type: lemma
---
# Statement

> [!important] Lemma
> [Max-SAT](max-satisfiability_problem.md) is [NP-hard](np-hard.md)

# Proof

There is a [many-one reduction](many-one_reduction_(problem).md) from the [SAT problem](satisfiability_problem_(sat_problem).md) to [max-SAT](max-satisfiability_problem.md).

If we have an instance of the [SAT problem](satisfiability_problem_(sat_problem).md) plug it into [max-SAT](max-satisfiability_problem.md) and if we get an assignment the satisfies all clauses return that, otherwise say no.

As [SAT is NP-complete](sat_is_np-complete.md) this gives that [max-SAT](max-satisfiability_problem.md) is [NP-hard](np-hard.md).
