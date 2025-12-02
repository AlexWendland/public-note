---
aliases:
checked: false
created: 2023-10-20
draft: false
last_edited: 2023-11-13
tags:
  - maths
title: Every min-cut has no flow going backwards along it in a max-flow
type: lemma
---
# Statement

> [!important] Lemma
> Given a [Flow network](flow_network.md) $(G, c, s, t)$ with a [max flow](max_flow_problem.md) $f$. Then for every [min st-cut](min_st-cut_problem.md) ($S$, $T$) we have $f(t',s') = 0$ all edges in $(t',s') \in E$ for $t' \in T$ and $s' \in S$.

# Proof

From the [Max-flow min-cut Theorem](max-flow_min-cut_theorem.md) we know that for any [min st-cut](min_st-cut_problem.md) $(S, T)$ we have
$$capacity(S,T) = size(f).$$
As [the flow across any st-cut is equal to the value of the flow itself](the_flow_across_an_st-cut_is_equal_to_the_value_of_the_flow_itself.md) we have
$$flow^f(S,T) = size(f).$$
So we have
$$
\begin{align*}
capacity(S,T) & = flow^f(S,T)\\
\sum_{\substack{(s',t') \in E\\ s' \in S, t' \in T}} c(s',t') & =  \left ( \sum_{\substack{(s',t') \in E\\ s' \in S, t' \in T}} f(s',t') \right ) - \left ( \sum_{\substack{(t',s') \in E\\ s' \in S, t' \in T}} f(t',s') \right ).\\
\end{align*}
$$
Given $0 \leq f(v,w) \leq c(v,w)$ for $(v,w) \in E$. This gives that $f(s', t') = c(s',t')$ for any $(s',t') \in E$ and $f(t', s') = 0$ $(t',s') \in E$ with $s' \in S$ and $T' \in T$.

Which is the required result.

Note this also gives [every min-cut is at full capacity in a max-flow](every_min-cut_is_at_full_capacity_in_a_max-flow.md).
