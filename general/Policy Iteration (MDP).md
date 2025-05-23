---
aliases: 
checked: false
created: 2024-04-06
last_edited: 2024-04-06
publish: true
tags:
  - programming
type: algorithm
---
# Policy Iteration (MDP)

This is a method of solving [[Markov decision process|Markov decision processes]]. It uses [[Discounted rewards|discounted rewards]] to get a local as well as global optimum solution. 

It uses the same set up as [[Value iteration (MDP)]] but instead we use the policy to decide the utility and iterate that.

## Pseudocode

Instead of looking at the utility of a state we could instead look at the policy and use the utility to guide us.

1. Start with a random policy $\pi_0$.
2. For $t \in \mathbb{N}$ do the following
	1. Calculate $v_t(s) = \sum_{s' \in S, r \in R} p(s', r \vert s, a) [ r + \gamma v_t(s')$
		1. This is now a system of simultaneous equations as there is no max!
		2. Functionally we solve this by using value iteration, to find a stable$v_t(s)$.
	2. Set $\pi_{t+1}(s) = \mbox{arg}\max_a \sum_{s' \in S, r \in R} p(s', r \vert s, a) [r + \gamma v_t(s')]$

Then stop once you reach some sense of convergence.