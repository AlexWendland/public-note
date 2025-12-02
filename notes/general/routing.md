---
aliases:
  - routing
checked: false
created: 2024-05-21
draft: false
last_edited: 2024-05-21
title: Routing
tags:
  - networks
type: definition
---
>[!tldr] Routing
>The process of routing is getting a [packet](packets.md) the network associated to its [IP address](internet_protocol_(ip).md). To do this all routers store a [routing table](routing_table.md) which maps the tuple of an IP address and a [network mask](network_mask.md) to either a interface or a IP address.
>
>There are two types of routing [Intradomain routing](intradomain_routing.md), how routers exchange information within the same [Autonomous system (AS)](autonomous_system_(as).md), and [interdomain routing](interdomain_routing.md) how routes get shared between [Autonomous system (AS)](autonomous_system_(as).md).
>
>There are 3 ways a router can populate its routing table
>1. Directly connected: This is for networks directly connected to the router. It adds an entry for that networks and the interface of the [router](router.md) it is connected to.
>2. Static route: This is a route that has been manually configured on a router. Instead of an interface it will have an IP address to forward that packet on to.
>3. Dynamic routing: This is the same in structure to the static rout but instead of being manually added this gets populated by routers sharing known addresses with one another.
>
>This table might grow very large but routers use [route summarization](route_summarization.md) to keep the tables shorter.
>
>Once a router has been configured when it receives a [packet](packets.md) it looks at its [layer 3](layer_3_network.md) header containing the destination IP address. It compares that again the known address, using the [network mask](network_mask.md) and finds the most precise match (matching on the longest [network mask](network_mask.md)) then forwards it to that interface or IP address.

