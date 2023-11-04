---
aliases: 
type: exercise
publish: false
created: 2023-10-27
last_edited: 2023-10-27
tags:
  - OMSCS
course: "[[CS6200 Introduction to Graduate Algorithms]]"
week: 11
chatgpt: false
---
# Week 11 - Homework 7 (assessed)

>[!question] Question (a)
>Some problems are formulated very closely to well known [[NP-hard]] problems, but they turn out to be in [[Polynomial time|P]]. Here is an example.
>
>**AllorNothing3SAT** takes as input a boolean formula in [[Conjunctive normal form (CNF)|CNF]] such that all clauses have three literals, and returns an assignment of the variables such that each clause has all TRUE literals or all FALSE literals, if such assignment exists. Design an efficient algorithm to solve **AllorNothing3SAT**.



>[!question] Question (b)
>Now consider a new variant of 3-SAT, we will call the **3-at most-3-SAT**:
>
>**Input**: A boolean formula in [[Conjunctive normal form (CNF)|CNF]] such that all clauses have at most three literals, and every variable appears in at most three clauses.
>
>**Output**: An assignment of the variables such that the boolean formula returns True, or report NO if such assignment does not exist.
>
>Prove that the **3-at most-3-SAT** problem is NP-complete.

