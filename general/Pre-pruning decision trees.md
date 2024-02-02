---
aliases: null
checked: false
created: 2024-02-02
last_edited: 2024-02-02
publish: false
tags: []
type: definition
---
>[!tldr] Pre-pruning decision trees
>When building a [[Decision tree|decision tree]] to avoid [[Overfitting|overfitting]] you may want to stop the branching process even if it could increase the accuracy on the [[Training data|training data]]. One method to do this is to put in requirements on the final form of the decision tree before you start training. The requirements might be:
>- Max depth of the decision tree in any one branch.
>- Minimum size of a leaf node for training data.
>- Minimum size of a parent node for training data. 

