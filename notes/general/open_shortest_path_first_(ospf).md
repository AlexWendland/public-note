---
aliases:
  - OSPF
  - LSA
checked: false
created: 2024-06-08
draft: false
last_edited: 2024-06-08
name: Open Shortest Path First (OSPF)
tags:
  - networks
type: definition
---
>[!tldr] Open Shortest Path First (OSPF)
>The OSPF [protocol](protocol_(networks).md) is a [intradomain routing](intradomain_routing.md) algorithm suggested as an improvement on [RIP](routing_information_protocol_(rip).md) for [ISP](internet_service_provider_(isp).md). This is a [link-state](link-state_routing_algorithms.md) algorithm that uses hierarchy to do [route summarization](route_summarization.md). It operates over one [autonomous system](autonomous_system_(as).md).
>
>In OSPF a single router is selected as the *backbone router* this is where all [AS](autonomous_system_(as).md) externally facing [routers](router.md) connect to.
>
>Routers withing the [AS](autonomous_system_(as).md) broadcast Link state advertisements (LSA) which include that routers neighbours. This is circulated to the whole network and is repeated at a set interval (normally 30 minutes). Then every router using itself as the root uses [Dijkstra's algorithm](dijkstra's_algorithm.md) to find the shortest path between itself and every other subnet.

