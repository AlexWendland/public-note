---
aliases: 
checked: false
course: "[[CS7641 Machine Learning]]"
created: 2024-04-03
last_edited: 2024-04-03
publish: true
tags:
  - OMSCS
type: lecture
week: 11
---
# Week 11 - Markov Decision Processes

![[Markov decision process]]

>[!example] Find home
> Suppose we have a world with 12 states defined by a 2d grid $S = \{(x,y) \vert 1 \leq x \leq 4, 1 \leq y \leq 3\}$. Where state $(2,2)$ is can't be entered, $(4,3)$ is home, $(4,2)$ is a pit of death, and $(1,1)$ is where we start.
> 
> ![[gridworld_example.excalidraw]]
> 
> Here we define actions $A = \{$up, down, left, right$\}$ where we can't take an action that would lead us off the board or into $(2,2)$. This gives us our function for $A(s)$. 
> This world is probabilistic so for each action we have a $0.8$ chance of doing what you would expect the action to do, but a $0.1$ chance of taking an action perpendicular to it (if you can't take that action then you stay where you are). This defines our transition probabilities, $T$.
> Lastly if we make it home we get a point if we die in the pit of death we lose a point.
> All this data defines a [[Markov decision process]], in fact a special kind of process. 

![[Gridworld]]

Given a [[Markov decision process]] we want to come up with a policy $\pi: S \rightarrow A$ that determines what action we take in each state.

## Assigning credit

In problems like the above we only get the reward at the end. Therefore at the end of the game we need to know which moves were good, and which were bad. This is hard to do without better feedback.

![[Credit assignment problem]]

