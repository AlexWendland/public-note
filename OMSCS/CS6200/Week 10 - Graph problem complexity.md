---
aliases: null
checked: false
course: '[[CS6200 Introduction to Graduate Algorithms]]'
created: 2023-11-03
last_edited: 2023-11-03
publish: true
tags:
  - OMSCS
type: lecture
week: 10
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

![[Max clique problem (graph)#Statement]]

![[Clique of a given size problem#Statement]]

Similarly to before the first problem is not know to be in [[Nondeterministic Polynomial time (NP)|NP]] however the second is.

![[Clique of a given size problem is in NP]]

Notice that really [[Clique (graph)|clique]] problems and [[Independent set (graph)|independent set]] problems are dual to one another. Through the concept of the [[Complement graph|complement graph]].

![[Complement graph]]

This is formalised through the following lemma.

![[Cliques in G are independent sets in the complement]]

So we can easily show [[Clique of a given size problem]] is [[NP-Complete|NP-complete]] by finding a [[Many-one reduction (problem)|many-one reduction]] of [[Independent set of a given size]].

![[Clique of a given size problem is NP-complete]]

We get a similar result for the max problem.

![[Max clique problem is NP-hard]]

## Vertex cover problem

First we define a new concept.

![[Vertex cover]]

Then similarly to before we get two logical problems.

![[Minimum vertex cover problem#Statement]]

![[Vertex cover of a given size#Statement]]

Like before the minimum problem is not known to be in [[Nondeterministic Polynomial time (NP)|NP]], however the second is.

![[Vertex cover of a given size is NP]]

The [[Vertex cover|vertex cover]] is closely related to the [[Independent set (graph)|independent set]].

![[Vertex cover if and only if the complement is an independent set]]

So we can prove [[Vertex cover of a given size]] is [[NP-Complete|NP-complete]] by finding a [[Many-one reduction (problem)|many-one reduction]] of [[Independent set of a given size]] to it.

![[Vertex cover of a given size is NP-complete]]

From this we get the [[Minimum vertex cover problem]] is [[NP-hard]].

![[Minimum vertex cover problem is NP-hard]]

## Practice problems

From [Algorithms](http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf) by S. Dasgupta, C. Papadimitriou, and U. Vazirani.

>[!question] 8.4 NP-completeness error

>[!question] 8.10 Proof by generalisation

>[!question] 8.14 Clique + Independent set (HW 6 assessed)

>[!question] 8.19 Kite

