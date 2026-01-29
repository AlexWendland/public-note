---
aliases:
  - policy
created: 2025-05-14
date_checked: 2026-01-29
draft: false
last_edited: 2025-05-14
tags:
  - reinforcement-learning
title: Policy (MDP)
type: definition
---
>[!note] Policy (MDP)
> In a [Markov decision process](markov_decision_process.md), a policy is how an actor will behave in a given situation, given by $\pi: S \rightarrow A$ where $\pi(s) \in A_s$. This concept can extend to become a probabilistic policy. Let $\mathcal{A}$ be the set of probability distributions over $A$. Then a probabilistic policy is given by $\pi: S \rightarrow \mathcal{A}$ where if $\pi(s)(a)$ is non-zero then $a \in A_s$.
