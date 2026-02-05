---
aliases:
  - residual network
created: 2023-10-02
date_checked:
draft: false
last_edited: 2026-02-05
tags:
  - maths
title: Residual Network (flow)
type: definition
---
>[!definition] Residual Network
>Let $(G, c, s, t)$ be a [flow network](flow_network.md) and $f$ be a [flow](flow.md). Further assume $G$ has no dual edges. Define the $G^f = (V,E^f)$ where
>$$E^f = \{(v,w) \in E \vert f(v,w) < c(v,w)\} \cup \{(w,v) \vert (v,w) \in E, f(v,w) > 0\}$$
>and capacity
>$$c^f(v,w) = \begin{cases} c(v,w) - f(v,w) & \mbox{if } (v,w) \in E \mbox{ and } f(v,w) < c(v,w)\\ f(w,v) & \mbox{if } (w,v) \in E \mbox{ and } f(w,v) > 0 \end{cases}.$$
>The let the *residual flow network* be $(G^f, c^f, s, t)$.

