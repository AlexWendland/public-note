---
aliases:
created: 2024-04-06
date_checked:
draft: false
last_edited: 2026-02-05
tags:
  - machine-learning
title: Q-function (RL)
type: definition
---
>[!definition] Q-function (RL)
>Suppose we are in a [Markov decision process](markov_decision_process.md) and using [discounted rewards](discounted_rewards.md) define the *Q-function* $Q : S \times A \rightarrow \mathbb{R}$ as the solution to the following equations
>$$Q(s,a) = R(s, a) + \gamma \sum_{s' \in S} T(s,a,s') \max_{a' \in A_{s'}} Q(s', a').$$

