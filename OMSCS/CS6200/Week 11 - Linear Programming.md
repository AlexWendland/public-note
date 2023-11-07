---
aliases: 
type: lecture
publish: false
created: 2023-11-07
last_edited: 2023-11-07
tags:
  - OMSCS
course: "[[CS6200 Introduction to Graduate Algorithms]]"
week: 
chatgpt: false
---
# Week 11 - Linear Programming

In broad terms a [[Linear programme|linear programme]] is an optimisation problem of a [[Linear function|linear]] function where there are [[Linear function|linear]] bounds on the variables.

>[!example] [[Max flow problem]]
>We are given a [[Directed graph|directed graph]] $G = (V,E)$ with capacities $c: E \rightarrow \mathbb{R}_{>0}$ and source $s \in V$ and sink $t \in V$.
>
>To define the [[Linear programme|linear programme]] make $\vert E \vert$ variables $f_e$ for each $e \in E$. These will represent the flow along these edges. Then we want to maximise the [[Flow|flow]] defined by the flow out of $s$
>$$ \max \sum_{(s,v) \in E} f_{(s,v)}.$$
>However, the edges must flow abiding by the capacity constraints
>$$0 \leq f_{e} \leq c(e) \mbox{ for } e \in E.$$
>As well as abide by the preservation of flow
>$$ \sum_{(u,v) \in E} f_{(u,v)} - \sum_{(v,w) \in E} f_{(v,w)} = 0 \mbox{ for } v \in V \backslash \{s,t\}.$$
>This defines our [[Linear programme|linear programme]] and the solution to this provides a solution to the [[Max flow problem|max flow]] problem. 

## Linear programme general form

![[Linear programme]]

It helps to standardise this into the following form. Note the use of [[Matrix|matrix]] notation here.

![[Linear programme standard form]]

We can convert all [[Linear programme|linear programmes]] into standard form using the following Lemma.

![[All linear programmes can be represented in standard form]]