---
aliases:
  - BGP
  - BGPs
  - iBGP
  - eBGP
checked: false
created: 2024-06-08
last_edited: 2024-06-08
draft: false
tags:
  - networks
type: definition
---
>[!tldr] Boarder gateway protocol (BGP)
>This is a class of [[Protocol (networks)|protocols]] that are used for [[Interdomain routing|interdomain routing]]. That is sharing subnets between [[Autonomous system (AS)|AS]]. Two [[Router|routers]] connected over [[Boarder gateway protocol (BGP)|BGP]] are called BGP peers. They open a semi-permanent [[Transmission Control Protocol (TCP)|TCP]] connection where they exchange routes. There are two varieties of this class.
>- **iBGP**: For internal to the [[Autonomous system (AS)|AS]] communication between boarder routers. 
>- **eBGP**: For two routers who are in different [[Autonomous system (AS)|AS]].
>The difference between iBGP and [[Interior gateway protocol (IGP)|IGP]] is that iBGP is communicating about what external subnets are available from that router wheres [[Interior gateway protocol (IGP)|IGP]] is communicating about what internal subnets there are.

