---
aliases:
  - switching
created: 2024-05-21
date_checked:
draft: false
last_edited: 2026-02-05
tags:
  - networks
title: Switching
type: definition
---
>[!definition] Switching
> This is the process of moving data within a network. A switch has devices connected on different ports. The switches main job is to keep a table of which [MAC address](mac_address.md) is connecting through which [port](port.md) (this is a many to one relationship as there could be other switches in the network).
> This is a [layer 2](layer_2_data_link.md) process so just works on the level of [MAC addresses](mac_address.md). There are 3 operations involved in switching that will involve looking at the [layer 2](layer_2_data_link.md) header.
>- Learn: when a new [frame](frame_(networks).md) arrives on a port with a previously unknown [MAC address](mac_address.md) as it source it updates its table,
>- Flood: when a new [frame](frame_(networks).md) arrives with a previously unknow [MAC address](mac_address.md) as its destination it duplicates this frame and posts it on all other ports of the switch, and
>- Forward: when a new frame arrives with a know MAC address as its destination it sends it along to the port associated to that address.
