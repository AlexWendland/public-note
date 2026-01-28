---
aliases:
created: 2023-11-12
date_checked: 2026-01-28
draft: false
last_edited: 2026-01-28
tags:
  - programming
title: Subset-sum problem is NP-complete
type: lemma
---
# Statement

> [!lemma] Lemma
> [Subset-sum problem](subset-sum_problem.md) is [NP-Complete](np-complete.md).

# Proof
We already know the [Subset-sum problem is in NP](subset-sum_problem_is_in_np.md). So we need to show it is [NP-hard](np-hard.md). To do this we will make a [many-one reduction](many-one_reduction_(problem).md) from the [3-SAT](k-satisfiability_problem_(k-sat_problem).md) problem. We know that [3-SAT is NP-complete](3-sat_is_np-complete.md) giving the desired result.

Suppose we have an instance of the [3-SAT](k-satisfiability_problem_(k-sat_problem).md) problem given by $f$ with variables $x_i$ with $1 \leq i \leq n$ and clauses $c_j$ for $1 \leq j \leq m$. Each clause $c_j$ can have at most 3 literals.

We will now construct an input to the [subset-sum problem](subset-sum_problem.md) that will have $2n + 2m$ input numbers and a target $t$. We will want to talk about these numbers' digits in base 10, i.e. express the number
$$
v_i^{\ast} = \sum_{i = 0}^{n+m-1} d_i \cdot 10^i.
$$
then $d_i$ is its $i$'th digit.

For each variable $x_i$ we will introduce two variables $v_i^+$ and $v_i^-$. Let $x_i^+ = \{j \ \vert \ x_i \in c_j\}$ and $x_i^- = \{j \ \vert \ \overline{x_i} \in c_j \}$. Then we define
$$
v_i^+ = 10^{i-1} + \sum_{j \in x_i^+} 10^{n + j - 2}, \mbox{ and } v_i^- = 10^{i-1} + \sum_{j \in x_i^-} 10^{n + j - 2}.
$$
For each $c_j$ we define two variables which are identical
$$
s_j^1 = s_j^2 = 10^{n + j - 2}.
$$
Lastly we define our target
$$
t = \sum_{i = 1}^{n} 10^{i-1} + \sum_{j=1}^m 3 \cdot 10^{j-2}.
$$
It is useful to talk about the map $\theta$ where
$$\theta(x_i) = v_i^+ \mbox{ and } \theta(\overline{x_i}) = v_i^-.$$
This map is a [bijection](bijection.md) so it has well defined inverse
$$\theta^{-1}(v_i^+) = x_i \mbox{ and } \theta^{-1}(v_i^-) = \overline{x_i}.$$

>[!note] Observation
>Let $S \subset \{v_i^+, v_i^-, s_j^1, s_j^2 \vert 1 \leq i \leq n, \ 1 \leq j \leq m\}$ then
>$$\sum_{s \in S} s = \sum_{i=1}^n \vert \{v_i^+, v_i^-\} \cap S \vert 10^{i-1} + \sum_{j=1}^m \left( \vert \{s_j^1, s_j^2\} \cap S \vert + \vert \{ l \in c_j \vert \theta(l) \in S \} \vert \right ) 10^{n + j - 1}. $$

Any sum of the $v_i^+$, $v_i^-$, $s_j^1$, and $s_j^2$ can have at most 5 in any digit (as each clause can have at most 3 literals and 2 values from the $s_j^1$ or $s_j^2$), therefore there is no overflow from one digit to another.

We provide this input to the [subset-sum problem](subset-sum_problem.md), this transformation takes $O((n+m)^2)$ time, so it is [polynomial time](polynomial_time.md).

Any solution $S$ to the constructed [subset-sum problem](subset-sum_problem.md) must have exactly one of $v_i^+$ or $v_i^-$ for each $1 \leq i \leq n$ as $t$ has a 1 in its first $n$ digits. Therefore we construct an assignment for $f$ where
$$a(x_i) = \begin{cases} T & \mbox{if } v_i^+ \in S\\ F & \mbox{if } v_i^- \in S \end{cases} \ \ \ \mbox{ for } 1 \leq i \leq n.$$

This takes $O(n + m)$ to construct, as we just need to iterate through $S$. So can be done in [polynomial time](polynomial_time.md).

Suppose we have a solution to the constructed [subset-sum problem](subset-sum_problem.md). Then we have a valid assignment by the observation.

When looking at the last $m$ digits of $t$ we require a 3 in each position. Therefore for each $1 \leq j \leq m$ we have at least one $l \in c_j$ such that $\theta(l) \in S$ therefore $a(l) = T$ and we satisfy clause $c_j$.

Therefore this is a valid solution to the [3-SAT](k-satisfiability_problem_(k-sat_problem).md) problem $f$.

Suppose we have a valid assignment $a$ to $x_i$ for the [3-SAT](k-satisfiability_problem_(k-sat_problem).md) problem $f$.

Then for each clause $c_j$ define $\vert c_j \vert$ to be the number of satisfied literals - note $1 \leq \vert c_j \vert \leq 3$.

Now define
$$S = \{v_i^+ \vert a(x_i) = T\} \cup \{v_i^- \vert a(x_i) = F\} \cup \{s_j^1 \vert \ \vert c_j \vert \leq 2\} \cup \{s_j^2 \vert \vert c_j \vert \leq 1 \}.$$

Consider the sum
$$\sum_{s \in S} s = \sum_{i=1}^n \vert \{v_i^+, v_i^-\} \cap S \vert 10^{i-1} + \sum_{j=1}^m \left( \vert \{s_j^1, s_j^2\} \cap S \vert + \vert \{ l \in c_j \vert \theta(l) \in S \} \vert \right ) 10^{n + j - 1}. $$
For the first $n$ digits, as $a(x_i) = T$ or $a(x_i) = F$ we have $\vert \{v_i^+, v_i^-\} \cap S \vert = 1$.

For the last $m$ digits, we have $\vert \{ l \in c_j \vert \theta(l) \in S \} \vert = \vert c_j \vert$ and
$$\vert \{s_j^1, s_j^2\} \cap S \vert = \begin{cases} 0 & \mbox{if } \vert c_j \vert = 3\\ 1 & \mbox{if } \vert c_j \vert = 2\\ 2 & \mbox{if } \vert c_j \vert = 1\end{cases}$$
which gives a 3 in these digits.

So $S$ is a solution to our constructed [subset-sum problem](subset-sum_problem.md).

Therefore this is a valid [many-one reduction](many-one_reduction_(problem).md) and we have [subset-sum problem](subset-sum_problem.md) is [NP-hard](np-hard.md) and thus [NP-complete](np-complete.md).

