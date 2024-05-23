---
aliases:
  - NAT boxes
  - NAT
checked: false
created: 2024-05-23
last_edited: 2024-05-23
publish: true
tags:
  - networks
type: definition
---
>[!tldr] Network Address Translation (NAT)
>A Network Address Translation boxs are used to solve the issue of limited [[IP address|IP addresses]] on the public [[Internet]]. They present a single public [[IP address]] and remap internal [[IP address|IP addresses]] and [[Port|ports]] to that [[IP address]] and allocate it a [[Port|port]]. To do this these boxes maintain a mapping table.
>This violates the [[End to end principle]] as a host that [[Packets|packets]] pass through has to change the [[Layer 3 Network|layer 3]] and [[Layer 4 Transport|layer 4]] header before it has arrived at the host.
