---
aliases: null
checked: false
created: 2023-09-29
last_edited: 2023-09-29
publish: true
tags:
  - programming
type: problem
---
## Statement

> [!tldr] Find [[Strongly connected components (directed graphs)|strongly connected components]] in an [[Directed graph|directed graph]]
> Given a [[Directed graph|directed graph]] $G = (V,E)$ how can we find a mapping from it's vertices $V$ to the [[Strongly connected components (directed graphs)|strongly connected components]] of $G$.

## Solutions

- [[DFS for finding strongly connected components]]
	- This runs in $O(\vert V \vert \cdot \vert E \vert)$ time.
	- It also outputs the strongly connected components in a reverse [[Topological sorting (DAG)|topologically sort]].
