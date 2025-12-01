---
aliases:
checked: false
course: '[[CS7642 Reinforcement Learning]]'
created: 2025-05-14
draft: false
last_edited: 2025-05-14
tags:
  - OMSCS
type: lecture
week: 1
---
# Week 1 - Chapter 3, Finite Markov Decision Process

Compulsory reading from [Reinforcement learning: An introduction](http://www.incompleteideas.net/book/the-book-2nd.html).

## Finite Markov Decision Process

![[Finite Markov Decision Process]]

Using the function $p$ we can calculate some other probabilities.

**State transition probability**: When in state $s_t$ and you take the action $a_t$ the probability of ending up in $s_{t+1}$:
$$
t(s_t,a_t,s_{t+1}) = \sum_{r \in R} p(s_{t+1}, r \vert s_t, a_t)
$$
**Expected state-action reward**: Given you are in state $s_t$ and take action $a_t$ what is your expected reward:
$$
r(s_t,a_t) = \mathbb{E}[R_t \vert s_t, a_t] = \sum_{r \in R} r \sum_{s_{t+1}}p(s_{t+1}, r \vert s_t, a_t)
$$
## Discounted returns

If we run a game with infinite steps which has positive expected reward for each step, then the value of the game is infinite. Which can make it hard to distinguish better options - as they both are over the long term worth infinite value. Therefore we instead consider [[Discounted rewards|discounted rewards]].

![[Discounted rewards]]

## Value and policy functions

![[Policy (MDP)|policy]]

The goal of [[Reinforcement learning|reinforcement learning]] is to determine the optimum policy that maximizes some reward function, such as [[Discounted rewards|discounted rewards]]. Though if the reward is too far in the future it can be hard to determine what to do earlier on. Therefore we determine the 'value' of a given state - this is a statement about its long term worth to the actor.

![[Value function (RL)]]

The best value function accurate evaluates the states long term worth to the actor. When using [[Discounted rewards|discounted rewards]] this can be given by the [[Bellman equation]].

![[Bellman equation]]

It is important to note that for lots of problems computing this optimum is infeasible. For example in games like chess or go. So [[Reinforcement learning|reinforcement learning]] focuses on techniques to provide computationally efficient ways to approximate this optimal.
