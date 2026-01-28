---
aliases:
created: 2023-11-12
date_checked: 2026-01-28
draft: false
last_edited: 2026-01-28
tags:
  - maths
title: Max-SAT is NP-hard
type: lemma
---
# Statement

> [!lemma] Lemma
> [Max-SAT](max-satisfiability_problem.md) is [NP-hard](np-hard.md)

# Proof

There is a [many-one reduction](many-one_reduction_(problem).md) from the [SAT problem](satisfiability_problem_(sat_problem).md) to [max-SAT](max-satisfiability_problem.md).

If we have an instance of the [SAT problem](satisfiability_problem_(sat_problem).md), we submit it to [max-SAT](max-satisfiability_problem.md). If the resulting assignment satisfies all clauses, we return it; otherwise, we return no.

As [SAT is NP-complete](sat_is_np-complete.md) this gives that [max-SAT](max-satisfiability_problem.md) is [NP-hard](np-hard.md).
