---
aliases:
checked: false
course_code: CS6215
course_name: Introduction to Graduate Algorithms
created: 2023-11-12
draft: false
last_edited: 2023-11-13
tags:
  - OMSCS
title: Week 12 - Knapsack complexity
type: lecture
week: 12
---

We are going to prove that the [Knapsack-search](../../notes/knapsack-search_(without_replacement).md) is [NP-complete](../../notes/np-complete.md). We will do this using the [3-SAT](../../notes/k-satisfiability_problem_(k-sat_problem).md) but first going through the [Subset-sum problem](../../notes/subset-sum_problem.md).

# Subset-sum problem

[Statement](../../notes/subset-sum_problem.md#statement)

This can be solves using [Dynamic Programming](../../notes/dynamic_programming.md) in a similar way to the [Knapsack problem](../../notes/knapsack_problem_(without_repetition).md) in $O(nt)$. However, similar to the [Knapsack problem](../../notes/knapsack_problem_(without_repetition).md) this is not a [polynomial time](../../notes/polynomial_time.md) algorithm in the length of the input as that is $n\log_2(t)$. Therefore it is [Pseudo-polynomial](../../notes/pseudo-polynomial_time.md).

[Subset-sum problem is in NP](../../notes/subset-sum_problem_is_in_np.md)

Moreover it is [NP-complete](../../notes/np-complete.md).

[Subset-sum problem is NP-complete](../../notes/subset-sum_problem_is_np-complete.md)

# Knapsack problem

This [subset-sum problem](../../notes/subset-sum_problem.md) is very similar to the [Knapsack-search](../../notes/knapsack-search_(without_replacement).md) problem so we have the following.

[Knapsack-search is NP-complete](../../notes/knapsack-search_is_np-complete.md)

