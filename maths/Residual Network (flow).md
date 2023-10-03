---
aliases:
  - residual network
type: defintion
publish: true
created: 2023-10-02
last_edited: 2023-10-02
tags:
  - maths
chatgpt: false
---
>[!tldr] Residual Network
>Let $(G, c, s, t)$ be a [[Flow network|flow network]] and $f$ be a [[Flow|flow]]. Further assume $G$ has no dual edges. Define the $G^f = (V,E^f)$ where
>$$E^f = \{(v,w) \in E \vert f(v,w) < c(v,w)\} \cup \{(w,v) \vert (v,w) \in E, f(v,w) > 0\}$$
>and capacity
>$$c^f(v,w) = \begin{cases} c(v,w) - f(v,w) & \mbox{if } (v,w) \in E \mbox{ and } f(v,w) < c(v,w)\\ f(w,v) & \mbox{if } (w,v) \in E \mbox{ and } f(w,v) > 0 \end{cases}.$$
>The let the *residual flow network* be $(G^f, c^f, s, t)$.

