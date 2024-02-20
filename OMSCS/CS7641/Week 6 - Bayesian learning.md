---
aliases: 
checked: false
course: "[[CS6200 Introduction to Graduate Algorithms]]"
created: 2024-02-19
last_edited: 2024-02-19
publish: true
tags:
  - OMSCS
type: lecture
week: 6
---
# Week 6 - Bayesian learning

## Bayes rule

To start this lecture lets remind ourselves of the definition of [[Conditional probability|conditional probability]].

![[Conditional probability]]

As a simple corollary we get [[Bayes rule]].

![[Bayes rule]]

## Applying this to learning

Suppose $h \in H$ is a hypothesis belonging to our [[Modelling paradigm|hypothesis space]] and we have $D$ data. Then to see the probability our hypothesis is given the data $\mathbb{P}[h \vert D]$ we can use [[Bayes rule]] to reduce it to things we can calculate
$$
\mathbb{P}[h \vert D] = \frac{\mathbb{P}[D \vert h]\mathbb{P}[h]}{\mathbb{P}[D]}.
$$
- Here $\mathbb{P}[D \vert h]$ is the accuracy of our prediction. 
- Then $\mathbb{P}[h]$ is a reflection of prior knowledge about which hypothesis are likely or not. 
- Lastly $\mathbb{P}[D]$ reflects our prior knowledge about the data we are sampling from.

