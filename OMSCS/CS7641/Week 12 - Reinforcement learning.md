---
aliases: 
checked: false
course: "[[CS7641 Machine Learning]]"
created: 2024-04-06
last_edited: 2024-04-06
publish: true
tags:
  - OMSCS
type: lecture
week: 12
---
# Week 12 - Reinforcement learning

![[Transitions (MDP)]]

![[Reinforcement learning]]

There are 4 kinds of process we think about: 
- Planning:
	- Input: Model (such as [[Markov decision process]])
	- Output: Policy
	- E.g. [[Value iteration (MDP)]] or [[Policy Iteration (MDP)]]
- Learning:
	- Input: Transitions
	- Output: Policy
	- E.g. [[Reinforcement learning]]
- Modelling:
	- Input: Transitions
	- Output: Model
- Simulation:
	- Input: Model
	- Output: transitions

We can compose these strategies in two major ways.

The first uses a simulator and learner to generate at [[Reinforcement learning|RL]] planner. This method was the first major successful [[Reinforcement learning|RL]] algorithm creating a competitive backgammon solver. 

![[Model-based reinforcement learning]]

## Approaches to [[Reinforcement learning]]

There are 3 different approaches to [[Reinforcement learning|RL]],
- Policy search: Here you iterate through different polices to get the closest fit to the data.
- Value-function based: Here you use your example transitions to generate a utility function which maps state to value. Which like in [[Policy Iteration (MDP)]] you can use make policy. 
- [[Model-based reinforcement learning]]: You use the transitions to generate a model, which consists of a transition function and reward function.

## Value-function based

When using [[Value iteration (MDP)]] we look for the optimum utility function
$$
U^{\ast}(s) = R(s) + \gamma \max_{a \in A(s)} \sum_{s' \in S} T(s,a,s') U^{\ast}(s').
$$
Whereas for [[Policy Iteration (MDP)]] we look for the optimum policy given a utility function
$$\pi^{\ast} = \mbox{arg}\max_{a \in A_s} \sum_{s' \in S} T(s,a,s')U^{\ast}(s').$$
We would like a way to incorporate both approaches. 

![[Q-function (RL)]]

The [[Q-function (RL)]] has nice properties as
$$
U^{\ast}(s) = \max_{a \in A_s} Q(s,a)
$$
from the definition of $Q$. But also we can write
$$
\pi^{\ast}(s) = \mbox{arg}\max_{a \in A_s} Q(s,a)
$$
as both $\gamma$ and $R(s)$ don't effect the $\mbox{arg}\max$. 

## Incremental learning

![[Incremental learning ]]

If we have a sequence where 
$$\sum_{t \in \mathbb{N}} \alpha_t = \infty, \mbox{ and } \sum_{t \in \mathbb{N}} \alpha_t^2 < \infty
$$
with $X$ is a random variable and $x_t$ are all [[Independent identically distributed samples|i.i.d.]] then $V = \mathbb{E}[X]$.

![[Q-learning]]

## Choosing an action

The two main ideas for choosing actions are:

- choose randomly, and
- choose the best action.

The trouble with the first is you never use what you are learning - so it will be slow to explore the space you care about. The trouble with the second is you might not explore routes that are better than your current guess.

![[Explore exploit dilemma]]

You want to pick a balance between the two of them.

![[Epsilon-greedy exploration]]

In the case where you really do explore infinitely if $\epsilon_t \rightarrow 0$ then $\hat{Q} \rightarrow Q$ and $\hat{\pi} \rightarrow \pi^{\ast}$. 

![[Optimistic exploration]]