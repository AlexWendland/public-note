---
aliases: 
checked: false
course: "[[CS7641 Machine Learning]]"
created: 2024-04-06
last_edited: 2024-04-06
publish: true
tags:
  - OMSCS
type: lecture
week: 12
---
# Week 12 - Reinforcement learning

![[Reinforcement learning]]

There are 4 kinds of process we think about: 
- Planning:
	- Input: Model (such as [[Markov decision process]])
	- Output: Policy
	- E.g. [[Value iteration (MDP)]] or [[Policy Iteration (MDP)]]
- Learning:
	- Input: Transitions
	- Output: Policy
	- E.g. [[Reinforcement learning]]
- Modelling:
	- Input: Transitions
	- Output: Model
- Simulation:
	- Input: Model
	- Output: transitions

We can compose these strategies in two major ways.
- Simulator + learner to generate at [[Reinforcement learning|RL]] planner
- Modeler + planner to get a model-based [[Reinforcement learning|RL]]

