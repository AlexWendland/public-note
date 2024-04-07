---
aliases: 
checked: false
created: 2024-04-07
last_edited: 2024-04-07
publish: true
tags:
  - game-theory
type: definition
---
>[!tldr] Minimax-Q
>This is a generalisation of [[Q-learning]] to [[Stochastic games]] and but is defined for each player.
>$$Q_i(s,a) = R_i(s,a) + \gamma \sum_{s' \in S} T(s,a,s') \max_{a_i \in A_i(s')} \min_{a_1, \ldots, a_{i-1}, a_{i+1}, \ldots a_n} Q_i(s', (a_1, \ldots, a_n)).$$
>Where we [[Incremental learning|incrementally learn]] this value
>$$Q_i(s,a) \leftarrow^{\alpha}  R_i(s,a) + \gamma \max_{a_i \in A_i(s')} \min_{a_1, \ldots, a_{i-1}, a_{i+1}, \ldots a_n} Q_i(s', (a_1, \ldots, a_n)).$$

