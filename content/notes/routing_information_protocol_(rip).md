---
aliases:
  - RIP
created: 2024-06-04
date_checked:
draft: false
last_edited: 2024-06-04
tags:
  - networks
title: Routing Information Protocol (RIP)
type: definition
---
>[!tldr] Routing Information Protocol (RIP)
>This is one of the first [protocols](protocol_(networks).md) that implemented [Distance vector routing algorithms](distance_vector_routing_algorithms.md). For the distance metric it just used the number of different routers it would have to go through.
>The messages each router sends are the routing table with each [subnet](subnets.md), the next router it would go through and the distance to that network in terms of "hops". This table is refereed to as the RIP table. Later iterations of RIP use address aggregation.
>To maintain connection with their neighbours they use a [UDP](user_datagram_protocol_(udp).md) message on [port](port.md) 520 if they don't hear from neighbours every 180 seconds they will assume they are no longer available and change the RIP table then broadcast it to its neighbours.
>This algorithms has challenges with updating routes and the time that takes to converge due to the [count to infinity problem](count_to_infinity_problem.md).

