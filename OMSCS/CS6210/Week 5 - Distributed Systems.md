---
aliases:
checked: false
course: "[[CS6210 Advanced Operating Systems]]"
created: 2025-10-01
last_edited: 2025-10-01
draft: true
tags:
  - OMSCS
type: lecture
week: 5
---

# Week 5 - Distributed Systems

The definition of what a distributed system is varies but in this course we use the following 3 properties:

1. Nodes on the network are connected via some LAN or WAN.
2. Nodes do not share memory.
3. The computational event time is significantly smaller than the communication time.

Definition 3 is used a fair bit and within this you can consider a cluster of machines even within the same rack in a data center - distributed computing.

> [!note] Parallel vs Distributed
> The concerns of parallel and distributed computing can overlap, however the main difference is that in parallel computing, the nodes share memory and are tightly coupled. In distributed computing, the nodes do not share memory and are loosely coupled.
