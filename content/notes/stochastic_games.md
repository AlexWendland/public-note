---
aliases:
checked: false
created: 2024-04-07
draft: false
last_edited: 2024-04-07
tags:
  - game-theory
title: Stochastic games
type: definition
---
>[!tldr] Stochastic games
>A Stochastic game is defined by the following data:
>- A number of players $n$,
>- A set $S$ of states the game can be in (normally thought of as $n$ tuples),
>- A set of actions $A_i$ for each player this may depend on the state $A_i(s) \subset A_i$ we refer to the joint set of actions as $A = A_1 \times A_2 \times \ldots \times A_n$,
>- A model which determines for each set of states $s,s' \in S$ and action $a \in A$ what the transition probabilities there are from $s$ to $s'$ given action $a$, i.e. $T(s, a, s') = \mathbb{P}[s' \vert s, a]$,
>- A reward function for each player $R_i: S \rightarrow \mathbb{R}$ for being at a given state. and
>- A discount factor $\gamma$ for [discounted rewards](discounted_rewards.md).
>
>When provided with this we are looking for a strategy for each player $\pi_i: S \rightarrow A_i$ that determines what action we take in each state.
