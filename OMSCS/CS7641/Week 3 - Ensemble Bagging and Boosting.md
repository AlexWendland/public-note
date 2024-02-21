---
aliases: 
checked: false
course: "[[CS7641 Machine Learning]]"
created: 2024-01-24
last_edited: 2024-01-24
publish: true
tags:
  - OMSCS
type: lecture
week: 3
---
# Week 3 - Ensemble Bagging and Boosting

![[Ensemble learning]]

The idea of Ensemble learning is to look at a subset of data and try to model that well. If we do that to enough small patches we hope we can combine this to give us a good overall understanding of the data.

This is a powerful idea when the function we are trying to map doesn't globally generalise but instead locally generalises like when people try to filter out spam from your inbox.

## Bagging

The simplest example of [[Ensemble learning]] is [[Bagging]].

![[Bagging]]

[[Bagging]] treated all data points evening and didn't focus on whether we performed well or poorly on a given data point to pick the next subset. If we fixed this we could potentially tighten up our model.

## Error rate and weak learners

![[Error rate (modelling)]]

Models that are considered good should always do better than chance.

![[Weak learner]]

## Boosting

![[Boosting]]