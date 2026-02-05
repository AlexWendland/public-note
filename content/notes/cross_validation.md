---
aliases:
  - cross validation
created: 2024-01-17
date_checked:
draft: false
last_edited: 2026-02-05
tags:
  - machine-learning
title: Cross validation
type: definition
---
>[!definition] Cross validation
> Suppose we are training a model on some [training data](training_data.md) $T$. If we [partition](partition_(set).md) $T$ into [folds](fold_(cross_validation).md) $T_i$ for $1 \leq i \leq k$. Then *cross validation* is the practice of training the model on all but one [fold](fold_(cross_validation).md) $T_j$ then assessing it on $T_j$ using our [objective function](objective_function.md). The practice usually involves doing this for all possible [folds](fold_(cross_validation).md) and picking the model with least error.

