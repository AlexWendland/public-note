---
aliases:
course_code: CS7642
course_name: Reinforcement Learning
created: 2025-05-14
date_checked: 2026-02-05
draft: false
last_edited: 2026-02-05
tags:
  - OMSCS
title: Week 1 - Chapter 3, Finite Markov Decision Process
type: lecture
week: 1
---

Compulsory reading from [Reinforcement learning: An introduction](http://www.incompleteideas.net/book/the-book-2nd.html).

# Finite Markov Decision Process

[Finite Markov Decision Process](../../notes/finite_markov_decision_process.md)

Using the function $p$ (defined in the finite Markov decision process), we can calculate some other probabilities.

**State transition probability**: When in state $s_t$ and you take the action $a_t$ the probability of ending up in $s_{t+1}$:
$$
T(s_t,a_t,s_{t+1}) = \sum_{r \in R} p(s_{t+1}, r \vert s_t, a_t)
$$
**Expected state-action reward**: Given you are in state $s_t$ and take action $a_t$ what is your expected reward:
$$
r(s_t,a_t) = \mathbb{E}[R_t \vert s_t, a_t] = \sum_{r \in R} r \sum_{s_{t+1}}p(s_{t+1}, r \vert s_t, a_t)
$$
# Discounted returns

If we run a game with infinite steps with positive expected reward for each step, then the value of the game is infinite. This can make it hard to distinguish better options, as they are both worth infinite value over the long term. Therefore we instead consider [discounted rewards](../../notes/discounted_rewards.md).

[Discounted rewards](../../notes/discounted_rewards.md)

# Value and policy functions

[policy](../../notes/policy_(mdp).md)

The goal of [reinforcement learning](../../notes/reinforcement_learning.md) is to determine the optimum policy that maximises some reward function, such as [discounted rewards](../../notes/discounted_rewards.md). However, if the reward is too far in the future, it can be hard to determine what to do earlier on. Therefore we determine the 'value' of a given state, which is a statement about its long-term worth to the actor.

[Value function (RL)](../../notes/value_function_(rl).md)

The best value function accurately evaluates the state's long-term worth to the actor. When using [discounted rewards](../../notes/discounted_rewards.md), this can be given by the [Bellman equation](../../notes/bellman_equation.md).

[Bellman equation](../../notes/bellman_equation.md)

It is important to note that for many problems, computing this optimum is infeasible. For example, in games like chess or Go. Therefore, [reinforcement learning](../../notes/reinforcement_learning.md) focuses on techniques to provide computationally efficient ways to approximate this optimum.
