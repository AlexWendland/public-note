---
aliases:
checked: false
course: CS6215 Introduction to Graduate Algorithms
created: 2023-11-07
draft: false
last_edited: 2023-11-13
tags:
  - OMSCS
title: Week 11 - Linear Programming
type: lecture
week:
---

In broad terms a [linear programme](../../general/linear_programme.md) is an optimisation problem of a [linear](../../general/linear_function.md) function where there are [linear](../../general/linear_function.md) bounds on the variables.

>[!example] [Max flow problem](../../general/max_flow_problem.md)
>We are given a [directed graph](../../general/directed_graph.md) $G = (V,E)$ with capacities $c: E \rightarrow \mathbb{R}_{>0}$ and source $s \in V$ and sink $t \in V$.
>
>To define the [linear programme](../../general/linear_programme.md) make $\vert E \vert$ variables $f_e$ for each $e \in E$. These will represent the flow along these edges. Then we want to maximise the [flow](../../general/flow.md) defined by the flow out of $s$
>$$ \max \sum_{(s,v) \in E} f_{(s,v)}.$$
>However, the edges must flow abiding by the capacity constraints
>$$0 \leq f_{e} \leq c(e) \mbox{ for } e \in E.$$
>As well as abide by the preservation of flow
>$$ \sum_{(u,v) \in E} f_{(u,v)} - \sum_{(v,w) \in E} f_{(v,w)} = 0 \mbox{ for } v \in V \backslash \{s,t\}.$$
>This defines our [linear programme](../../general/linear_programme.md) and the solution to this provides a solution to the [max flow](../../general/max_flow_problem.md) problem.

# Linear programme general form

[Linear programme](../../general/linear_programme.md)

It helps to standardise this into the following form. Note the use of [matrix](../../general/matrix.md) notation here.

[Linear programme standard form](../../general/linear_programme_standard_form.md)

We can convert all [linear programmes](../../general/linear_programme.md) into standard form using the following Lemma.

[All linear programmes can be represented in standard form](../../general/all_linear_programmes_can_be_represented_in_standard_form.md)

# Geometric view

From now on we just consider [linear programmes in standard form](../../general/linear_programme_standard_form.md).

We can consider the *feasible* $x$ such that $x \geq 0$ and $x^T A \leq b$.

As there are $n$ variables we know $x \in \mathbb{R}^n$, more over as $x \geq 0$ we have that it lies in the positive region on $\mathbb{R}^n$.

Each row of $Ax \leq b$ defines a half space, so the feasible $x$ lie in the positive region of $x \in \mathbb{R}^n$ cut out by these half spaces.

>[!example] 2D-example
>Suppose we have the linear programme
>$$\max_x x_1 + 6 x_2$$
>with respect to $x \geq 0$ and
>$$ x_1 \leq 300, \ x_2 \leq 200, \mbox{ and } x_1 + 3 x_2 \leq 700.$$
>This region can be visualised as follows.
>
>![2d_feasible_region](../../../images/excalidraw/2d_feasible_region.excalidraw.svg)

So the feasible region is cut out by $n + m$ half spaces in $\mathbb{R}^n$.

The *vertices* in this feasible space are ones that lie on a 0-dimensional intersection of the boundary of the half spaces. In the example above these would be
$$(0,0), (0,200), (100,200), (300,0), \mbox{ and } (300, 133.33..).$$

# Linear programme solvers

When it comes to solving a linear programming problem.

