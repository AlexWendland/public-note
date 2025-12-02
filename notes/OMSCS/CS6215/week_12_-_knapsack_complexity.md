---
aliases:
checked: false
course: 'CS6215 Introduction to Graduate Algorithms'
created: 2023-11-12
draft: false
last_edited: 2023-11-13
title: Week 12 - Knapsack complexity
tags:
  - OMSCS
type: lecture
week: 12
---
# Week 12 - Knapsack complexity

We are going to prove that the [Knapsack-search](../../general/knapsack-search_(without_replacement).md) is [NP-complete](../../general/np-complete.md). We will do this using the [3-SAT](../../general/k-satisfiability_problem_(k-sat_problem).md) but first going through the [Subset-sum problem](../../general/subset-sum_problem.md).

## Subset-sum problem

[Statement](../../general/subset-sum_problem.md#statement)

This can be solves using [Dynamic Programming](../../general/dynamic_programming.md) in a similar way to the [Knapsack problem](../../general/knapsack_problem_(without_repetition).md) in $O(nt)$. However, similar to the [Knapsack problem](../../general/knapsack_problem_(without_repetition).md) this is not a [polynomial time](../../general/polynomial_time.md) algorithm in the length of the input as that is $n\log_2(t)$. Therefore it is [Pseudo-polynomial](../../general/pseudo-polynomial_time.md).

[Subset-sum problem is in NP](../../general/subset-sum_problem_is_in_np.md)

Moreover it is [NP-complete](../../general/np-complete.md).

[Subset-sum problem is NP-complete](../../general/subset-sum_problem_is_np-complete.md)

## Knapsack problem

This [subset-sum problem](../../general/subset-sum_problem.md) is very similar to the [Knapsack-search](../../general/knapsack-search_(without_replacement).md) problem so we have the following.

[Knapsack-search is NP-complete](../../general/knapsack-search_is_np-complete.md)

