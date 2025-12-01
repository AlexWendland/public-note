---
aliases:
checked: false
course: '[[CS7642 Reinforcement Learning]]'
created: 2025-05-14
draft: false
last_edited: 2025-05-14
tags:
  - OMSCS
type: lecture
week: 2
---
# Week 2 - Reinforcement learning basics

When evaluating different learners we normally evaluate them by the [[Policy (MDP)|policy]] they produce. However, different methods of learning can create policies in different ways - therefore we may need to also consider:

- **Computation complexity**: The time it takes for that learner to come up with that policy.
- **Sample complexity**: The amount of interactions with its environment it needs to come up with that policy.

We don't normally think about *space complexity* as with other subjects - as that is not normally a limiting factor.
