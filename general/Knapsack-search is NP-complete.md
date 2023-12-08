---
aliases: null
checked: false
created: 2023-11-13
last_edited: 2023-11-13
publish: true
tags:
  - programming
type: lemma
---
# Statement

> [!important] Lemma
> [[Knapsack-search (without replacement)|Knapsack-search]] is [[NP-Complete|NP-complete]].

# Proof

Note we already have [[Knapsack-search is NP]] so we just need to show it is [[NP-hard]]. We do this be finding a [[Many-one reduction (problem)|many-one reduction]] of the [[Subset-sum problem|subset-sum problem]] to it. We already have [[Subset-sum problem is NP-complete]] so this gives us the desired result.

Suppose we have an instance of the [[Subset-sum problem|subset-sum problem]] given by $a_i$ for $1 \leq i \leq n$ and $t$.

Construct a [[Knapsack-search (without replacement)|Knapsack-search]] problem with items with $o_i$ with weight $b_i := a_i$ and value $v_i := a_i$. Then set the limit $B := t$ and goal $g := t$.

Note this transformation is $O(n)$ as we just need to construct the objects. So it is [[Polynomial time]].

Suppose the constructed [[Knapsack-search (without replacement)|Knapsack-search]] problem provides solution $S$, then provide this as the solution to the [[Subset-sum problem|subset-sum problem]].

This takes $O(1)$ as we don't need to change the solution. Therefore it is [[Polynomial time|polynomial time]].

Suppose we have a solution to the constructed [[Knapsack-search (without replacement)|Knapsack-search]] problem. Then we know
$$
t = g \leq \sum_{i \in S} v_i = \sum_{i \in S} a_i = \sum_{i \in S} b_i \leq B = t$$
giving $S$ solves the [[Subset-sum problem|subset-sum problem]].

Suppose we have a solution to the [[Subset-sum problem|subset-sum problem]] $S$, then this solves the constructed [[Knapsack-search (without replacement)|Knapsack-search]] problem from the same inequalities above.

Therefore this is a valid [[Many-one reduction (problem)|many-one reduction]] and we have that [[Knapsack-search (without replacement)|Knapsack-search]] is [[NP-Complete|NP-complete]].pro
