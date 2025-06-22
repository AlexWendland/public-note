---
aliases: 
checked: false
created: 2024-04-06
last_edited: 2024-04-06
draft: false
tags:
  - programming
type: algorithm
---
# Q-learning

Q-learning is a [[Reinforcement learning|reinforcement learning]] **class** of algorithms which are value function based. It uses the approach of [[Incremental learning]] of the [[Q-function (RL)]]. We use the model of [[Transitions (MDP)|transitions]] where the learning can provide the action each iteration.

Pick an initial estimation $\hat{Q}(s,a)$ of the [[Q-function (RL)]]. 

We need to pick a learning rate $\alpha_t$ such that
$$
\sum_{t \in \mathbb{N}} \alpha_t = \infty, \mbox{ and } \sum_{t \in \mathbb{N}} \alpha_t^2 < \infty.
$$
Lastly pick how we will choose an action for a given state.

Then we [[Incremental learning|incrementally learn]] $\hat{Q}$ from our choices by
$$
\hat{Q}(s,a) \leftarrow^{\alpha} r + \gamma \max_{a' \in A_s} \hat{Q}(s', a').
$$
Note as time changes we switch which state $s \in S$ we look at, and will choose different actions.

## Correctness

There is a theorem that states for a [[Markov decision process]] if we apply $Q$ learning where a given a state $s,a$ is visited infinitely often, the states $s'$ are sampled using the transition probabilities and the rewards are distributed correctly. Then $\hat{Q}(s,a) \rightarrow Q(s,a)$ and Q-learning converges correctly.