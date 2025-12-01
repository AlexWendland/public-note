---
aliases:
  - RIP
checked: false
created: 2024-06-04
draft: false
last_edited: 2024-06-04
tags:
  - networks
type: definition
---
>[!tldr] Routing Information Protocol (RIP)
>This is one of the first [[Protocol (networks)|protocols]] that implemented [[Distance vector routing algorithms]]. For the distance metric it just used the number of different routers it would have to go through.
>The messages each router sends are the routing table with each [[Subnets|subnet]], the next router it would go through and the distance to that network in terms of "hops". This table is refereed to as the RIP table. Later iterations of RIP use address aggregation.
>To maintain connection with their neighbours they use a [[User Datagram Protocol (UDP)|UDP]] message on [[Port|port]] 520 if they don't hear from neighbours every 180 seconds they will assume they are no longer available and change the RIP table then broadcast it to its neighbours.
>This algorithms has challenges with updating routes and the time that takes to converge due to the [[Count to infinity problem|count to infinity problem]].

