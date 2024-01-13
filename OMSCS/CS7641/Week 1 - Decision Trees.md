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

## Boolean decision trees

Suppose our domain consists of $A_i = \{T, F\}$ [[Boolean variable|Boolean's]], either true or false as well as our [[Function codomain|codomain]] $B = \{T, F\}$. Then our function $f^{\ast}$ represented by the [[Decision tree|decision trees]] is a [[Boolean function|boolean function]].

![[boolean decision trees.excalidraw]]


These can expand to many variables, and for different functions can grow with different rates.

- [[Logical or]] and [[Logical and]] with $n$ variables uses $O(n)$ nodes.
- Even/odd parity (true if an even/odd number of inputs are True) with $n$ variables uses $O(2^n)$ nodes. 

# ID3

![[Iterative Dichotomiser 3 (ID3)#Iterative Dichotomiser 3 (ID3)]]

# Bias

![[Inductive bias]]

![[Preference bias]]

![[Restriction bias]]

In [[Iterative Dichotomiser 3 (ID3)|ID3]] the [[Restriction bias|restriction bias]] comes from the fact that the have a [[Decision tree|decision tree]] based on a set of attributes. 

For example, if you let the attributes $T = Func(A,B)$ then the [[Decision tree|decision tree]] can represent any function in $Func(A,B)$ trivially. Though this might be computationally completely infeasible in most cases!

Whereas the [[Preference bias|preference bias]] comes from the [[Iterative Dichotomiser 3 (ID3)|ID3]] algorithm itself:
- good splits near the root of the tree,
- ones that lower the entropy more, and
- shorter trees.

# Other considerations

## Continuous variables

Suppose we have some continuous attribute in $A$. Whilst we could have a branch for every value that attribute could take, it is most probably best to categorify the value by their picking Boolean decisions like is it $\geq a$ or $< a$ for $a \in A$ or splitting the value into ranges.

## Pruning

![[Overfitting]]

The model can have [[Overfitting|overfitting]] if the tree gets too large. Therefore it is good practice to contract (or prune) branches of the tree if they have marginal effect on the outcome of the [[Decision tree|decision tree]].

## [[Regression problems]]

It is possible to tackle this with a [[Decision tree|decision tree]] if you only care about approximate answer. However, you will have to change the definition of [[Information entropy|information entropy]] to work in the continuous space. This will have to use something like an average of the leaf nodes.