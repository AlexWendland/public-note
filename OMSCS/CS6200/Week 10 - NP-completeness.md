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
# Week 10 - NP-completeness

We are going to assume the following.

![[SAT is NP-complete#Statement]]

## k-SAT

We are going to show that the [[k-satisfiability problem (k-SAT problem)|k-SAT]] problem is [[NP-Complete]] for $k \geq 3$.

![[k-satisfiability problem (k-SAT problem)#Statement|k-SAT]]

To do this we will show [[k-satisfiability problem (k-SAT problem)|3-SAT]] is [[NP-Complete|NP-complete]] which as [[k-satisfiability problem (k-SAT problem)|3-SAT]] is a subproblem to [[k-satisfiability problem (k-SAT problem)|k-SAT]] for $k \geq 3$ this will prove all we need to.

We need to do the following to show this:
- Show that [[k-satisfiability problem (k-SAT problem)|3-SAT]] is [[Nondeterministic Polynomial time (NP)|NP]]
- Show there is a reduction from the [[Satisfiability problem (SAT problem)|SAT problem]] to [[k-satisfiability problem (k-SAT problem)|3-SAT]].

## [[k-satisfiability problem (k-SAT problem)|k-SAT]] is in [[Nondeterministic Polynomial time (NP)|NP]]

![[k-SAT is in NP]]

## [[k-satisfiability problem (k-SAT problem)|3-SAT]] is [[NP-Complete]]

![[3-SAT is NP-complete]]

