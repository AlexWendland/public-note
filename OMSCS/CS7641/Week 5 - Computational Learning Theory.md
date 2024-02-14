---
aliases: 
checked: false
course: "[[CS6200 Introduction to Graduate Algorithms]]"
created: 2024-02-13
last_edited: 2024-02-13
publish: false
tags:
  - OMSCS
type: lecture
week: 5
---
# Week 5 - Learning Theory

[[Computational learning theory]] is fundamentally about 3 things:
- defining learning problems,
- show algorithms work, and
- showing problems are easy or hard. 

When considering problems it is useful to think about:
1. The probability of successful training.
	1. The probability the process works $1 - \delta$ 
2. Number of examples you need to train on.
	1. The size of the training set $m$.
3. Complexity of the hypothesis class.
	1. How complex is the representation - [[Modelling paradigm|modelling paradigm]]
4. Accuracy to which the target concept is approximated. 
	1. Within some $\epsilon$.
5. Manner in which the examples are presented.
	1. Batch or online.
6. Manner in which the [[Training data|training data]] is collected.
	1. Learner requests examples.
	2. Teacher gives examples.
	3. Fix distribution.
	4. Examples are picked poorly.

