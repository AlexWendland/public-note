---
aliases:
checked: false
course_code: CS6215
course_name: Introduction to Graduate Algorithms
created: 2023-11-03
draft: false
last_edited: 2023-11-19
tags:
  - OMSCS
title: Week 10 - Graph problem complexity
type: lecture
week: 10
---
# Independent set problem

[independent set](../../general/independent_set_(graph).md)

Therefore we have the following problem.

[Statement](../../general/max_independent_set_problem_(graph).md#statement)

Though this problem is not known to be in [NP](../../general/nondeterministic_polynomial_time_(np).md) as to verify if a set is the largest set we would require to calculate the set of largest size. However, we can edit this question to make one that is in [NP](../../general/nondeterministic_polynomial_time_(np).md).

[Statement](../../general/independent_set_of_a_given_size.md#statement)

# Independent set of a given size is [NP-Complete](../../general/np-complete.md)

[Independent set of a given size is in NP](../../general/independent_set_of_a_given_size_is_in_np.md)

More over we have it is [NP-Complete](../../general/np-complete.md).

[Independent set of a given size is NP-complete](../../general/independent_set_of_a_given_size_is_np-complete.md)

# Max independent set is [NP-hard](../../general/np-hard.md)

[Max independent set problem is NP-hard](../../general/max_independent_set_problem_is_np-hard.md)

# Clique problem

[Clique (graph)](../../general/clique_(graph).md)

So similarly with the [Independent set problem](../../general/max_independent_set_problem_(graph).md) we can define two problems.

[Statement](../../general/max_clique_problem_(graph).md#statement)

[Statement](../../general/clique_of_a_given_size_problem.md#statement)

Similarly to before the first problem is not know to be in [NP](../../general/nondeterministic_polynomial_time_(np).md) however the second is.

[Clique of a given size problem is in NP](../../general/clique_of_a_given_size_problem_is_in_np.md)

Notice that really [clique](../../general/clique_(graph).md) problems and [independent set](../../general/independent_set_(graph).md) problems are dual to one another. Through the concept of the [complement graph](../../general/complement_graph.md).

[Complement graph](../../general/complement_graph.md)

This is formalised through the following lemma.

[Cliques in G are independent sets in the complement](../../general/cliques_in_g_are_independent_sets_in_the_complement.md)

So we can easily show [Clique of a given size problem](../../general/clique_of_a_given_size_problem.md) is [NP-complete](../../general/np-complete.md) by finding a [many-one reduction](../../general/many-one_reduction_(problem).md) of [Independent set of a given size](../../general/independent_set_of_a_given_size.md).

[Clique of a given size problem is NP-complete](../../general/clique_of_a_given_size_problem_is_np-complete.md)

We get a similar result for the max problem.

[Max clique problem is NP-hard](../../general/max_clique_problem_is_np-hard.md)

# Vertex cover problem

First we define a new concept.

[Vertex cover](../../general/vertex_cover.md)

Then similarly to before we get two logical problems.

[Statement](../../general/minimum_vertex_cover_problem.md#statement)

[Statement](../../general/vertex_cover_of_a_given_size.md#statement)

Like before the minimum problem is not known to be in [NP](../../general/nondeterministic_polynomial_time_(np).md), however the second is.

[Vertex cover of a given size is NP](../../general/vertex_cover_of_a_given_size_is_np.md)

The [vertex cover](../../general/vertex_cover.md) is closely related to the [independent set](../../general/independent_set_(graph).md).

[Vertex cover if and only if the complement is an independent set](../../general/vertex_cover_if_and_only_if_the_complement_is_an_independent_set.md)

So we can prove [Vertex cover of a given size](../../general/vertex_cover_of_a_given_size.md) is [NP-complete](../../general/np-complete.md) by finding a [many-one reduction](../../general/many-one_reduction_(problem).md) of [Independent set of a given size](../../general/independent_set_of_a_given_size.md) to it.

[Vertex cover of a given size is NP-complete](../../general/vertex_cover_of_a_given_size_is_np-complete.md)

From this we get the [Minimum vertex cover problem](../../general/minimum_vertex_cover_problem.md) is [NP-hard](../../general/np-hard.md).

[Minimum vertex cover problem is NP-hard](../../general/minimum_vertex_cover_problem_is_np-hard.md)

# Practice problems

From [Algorithms](http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf) by S. Dasgupta, C. Papadimitriou, and U. Vazirani.

>[!question] 8.4 NP-completeness error

>[!question] 8.10 Proof by generalisation

>[!question] 8.14 Clique + Independent set (HW 6 assessed)

>[!question] 8.19 Kite

