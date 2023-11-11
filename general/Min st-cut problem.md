---
aliases:
  - min st-cut
checked: false
created: 2023-10-03
last_edited: 2023-10-03
publish: true
tags:
  - programming
type: problem
---
# Statement

>[!tldr] Min st-cut
>Given a [[Flow network|flow network]] $(G, c, s, t)$ what is the [[st-cut]] $(L, R)$ with minimum capacity.

# Solutions

- [[Ford-Fulkerson Algorithm]]
	- $O(C \vert E \vert)$ where $C$ is the min cut.
	- This is only guaranteed to terminate for integer flows.
-

# Theory

- [[Max-flow min-cut Theorem]]
	- This says the solutions are the same as the [[Max flow problem|max flow]] problems.
