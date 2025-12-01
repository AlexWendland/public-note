---
aliases:
  - link-state
checked: false
created: 2024-06-02
draft: false
last_edited: 2024-06-02
tags:
  - networks
type: definition
---
>[!tldr] Link-state routing algorithms
>Link-state algorithms are used for [[Intradomain routing|intradomain routing]]. These use knowledge of the whole network - including topology and weights - to perform [[Dijkstra's algorithm]] on the network to find the shortest path to every node. This gives us where to route [[Packets|packets]] to. The computational complexity of this is $O(n^2)$ where $n$ is the size of the network.

