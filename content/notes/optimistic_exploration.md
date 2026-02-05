---
aliases:
created: 2024-04-06
date_checked:
draft: false
last_edited: 2026-02-05
tags:
  - machine-learning
title: Optimistic exploration
type: definition
---
>[!definition] Optimistic exploration
>Optimistic exploration is a way of choosing actions in [Q-learning](q-learning.md). Here we set the initial values of our $\hat{Q}$ to all be very high and we always pick the action that maximises $\hat{Q}$. Then in uncertainty it will explore actions it does not know about.

