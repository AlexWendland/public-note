---
aliases: []
type: lecture
publish: false
created: 2023-09-11
last_edited: 2023-09-11
tags:
  - OMSCS
course: "[[CS6200 Introduction to Graduate Algorithms]]"
week: int
chatgpt: false
---
# Week 3 - Homework 2 (unassessed) 

> [!question] From [[Week 3 - Linear-Time Median]]  change 5 in the analysis
> What happens to the run time if we switch out 5 for 3 or 7 in the analysis of this algorithm?

>[!question] Smallest missing natural number
>Design an $O(\log(n))$ algorithm to find the smallest missing natural number in a given sorted array. The given array only has natural numbers. For example, the smallest missing natural number from $A = \{3, 4, 5\}$ is $1$ and from $A = \{1, 3, 4, 6\}$ is $2$.

From [Algorithms](http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf) by S. Dasgupta, C. Papadimitriou, and U. Vazirani.

> [!question] 4.11 Length of the shortest cycle
> Give an algorithm that takes as input a directed graph with positive edge lengths, and returns the length of the shortest cycle in the graph (if the graph is acyclic, it should say so). Your algorithm should take time at most $O(\vert V \vert^3)$.

>[!question] 4.21 Currency exchange
>Shortest path algorithms can be applied in currency trading. Let $c_1, c_2, \ldots , c_n$ be various currencies; for instance, $c_1$ might be dollars, $c_2$ pounds, and $c_3$ lire. For any two currencies $c_i$ and $c_j$ , there is an exchange rate $r_{i,j}$ ; this means that you can purchase $r_{i,j}$ units of currency $c_j$ in exchange for one unit of $c_i$. These exchange rates satisfy the condition that $r_{i,j} \cdot r_{j,i} < 1$, so that if you start with a unit of currency $c_i$, change it into currency $c_j$ and then convert back to currency $c_i$, you end up with less than one unit of currency $c_i$ (the difference is the cost of the transaction). 
>
>(a) Give an efficient algorithm for the following problem: Given a set of exchange rates $r_{i,j}$, and two currencies $s$ and $t$, find the most advantageous sequence of currency exchanges for converting currency $s$ into currency $t$. Toward this goal, you should represent the currencies and rates by a graph whose edge lengths are real numbers. 
>
>The exchange rates are updated frequently, reflecting the demand and supply of the various currencies. Occasionally the exchange rates satisfy the following property: there is a sequence of currencies $c_{i_1} , c_{i_2} , \ldots , c_{i_k}$ such that $r_{i_1,i_2} \cdot r_{i_2,i_3} \ldots r_{i_{k−1},i_k} \cdot r_{i_k,i_1} > 1$. This means that by starting with a unit of currency $c_{i_1}$ and then successively converting it to currencies $c_{i_2} , c_{i_3} , \ldots , c_{i_k}$ , and finally back to $c_{i_1}$ , you would end up with more than one unit of currency $c_{i_1}$. Such anomalies last only a fraction of a minute on the currency exchange, but they provide an opportunity for risk-free profits. 
>
>(b) Give an efficient algorithm for detecting the presence of such an anomaly. Use the graph representation you found above.

>[!question] 2.1 Practice Fast Multiplication
>Use the divide-and-conquer integer multiplication algorithm to multiply the two binary integers 10011011 and 10111010.

> [!question] 2.5 Solving recurrence
> Lots of practice problems.

**Divide and Conquer (Chapter 2)**

2.4, 2.10, 2.12, 2.15, 2.16-2.20

2.22 (you should come up with two solutions: a straightforward Median of medians application and a "merging" approach.)

2.23 (part (a) should follow using a D&C standard, part (b) is more demanding)

2.27-2.28 (if you are curious about further extensions of the Fast Multiplication Algorithm)

2.32 (a very nice application of D&C in a geometric setting, this problem is harder and its runtime analysis is above what we had covered in class so far)