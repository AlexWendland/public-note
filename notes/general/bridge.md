---
aliases:
  - bridge
  - bridges
checked: false
created: 2024-05-21
draft: false
last_edited: 2024-05-21
title: Bridge
tags:
  - networks
type: definition
---
>[!tldr] Bridge
>A bridge only has two [ports](port.md) but they know which devices are on either side. They will only repeat signals if the destination host is on the opposite side of the bridge.
>To do this a bridge maintains a forwarding table which maps [MAC addresses](mac_address.md) to [ports](port.md). It learns which hosts are on either side by reading the source [MAC address](mac_address.md) of [frames](frame_(networks).md) coming into the bridge.

