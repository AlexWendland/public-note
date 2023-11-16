---
aliases: null
checked: false
created: 2023-11-03
last_edited: 2023-11-11
publish: true
tags:
  - maths
type: lemma
---
# Statement

> [!important] Lemma
> [[Independent set of a given size]] is [[NP-Complete|NP-complete]].

# Proof

As [[Independent set of a given size is in NP]] all we need to show is that [[Independent set of a given size]] is [[NP-hard]].

To show this we are going to find a [[Many-one reduction (problem)|many-one reduction]] of the [[k-satisfiability problem (k-SAT problem)|3-SAT]] problem to [[Independent set of a given size]] problem. (We know [[3-SAT is NP-complete]] so this gives us that [[Independent set of a given size]] is also [[NP-Complete|NP-complete]].) This will involve:

- Taking an instance of the [[k-satisfiability problem (k-SAT problem)|3-SAT]] problem and converting it to a [[Independent set of a given size]] problem in [[Polynomial time|polynomial time]],
- Showing how to transform a solution to the [[Independent set of a given size]] problem back to a solution to the [[k-satisfiability problem (k-SAT problem)|3-SAT]] problem in [[Polynomial time|polynomial time]], and
- Showing that a solution exists to the [[k-satisfiability problem (k-SAT problem)|3-SAT]] problem if and only if a solution exists to the [[Independent set of a given size]] problem.

Suppose we are given a [[k-satisfiability problem (k-SAT problem)|3-SAT]] problem $f$ with variables $x_1, \ldots, x_n$ and clauses $c_1, \ldots, c_m$.
We know each clause $c_i$ has at most 3 literals $l_i^1$, $l_i^2$, and $l_i^3$ (maybe less). Set
$$L = \{l_i^j \vert 1 \leq i \leq m, \ 1 \leq j \leq 3\}$$ be the set of literals in the clauses $c_i$. We are going to construct a graph where each clauses is a [[Clique (graph)|clique]] and we connect any literals to their inverses. So we will two sets of edges, clause edges
$$C_E = \{(l_i^j, l_i^{j'}) \ \vert \ l_i^j, l_i^{j'} \in L, \ j \not = j'\}$$
and negation edges
$$N_E = \{(l_i^j, l_a^b) \ \vert \ l_i^j, l_a^b \in L, \ \overline{l_i^j} = l_a^b \}.$$
Then an independent set of size $m$ will indicate a set of literals to set to true to get a correct assignment. Define the [[Graph|undirected graph]]
$$G = (L, C_E \cup N_E).$$
We now apply the solution of [[Independent set of a given size]] to $G$ and $g = m$.

To make $G$ we need to scan through each clause and make at most 3 vertices, this is $O(m)$. Then to connect the edges we need to first add the $C_E$ which takes $O(m)$ again. To find all the negation edges for each variable we need to find all the literals using that, this takes $O(nm)$. Therefore this process takes $O(nm)$ and is [[Polynomial time|polynomial time]] in the size of the input.

When we have a solution to the [[Independent set of a given size]] problem we all the literals in the independent set to true. (This is valid as we know no 2 literals in this independent set can be the negation of one another from the negation edges.) Then for any left over variables we just set them to be true.

This process takes $O(n)$ time as we have to check if a variable is in the set of returned literals.

Suppose $f$ the [[k-satisfiability problem (k-SAT problem)|3-SAT]] problem has an assignment $a$ that solves it.

For each clause at least one literal must be correct, define this set $S = \{l_i^{j_i}\ \vert \ 1 \leq i \leq m, \ 1 \leq j_i \leq 3, \ a(l_i^{j_i}) = \mbox{ True} \}$.

The set $S$ forms the independent set in $G$ of size $m$. As $a$ is a valid assignment for $l, l' \in S$ we have $\overline{l} \not = l'$. By definition each literal in $S$ belongs to a different clause.

Suppose we have an independent set $S$ in $G$ of size $m$.

As this is an [[Independent set (graph)|independent set]] the negation edges $N_E$ guarantee for $l, l' \in S$  we have $\overline{l} \not = l'$. Therefore we can define a partial assignment $a$ of the original $n$ variables where $a(l) =$ True for $l \in S$. This can be extended to a full assignment $a$ of the original $n$ variables where if $x$ is not assigned we just set $a(x) =$ True.

As each clause is a [[Clique (graph)|clique]] in $G$ from the clause edges $C_E$ every element of $S$ belongs to a different clause. As it is of size $m$ each clause has an element in $S$. So $S = \{l_i^{j_i}\ \vert \ 1 \leq i \leq m, \ 1 \leq j_i \leq 3 \}$.

As we have at least one literal in each clause being true, the assignment $a$ satisfies the original [[Conjunctive normal form (CNF)|CNF]] $f$. Therefore $f$ is satisfiable.

This gives the reduction of [[k-satisfiability problem (k-SAT problem)|3-SAT]] to the [[Independent set of a given size]] problem and makes it [[NP-Complete|NP-complete]].

