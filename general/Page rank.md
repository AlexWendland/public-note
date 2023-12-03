---
aliases:
  - page rank
checked: false
created: 2023-12-03
last_edited: 2023-12-03
publish: true
tags:
  - programming
type: definition
---
>[!tldr] Page rank
>The page rank is a [[Probability distribution|probability distribution]] over the vertices of the [[Webgraph]] $G = (V,E)$. This is a function $\pi : V \rightarrow [0,1]$ that assigns a ranking to each page. It is defined recursively as
> $$\pi(x) = \sum_{y \in In(x)} \frac{\pi(y)}{\vert Out(y) \vert}.$$
> With
> - $Out(x) = \{y \in V \vert (x,y) \in E\}$, and
> - $In(x) = \{y \in V \vert (y,x) \in E\}$. 

