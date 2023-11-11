---
aliases: null
chatgpt: false
course: '[[CS6200 Introduction to Graduate Algorithms]]'
created: 2023-10-27
last_edited: 2023-10-27
publish: false
tags:
  - OMSCS
type: exercise
week: 11
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

The run time is $O((n + m)\log(n))$ so it runs in [[Polynomial time|polynomial time]] - this is proved below.

Step 1 takes $O(n)$ to initialise the data structure.

In step 2 for each clause we do 6 union operations each taking $O(\log(2n))$ time. Therefore this step takes $O(m \log(n))$.

Step 3 runs 2n find operations each taking $O(log(2n))$ time. So this step takes $O(n \log(n))$.

In Step 4 there are at most $2n$ sets and we need to run through them all so this takes $O(n)$.

In Step 5 involves assigning a value to each of the $n$ variables which takes $O(n)$ time.

All in all this takes
$$3O(n) + O(m\log(n)) + O(n \log(n)) = O((n + m)\log(n)).$$

>[!question] Question (b)
>Now consider a new variant of 3-SAT, we will call the **3-at most-3-SAT**:
>
>**Input**: A boolean formula in [[Conjunctive normal form (CNF)|CNF]] such that all clauses have at most three literals, and every variable appears in at most three clauses.
>
>**Output**: An assignment of the variables such that the boolean formula returns True, or report NO if such assignment does not exist.
>
>Prove that the **3-at most-3-SAT** problem is NP-complete.

To prove 3-at most-3-SAT is [[NP-Complete|NP-complete]] I will show 2 things.

1. Demonstrate that 3-at most-3-SAT is in the class of [[Nondeterministic Polynomial time (NP)|NP]] problems.
2. Then demonstrate that the 3-at most-3-SAT problem is at least as hard as the 3-SAT - which is known to be [[NP-Complete]]. The specific steps are as follows:
	1. Show how an instance of the [[k-satisfiability problem (k-SAT problem)|3-SAT]] problem is converted to an instance of the  3-at most-3-SAT problem, in polynomial time.
	2. Show how a solution the 3-at most-3-SAT can be converted to a solution for the [[k-satisfiability problem (k-SAT problem)|3-SAT]] problem, again in polynomial time.
	3. Show that a solution for the [[k-satisfiability problem (k-SAT problem)|3-SAT]] exists if and only if a solution to the 3-at most-3-SAT exists.

## 3-at most-3-SAT is [[Nondeterministic Polynomial time (NP)|NP]]

Note that 3-at most-3-SAT is in the correct form to be a [[Search problems|search problem]], we either return an correct solution or we say that no such solution exists.

Suppose we have $f$ a [[Conjunctive normal form (CNF)|CNF]] that is an instance 3-at most-3-SAT problem with $n$ variables and $m$ ($\leq 3n$) literals and an assignment $a$ to the $n$ variables.

To check the solution we go through each clause and check one of the 3 literals is true - if any are not we say this solution is not valid otherwise if all clauses are passed we say the solution is valid. This takes at most $m \leq 3n$ steps checking $3$ values in each step. Therefore takes $O(m) = O(n)$.

As this is in the form of a [[Search problems|search problem]] and verifying a solution takes [[Polynomial time|polynomial time]], we have that 3-at most-3-SAT is in [[Nondeterministic Polynomial time (NP)|NP]].

## Reduction of 3-SAT to 3-at most-3-SAT

Suppose we have $f$ a [[Conjunctive normal form (CNF)|CNF]] that is an instance of the [[k-satisfiability problem (k-SAT problem)|3-SAT]] problem. Therefore each clause of $f$ has at-most 3 literals in.

### Transformation from 3-SAT to 3-at most-3-SAT

To reduce $f$ to an instance of 3-at most-3-SAT $f'$, first set $f' = f$ then do the following for each variable $x_i$ with $1 \leq i \leq n$:
- Suppose there are $k_i$ literals $x_i$ or $\overline{x_i}$ in $f'$.
- Make $k_i$ new variables $x_i^j$ with $1 \leq j \leq k_i$.
- Replace every literal $x_i$ or $\overline{x_i}$ in $f'$ with a distinct $x^j_i$ or $\overline{x^j_i}$ respectively. So each $x_i^j$ is used exactly once and no $x_i$ or $\overline{x_i}$ literals exist in $f'$.
- If $k_i \geq 1$ then append to $f'$
$$f_i := (x_i^{k_i} \lor \overline{x_i^1}) \land \bigwedge_{j = 1}^{k_i-1} (x_i^j \lor \overline{x_i^{j+1}}).$$
Therefore $f'$ is now a [[Conjunctive normal form (CNF)|CNF]] with $n' := \sum_{i=1}^n k_i$ variables $x^j_i$ with $1 \leq i \leq n$ and $1 \leq j \leq k_i$ and at most $m + n'$ clauses.

