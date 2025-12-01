---
aliases:
checked: false
created: 2024-07-27
draft: false
last_edited: 2024-07-27
tags:
  - networks
type: definition
---
>[!tldr] IP Anycast
>This is a [[Protocol (networks)|protocol]] that uses [[Hot potato routing]] in the [[Boarder gateway protocol (BGP)|BGP]]. It broadcasts the same [[Internet Protocol (IP)|IP address]] from multiple different locations and records the path that gets advertised to a given [[Autonomous system (AS)|AS]]. This is a cheap way to calculate the shortest path in terms of [[Autonomous system (AS)|AS]]-paths from a set of locations to your [[Autonomous system (AS)|AS]]. This is used in server selection within [[Content delivery network (CDN)|CDNs]].

