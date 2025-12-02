---
aliases:
  - ARP
checked: false
created: 2024-05-21
draft: false
last_edited: 2024-05-21
title: Address Resolution Protocol (ARP)
tags:
  - networks
type: definition
---
>[!tldr] Address Resolution Protocol (ARP)
> This [protocol](protocol_(networks).md) is used to update a [nodes](node_(ipv6).md) [ARP cache](arp_cache.md) within a [network](network.md). When this node needs to send [packet](packets.md) to a address within its network (as identified by the [network mask](network_mask.md)) but that entry is missing from the [ARP cache](arp_cache.md) it does the following.
> - It [broadcasts](broadcast_(networks).md) a [frame](frame_(networks).md) with its [IP address](internet_protocol_(ip).md) and [MAC address](mac_address.md) as the source and the [IP address](internet_protocol_(ip).md) and the [all f's address](broadcast_(networks).md) as the destination.
> - All hosts on the network receive this [frame](frame_(networks).md).
> 	- Hosts that don't have a matching [IP address](internet_protocol_(ip).md) throw this frame away.
> 	- The host that matches this [IP address](internet_protocol_(ip).md) first updates its [ARP cache](arp_cache.md) if it does not have the senders [MAC address](mac_address.md) then responds with a [unicast](unicast.md) message.
> - In receipt of this message the original [node](node_(ipv6).md) can now update its [ARP cache](arp_cache.md) and then complete sending its message.
>
> If no host responds to the ARP message - the original message is dropped.
