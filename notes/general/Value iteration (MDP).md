---
aliases:
checked: false
created: 2024-04-06
draft: false
last_edited: 2024-04-06
tags:
  - programming
  - machine-learning
type: algorithm
---
# Value iteration (MDP)

This is a method of solving [[Markov decision process|Markov decision processes]]. It uses [[Discounted rewards|discounted rewards]] to get a local as well as global optimum solution.

We ideally would like to work out what the best policy is
$$
\pi^{\ast} = \mbox{arg}\max_{\pi} \mathbb{E}\left [ \sum_{i=1}^{\infty} \gamma^i R(s_t) \ \Bigg \vert \ \pi \right ].
$$
To help us work out what $\pi^{\ast}$ should be lets define the utility of a state
$$
U^{\pi}(s) = \mathbb{E}\left [ \sum_{i=1}^{\infty} \gamma^i R(s_t) \ \Bigg \vert \ \pi, s_o = s \right ].
$$
Given we could calculate the above for a given state then we can write down what the optimum strategy should be
$$
\pi^{\ast}(s) = \mbox{arg}\max_{a \in A(s)} \sum_{s' \in S} T(s,a,s') U^{\pi^{\ast}}(s').
$$
This equation should concern you as to work out $\pi^{\ast}$ you would have to know $U^{\pi^{\ast}}$ which will depend on $\pi^{\ast}$ making it circular. However using the above strategy we get a nice set of simultaneous-like equations using the following.
$$
U^{\pi^{\ast}}(s) = R(s) + \gamma \max_{a \in A(s)} \sum_{s' \in S} T(s,a,s') U^{\pi^{\ast}}(s')
$$
What is above is a [[Bellman equation]]. They are simultaneous-like due to the max in it.

## Pseudocode

We would like to solve it like a set of simultaneous equations but that doesn't work due to the max. However instead we can interactively calculate it by doing the following:

1. Start with some guess at $U^{\pi^{\ast}}(s)$ called $U_0(s)$
2. The for $t \in \mathbb{N}$ set
$$
U_{t+1} = R(s) + \gamma \max_{a \in A(s)} \sum_{s' \in S} T(s,a,s') U_t(s')
$$
keep iterating until we converge to a stable answer.

