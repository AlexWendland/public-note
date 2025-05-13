---
aliases: 
checked: false
course: "[[CS6200 Graduate introduction to Operating Systems]]"
created: 2025-05-12
last_edited: 2025-05-12
publish: true
tags:
  - OMSCS
type: lecture
week: 1
---
# Week 1 - Smoov & Curly's Bogus Journey

The first part of this course is a review of:

[[Week 12 - Reinforcement learning]]

There is a change of notation within this course to the referenced lecture. Instead of using $U(s)$ for the utility - instead we use $V(s)$ for value. Instead of considering the reward function $R: S \rightarrow \mathbb{R}$ instead we consider it $R: S \times A \rightarrow \mathbb{R}$, i.e. the reward takes into account the action you have done. Therefore restated the [[Bellman equation]] in this notation is as below.
$$
V(s) = \max_{a \in A_s} \left ( R(s,a) + \gamma \sum_{s' \in S} T(s,a,s') V(s') \right )
$$
Reminder of the below notation.

- **Discount factor**: $\gamma$ with $0 \leq \gamma < 1$.
- **Transition probability**: Given you are in state $s$ and you take action $a$ $T(s,a,s')$ is the probability you end up in state $s'$.
- **States**: $S$ is the set of all states.
- **Actions**: $A$ is the set of all actions, it could depend on the state therefore we talk about $A_s$ for the actions at state $s \in S$.



