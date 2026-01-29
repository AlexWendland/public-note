---
aliases:
course_code: CS7642
course_name: Reinforcement Learning
created: 2025-05-22
date_checked: 2026-01-29
draft: false
last_edited: 2025-05-22
tags:
  - OMSCS
title: Week 3 - Supplementary planning methods
type: lecture
week:
---
# Return

In [Reinforcement learning](../../notes/reinforcement_learning.md) some people interpret the goal to be maximizing the rewards. However, with rewards sometimes distant from the current action - functionally most algorithms try to maximize the return.

[Return (RL)](../../notes/return_(rl).md)

# Value function

[value function](../../notes/value_function_(rl).md)

Again using the recursive definition of return we get a recursive definition of the value function.
$$
V^{\pi}(s) = \mathbb{E}[R_{t+1} + \gamma G_{t+1} \vert S_t = s]
$$
Which derives us the [Bellman equation](../../notes/bellman_equation.md) again.
$$
v_{\pi}(s) = \sum_{a \in A_s} \pi(a \vert s) \sum_{s \in S, r \in R}p(s', r \vert s, a)[r + \gamma v_{\pi}(s')].
$$
The first term $\pi(a \vert s)$ accounts for a probabilistic policy $\pi$ otherwise it will be 0 for all $s$ other than $\pi(s)$.

# Quality function

[Quality function (RL)](../../notes/quality_function_(rl).md)

Again using the recursive definition of return we get a recursive definition of the return we can derive the quality function in terms of the value function.
$$
q_{\pi}(s, a) = \mathbb{E}_{\pi}[R_{t+1} + \gamma G_{t+1} \vert S_t = s, A_t = a]
$$
Which in simple terms is as follows.
$$
q^{\pi}(s,a) = \sum_{s' \in S, r \in R} p(s', r \vert s, a)[r + \gamma v_{\pi}(s')].
$$
# Action-advantage function

[Action-advantage function (RL)](../../notes/action-advantage_function_(rl).md)

# Learning as you play

It is common that when you start interacting with a new environment that you don't know the [Markov decision process](../../notes/markov_decision_process.md) up front. So instead of being able to calculate the [value function](../../notes/value_function_(rl).md) or [quality function](../../notes/quality_function_(rl).md) off the bat, you need to sample the environment to learn them.

When doing this we call one sample a **trajectory**, that consists of a series of
$$
(s_t, a_{t}, r_{t+1}, s_{t+1})_{t \in \mathbb{N}}.
$$
after seeing these samples we can calculate the [Return (RL)](../../notes/return_(rl).md) for each step within the trajectory and use it estimate the [value function](../../notes/value_function_(rl).md) and [quality function](../../notes/quality_function_(rl).md) above.
$$
\begin{align*}
v_{\pi}(s) & = \mathbb{E}_{\pi}[G_t \vert S_t = s]\\
q_{\pi}(s, a) & = \mathbb{E}_{\pi}[G_t \vert S_t = s, A_t = a]\\
\end{align*}
$$
Which in practical terms just means averaging the experienced return of being in the state $s$ (and taking action $a$ for $q$). However note, this is always conditional on following policy $\pi$. When learning a policy however we want to change $\pi$ and this can be done by looking for the best one!
$$
\begin{align*}
v_{\ast}(s) & = \max_{\pi} v_{\pi}(s)
q_{\pi}(s, a) & = \max_{\pi} q_{\pi}(s,a)
\end{align*}
$$
To solve this brings us back to [Bellman equation](../../notes/bellman_equation.md)'s above.
$$
\begin{align*}
v_{\ast}(s) & = \max_a \sum_{s' \in S, r \in R} p(s',r \vert s, a) [r + \gamma v_{\ast}(s')]\\
q_{\ast}(s, a) & = \sum_{s' \in S, r \in R} p(s',r \vert s, a)[r + \gamma \max_{a' \in A} q_{\ast}(s',a')]
\end{align*}
$$
# Policy iteration

[Policy Iteration (MDP)](../../notes/policy_iteration_(mdp).md)

# Value iteration

Note: Slightly different notation in the note below.

[Value iteration (MDP)](../../notes/value_iteration_(mdp).md)
