---
aliases:
  - Markov decision processes
  - MDP
checked: false
created: 2024-04-03
draft: false
last_edited: 2024-04-03
tags:
  - probability
  - machine-learning
type: definition
---
>[!tldr] Markov decision process
>A Markov decision process is defined by the following data:
>- A set $S$ of states,
>- A set of actions $A$ (which might be dependent on the state i.e. for each state $s \in S$ we have a set $A(s) \subset A$),
>- A model which determines for each set of states $s,s' \in S$ and action $a \in A$ what the transition probabilities there are from $s$ to $s'$ given action $a$, i.e. $T(s, a, s') = \mathbb{P}[s' \vert s, a]$, and
>- A reward $R: S \rightarrow \mathbb{R}$ for being at a given state.
>When provided with this we are looking for a policy $\pi: S \rightarrow A$ that determines what action we take in each state.
