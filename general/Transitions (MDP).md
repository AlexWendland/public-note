---
aliases:
  - transitions
  - transition
checked: false
created: 2024-04-06
last_edited: 2024-04-06
draft: false
tags:
  - machine-learning
type: definition
---
>[!tldr] Transitions (MDP)
>When presented with a learning problem you are not provided with the [[Markov decision process|Markov decision processes]] instead you will be provided with *transitions* which are the outcome of a previous action - i.e. a tuple $(s,a,r,s') \in S \times A \times \mathbb{R} \times S$ where $s \in S$ is the start state, $a \in A$ is the action taken, $r \in \mathbb{R}$ is the reward gotten and $s' \in S$ the is state you ended up in.
>These can either be pre-computed or given a state the learn can provide the action to find out what the transition was.

