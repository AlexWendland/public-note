---
aliases:
created: 2024-04-03
date_checked:
draft: false
last_edited: 2024-04-03
tags:
  - reinforcement-learning
title: Bellman equation
type: definition
---
>[!tldr] Bellman equation
>The *Bellman equation* is used to determine the optimum [value function](value_function_(rl).md) for a given [Markov decision process](markov_decision_process.md). It defines this value function recursively as follows:
>$$
>V(s) = \max_{a \in A_s} \left ( R(s,a) + \gamma \sum_{s' \in S} T(s,a,s') V(s') \right )
>$$

