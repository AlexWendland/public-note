---
aliases:
  - routing
created: 2024-05-21
date_checked: 2026-02-05
draft: false
last_edited: 2026-02-05
tags:
  - networks
title: Routing
type: definition
---
> [!definition] Routing
> The process of routing is delivering a [packet](packets.md) to the network associated with its [IP address](internet_protocol_(ip).md). To do this all routers store a [routing table](routing_table.md) which maps the tuple of an IP address and a [network mask](network_mask.md) to either an interface or an IP address.
>
> There are two types of routing: [intradomain routing](intradomain_routing.md), how routers exchange information within the same [Autonomous System (AS)](autonomous_system_(as).md), and [interdomain routing](interdomain_routing.md), how routes get shared between [Autonomous System (AS)](autonomous_system_(as).md).
>
> There are three ways a router can populate its routing table:
> 1. Directly connected: This is for networks directly connected to the router. It adds an entry for that network and the interface of the [router](router.md) it is connected to.
> 2. Static route: This is a route that has been manually configured on a router. Instead of an interface it will have an IP address to forward that packet on to.
> 3. Dynamic routing: This is the same in structure as the static route but instead of being manually added this gets populated by routers sharing known addresses with one another.
>
> This table might grow very large but routers use [route summarization](route_summarization.md) to keep the tables shorter.
>
> Once a router has been configured, when it receives a [packet](packets.md) it looks at its [layer 3](layer_3_network.md) header containing the destination IP address. It compares that against the known addresses, using the [network mask](network_mask.md) and finds the most precise match (matching on the longest [network mask](network_mask.md)) then forwards it to that interface or IP address.

