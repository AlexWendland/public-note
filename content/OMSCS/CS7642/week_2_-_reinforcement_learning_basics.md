---
aliases:
course_code: CS7642
course_name: Reinforcement Learning
created: 2025-05-14
date_checked: 2026-01-29
draft: false
last_edited: 2025-05-14
tags:
  - OMSCS
title: Week 2 - Reinforcement Learning Basics
type: lecture
week: 2
---

When evaluating different learners we normally evaluate them by the [policy](../../notes/policy_(mdp).md) they produce. However, different methods of learning can create policies in different ways - therefore we may need to also consider:

- **Computation complexity**: The time it takes for that learner to come up with that policy.
- **Sample complexity**: The amount of interactions with its environment it needs to come up with that policy.

We don't normally think about *space complexity* unlike other subjects - since that is not normally a limiting factor.
