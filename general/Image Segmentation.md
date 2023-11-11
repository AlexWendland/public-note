---
aliases: null
chatgpt: false
created: 2023-10-04
last_edited: 2023-10-04
publish: true
tags:
  - programming
type: problem
---
# Statement

>[!tldr] Image Segmentation
>Given an undirected graph $G = (V,E)$ with weights:
>- for each $v \in V$, $f(v), b(v) \geq 0$, and
>- for each $e \in E$, $p(e) \geq 0$.
>We we find [[Cut (graph)|cut]] $V = F \cup B$ that maximises
>$$w(F,B) = \sum_{v \in F} f(v) + \sum_{u \in B} b(u) - \sum_{(v,u) \in cut(F,B)} p(u,v).$$

# Solutions
- [[Image segmentation by max flow]]
	- This runs as fast as your solution to [[Min st-cut problem|min st-cut]]
