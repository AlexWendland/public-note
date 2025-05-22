---
aliases: 
checked: false
created: 2024-04-03
last_edited: 2024-04-03
publish: true
tags:
  - reinforcement-learning
type: definition
---
>[!tldr] Bellman equation
>The *Bellman equation* is used to determine the optimum [[Value function (RL)|value function]] for a given [[Markov decision process]]. It defines this value function recursively as follows:
>$$
>V(s) = \max_{a \in A_s} \left ( R(s,a) + \gamma \sum_{s' \in S} T(s,a,s') V(s') \right )
>$$

