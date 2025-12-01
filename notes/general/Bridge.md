---
aliases:
  - bridge
  - bridges
checked: false
created: 2024-05-21
draft: false
last_edited: 2024-05-21
tags:
  - networks
type: definition
---
>[!tldr] Bridge
>A bridge only has two [[Port|ports]] but they know which devices are on either side. They will only repeat signals if the destination host is on the opposite side of the bridge.
>To do this a bridge maintains a forwarding table which maps [[MAC address|MAC addresses]] to [[Port|ports]]. It learns which hosts are on either side by reading the source [[MAC address]] of [[Frame (networks)|frames]] coming into the bridge.

