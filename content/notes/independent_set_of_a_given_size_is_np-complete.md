---
aliases:
created: 2023-11-03
date_checked:
draft: false
last_edited: 2025-12-05
tags:
  - maths
title: Independent set of a given size is NP-complete
type: lemma
---
# Statement

> [!lemma] Lemma
> [Independent set of a given size](independent_set_of_a_given_size.md) is [NP-complete](np-complete.md).

# Proof

As [Independent set of a given size is in NP](independent_set_of_a_given_size_is_in_np.md) all we need to show is that [Independent set of a given size](independent_set_of_a_given_size.md) is [NP-hard](np-hard.md).

To show this we are going to find a [many-one reduction](many-one_reduction_(problem).md) of the [3-SAT](k-satisfiability_problem_(k-sat_problem).md) problem to [Independent set of a given size](independent_set_of_a_given_size.md) problem. (We know [3-SAT is NP-complete](3-sat_is_np-complete.md) so this gives us that [Independent set of a given size](independent_set_of_a_given_size.md) is also [NP-complete](np-complete.md).) This will involve:

- Taking an instance of the [3-SAT](k-satisfiability_problem_(k-sat_problem).md) problem and converting it to a [Independent set of a given size](independent_set_of_a_given_size.md) problem in [polynomial time](polynomial_time.md),
- Showing how to transform a solution to the [Independent set of a given size](independent_set_of_a_given_size.md) problem back to a solution to the [3-SAT](k-satisfiability_problem_(k-sat_problem).md) problem in [polynomial time](polynomial_time.md), and
- Showing that a solution exists to the [3-SAT](k-satisfiability_problem_(k-sat_problem).md) problem if and only if a solution exists to the [Independent set of a given size](independent_set_of_a_given_size.md) problem.

Suppose we are given a [3-SAT](k-satisfiability_problem_(k-sat_problem).md) problem $f$ with variables $x_1, \ldots, x_n$ and clauses $c_1, \ldots, c_m$.
We know each clause $c_i$ has at most 3 literals $l_i^1$, $l_i^2$, and $l_i^3$ (maybe less). Set
$$L = \{l_i^j \vert 1 \leq i \leq m, \ 1 \leq j \leq 3\}$$ be the set of literals in the clauses $c_i$. We are going to construct a graph where each clauses is a [clique](clique_(graph).md) and we connect any literals to their inverses. So we will two sets of edges, clause edges
$$C_E = \{(l_i^j, l_i^{j'}) \ \vert \ l_i^j, l_i^{j'} \in L, \ j \not = j'\}$$
and negation edges
$$N_E = \{(l_i^j, l_a^b) \ \vert \ l_i^j, l_a^b \in L, \ \overline{l_i^j} = l_a^b \}.$$
Then an independent set of size $m$ will indicate a set of literals to set to true to get a correct assignment. Define the [undirected graph](graph.md)
$$G = (L, C_E \cup N_E).$$
We now apply the solution of [Independent set of a given size](independent_set_of_a_given_size.md) to $G$ and $g = m$.

To make $G$ we need to scan through each clause and make at most 3 vertices, this is $O(m)$. Then to connect the edges we need to first add the $C_E$ which takes $O(m)$ again. To find all the negation edges for each variable we need to find all the literals using that, this takes $O(nm)$. Therefore this process takes $O(nm)$ and is [polynomial time](polynomial_time.md) in the size of the input.

When we have a solution to the [Independent set of a given size](independent_set_of_a_given_size.md) problem we all the literals in the independent set to true. (This is valid as we know no 2 literals in this independent set can be the negation of one another from the negation edges.) Then for any left over variables we just set them to be true.

This process takes $O(n)$ time as we have to check if a variable is in the set of returned literals.

Suppose $f$ the [3-SAT](k-satisfiability_problem_(k-sat_problem).md) problem has an assignment $a$ that solves it.

For each clause at least one literal must be correct, define this set $S = \{l_i^{j_i}\ \vert \ 1 \leq i \leq m, \ 1 \leq j_i \leq 3, \ a(l_i^{j_i}) = \mbox{ True} \}$.

The set $S$ forms the independent set in $G$ of size $m$. As $a$ is a valid assignment for $l, l' \in S$ we have $\overline{l} \not = l'$. By definition each literal in $S$ belongs to a different clause.

Suppose we have an independent set $S$ in $G$ of size $m$.

As this is an [independent set](independent_set_(graph).md) the negation edges $N_E$ guarantee for $l, l' \in S$  we have $\overline{l} \not = l'$. Therefore we can define a partial assignment $a$ of the original $n$ variables where $a(l) =$ True for $l \in S$. This can be extended to a full assignment $a$ of the original $n$ variables where if $x$ is not assigned we just set $a(x) =$ True.

As each clause is a [clique](clique_(graph).md) in $G$ from the clause edges $C_E$ every element of $S$ belongs to a different clause. As it is of size $m$ each clause has an element in $S$. So $S = \{l_i^{j_i}\ \vert \ 1 \leq i \leq m, \ 1 \leq j_i \leq 3 \}$.

As we have at least one literal in each clause being true, the assignment $a$ satisfies the original [CNF](conjunctive_normal_form_(cnf).md) $f$. Therefore $f$ is satisfiable.

This gives the reduction of [3-SAT](k-satisfiability_problem_(k-sat_problem).md) to the [Independent set of a given size](independent_set_of_a_given_size.md) problem and makes it [NP-complete](np-complete.md).

