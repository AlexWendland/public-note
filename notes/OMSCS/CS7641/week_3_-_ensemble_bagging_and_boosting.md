---
aliases:
checked: false
course_code: CS7641
course_name: Machine Learning
created: 2024-01-24
draft: false
last_edited: 2024-01-24
tags:
  - OMSCS
title: Week 3 - Ensemble Bagging and Boosting
type: lecture
week: 3
---

[Ensemble learning](../../general/ensemble_learning.md)

The idea of Ensemble learning is to look at a subset of data and try to model that well. If we do that to enough small patches we hope we can combine this to give us a good overall understanding of the data.

This is a powerful idea when the function we are trying to map doesn't globally generalise but instead locally generalises like when people try to filter out spam from your inbox.

# Bagging

The simplest example of [Ensemble learning](../../general/ensemble_learning.md) is [Bagging](../../general/bagging.md).

[Bagging](../../general/bagging.md)

[Bagging](../../general/bagging.md) treated all data points equally and didn't focus on whether we performed well or poorly on a given data point to pick the next subset. If we fixed this we could potentially tighten up our model.

# Error rate and weak learners

[Error rate (modelling)](../../general/error_rate_(modelling).md)

Models that are considered good should always do better than chance.

[Weak learner](../../general/weak_learner.md)

# Boosting

[Boosting](../../general/boosting.md)
