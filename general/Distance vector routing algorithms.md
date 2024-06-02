---
aliases:
  - DV
checked: false
created: 2024-06-02
last_edited: 2024-06-02
publish: true
tags:
  - networks
type: definition
---
>[!tldr] Distance vector routing algorithms
>Distance vector routing is a distributed [[Routing|routing]] algorithm. It uses the [[Bellman-Ford algorithm]] but in a distributed manner. 
>
>For this was assume all [[Router|routers]] know the routers they are directly connected to - within a [[Network|network]] they have an interface to. They also know the network cost of communicating with their neighbours. 
>
>Each [[Router|router]] maintains a table with all routers within their [[Autonomous system (AS)|AS]] to each they associate, that routers best guess at the distance to the router, and which neighbour router they need to send any [[Packets|packets]] to to achieve that best guess.
>
>Then all the routers broadcast this information to its neighbours and use their neighbours broadcasts to update their own tables. They update their tables using the [[Bellman-Ford algorithm|Bellman-Ford equation]]. This has the pseudocode as below.

## Pseudocode

Let us have a network $

```pseudocode


Initalisation

```

