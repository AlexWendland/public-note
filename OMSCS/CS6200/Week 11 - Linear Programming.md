---
aliases: 
type: lecture
publish: false
created: 2023-11-07
last_edited: 2023-11-07
tags:
  - OMSCS
course: "[[CS6200 Introduction to Graduate Algorithms]]"
week: 
chatgpt: false
---
# Week 11 - Linear Programming

In broad terms a [[Linear programme|linear programme]] is an optimisation problem of a [[Linear function|linear]] function where there are [[Linear function|linear]] bounds on the variables.

>[!example] [[Max flow problem]]
>We are given a [[Directed graph|directed graph]] $G = (V,E)$ with capacities $c: E \rightarrow \mathbb{R}_{>0}$ and source $s \in V$ and sink $t \in V$.
>
>To define the [[Linear programme|linear programme]] make $\vert E \vert$ variables $f_e$ for each $e \in E$. These will represent the flow along these edges. Then we want to maximise the [[Flow|flow]] defined by the flow out of $s$
>$$ \max \sum_{(s,v) \in E} f_{(s,v)}.$$
>However, the edges must flow abiding by the capacity constraints
>$$0 \leq f_{e} \leq c(e) \mbox{ for } e \in E.$$
>As well as abide by the preservation of flow
>$$ \sum_{(u,v) \in E} f_{(u,v)} - \sum_{(v,w) \in E} f_{(v,w)} = 0 \mbox{ for } v \in V \backslash \{s,t\}.$$
>This defines our [[Linear programme|linear programme]] and the solution to this provides a solution to the [[Max flow problem|max flow]] problem. 

## Linear programme general form

![[Linear programme]]

It helps to standardise this into the following form. Note the use of [[Matrix|matrix]] notation here.

![[Linear programme standard form]]

We can convert all [[Linear programme|linear programmes]] into standard form using the following Lemma.

![[All linear programmes can be represented in standard form]]

## Geometric view

From now on we just consider [[Linear programme standard form|linear programmes in standard form]].

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
>![[2d_feasible_region]]

So the feasible region is cut out by $n + m$ half spaces in $\mathbb{R}^n$.

The *vertices* in this feasible space are ones that lie on a 0-dimensional intersection of the boundary of the half spaces. In the example above these would be
$$(0,0), (0,200), (100,200), (300,0), \mbox{ and } (300, 133.33..).$$

## Linear programme solvers

When it comes to solving a linear programming problem.

![[Linear programme problem#Statement]]

There are [[Polynomial time|polynomial time]] algorithms like the [[Ellipsoid method (linear programming)|ellipsoid method]] and [[Interior-point method (linear programme)|interior-point method]] but in practice these can be slower than the much more widely used [[Simplex method (linear programme)|simplex method]] which can be exponential in its worst cases.

## Simplex method

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

![[Infeasible linear programme]]

![[Unbounded linear programme]]

## Determining if a [[Linear programme|linear programme]] is infeasible

Suppose we have a [[Linear programme standard form|linear programme in standard form]] which may or may not be a [[Infeasible linear programme]]. For any inequality and $x \in \mathbb{R}^n$
$$ \sum_i a_{i,j} x_j \leq b_i$$
we can satisfy it by adding an arbitrarily small $z \in \mathbb{R}$ to the left hand side
$$ z + \sum_i a_{i,j} x_j \leq b_i.$$
If $z \geq 0$ we now that the original  $x \in \mathbb{R}^n$ satisfied the inequality.

In summary from our original [[Linear programme|linear programme]] we can extend it to include an $n+1$'th variable $z$. We augment the $m$ constraints to include this variable $z$ on the left hand side. This is now a [[Infeasible linear programme|feasible linear programme]].

Moreover, we can change the objective function of the linear programme to simply maximise $z$ and if that value is positive we have a feasible point in the original [[Linear programme|linear programme]].

![[Checking if a linear programme is feasible]]

## Aside: How to verify solutions?

>[!example] Is a point optimal?
>Define a [[Linear programme|linear programme]] where we need to
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

## Dual linear programme

