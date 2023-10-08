---
aliases: 
type: exercise
publish: false
created: 2023-09-30
last_edited: 2023-09-30
tags:
  - OMSCS
course: "[[CS6200 Introduction to Graduate Algorithms]]"
week: 7
chatgpt: false
---
# Week 7 - Homework 5 (unassessed) 

From [Algorithms](http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf) by S. Dasgupta, C. Papadimitriou, and U. Vazirani.

> [!question] Problem 7.10 max-flow = min-cut example
> For the following network, with edge capacities as shown, find the maximum flow from $S$ to $T$, along with a matching cut.

![[ex_7_10]]

>[!question] Problem 7.17 Bottleneck edges
>Consider the following network (the numbers are edge capacities).
>(a) Find the maximum flow $f$ and a minimum cut. 
>(b) Draw the residual graph $G^f$ (along with its edge capacities). In this residual network, mark the vertices reachable from $S$ and the vertices from which $T$ is reachable. 
>(c) An edge of a network is called a bottleneck edge if increasing its capacity results in an increase in the maximum flow. List all bottleneck edges in the above network. 
>(d) Give a very simple example (containing at most four nodes) of a network which has no bottleneck edges. 
>(e) Give an efficient algorithm to identify all bottleneck edges in a network. (Hint: Start by running the usual network flow algorithm, and then examine the residual graph.)

![[ex_7_17]]

>[!question] Problem 7.19 verify max-flow
>Suppose someone presents you with a solution to a max-flow problem on some network. Give a linear time algorithm to determine whether the solution does indeed give a maximum flow.
