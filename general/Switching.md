---
aliases:
  - switching
checked: false
created: 2024-05-21
last_edited: 2024-05-21
draft: false
tags:
  - networks
type: definition
---
>[!tldr] Switching
> This is the process of moving data within a network. A switch has devices connected on different ports. The switches main job is to keep a table of which [[MAC address]] is connecting through which [[Port|port]] (this is a many to one relationship as there could be other switches in the network). 
> This is a [[Layer 2 Data Link|layer 2]] process so just works on the level of [[MAC address|MAC addresses]]. There are 3 operations involved in switching that will involve looking at the [[Layer 2 Data Link|layer 2]] header.
>- Learn: when a new [[Frame (networks)|frame]] arrives on a port with a previously unknown [[MAC address]] as it source it updates its table,
>- Flood: when a new [[Frame (networks)|frame]] arrives with a previously unknow [[MAC address]] as its destination it duplicates this frame and posts it on all other ports of the switch, and
>- Forward: when a new frame arrives with a know MAC address as its destination it sends it along to the port associated to that address. 