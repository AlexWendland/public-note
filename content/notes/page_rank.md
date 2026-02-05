---
aliases:
  - page rank
created: 2023-12-03
date_checked:
draft: false
last_edited: 2026-02-05
tags:
  - programming
title: Page rank
type: definition
---
>[!definition] Page rank
>The page rank is a [probability distribution](probability_distribution.md) over the vertices of the [Webgraph](webgraph.md) $G = (V,E)$. This is a function $\pi : V \rightarrow [0,1]$ that assigns a ranking to each page. It is defined recursively as
> $$\pi(x) = \sum_{y \in In(x)} \frac{\pi(y)}{\vert Out(y) \vert}.$$
> With
> - $Out(x) = \{y \in V \vert (x,y) \in E\}$, and
> - $In(x) = \{y \in V \vert (y,x) \in E\}$.

