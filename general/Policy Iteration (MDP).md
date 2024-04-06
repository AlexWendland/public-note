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
	1. Calculate $U_t(s) = R(s) + \gamma \sum_{s' \in S} T(S, \pi_t(s), s') U_t(s')$
		1. This is now a system of simultaneous equations as there is no max!
	2. Set $\pi_{t+1} = \mbox{arg}\max_a \sum_{s' \in S} T(s,a,s')U_t(s')$

Then stop once you reach some sense of convergence.