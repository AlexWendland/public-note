---
aliases:
checked: false
created: 2023-11-03
draft: false
last_edited: 2023-11-11
name: Clique of a given size problem is NP-complete
tags:
  - maths
type: lemma
---
# Statement

> [!important] Lemma
> [Clique of a given size problem](clique_of_a_given_size_problem.md) is [NP-Complete](np-complete.md).

# Proof

We have already shown that [Clique of a given size problem is in NP](clique_of_a_given_size_problem_is_in_np.md).

We will show that [Independent set of a given size](independent_set_of_a_given_size.md) has a [many-one reduction](many-one_reduction_(problem).md) to [Clique of a given size problem](clique_of_a_given_size_problem.md).

Suppose we have an [undirected graph](graph.md) $G = (V,E)$ and $g > 0$ a positive integer. If we are looking for an [independent set](independent_set_(graph).md) of size $g$, we will pass $G^C$ the [complement graph](complement_graph.md) and $g$ to the [Clique of a given size problem](clique_of_a_given_size_problem.md).

Calculating the [complement graph](complement_graph.md) takes $O(\vert V \vert^2)$, therefore this reduction is in [polynomial time](polynomial_time.md).

Then if a [clique](clique_(graph).md) $S$ is returned in $G^C$ then we return this as our [independent set](independent_set_(graph).md) in $G$.

This takes $O(1)$ as we are doing no transformations to the output.

As [Cliques in G are independent sets in the complement](cliques_in_g_are_independent_sets_in_the_complement.md) we have a solution to the [Independent set of a given size](independent_set_of_a_given_size.md) if and only if we have a solution to the [Clique of a given size problem](clique_of_a_given_size_problem.md).

This gives [Clique of a given size problem](clique_of_a_given_size_problem.md) is [NP-hard](np-hard.md) making it [NP-complete](np-complete.md).
