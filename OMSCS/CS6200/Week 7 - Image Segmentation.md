---
aliases: 
type: lecture
publish: true
created: 2023-10-04
last_edited: 2023-10-04
tags:
  - OMSCS
course: "[[CS6200 Introduction to Graduate Algorithms]]"
week: 7
chatgpt: false
---
# Week 7 - Image Segmentation

![[Image Segmentation#Statement]]

## Formulation

Suppose we have picture $P$ which is a grid of different pixels. Define a [[Graph|undirected graph]] $G = (V, E)$ where $V$ is the set of pixels and $E$ is neighbouring pixels. Suppose in addition we are provided:

- $f(v)$ is the likelihood $v \in V$ is in the foreground (assume $f(v) \geq 0$),
- $b(v)$ is the likelihood $v \in V$ is in the background (assume $b(v) \geq 0$), and
- $p(u,v)$ is the separation penalty for separating $u,v \in V$ for $(u,v) \in E$ (assume $p(u,v) \geq 0$).

Then for any [[Cut (graph)|cut]] of $V$ into $V = F \cup B$, foreground and background, we define a weight:
$$w(F,B) = \sum_{v \in F} f(v) + \sum_{u \in B} b(u) - \sum_{(v,u) \in cut(F,B)} p(u,v).$$
The goal is to find the [[Cut (graph)|cut]] of $V$ with maximum weight.


