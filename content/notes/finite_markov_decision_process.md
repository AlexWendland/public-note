---
aliases:
  - MDP
created: 2025-05-14
date_checked:
draft: false
last_edited: 2025-05-14
tags:
  - probability
title: Finite Markov Decision Process
type: definition
---
>[!tldr] Finite Markov Decision Process
> This summaries the environment that an actor in a discrete Markovian universe experiences. It is given by:
> - **States**: A finite set of states $S$ that the actor can be in.
> - **Actions**: For each state $s \in S$ a finite set of actions $A_s$, sometimes it is convenient to refer to this as $A := \cup_{s \in S} A_s$.
> - **Rewards**: The value the actor gets from doing each action within a state, these are real values $R \subset \mathbb{R}$.
>
> We assume the actor works on discrete time steps $t \in \mathbb{N}$, at time $t$ it is in state $s_t \in S$, takes action $a_t \in A$ and gets rewards $r_t \in R$.  The actor deterministically chooses $a_t$ when in state $s_t$ but we have a probability distribution that determines the reward and next state
> $$
> p(s_{t+1}, r_{t+1} \vert s_t, a_t): S \times R \times S \times A \rightarrow [0,1]
> $$
> read this as, the probability of ending up in state $s_{t+1}$ with reward $r_{t+1}$ given they are in state $s_t$ and take action $a_t$. This is what determines how the world progresses. Notice it is Markovian as it does not depend on $t$.
>
> It is sometimes useful to think of the state you are going to be in at time step $t$ as a random variable we refer to as $S_t$, similarly for rewards as $R_t$.
