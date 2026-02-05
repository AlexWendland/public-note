---
aliases:
  - version space
created: 2024-02-16
date_checked:
draft: false
last_edited: 2026-02-05
tags:
  - machine-learning
title: Version space
type: definition
---
>[!definition] Version space
>Suppose we are in the [modelling framework](modelling_framework.md) with some training data $T$ and a [hypothesis space](modelling_paradigm.md) $H$. The *version space* for $T$ is
>$$VS_H(T) = \{h \in H \ \vert \ h(a) = b \mbox{ for all } (a,b) \in T\}.$$
>This is the set of all [consistent learners](consistent_learner.md).

