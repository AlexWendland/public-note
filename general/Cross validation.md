---
aliases:
  - cross validation
checked: false
created: 2024-01-17
last_edited: 2024-01-17
publish: true
tags:
  - machine-learning
type: definition
---
>[!tldr] Cross validation
> Suppose we are training a model on some [[Training data|training data]] $T$. If we [[Partition (set)|partition]] $T$ into [[Fold (cross validation)|folds]] $T_i$ for $1 \leq i \leq k$. Then *cross validation* is the practice of training the model on all but one [[Fold (cross validation)|fold]] $T_j$ then assessing it on $T_j$ using our [[Objective function|objective function]]. The practice usually involves doing this for all possible [[Fold (cross validation)|folds]] and picking the model with least error.  

