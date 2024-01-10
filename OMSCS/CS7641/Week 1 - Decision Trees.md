---
aliases: 
checked: false
course: "[[CS6200 Introduction to Graduate Algorithms]]"
created: 2024-01-10
last_edited: 2024-01-10
publish: true
tags:
  - OMSCS
type: lecture
week: 1
---
# Week 1 - Decision Trees

# Supervised learning

[[Supervised learning]] falls into two main problems sets

[[Classification problems]] - Mapping from a domain to some discrete set, and
[[Regression problems]] - mapping from a domain to some continuous space like the [[Real numbers]] ($\mathbb{R}$).

For example, making a decision on whether you should give someone a loan is a classification problem as there are only two outcomes - whereas mapping from someone's picture to their age would be a regression problem. 

# Classification

First lets start by defining terms used in this course.

- Instance - an input,
- Concept - the function from inputs to outputs,
	- for example a car is simply a mapping from things in the world to True or False based on if that is a car or not.
- Target concept - the ideal answer or optimal concept.
- Hypothesis class - This is the set of all concepts we want to consider
	- This might be smaller than the set of all concepts.
- Sample / Training set - A set of labelled data i.e. a pair (input, output)
- Candidate - the current concept under investigation.
- Testing set - A set of labelled data that will be used to evaluate your candidate
	- It is important it is distinct from the training set.

## My mathematical interpretation

Suppose we have two sets $A$ and $B$ and we are looking to find some function optimal function $f^{\ast}: A \rightarrow B$. 

- Instance - some element $a \in A$.
- Concept - a [[Function|function]] $f: A \rightarrow B$.
- Target concept - the function $f^{\ast}$.
- Hypothesis class - a restricted class $C \subset Func(A,B)$ that we will consider.
	- This restriction may be applied due to the set of algorithms you are considering.
- Sample / Training set - A set $T \subset A \times B$ of observations. 
	- Ideally $T \subset \{(a,f^{\ast}(a)) \vert a \in A\}$ however this might not be possible.
- Candidate - a function $f': A \rightarrow B$ which is our current guess at $f^{\ast}$. 
- Testing set - A set $E \subset A \times B$ similar to training set but with intent to test the current candidate on.

# Decision trees

Suppose your domain $A$ actually breaks down into many different aspects $A = \oplus_{i=1}^k A_i$. Like if you were making a decision about whether to go into the restaurant your aspects could be the type of restaurant, whether it is raining, and how full the restaurant is.

Then a [[Decision tree]] is a [[Rooted tree|rooted tree]] where
- Each parent node is affiliated with an aspect with each child branch being affiliated with a collection of potential values. We make sure all potential values of that aspect are covered by the branches.  
- Each child node is associated to a value in the [[Function codomain|codomain]] $B$.

An example for the problem of restaurant choosing is below.

![[decision tree example.excalidraw]]

## Learning with Decision trees


