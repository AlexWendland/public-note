---
aliases:
created: 2024-02-24
date_checked:
draft: false
last_edited: 2024-02-24
tags:
  - programming
title: Hill climbing
type: algorithm
---

This is the most naïve random optimisation algorithm. Suppose we have a [optimisation problem](optimisation_problem.md) where $A$ has some sense of neighbourhood $N(a)$ for each point $a \in A$.

Start at some random point $a_s \in A$ then move to the point
$$a' = \mbox{arg}\max_{a' \in N(a_s)} f(a')$$
keep iterating until $a_s = a'$.

# Pseudocode

```pseudocode
hill_climber(optimise, neighourhood):
	Input:
		optimise: The function you are looking to optimise
		neighbourhood: A function that returns the neighbourhood of a point A -> P(A).
	Output: Some a in A that is a local optimum for optimise.
1. Select random point current_best in A.
2. Let next_best be some different point in A.
3. While current_best != next_best:
	1. Let current_best = next_best
	2. next_best_score = optimise(current_best)
	3. for n in neighourhood(next_best):
		1. if optimise(n) > next_best_score
			1. next_best_score = optimise(n)
			2. next_best = n
4. Return current_best
```

# Run time

This strongly depends on the sense of neighbourhood. For example if the neighbourhoods were the entire domain this might be very slow.

# Correctness

It will only return you a local optimum but no guarantee it will hit a global optimum.
We need that the sense of neighbourhood kind of aligns with how the function behaves otherwise we are just looking at random subsets of points.
