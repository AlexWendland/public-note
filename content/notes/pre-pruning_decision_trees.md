---
aliases:
created: 2024-02-02
date_checked:
draft: false
last_edited: 2026-02-05
tags:
  - machine-learning
title: Pre-pruning decision trees
type: definition
---
>[!definition] Pre-pruning decision trees
>When building a [decision tree](decision_tree.md) to avoid [overfitting](overfitting.md) you may want to stop the branching process even if it could increase the accuracy on the [training data](training_data.md). One method to do this is to put in requirements on the final form of the decision tree before you start training. The requirements might be:
>- Max depth of the decision tree in any one branch.
>- Minimum size of a leaf node for training data.
>- Minimum size of a parent node for training data.

