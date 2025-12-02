---
aliases:
checked: false
created: 2023-11-13
draft: false
last_edited: 2023-11-13
title: Knapsack-search is NP-complete
tags:
  - programming
type: lemma
---
# Statement

> [!important] Lemma
> [Knapsack-search](knapsack-search_(without_replacement).md) is [NP-complete](np-complete.md).

# Proof

Note we already have [Knapsack-search is NP](knapsack-search_is_np.md) so we just need to show it is [NP-hard](np-hard.md). We do this be finding a [many-one reduction](many-one_reduction_(problem).md) of the [subset-sum problem](subset-sum_problem.md) to it. We already have [Subset-sum problem is NP-complete](subset-sum_problem_is_np-complete.md) so this gives us the desired result.

Suppose we have an instance of the [subset-sum problem](subset-sum_problem.md) given by $a_i$ for $1 \leq i \leq n$ and $t$.

Construct a [Knapsack-search](knapsack-search_(without_replacement).md) problem with items with $o_i$ with weight $b_i := a_i$ and value $v_i := a_i$. Then set the limit $B := t$ and goal $g := t$.

Note this transformation is $O(n)$ as we just need to construct the objects. So it is [Polynomial time](polynomial_time.md).

Suppose the constructed [Knapsack-search](knapsack-search_(without_replacement).md) problem provides solution $S$, then provide this as the solution to the [subset-sum problem](subset-sum_problem.md).

This takes $O(1)$ as we don't need to change the solution. Therefore it is [polynomial time](polynomial_time.md).

Suppose we have a solution to the constructed [Knapsack-search](knapsack-search_(without_replacement).md) problem. Then we know
$$
t = g \leq \sum_{i \in S} v_i = \sum_{i \in S} a_i = \sum_{i \in S} b_i \leq B = t$$
giving $S$ solves the [subset-sum problem](subset-sum_problem.md).

Suppose we have a solution to the [subset-sum problem](subset-sum_problem.md) $S$, then this solves the constructed [Knapsack-search](knapsack-search_(without_replacement).md) problem from the same inequalities above.

Therefore this is a valid [many-one reduction](many-one_reduction_(problem).md) and we have that [Knapsack-search](knapsack-search_(without_replacement).md) is [NP-complete](np-complete.md).pro
