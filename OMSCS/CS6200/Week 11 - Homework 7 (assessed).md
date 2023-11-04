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

## Algorithm

Suppose we have a [[Conjunctive normal form (CNF)|CNF]] $f$ with $n$ variables $x_i$ for $1 \leq i \leq n$ and $m$ clauses $c_i = l_i^1 \lor l_i^2 \lor l_i^3$ for $1 \leq i \leq m$. 

1. Initialise a union-find data structure on the set $V = \{x_i, \overline{x_i} \vert 1 \leq i \leq n\}$.
2. For each $c_i$ run $union(l_i^a, l_i^b)$ and $union(\overline{l_i^a}, \overline{l_i^b})$ for $a,b \in \{1,2,3\}$ with $a < b$.
3. For each $x_i$ if $find(x_i) = find(\overline{x_i})$ say there is no such solution.
4. Go through the list of disjoint sets, if the set $S$ hasn't been assignment a value - assign it true and assign $\overline{S} = \{\overline{s} \vert s \in S\}$ false.
5. For each set $S$ assigned True if $x_i \in S$ assign $x_i$ true, if $\overline{x_i} \in S$ assign $x_i$ false. Then output this assignment.

>[!note] Step 4 is possible
>From [[Week 11 - Homework 7 (assessed)#Claim 1|Claim 1]] below for each set $S$ in the disjoint union, we have $\overline{S}$ in it as well.

## Correctness

We need to show it is correct in 2 cases. If is says it is not possible or if it provides an assignment.

Suppose we say the assignment is not possible. 

Then there is an $x_i$ such that there are a set of clauses (or a clauses negation) such that $x_i$ and $\overline{x_i}$ need to share the same assignment for us to have each clause having all literals be True or False. 

As $x_i$ and $\overline{x_i}$ have opposite assignments this is not possible. Therefore no assignment to the variables will guarantee all clauses literals are either positive or negative.

Suppose we return an assignment.

As the set $V$ contained all $x_i$ and $\overline{x_i}$  for $1 \leq i \leq n$ and the set contain $x_i$ was assigned true or the set containing $\overline{x_i}$ was assigned true, the assignment returned was an assignment to all $n$ variables.

Step 4 guarantees that for each clause $c_i$ all the literals are contained in the same set. Therefore the assignment generated in step $5$ means all literals in clause $c_i$ are true or false. 

So the returned assignment is a valid AllorNothing3SAT assignment to $f$.

Therefore the algorithm correctly solves the AllorNothing3SAT problem.

### Claim 1

>[!important] Claim 1
>If $S$ is a set in the disjoint union then so is $\overline{S} = \{\overline{s} \vert s \in S\}$.

### Proof of claim 1

For each $union(s_1, s_2)$ ran in step 2 for $s_1, s_2 \in S$ we ran $union(\overline{s_1}, \overline{s_2})$. Therefore there is a set $T$ in the disjoint union such that $\overline{S} \subset T$.

For each $union(\overline{s}, t)$ ran in step 2 for $s \in S$ and $t \in T$ we ran $union(s, \overline{t})$ therefore by definition $\overline{t} \in S$ and $t \in \overline{S}$. So $T = \overline{S}$.

## Run time

The run time is ... so it runs in [[Polynomial time|polynomial time]] - this is proved below.

Step 1 takes $O(n)$ to initialise the data structure.

In step 2 for each clause we do 6 union operations each taking $O(\log(2n))$ time. Therefore this step takes $O(m \log(n))$.

Step 3 runs 2n find operations each taking $O(log(2n))$ time. So this step takes $O(n \log(n))$.

In Step 4 there are at most $2n$ sets and we need to run through them all so this takes $O(n)$.

In Step 

>[!question] Question (b)
>Now consider a new variant of 3-SAT, we will call the **3-at most-3-SAT**:
>
>**Input**: A boolean formula in [[Conjunctive normal form (CNF)|CNF]] such that all clauses have at most three literals, and every variable appears in at most three clauses.
>
>**Output**: An assignment of the variables such that the boolean formula returns True, or report NO if such assignment does not exist.
>
>Prove that the **3-at most-3-SAT** problem is NP-complete.

