---
aliases: []
checked: false
created: 2024-04-06
last_edited: 2024-04-06
publish: true
tags:
  - machine-learning
type: definition
---
>[!tldr] Epsilon-greedy exploration
>$\epsilon$-greedy exploration is a way of choosing actions in [[Q-learning]]. For a sequence $\epsilon: \mathbb{N} \rightarrow [0,1]$ at time step $t \in \mathbb{N}$ you choose action
>$$\hat{\pi}_t(s) = \begin{cases} \mbox{arg}\max_{a \in A_s} Q(s,a) & \mbox{with probability } 1 - \epsilon_t\\ a & \mbox{for } a \in A_s \mbox{with probability } \frac{\epsilon}{\vert A_s \vert}\end{cases}$$

