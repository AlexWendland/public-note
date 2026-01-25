---
aliases:
course_code: CS7641
course_name: Machine Learning
created: 2024-04-03
date_checked:
draft: false
last_edited: 2024-04-03
tags:
  - OMSCS
title: Week 11 - Markov Decision Processes
type: lecture
week: 11
---

[Markov decision process](../../notes/markov_decision_process.md)

>[!example] Find home
> Suppose we have a world with 12 states defined by a 2d grid $S = \{(x,y) \vert 1 \leq x \leq 4, 1 \leq y \leq 3\}$. Where state $(2,2)$ is can't be entered, $(4,3)$ is home, $(4,2)$ is a pit of death, and $(1,1)$ is where we start.
>
> ![gridworld_example](../../../static/images/excalidraw/gridworld_example.excalidraw.svg)
>
> Here we define actions $A = \{$up, down, left, right$\}$ where we can't take an action that would lead us off the board or into $(2,2)$. This gives us our function for $A(s)$.
> This world is probabilistic so for each action we have a $0.8$ chance of doing what you would expect the action to do, but a $0.1$ chance of taking an action perpendicular to it (if you can't take that action then you stay where you are). This defines our transition probabilities, $T$.
> Lastly if we make it home we get a point if we die in the pit of death we lose a point.
> All this data defines a [Markov decision process](../../notes/markov_decision_process.md), in fact a special kind of process.

[Gridworld](../../notes/gridworld.md)

Given a [Markov decision process](../../notes/markov_decision_process.md) we want to come up with a policy $\pi: S \rightarrow A$ that determines what action we take in each state.

# Assigning credit

In problems like the above we only get the reward at the end. Therefore at the end of the game we need to know which moves were good, and which were bad. This is hard to do without better feedback.

[Credit assignment problem](../../notes/credit_assignment_problem.md)

# Cumulative rewards

Suppose we now get a reward for each state and the score of the run was the cumulative score of all the states we have visited.

For example in the example above instead of just providing a reward for the pit of death and getting home instead we provided a reward for all the other squares it might influence what we want to do. If it were strongly positive we might want to stay out for longer. If it were strongly negative we might chance walking past the pit of death to get home sooner or even jump in the pit of death!

# Trouble with cumulative rewards and infinite time

Suppose our actions will lead to a [sequence](../../notes/sequence.md) of rewards $r_i$ for $i \in \mathbb{N}$. If there exists some $c > 0$ such that for all $r_i > c$ then if we sum the rewards
$$
\sum_{i=1}^{\infty} r_i = \infty
$$
Instead suppose there was another sequence of actions that lead to rewards $s_i$ with $s_i > r_i$ for all $i \in \mathbb{N}$. Then taking this second set of actions we have
$$
\sum_{i=1}^{\infty} s_i = \infty.
$$
So we will have no preference over these two sets of actions even though it seems like the second set are strictly better. This is an issue so we want to factor this out.

[Discounted rewards](../../notes/discounted_rewards.md)

[Value iteration (MDP)](../../notes/value_iteration_(mdp).md)

>[!note] We only care about the policy
>Whilst we might worry that convergence of the above takes infinite time - in reality we only care about when the policy based on these utilities stops changing. This might take less time.

[Policy Iteration (MDP)](../../notes/policy_iteration_(mdp).md)

