---
aliases:
checked: false
created: 2023-10-20
draft: false
last_edited: 2023-11-13
tags:
  - maths
type: lemma
---
# Statement

> [!important] Lemma
> Given a [[Flow network]] $(G, c, s, t)$ with a [[Max flow problem|max flow]] $f$. Then for every [[Min st-cut problem|min st-cut]] ($S$, $T$) we have $f(t',s') = 0$ all edges in $(t',s') \in E$ for $t' \in T$ and $s' \in S$.

# Proof

From the [[Max-flow min-cut Theorem]] we know that for any [[Min st-cut problem|min st-cut]] $(S, T)$ we have
$$capacity(S,T) = size(f).$$
As [[The flow across an st-cut is equal to the value of the flow itself|the flow across any st-cut is equal to the value of the flow itself]] we have
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

Note this also gives [[Every min-cut is at full capacity in a max-flow|every min-cut is at full capacity in a max-flow]].
