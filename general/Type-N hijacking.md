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
>[!tldr] Type-N hijacking
>This is a form of [[BGP Hijacking]] where the attacking [[Autonomous system (AS)|AS]] announces an illegitimate path for a prefix that it does not own to create a fake route between different [[Autonomous system (AS)|AS's]]. 
>For example, {_AS2, ASx, ASy, AS1 – 10.0.0.0/23_} denotes a fake path between AS2 and AS1, where there is no link between AS2 and ASx. The N denotes the position of the rightmost fake link in the illegitimate announcement, e.g. {_AS2, ASx, ASy, AS1 – 10.0.0.0/23_} is a Type-2 hijacking.

