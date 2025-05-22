---
aliases: 
checked: false
created: 2025-05-22
last_edited: 2025-05-22
publish: true
tags:
  - reinforcement-learning
type: definition
---
>[!tldr] Action-advantage function (RL)
>Using the [[Value function (RL)|value function]] and [[Quality function (RL)]] of a [[Policy (MDP)|policy]] $\pi$ we can work out how advantageous taking a particular action is for us given we are in a state.
>$$
>a_{\pi}(s,a) = q_{\pi}(s,a) - v_{\pi}(s)
>$$

