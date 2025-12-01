---
aliases:
  - Knapsack-search
checked: false
created: 2023-11-02
draft: false
last_edited: 2023-11-13
name: Knapsack-search (without replacement)
tags:
  - programming
type: problem
---
# Statement

> [!tldr] Knapsack-search (without replacement)
> Given $n$ objects $o_i$ with weight $w_i$ and value $v_i$, and a goal $g$ is there a bag that has weight less than $B$ but value at least $g$. The solution to this is a subset of objects $S \subset \{1, 2, \ldots, n\}$ such that:
>
> - $\sum_{i \in S} w_i \leq B$, and
> - $\sum_{i \in S} v_i \geq g$.
>
> If there is such a bag what is it otherwise say there is no such solution.

# Solutions

- First solution
	- run time

# Theory
 - [Knapsack-search is NP](knapsack-search_is_np.md)

# Related problems

- [Knapsack problem](knapsack_problem_(without_repetition).md)

