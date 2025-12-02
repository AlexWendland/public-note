---
aliases:
checked: false
course_code: CS7641
course_name: Machine Learning
created: 2024-04-06
draft: false
last_edited: 2024-04-06
tags:
  - OMSCS
title: Week 12 - Reinforcement learning
type: lecture
week: 12
---

[Transitions (MDP)](../../general/transitions_(mdp).md)

[Reinforcement learning](../../general/reinforcement_learning.md)

There are 4 kinds of process we think about:
- Planning:
	- Input: Model (such as [Markov decision process](../../general/markov_decision_process.md))
	- Output: Policy
	- E.g. [Value iteration (MDP)](../../general/value_iteration_(mdp).md) or [Policy Iteration (MDP)](../../general/policy_iteration_(mdp).md)
- Learning:
	- Input: Transitions
	- Output: Policy
	- E.g. [Reinforcement learning](../../general/reinforcement_learning.md)
- Modelling:
	- Input: Transitions
	- Output: Model
- Simulation:
	- Input: Model
	- Output: transitions

We can compose these strategies in two major ways.

The first uses a simulator and learner to generate at [RL](../../general/reinforcement_learning.md) planner. This method was the first major successful [RL](../../general/reinforcement_learning.md) algorithm creating a competitive backgammon solver.

[Model-based reinforcement learning](../../general/model-based_reinforcement_learning.md)

# Approaches to [Reinforcement learning](../../general/reinforcement_learning.md)

There are 3 different approaches to [RL](../../general/reinforcement_learning.md),
- Policy search: Here you iterate through different polices to get the closest fit to the data.
- Value-function based: Here you use your example transitions to generate a utility function which maps state to value. Which like in [Policy Iteration (MDP)](../../general/policy_iteration_(mdp).md) you can use make policy.
- [Model-based reinforcement learning](../../general/model-based_reinforcement_learning.md): You use the transitions to generate a model, which consists of a transition function and reward function.

# Value-function based

When using [Value iteration (MDP)](../../general/value_iteration_(mdp).md) we look for the optimum utility function
$$
U^{\ast}(s) = R(s) + \gamma \max_{a \in A(s)} \sum_{s' \in S} T(s,a,s') U^{\ast}(s').
$$
Whereas for [Policy Iteration (MDP)](../../general/policy_iteration_(mdp).md) we look for the optimum policy given a utility function
$$\pi^{\ast} = \mbox{arg}\max_{a \in A_s} \sum_{s' \in S} T(s,a,s')U^{\ast}(s').$$
We would like a way to incorporate both approaches.

[Q-function (RL)](../../general/q-function_(rl).md)

The [Q-function (RL)](../../general/q-function_(rl).md) has nice properties as
$$
U^{\ast}(s) = \max_{a \in A_s} Q(s,a)
$$
from the definition of $Q$. But also we can write
$$
\pi^{\ast}(s) = \mbox{arg}\max_{a \in A_s} Q(s,a)
$$
as both $\gamma$ and $R(s)$ don't effect the $\mbox{arg}\max$.

# Incremental learning

[Incremental learning](../../general/incremental_learning.md)

If we have a sequence where
$$\sum_{t \in \mathbb{N}} \alpha_t = \infty, \mbox{ and } \sum_{t \in \mathbb{N}} \alpha_t^2 < \infty
$$
with $X$ is a random variable and $x_t$ are all [i.i.d.](../../general/independent_identically_distributed_samples.md) then $V = \mathbb{E}[X]$.

[Q-learning](../../general/q-learning.md)

# Choosing an action

The two main ideas for choosing actions are:

- choose randomly, and
- choose the best action.

The trouble with the first is you never use what you are learning - so it will be slow to explore the space you care about. The trouble with the second is you might not explore routes that are better than your current guess.

[Explore exploit dilemma](../../general/explore_exploit_dilemma.md)

You want to pick a balance between the two of them.

[Epsilon-greedy exploration](../../general/epsilon-greedy_exploration.md)

In the case where you really do explore infinitely if $\epsilon_t \rightarrow 0$ then $\hat{Q} \rightarrow Q$ and $\hat{\pi} \rightarrow \pi^{\ast}$.

[Optimistic exploration](../../general/optimistic_exploration.md)