Every variable $x_i^j$ appears in at most 3 literals of $f'$, once where it is replaced in the original formula then twice in $f_i$ (if $f_i$ is appended).

As $f$ has clauses of at-most 3 literals and the $f_i$ has only clauses of size 2. All the clauses of $f'$ have size at-most 3.

Combined this gives that $f'$ is a valid 3-at most-3-SAT formula, so we can solve it using a valid algorithm for the 3-at most-3-SAT problem.

The transformation of $f$ to $f'$ involves going through the variables one by one, then replacing up to $nm$ instances of that variable and appending a formula of length up to $nm$. Therefore it takes us $O(n^2m)$ and so is in [[Polynomial time|polynomial time]] in the size of the input.

### Transformation of the solution to 3-at most-3-SAT to a solution to 3-SAT

If there is no valid assignment to $f'$ say there is none to $f$.

If there is a valid assignment to $f'$, make assignment for $f$ by setting $x_i = x_i^1$ and return that.

This involves assigning each variable that takes $O(n)$, so this transformation can be done in [[Polynomial time|polynomial time]] in the size of the input $f$.

### Correctness of the reduction

Suppose there is a valid assignment for $f'$.

Then we have made assignment $x_i = x_i^1$ for $f$.

From [[Week 11 - Homework 7 (assessed)#Claim 2|Claim 2]] we know for any $1 \leq i \leq n$ that all $x^i_j$ have the same value - so they all have the same assignment as $x_i$.

As $f$ is a subset of $f'$ with each $x_i$ replaced with $x_i^j$ for some $1 \leq j \leq k_i$ but each of the $x_i^j$ have the same assignment as $x_i$ and $f'$ has a valid assignment then $f$ with this assignment is valid.

Suppose $f$ has some valid assignment.

Then create assignment for $f'$ by setting $x_i^j = x_i$.

As this assignment is valid for $f$ it is valid for the component of $f'$ that comes from $f$.

For any $i$ we have $x_i^j$ have the same assignment, so by [[Week 11 - Homework 7 (assessed)#Claim 3|Claim 3]] this is a valid assignment for $f_i$.

Therefore every component of $f'$ has a valid assignment, giving this assignment is valid for $f'$.

Therefore this reduction is valid and 3-at most-3-SAT [[NP-Complete|NP-complete]] as it is in [[Nondeterministic Polynomial time (NP)|NP]] and [[k-satisfiability problem (k-SAT problem)|3-SAT]] is [[NP-Complete|NP-complete]].

### Claim 2

>[!important] Claim 2
>In a valid assignment for $f'$ for all $1 \leq i \leq n$ we have that $x_i^j$ have the same value for $1 \leq j \leq k_i$.

### Proof of Claim 2

Let $1 \leq i \leq n$.

If $k_i = 1$ then there is only one variable $x_i^1$ and so the claim holds.

If $k_i \geq 2$ then we have appended $f_i$ to $f'$ and so this assignment is valid for $f_i$ also. By [[Week 11 - Homework 7 (assessed)#Claim 3|Claim 3]] all $x_i^j$ have the same value and so the claim holds.

### Claim 3

>[!important] Claim 3
>$f_i$ has a valid assignment if and only if all $x_i^j$ have the same value.

### Proof of Claim 3

We only define $f_i$ if $k_i \geq 2$ so suppose this.

Suppose we have a valid assignment for $f_i$.

For $1 \leq j \leq k_i$,
- as we have clause $(x_i^{j-1} \lor \overline{x_i^j})$ if $x_i^j$ is True then $x^{j-1}_i$ has to be True, and
- as we have clause $(x_i^{j} \lor \overline{x_i^{j+1}})$ if $x_i^j$ is False then $x^{j+1}_i$ has to be False.
(Where $x_i^0 := x_i^{k_i}$ and $x_i^{k_i + 1} := x_i^1$.)

If $x^1_i$ is True then $x_i^{k_i}, x_i^{k_i-1}, \ldots, x^2_i$ must all be True.

If $x^1_i$ is False then $x_i^2, x_i^3, \ldots, x_i^{k_i}$ must all be False.

Therefore all $x_i^j = x_i^1$ and all $x_i^j$ have the same value.

Suppose all $x^j_i$ have the same value.

If they are all true, as every clause of $f_i$ contains an $x_i^j$ this is a valid assignment for $f_i$.

If they are all false, as every clause of $f_i$ contains an $\overline{x^j_i}$ this is a valid assignment for $f_i$.
