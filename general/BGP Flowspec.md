---
aliases: 
checked: false
created: 2024-07-21
last_edited: 2024-07-21
draft: false
tags:
  - networks
  - security
type: definition
---
>[!tldr] BGP Flowspec
>[[Boarder gateway protocol (BGP)|BGP]] Flowspec is an extension of [[Boarder gateway protocol (BGP)|BGP]] designed to allow the creation and propagation of detailed traffic flow filtering rules. These rules can be applied across different [[Autonomous system (AS)|ASs]].
>
>The following table shows the available components to select a flow:
>![[bcg_flowspec.png]]
>After you have specified a particular flow you can select an action associated to it such as traffic-rate, redirect or drop. This will be implemented at the boarder router.
>
>This has the following advantages:
>1. **Fine-Grained Control**: Flowspec allows for detailed and specific traffi management rules.
>2. **Centralized Management**: Leveraging the BGP control plane, it enables easy and simultaneous updates to all routers in a network.
>3. **Effective Mitigation**: It is particularly effective in mitigating DDoS attacks within a single network or AS.
>
> Though comes with some downsides:
>1. **Inter-Domain Deployment**: Flowspec's effectiveness diminishes when rules need to be applied across multiple AS, especially if these AS belong to competing networks. Trust and cooperation are crucial but often lacking.
>2. **Scalability Issues**: For large-scale attacks originating from many sources, creating numerous rules or aggregating sources into a single prefix can be challenging and inefficient.
>
>Practically due to the need for trust this is only deployed within a [[Autonomous system (AS)|AS]] and is not used more broadly.

