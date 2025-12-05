---
aliases:
checked: false
created: 2024-02-24
draft: false
last_edited: 2024-02-24
tags:
  - programming
  - machine-learning
title: Restart hill climbing
type: algorithm
---
# Random restart hill climbing

Suppose we have a [optimisation problem](optimisation_problem.md) where $A$ has some sense of neighbourhood $N(a)$ for each point $a \in A$.

Then we want to run [Hill climbing](hill_climbing.md) but try to get around the issue with only finding local optimum by at the end of a run restarting in a new place.

There are lots of choices and optimisations to make here, we will need to decide a stopping condition.
- Number of iterations.
- Stop improving on the optimum value.
- A % of coverage of the points.

We can also make optimisations like remembering where a point lead us and choosing not to revisit the point - [Memoization](memoization.md).

## Run time

The run time can vary, however if we use [Memoization](memoization.md) we will try to save on number of times we run the function we are trying to optimise.

## Correctness

This has a higher chance of finding a global optimum but no guarantee.
