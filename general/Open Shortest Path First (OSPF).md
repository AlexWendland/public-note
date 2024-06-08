---
aliases:
  - OSPF
  - LSA
checked: false
created: 2024-06-08
last_edited: 2024-06-08
publish: true
tags:
  - networks
type: definition
---
>[!tldr] Open Shortest Path First (OSPF)
>The OSPF [[Protocol (networks)|protocol]] is a [[Intradomain routing|intradomain routing]] algorithm suggested as an improvement on [[Routing Information Protocol (RIP)|RIP]] for [[Internet Service Provider (ISP)|ISP]]. This is a [[Link-state routing algorithms|link-state]] algorithm that uses hierarchy to do [[Route summarization|route summarization]]. It operates over one [[Autonomous system (AS)|autonomous system]].
>
>In OSPF a single router is selected as the *backbone router* this is where all [[Autonomous system (AS)|AS]] externally facing [[Router|routers]] connect to. 
>
>Routers withing the [[Autonomous system (AS)|AS]] broadcast Link state advertisements (LSA) which include that routers neighbours. This is circulated to the whole network and is repeated at a set interval (normally 30 minutes). Then every router using itself as the root uses [[Dijkstra's algorithm]] to find the shortest path between itself and every other subnet. 

