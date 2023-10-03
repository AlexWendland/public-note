---
aliases:
  - max flow
type: problem
publish: true
created: 2023-10-02
last_edited: 2023-10-02
tags:
  - programming
chatgpt: false
---
# Statement

> [!tldr] Max-flow problem
> Given a [[Flow network|flow network]] $(G, c, s, t)$ what is the max value a [[Flow|flow]] on this network can have?

# Solutions
- [[Ford-Fulkerson Algorithm]]
	- $O(C \vert E \vert)$ where $C$ is the max flow.
	- This is only guaranteed to terminate for integer flows. 
- 

# Theory

- [[Max-flow min-cut Theorem]]