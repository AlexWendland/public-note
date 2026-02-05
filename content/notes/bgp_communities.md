---
aliases:
created: 2024-07-21
date_checked:
draft: false
last_edited: 2026-02-05
tags:
  - networks
title: BGP Communities
type: definition
---
>[!definition] BGP Communities
>A **BGP (Border Gateway Protocol) community** is a mechanism used to group multiple routes together to simplify routing policies and facilitate route management.
>
>1. **Tagging Mechanism**: [BGP](border_gateway_protocol_(bgp).md) communities are essentially tags or labels that can be applied to routes, allowing routers to apply certain policies to all routes with a specific community tag.
>2. **Format**: They are typically represented as a 32-bit value, often written in the format `ASN:NN` ([Autonomous system number (ASN)](autonomous_system_number_(asn).md): Number) with both sides be 16-[bit](bit.md) values.
>3. **Usage**:
>    - **Policy Control**: They help in implementing routing policies such as route preference, route filtering, and traffic engineering.
>    - **Route Management**: Simplify the management of routing information by allowing bulk changes to be made to routes that share the same community tag.
>    - **DDoS Mitigation**: Specific community values, like those used in BGP blackholing (e.g., `ASN:666`), can be used to signal special actions such as dropping traffic to mitigate [DDoS](distributed_denial-of-service_(ddos).md) attacks.
>4. **Propagation**: Communities are transitive, meaning they can be passed along to other routers within the same [AS](autonomous_system_(as).md) or to other ASes, depending on the routing policies configured.
>5. **Flexibility**: Operators can define custom community values to meet their specific needs, making BGP communities a versatile tool in network management.
>In summary, BGP communities are a powerful and flexible tool for managing routing policies and enhancing the control over how routes are handled and propagated across networks.

