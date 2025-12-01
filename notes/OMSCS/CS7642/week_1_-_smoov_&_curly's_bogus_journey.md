---
aliases:
checked: false
course: '[CS7642 Reinforcement Learning](../cs7642_reinforcement_learning.md)'
created: 2025-05-12
draft: false
last_edited: 2025-05-12
name: Week 1 - Smoov & Curly's Bogus Journey
tags:
  - OMSCS
type: lecture
week: 1
---
# Week 1 - Smoov & Curly's Bogus Journey

## Review

The first part of this course is a review of:

[Week 12 - Reinforcement learning](../CS7641/week_12_-_reinforcement_learning.md)

There is a change of notation within this course to the referenced lecture. Instead of using $U(s)$ for the utility - instead we use $V(s)$ for value. Instead of considering the reward function $R: S \rightarrow \mathbb{R}$ instead we consider it $R: S \times A \rightarrow \mathbb{R}$, i.e. the reward takes into account the action you have done. Therefore restated the [Bellman equation](../../general/bellman_equation.md) in this notation is as below.
$$
V(s) = \max_{a \in A_s} \left ( R(s,a) + \gamma \sum_{s' \in S} T(s,a,s') V(s') \right )
$$
Reminder of the below notation.

- **Discount factor**: $\gamma$ with $0 \leq \gamma < 1$.
- **Transition probability**: Given you are in state $s$ and you take action $a$ $T(s,a,s')$ is the probability you end up in state $s'$.
- **States**: $S$ is the set of all states.
- **Actions**: $A$ is the set of all actions, it could depend on the state therefore we talk about $A_s$ for the actions at state $s \in S$.

## Quality

Within the [Bellman equation](../../general/bellman_equation.md) if we take what is within the brackets and set it to a new function $Q(s,a)$ the quality of taking action $a$ in state $s$ we then derive the next set of equations.
$$
\begin{align*}
V(s) & = \max_{a \in A_s} Q(s,a)\\
Q(s,a) & = R(s,a) + \gamma \sum_{s' \in S} T(s,a,s') V(s')\\
& = R(s,a) + \gamma \sum_{s' \in S} T(s,a,s') \max_{a' \in A_{s'}} Q(s',a')
\end{align*}
$$
The motivation for doing this will come later, however intuitively this form will be more useful when you do not have access to $T(s,a,s')$ and $R(s,a)$ directly. Instead you can only sample 'experience data'.

## Continuations

We can apply a similar trick to derive a 3rd form of the [Bellman equation](../../general/bellman_equation.md) this time we just set $C(s,a)$ to be the summation within the definition of $Q(s,a)$.

$$
\begin{align*}
Q(s,a) & = R(s,a) + C(s,a)\\
C(s,a) & = \gamma \sum_{s' \in S} T(s,a,s') \max_{a' \in A} Q(s',a')\\
& = \gamma \sum_{s' \in S} T(s,a,s') \max_{a' \in A} R(s,a) + C(s,a)
\end{align*}
$$

Each of these will enable us to do reinforcement learning in different circumstances - but notice how they relate to one another.

|          | $V(s)$                                                     | $Q(s, a)$                                                                  | $C(s,a)$                                                 |
| -------- | ---------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------- |
| $V(s)$   | $V(s) = V(s)$                                              | $V(s) = \max_{a \in A_s} Q(s,a)$                                           | $V(s) = \max_{a \in A_s} \left(R(s,a) + C(s,a) \right )$ |
| $Q(s,a)$ | $Q(s,a) = R(s,a) + \gamma \sum_{s' \in A} T(s,a,s') V(s')$ | $Q(s,a) = Q(s,a)$                                                          | $Q(s,a) = R(s,a) + C(s,a)$                               |
| $T(s,a)$ | $C(s,a) = \gamma \sum_{s' \in S} T(s,a,s')V(s')$           | $C(s,a) = \gamma \sum_{s' \in S} T(s,a,s') \max_{a' \in A_{s'}} Q(s', a')$ | $C(s,a) = C(s,a)$                                        |

If we find $V(s)$ we need to know both the transition probabilities and the reward to derive either $Q$ or $T$ however $Q$ and $T$ have a nice property that from $Q$ we only need to know the transition probabilities to find $C$ and $V$ whereas from $C$ we only need to know the reward to determine $V$ and $Q$.
