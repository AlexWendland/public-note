---
aliases:
  - link-state
created: 2024-06-02
date_checked:
draft: false
last_edited: 2026-02-05
tags:
  - networks
title: Link-state routing algorithms
type: definition
---
>[!definition] Link-state routing algorithms
>Link-state algorithms are used for [intradomain routing](intradomain_routing.md). These use knowledge of the whole network - including topology and weights - to perform [Dijkstra's algorithm](dijkstra's_algorithm.md) on the network to find the shortest path to every node. This gives us where to route [packets](packets.md) to. The computational complexity of this is $O(n^2)$ where $n$ is the size of the network.