[Statement](../../general/linear_programming_problem.md#statement)

There are [polynomial time](../../general/polynomial_time.md) algorithms like the [ellipsoid method](../../general/ellipsoid_method_(linear_programming).md) and [interior-point method](../../general/interior-point_method_(linear_programme).md) but in practice these can be slower than the much more widely used [simplex method](../../general/simplex_method_(linear_programme).md) which can be exponential in its worst cases.

# Simplex method

As vertices are extremal points with regards to the constraints we have that if the maximum of the objective function exists then it must be achieved on one of the vertices. Therefore the idea of the simplex algorithm is to start at a vertex then compare the objective function to all other vertices connecting to it.

So in short

```pseudocode
1. Start at x = 0, if that is feasible.
2. Find all vertices adjacent to x along an edge.
3. compare the objective function of all vertices and
	1. If the current x is highest return that value.
	2. Switch x to be the highest of the objective functions found around x.
4. Go to step 2.
```

This only works if there is a point in the feasible region that achieves this maximum. Here we have 2 constraints:
- There is a point in the feasible region.
- That some point achieves a maximum - this happens when the region is bounded and has finite volume.

These are summarised by the two types of linear programme.

[Infeasible linear programme](../../general/infeasible_linear_programme.md)

[Unbounded linear programme](../../general/unbounded_linear_programme.md)

# Determining if a [linear programme](../../general/linear_programme.md) is infeasible

Suppose we have a [linear programme in standard form](../../general/linear_programme_standard_form.md) which may or may not be a [Infeasible linear programme](../../general/infeasible_linear_programme.md). For any inequality and $x \in \mathbb{R}^n$
$$ \sum_i a_{i,j} x_j \leq b_i$$
we can satisfy it by adding an arbitrarily small $z \in \mathbb{R}$ to the left hand side
$$ z + \sum_i a_{i,j} x_j \leq b_i.$$
If $z \geq 0$ we now that the original  $x \in \mathbb{R}^n$ satisfied the inequality.

In summary from our original [linear programme](../../general/linear_programme.md) we can extend it to include an $n+1$'th variable $z$. We augment the $m$ constraints to include this variable $z$ on the left hand side. This is now a [feasible linear programme](../../general/infeasible_linear_programme.md).

Moreover, we can change the objective function of the linear programme to simply maximise $z$ and if that value is positive we have a feasible point in the original [linear programme](../../general/linear_programme.md).

[Checking if a linear programme is feasible](../../general/checking_if_a_linear_programme_is_feasible.md)

# Aside: How to verify solutions?

>[!example] Is a point optimal?
>Define a [linear programme](../../general/linear_programme.md) where we need to
>$$ \max x_1 + 6 x_2 + 10 x_3 $$
>with constraints
>$$
>\begin{align*}
>x_1 & \leq 300\\
>x_2 & \leq 200\\
>x_1 + 3 x_2 + 2 x_3 & \leq 1000\\
>x_2 + 3 x_3 & \leq 500\\
>x_1, x_2, x_3 & \geq 0
>\end{align*}
>$$
>this uses 3 variables and 4 constraints. If will tell you the point $(200, 200, 100)$ achieves a score of 2400 and is this point optimal?

Lets try to upper bound the objective function $x_1 + 6 x_2 + 10 x_3$, we will do this with linear combinations of the inequalities. Lets consider the following

$$
\begin{align*}
(x_2) * 1/3 + (x_1 + 3x_2 + 2 x_3) + (x_2 + 3x_3) * 8/3 & \leq 200 * 1/3 + 1000 + 500 * 8/3\\
x_1 + x_2(1/3 + 1 + 8/3) + x_3 (2 + 3 * 8/3) & \leq 2400\\
x_1 + 6 x_2 + 10 x_3 \leq 2400
\end{align*}
$$
This then gives that the objective function is bounded above 2400, so the point provided must be optimal as we can never get a larger objective score.

Though I picked some values for the linear combination, how do we more generically find them and when will I know the bound is low enough?

# Dual linear programme

How do we get which linear combinations will be "optimal"?

Define $y_i$ for $1 \leq i \leq m$ and take $y_i \geq 0$ linear combinations of each of the constraints defined by
$$\sum_j a_{i,j} x_j \leq b_i.$$
With the goal to finish with an equation of the form
$$ \sum_j c_j x_j \leq \sum_i y_i \left ( \sum_j a_{i,j} x_j \right ) = \sum_j \left ( \sum_i y_i a_{i,j} \right ) x_j \leq C = \sum_i y_i b_i.$$
For the optimum bound we would like to minimise the quantity on the right.

To do this define a new [linear programme](../../general/linear_programme.md).

[Dual linear programme](../../general/dual_linear_programme.md)

If in the original [linear programme](../../general/linear_programme.md) we have $n$ variables and $m$ constraints. In the [dual linear programme](../../general/dual_linear_programme.md) we have $m$ variables and $n$ constraints.

We call the initial [linear programme](../../general/linear_programme.md) the *primal linear programme* however we will try not to use that term.

# Dual of a Dual

[The dual dual linear programme is the original linear programme](../../general/the_dual_dual_linear_programme_is_the_original_linear_programme.md)

# Weak duality

The intuition behind the [dual linear programme](../../general/dual_linear_programme.md) was that it bounded the objective function. So lets check if that is true.

[Weak duality theorem (linear programme)](../../general/weak_duality_theorem_(linear_programme).md)

This means the example above gives us a good way to check for optimal points.

[If a point in a linear programme has equal objective function to a point in its dual linear programme they are both optimal](../../general/if_a_point_in_a_linear_programme_has_equal_objective_function_to_a_point_in_its_dual_linear_programme_they_are_both_optimal.md)

# Check for unbounded linear programme

Another corollary of the [Weak duality theorem](../../general/weak_duality_theorem_(linear_programme).md) helps us identify when we have [unbounded linear programmes](../../general/unbounded_linear_programme.md).

[Unbounded linear programmes have infeasible duals](../../general/unbounded_linear_programmes_have_infeasible_duals.md)

Note that as [the dual dual linear programme is the original linear programme](../../general/the_dual_dual_linear_programme_is_the_original_linear_programme.md) this also gives us that if the [dual linear programme](../../general/dual_linear_programme.md) is unbounded then the original [linear programme](../../general/linear_programme.md) is [infeasible](../../general/infeasible_linear_programme.md).

This gives us a nice check for if a [linear programme](../../general/linear_programme.md) is [unbounded](../../general/unbounded_linear_programme.md). As we know [Checking if a linear programme is feasible](../../general/checking_if_a_linear_programme_is_feasible.md) can be done, we just need to check if the [dual linear programme](../../general/dual_linear_programme.md) is feasible - if it is then the original [linear programme](../../general/linear_programme.md) is bounded. If the [dual linear programme](../../general/dual_linear_programme.md) is not [feasible](../../general/infeasible_linear_programme.md) then we still need to check if the original [linear programme](../../general/linear_programme.md) is [feasible](feasible.md) or not (note a [linear programme](../../general/linear_programme.md)  can't be both [infeasible](../../general/infeasible_linear_programme.md) and [unbounded](../../general/unbounded_linear_programme.md)).

Therefore we have a nice algorithm to check if we have a solvable [linear programme](../../general/linear_programme.md).

[Algorithm](../../general/check_if_a_linear_programme_is_solvable.md#algorithm)

# Strong duality theorem

[Strong duality theorem (linear programme)](../../general/strong_duality_theorem_(linear_programme).md)

This can be reformulated in terms of optimal points.

[Strong duality theorem optimum (linear programme)](../../general/strong_duality_theorem_optimum_(linear_programme).md)

As a cool corollary we can use this to prove [Max-flow min-cut Theorem](../../general/max-flow_min-cut_theorem.md) using the restatement of the problems in terms of [linear programmes](../../general/linear_programme.md).

