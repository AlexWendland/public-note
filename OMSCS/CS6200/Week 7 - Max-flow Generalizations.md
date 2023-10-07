---
aliases: 
type: lecture
publish: true
created: 2023-10-07
last_edited: 2023-10-07
tags:
  - OMSCS
course: "[[CS6200 Introduction to Graduate Algorithms]]"
week: 7
chatgpt: false
---
# Week 7 - Max-flow Generalizations

## [[Max flow problem|Max flow]] with demands

>[!tldr] [[Max flow problem|Max flow]] with demands
>Let $(G=(V,E), c, s, t)$ be a [[Flow network|flow network]] and assume we are provided with demands $d(e) \geq 0$ for $e \in E$. A flow $f$ is called feasible if
>$$d(e) \leq f(e) \leq c(e).$$
>Is there a feasible flow and if so what is the max feasible flow?

