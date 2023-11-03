---
aliases: 
type: lecture
publish: true
created: 2023-11-03
last_edited: 2023-11-03
tags:
  - OMSCS
course: "[[CS6200 Introduction to Graduate Algorithms]]"
week: 10
chatgpt: false
---
# Week 10 - Graph problem complexity

## Independent set problem

![[Independent set (graph)|independent set]]

Therefore we have the following problem.
![[Max independent set problem (graph)#Statement]]

Though this problem is not known to be in [[Nondeterministic Polynomial time (NP)|NP]] as to verify if a set is the largest set we would require to calculate the set of largest size. However, we can edit this question to make one that is in [[Nondeterministic Polynomial time (NP)|NP]].
![[Independent set of a given size#Statement]]

## Independent set of a given size is [[NP-Complete]]

![[Independent set of a given size is in NP]]

More over we have it is [[NP-Complete]].

![[Independent set of a given size is NP-complete]]

## Max independent set is [[NP-hard]]

![[Max independent set problem is NP-hard]]

## Clique problem

![[Clique (graph)]]

So similarly with the [[Max independent set problem (graph)|Independent set problem]] we can define two problems.

![[Max clique size problem (graph)#Statement]]

![[Clique of a given size problem#Statement]]

Similarly to before the first problem is not know to be in [[Nondeterministic Polynomial time (NP)|NP]] however the second is.

![[Clique of a given size problem is in NP]]

Notice that really [[Clique (graph)|clique]] problems and [[Independent set (graph)|independent set]] problems are dual to one another. Through the concept of the [[Complement graph|complement graph]].

![[Complement graph]]

This is formalised through the following lemma.

![[Cliques in G are independent sets in the complement]]


