---
aliases:
course_code: CS6215
course_name: Introduction to Graduate Algorithms
created: 2023-11-03
date_checked:
draft: false
last_edited: 2023-11-19
tags:
  - OMSCS
title: Week 10 - Graph problem complexity
type: lecture
week: 10
---
# Independent set problem

[independent set](../../notes/independent_set_(graph).md)

Therefore we have the following problem.

[Statement](../../notes/max_independent_set_problem_(graph).md#statement)

Though this problem is not known to be in [NP](../../notes/nondeterministic_polynomial_time_(np).md) as to verify if a set is the largest set we would require to calculate the set of largest size. However, we can edit this question to make one that is in [NP](../../notes/nondeterministic_polynomial_time_(np).md).

[Statement](../../notes/independent_set_of_a_given_size.md#statement)

# Independent set of a given size is [NP-Complete](../../notes/np-complete.md)

[Independent set of a given size is in NP](../../notes/independent_set_of_a_given_size_is_in_np.md)

More over we have it is [NP-Complete](../../notes/np-complete.md).

[Independent set of a given size is NP-complete](../../notes/independent_set_of_a_given_size_is_np-complete.md)

# Max independent set is [NP-hard](../../notes/np-hard.md)

[Max independent set problem is NP-hard](../../notes/max_independent_set_problem_is_np-hard.md)

# Clique problem

[Clique (graph)](../../notes/clique_(graph).md)

So similarly with the [Independent set problem](../../notes/max_independent_set_problem_(graph).md) we can define two problems.

[Statement](../../notes/max_clique_problem_(graph).md#statement)

[Statement](../../notes/clique_of_a_given_size_problem.md#statement)

Similarly to before the first problem is not know to be in [NP](../../notes/nondeterministic_polynomial_time_(np).md) however the second is.

[Clique of a given size problem is in NP](../../notes/clique_of_a_given_size_problem_is_in_np.md)

Notice that really [clique](../../notes/clique_(graph).md) problems and [independent set](../../notes/independent_set_(graph).md) problems are dual to one another. Through the concept of the [complement graph](../../notes/complement_graph.md).

[Complement graph](../../notes/complement_graph.md)

This is formalised through the following lemma.

[Cliques in G are independent sets in the complement](../../notes/cliques_in_g_are_independent_sets_in_the_complement.md)

So we can easily show [Clique of a given size problem](../../notes/clique_of_a_given_size_problem.md) is [NP-complete](../../notes/np-complete.md) by finding a [many-one reduction](../../notes/many-one_reduction_(problem).md) of [Independent set of a given size](../../notes/independent_set_of_a_given_size.md).

[Clique of a given size problem is NP-complete](../../notes/clique_of_a_given_size_problem_is_np-complete.md)

We get a similar result for the max problem.

[Max clique problem is NP-hard](../../notes/max_clique_problem_is_np-hard.md)

# Vertex cover problem

First we define a new concept.

[Vertex cover](../../notes/vertex_cover.md)

Then similarly to before we get two logical problems.

[Statement](../../notes/minimum_vertex_cover_problem.md#statement)

[Statement](../../notes/vertex_cover_of_a_given_size.md#statement)

Like before the minimum problem is not known to be in [NP](../../notes/nondeterministic_polynomial_time_(np).md), however the second is.

[Vertex cover of a given size is NP](../../notes/vertex_cover_of_a_given_size_is_np.md)

The [vertex cover](../../notes/vertex_cover.md) is closely related to the [independent set](../../notes/independent_set_(graph).md).

[Vertex cover if and only if the complement is an independent set](../../notes/vertex_cover_if_and_only_if_the_complement_is_an_independent_set.md)

So we can prove [Vertex cover of a given size](../../notes/vertex_cover_of_a_given_size.md) is [NP-complete](../../notes/np-complete.md) by finding a [many-one reduction](../../notes/many-one_reduction_(problem).md) of [Independent set of a given size](../../notes/independent_set_of_a_given_size.md) to it.

[Vertex cover of a given size is NP-complete](../../notes/vertex_cover_of_a_given_size_is_np-complete.md)

From this we get the [Minimum vertex cover problem](../../notes/minimum_vertex_cover_problem.md) is [NP-hard](../../notes/np-hard.md).

[Minimum vertex cover problem is NP-hard](../../notes/minimum_vertex_cover_problem_is_np-hard.md)

# Practice problems

From [Algorithms](http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf) by S. Dasgupta, C. Papadimitriou, and U. Vazirani.

>[!question] 8.4 NP-completeness error

>[!question] 8.10 Proof by generalisation

>[!question] 8.14 Clique + Independent set (HW 6 assessed)

>[!question] 8.19 Kite

