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

## 20 Questions

20 Questions is a game where there is a set of possible answers $A$ and a correct answer $c \in A$. There is a player (questioner) who wants to find $c \in A$ and a questionee who knows $c \in A$. The player then asks questions [[Boolean variable|boolean]] questions to questionee who answers True or false about item $c \in A$. 

> [!Note] 20 Questions
> In the traditional version of the game you have until 20 questions to guess the answer, thus the name!

There are different set ups for this game - but the point is to demonstrate the power of how [[Training data]] is collected. 

For simplicity we will call the questionee the teacher and the questioner the learner. 

### Simple: Teacher provides questions

If the goal of the game is too arrive at the answer as quickly as possible but the teacher can provide the questions. This should be solvable in 1 question.

The teacher can provide the question
- "Is the answer $c \in A$?"

### Normal: Binary search

If the learner has to come up with the questions. The best strategy in terms of expectation is to ask questions that divide the remaining potential answers into two even sized chunks. That way no matter the answers you have halved the solution space. This takes $\log_2(\vert A \vert)$ time to find $c$.

This method assumes that any question is valid.

### Restricted questions for the teacher

Lets further formalise this problem. Suppose further you can only ask questions in set $X$. 

