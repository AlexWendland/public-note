---
aliases:
  - max flow
chatgpt: false
created: 2023-10-02
last_edited: 2023-10-02
publish: true
tags:
  - programming
type: problem
---
# Statement

> [!tldr] Max-flow problem
> Given a [[Flow network|flow network]] $(G, c, s, t)$ what is the max value a [[Flow|flow]] on this network can have?

# Solutions
- [[Ford-Fulkerson Algorithm]]
	- $O(C \vert E \vert)$ where $C$ is the max flow.
	- This is only guaranteed to terminate for integer flows.
- [[Edmonds-Karp algorithm]]
	- $O(\vert E \vert^2 \cdot \vert V \vert)$ run time.
	- Assumes positive flow values.

# Theory

- [[Max-flow min-cut Theorem]]
	- This says the solutions are the same as the [[Min st-cut problem|min st-cut]] problems.
