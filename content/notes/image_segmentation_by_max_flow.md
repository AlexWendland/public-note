---
aliases:
created: 2023-10-05
date_checked:
draft: false
last_edited: 2026-02-05
tags:
  - programming
title: Image segmentation by max flow
type: algorithm
---
# Theory

## Reformulation

Right now we have two problems, it is a maximalisation problem and the weights might not be non-negative.

Let
$$L = \sum_{v \in V} f(v) + b(v).$$
Then we can reformulate
$$\begin{aligned}w(F,B) & = \sum_{v \in F} f(v) + \sum_{u \in B} b(u) - \sum_{(v,u) \in cut(F,B)} p(u,v)\\
& = L - \sum_{u \in B} f(u) - \sum_{v \in F} b(v) - \sum_{(v,u) \in cut(F,B)} p(u,v)\end{aligned}$$
Therefore to maximise $w(F,B)$ we could instead minimise
$$w'(F,B) = \sum_{u \in B} f(u) + \sum_{v \in F} b(v) + \sum_{(v,u) \in cut(F,B)} p(u,v).$$
## New problem

>[!definition] Image segmentation altered
>Given an undirected graph $G = (V,E)$ with weights:
>- for each $v \in V$, $f(v), b(v) \geq 0$, and
>- for each $e \in E$, $p(e) \geq 0$.
>We we find [cut](cut_(graph).md) $V = F \cup B$ that minimises
>$$w'(F,B) = \sum_{u \in B} f(u) + \sum_{v \in F} b(v) + \sum_{(v,u) \in cut(F,B)} p(u,v).$$

## Making a flow network

Define directed graph $G' = (V', E')$ where $V' = V \cup \{s,t\}$ and
$$E' = \{ (u,v), (v,u), (s,x), (x,t) \vert (u,v) \in E, x \in V \}.$$
Where we define capacity
$$c(u,v) = \begin{cases} p(u,v) & \mbox{if } (u,v) \in E\\ f(v) & \mbox{if } u = s\\ b(u) & \mbox{if } v = t\\ \end{cases}.$$
To give [flow network](flow_network.md) $(G', c, s, t)$.

Note a [min st-cut](min_st-cut_problem.md) of this graph relates to a solution to the altered problem.  The solution is some cut $(F \cup \{s\}, B \cup \{t\})$ with minimum capacity:
$$\begin{aligned} capacity(F \cup \{s\}, B \cup \{t\}) & = \sum_{\substack{(v,w) \in E'\\ v \in F \cup \{s\}, w \in B \cup \{t\}}} c(v,w)\\
& = \sum_{u \in B} c(s, u) + \sum_{v \in F} c(v,t) + \sum_{\substack{(v,w) \in E\\ v \in F, w \in B}} c(v,w)\\
& = \sum_{u \in B} f(u) + \sum_{v \in F} b(v) + \sum_{\substack{(v,w) \in E\\ v \in F, w \in B}} p(v,w)\\
& = w'(F,B).
\end{aligned}$$
# Pseudo code

```pseudocode
Image_segmentation(G,f,b,p):
	Input: Image segmentation problem defined by G, f, b, p.
	Output: Maximum value image segmentation.
1. Define flow network (G', c, s, t) as above.
2. Solve the flow network problem F U {s}, B U {t}
3. return F, b.
```

# Runtime

Defining the graph takes at most $O(\vert V \vert + \vert E \vert)$ so the algorithm is dominated by the solution to your flow network problem.
