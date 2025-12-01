---
aliases: []
checked: false
created: 2023-08-27
draft: false
last_edited: 2023-11-11
name: Big-Omega notation
tags:
  - programming
  - maths
type: notation
---
# Big-Omega notation

[Big-Omega notation](big-omega_notation.md) is said to be the best case [runtime](run_time_complexity.md) of an algorithm. However formally it is simply a lower bound on the run time - the same as [Big-O notation](big-o_notation.md) is simply an upper bound. This has a similar formal definition
$$ f = \Omega(g) \mbox{ if } \exists \ x_0 \in \mathbb{N}, m \in \mathbb{R}_{>0} \mbox{ such that } 0 \leq m \ast g(x) \leq f(x) \ \forall x > x_0.$$
This is just saying that $f$ eventually is at least a scalar multiple of $g$.
