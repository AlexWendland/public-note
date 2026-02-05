---
aliases:
  - training error
created: 2024-02-16
date_checked:
draft: false
last_edited: 2026-02-05
tags:
  - machine-learning
title: Training error
type: definition
---
>[!definition] Training error
>Suppose we are in the [modelling framework](modelling_framework.md) with some [training data](training_data.md) $T$ and [hypothesis space](modelling_paradigm.md) $H$. For some candidate hypothesis $h \in H$ the *training error*
>$$TrainingError(h,T) = \frac{\vert \{ (a,b) \in T \vert h(a) \neq b \}\vert}{\vert T \vert}.$$


