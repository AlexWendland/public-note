---
aliases: 
checked: false
course: "[[CS6200 Introduction to Graduate Algorithms]]"
created: 2024-02-24
last_edited: 2024-02-24
publish: true
tags:
  - OMSCS
type: lecture
week: 7
---
# Week 7 - Randomized Optimization

We are now moving onto to [[Unsupervised learning]].

![[Unsupervised learning]]

The difference from [[Supervised learning|supervised learning]] is we don't get given labels - so how we actually learn the function is beyond me!

## Optimisation problem

![[Optimisation problem]]

There are lots of examples of this.
- Process control or optimisation, think chemical factory.
- Finding a route on a map.
- Find a root of a function!
- Neural network weights.
- Minimising error in another model!

There are a couple of good methods here: 
- Generate and test
	- Good when we have a small input space but complex function.
- Calculus:
	- We need the function to have a derivative and solvable!
- Search method like [[Newton Raphson method]]
	- Similar problems to calculus.
- Random Optimisation, todays lecture :)

## Hill climbing

