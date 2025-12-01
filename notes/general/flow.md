---
aliases:
  - flow
checked: false
created: 2023-10-02
draft: false
last_edited: 2023-11-11
name: Flow
tags:
  - programming
type: definition
---
>[!tldr] Flow
>Given a [flow network](flow_network.md) $(G, c, s, t)$ a flow is an allocation $f: E \rightarrow \mathbb{R}_{\geq0}$ such that the following holds:
>
>- capacity constraint: $f(e) \leq c(e)$ for all $e \in E$, and
>- conservation of flow: $\sum_{(a,v) \in E} f(a,v) = \sum_{(v,b)} f(v,b)$ for all $v \in V \backslash \{s, t\}$.
>
>The size of this flow is $size(f) = \sum_{(s,a) \in E} f(s,a) = \sum_{(b,t) \in E} f(b,t)$.





