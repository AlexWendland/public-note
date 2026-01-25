---
aliases:
created: 2023-10-20
date_checked:
draft: false
last_edited: 2025-12-05
tags:
  - programming
title: The flow across an st-cut is equal to the value of the flow itself
type: lemma
---
# Statement

> [!lemma] Lemma
> Let $(G, c, s, t)$ be a [flow network](flow_network.md) with a [flow](flow.md) $f$ and an [st-cut](st-cut.md) $(S,T)$. Then the flow across $(S,T)$
> $$flow^f(S,T) := \left ( \sum_{\substack{(s',t') \in E\\ s' \in S, t' \in T}} f(s',t') \right ) - \left ( \sum_{\substack{(t',s') \in E\\ s' \in S, t' \in T}} f(t',s') \right )$$
> is equal to the $size(f)$
> $$flow^f(S,T) = size(f).$$
# Proof

We prove by induction on the size of $\vert S \vert$.

If $\vert S \vert = 1$ then $S = \{s\}$ then $flow^f(S,T)$ is easy to calculate.
$$
\begin{align*}
flow^f(S,T) & = \left ( \sum_{\substack{(s',t') \in E\\ s' \in S, t' \in T}} f(s',t') \right ) - \left ( \sum_{\substack{(t',s') \in E\\ s' \in S, t' \in T}} f(t',s') \right )\\
& = \sum_{\substack{(s,v) \in E\\ v \in V}} f(s,v)\\
& = size(f)
\end{align*}
$$
This gives the desired result.

Suppose now $\vert S \vert > 1$ and we have shown the result for [st-cuts](st-cut.md) with smaller $\vert S \vert$.

As $\vert S \vert > 1$ there is an element $s^{\ast} \in S$ with $s^{\ast} \not = s$ (note as $s^{\ast} \in S$ $s^{\ast} \not = t$). Therefore consider the altered [st-cut](st-cut.md) $S' = S \backslash \{s^{\ast}\}, T' = T \cup \{s^{\ast}\}$.

By the conservation of flow we have
$$
\begin{align*}
0 & = \left ( \sum_{(v,s^{\ast}) \in E} f(v,s^{\ast}) \right ) - \left ( \sum_{(s^{\ast},v) \in E} f(s^{\ast},v) \right )\\
& = \left ( \sum_{\substack{(s',s^{\ast}) \in E\\ s' \in S'}} f(s',s^{\ast}) + \sum_{\substack{(t',s^{\ast}) \in E\\ t' \in T}} f(t',s^{\ast}) \right ) - \left ( \sum_{\substack{(s^{\ast}, s') \in E\\ s' \in S'}} f(s^{\ast}, s') + \sum_{\substack{(s^{\ast}, t') \in E\\ t' \in T}} f(s^{\ast}, t') \right )\\
& = \left ( \sum_{\substack{(s',s^{\ast}) \in E\\ s' \in S'}} f(s',s^{\ast}) - \sum_{\substack{(s^{\ast}, s') \in E\\ s' \in S'}} f(s^{\ast}, s')  \right ) - \left ( \sum_{\substack{(s^{\ast}, t') \in E\\ t' \in T}} f(s^{\ast}, t') - \sum_{\substack{(t',s^{\ast}) \in E\\ t' \in T}} f(t',s^{\ast}) \right )
\end{align*}
$$
giving
$$
\sum_{\substack{(s',s^{\ast}) \in E\\ s' \in S'}} f(s',s^{\ast}) - \sum_{\substack{(s^{\ast}, s') \in E\\ s' \in S'}} f(s^{\ast}, s') = \sum_{\substack{(s^{\ast}, t') \in E\\ t' \in T}} f(s^{\ast}, t') - \sum_{\substack{(t',s^{\ast}) \in E\\ t' \in T}} f(t',s^{\ast})
$$
As $\vert S' \vert = \vert S \vert - 1 < \vert S \vert$ by induction we have
$$
\begin{align*}
size(f) & = \left ( \sum_{\substack{(s',t') \in E\\ s' \in S', t' \in T'}} f(s',t') \right ) - \left ( \sum_{\substack{(t',s') \in E\\ s' \in S', t' \in T'}} f(t',s') \right )\\
& = \left ( \sum_{\substack{(s',\overline{t}) \in E\\ s' \in S', \overline{t} \in T}} f(s',\overline{t}) + \sum_{\substack{(s',s^{\ast}) \in E\\ s' \in S'}} f(s',s^{\ast}) \right ) - \left ( \sum_{\substack{(\overline{t},s') \in E\\ s' \in S', \overline{t} \in T}} f(\overline{t},s') + \sum_{\substack{(s^{\ast}, s') \in E\\ s' \in S'}} f(s^{\ast}, s') \right )\\
& = \left ( \sum_{\substack{(s',\overline{t}) \in E\\ s' \in S', \overline{t} \in T}} f(s',\overline{t}) - \sum_{\substack{(\overline{t},s') \in E\\ s' \in S', \overline{t} \in T}} f(\overline{t},s') \right ) + \left ( \sum_{\substack{(s',s^{\ast}) \in E\\ s' \in S'}} f(s',s^{\ast}) - \sum_{\substack{(s^{\ast}, s') \in E\\ s' \in S'}} f(s^{\ast}, s') \right)\\
& = \left ( \sum_{\substack{(s',\overline{t}) \in E\\ s' \in S', \overline{t} \in T}} f(s',\overline{t}) - \sum_{\substack{(\overline{t},s') \in E\\ s' \in S', \overline{t} \in T}} f(\overline{t},s') \right ) + \left ( \sum_{\substack{(s^{\ast}, \overline{t}) \in E\\ \overline{t} \in T}} f(s^{\ast}, \overline{t}) - \sum_{\substack{(\overline{t},s^{\ast}) \in E\\ \overline{t} \in T}} f(\overline{t},s^{\ast}) \right)\\
& = \left ( \sum_{\substack{(s',t') \in E\\ s' \in S, t' \in T}} f(s',t') \right ) - \left ( \sum_{\substack{(t',s') \in E\\ s' \in S, t' \in T}} f(t',s') \right )\\
& = flow(S,T)
\end{align*}
$$
giving the desired result for $(S, T)$.

So by induction we have the result holds in general.
