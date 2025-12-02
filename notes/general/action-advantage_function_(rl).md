---
aliases:
checked: false
created: 2025-05-22
draft: false
last_edited: 2025-05-22
title: Action-advantage function (RL)
tags:
  - reinforcement-learning
type: definition
---
>[!tldr] Action-advantage function (RL)
>Using the [value function](value_function_(rl).md) and [Quality function (RL)](quality_function_(rl).md) of a [policy](policy_(mdp).md) $\pi$ we can work out how advantageous taking a particular action is for us given we are in a state.
>$$
>a_{\pi}(s,a) = q_{\pi}(s,a) - v_{\pi}(s)
>$$

