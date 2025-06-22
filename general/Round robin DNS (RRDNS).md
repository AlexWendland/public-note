---
aliases:
  - RRDNS
  - Round robin DNS
checked: false
created: 2024-07-21
last_edited: 2024-07-21
draft: false
tags:
  - networks
type: definition
---
>[!tldr] Round robin DNS (RRDNS)
>Round Robin [[Domain Name System (DNS)|DNS]] is a technique used by large websites to manage and distribute incoming traffic across multiple servers at a single location. When a DNS request is made, RRDNS responds with a list of IP addresses (A records) for the requested domain. These addresses are rotated in sequence with each request, ensuring that no single server is overloaded with too many requests.
>
>The DNS client, which receives this list, can select an IP address based on various strategies, such as always choosing the first address or selecting the one closest in terms of network proximity. Each IP address in the list has a Time to Live (TTL), which dictates how long the address remains valid. If a DNS lookup is repeated before the TTL expires, the client receives the same list of IPs but in a different order, further balancing the traffic across servers.

