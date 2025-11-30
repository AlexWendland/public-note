---
aliases: 
checked: false
course: "[[CS6215 Introduction to Graduate Algorithms]]"
created: 2023-10-24
last_edited: 2023-11-11
draft: false
tags:
  - OMSCS
type: lecture
week: 10
---
# Week 10 - NP overview

## Complexity classes

![[Nondeterministic Polynomial time (NP)]]

In this class we use the [[Search problems|search problem]] definition.

![[Search problems]]

Note here we have.

![[Polynomial time is a subset of NP-complete#Statement]]

There is an open problem.

![[P equals NP or P not equals NP#P equals NP or P not equals NP]]

## Satisfiability

![[Satisfiability problem (SAT problem)#Statement|SAT problem]]

![[The Satisfiability problem is in NP]]

## k-colourings problem

![[k-colourings problem (graphs)#Statement]]

![[The k-colourings problem is in NP]]

## [[Minimum Spanning Tree problem (MST)|MST]]

![[Minimum Spanning Tree problem (MST)#Statement|MST]]

![[Minimum Spanning Tree problem is in NP]]

This proof was relatively easy as [[Minimum Spanning Tree problem (MST)|MST]] is a [[Polynomial time|polynomial time]] problem. This is shown by what is above and [[Kruskal's algorithm]].

## Knapsack problem

![[Knapsack problem (without repetition)#Statement]]

Whilst the [[Knapsack problem (without repetition)|Knapsack problem]] is of the correct form to be a [[Search problems|search problem]] we can't currently check if a solution is correct in polynomial time. Therefore the [[Knapsack problem (without repetition)|Knapsack problem]] isn't known to be in [[Nondeterministic Polynomial time (NP)|NP]].

Similarly we say that the [[Knapsack problem (without repetition)|Knapsack problem]] isn't known to be in [[Polynomial time|polynomial time]] either.

We say it isn't known to be as there might be a super clever algorithm that happens to solve the [[Knapsack problem (without repetition)|Knapsack problem]] in polynomial time.

However, there is a variant of the problem that is in [[Nondeterministic Polynomial time (NP)|NP]].

![[Knapsack-search (without replacement)#Statement]]

Here instead of having to check if a solution is maximal we can instead just check if it has enough value.

![[Knapsack-search is NP]]

## [[Polynomial time]] and [[Nondeterministic Polynomial time (NP)|Nondeterministic Polynomial time]]

Note that [[Nondeterministic Polynomial time (NP)|NP]] isn't Not [[Polynomial time]]. In fact we have the following result.

![[Polynomial time is a subset of NP-complete]]

![P Vs Np](../../../images/P_vs_NP.png)

The question is, are there problems that are in [[Nondeterministic Polynomial time (NP)|NP]] but are not in [[Polynomial time|P]]?

## NP-complete

If [[P equals NP or P not equals NP|P not equal to NP]] then we would have a problem in [[Nondeterministic Polynomial time (NP)|NP]] that didn't lie in [[Polynomial time|P]]. Therefore the green region above would be non-empty.

![P Not Equal To Np](../../../images/P_not_equal_to_NP.png)

Therefore lets look at the hardest problems in [[Nondeterministic Polynomial time (NP)|NP]].

![[NP-hard]]

We define a [[Many-one reduction (problem)|many-one reduction]] as bellow.

![[Many-one reduction (problem)|Many-one reduction]]

However, we want to look at the hardest problems in [[Nondeterministic Polynomial time (NP)|NP]].

![[NP-Complete]]

A classic [[NP-Complete]] problem is the [[Satisfiability problem (SAT problem)|SAT problem]].

## Reductions functionally

To show a [[Many-one reduction (problem)|many-one reduction]] from $A$ to $B$ you need to construct $f$ a way to transform an instance of problem $A$ into some input to the problem $B$. This needs to be done in polynomial time. Then the solution from solving $f(I)$ in problem $B$ should relate back to the solution of problem $A$. Either you should construct $h$ a way to transform the solution from problem $B$ into a solution to problem $A$ or forward on the fact that no solution can exist.

![reduction](../../../images/excalidraw/reduction.excalidraw.svg)

Therefore to show $A$ reduces to $B$ we need:
- **Define $f$:** Show how an instance of problem $A$ can be converted into an instance of problem $B$ in polynomial time.
- **Define $h$:** Show how a solution to the problem $B$ can be converted into a solution to problem $A$ in polynomial time.
- **Proof**: Show that a solution for $B$ exists if and only if a solution to $A$ exists.

## Showing [[NP-Complete]]

To show a problem $A$ is [[NP-Complete]] need to show
- $A$ is in [[Nondeterministic Polynomial time (NP)|NP]], and
- $A$ is [[NP-hard]].

Generically showing $A$ is [[NP-hard]], is ironically quite hard. However we get around this by having some [[NP-Complete|NP-complete]] problems already, such as the [[Satisfiability problem (SAT problem)|SAT problem]]. Then to show $A$ is [[NP-hard]] we just need to show another [[NP-Complete]] problem reduces to it. So functionally we show:

- $A$ is [[Nondeterministic Polynomial time (NP)|NP]], and
- there is some [[NP-complete]] problem $B$ that reduces to $A$.

## Practice problems

From [Algorithms](http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf) by S. Dasgupta, C. Papadimitriou, and U. Vazirani.

>[!question] 8.1 Optimisation vs Search problems

>[!question] 8.2 Search problems vs Decision problems

