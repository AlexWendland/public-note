---
aliases:
  - ARP
checked: false
created: 2024-05-21
last_edited: 2024-05-21
publish: true
tags:
  - networks
type: definition
---
>[!tldr] Address Resolution Protocol (ARP)
> This [[Protocol (networks)|protocol]] is used to update a [[Node (IPv6)|nodes]] [[ARP cache]] within a [[Network|network]]. When this node needs to send [[Packets|packet]] to a address within its network (as identified by the [[Network mask|network mask]]) but that entry is missing from the [[ARP cache]] it does the following.
> - It [[Broadcast (networks)|broadcasts]] a [[Frame (networks)|frame]] with its [[IP address]] and [[MAC address]] as the source and the [[IP address]] and the [[Broadcast (networks)|all f's address]] as the destination.
> - All hosts on the network receive this [[Frame (networks)|frame]].
> 	- Hosts that don't have a matching [[IP address]] throw this frame away.
> 	- The host that matches this [[IP address]] first updates its [[ARP cache]] if it does not have the senders [[MAC address]] then responds with a [[Unicast|unicast]] message.
> - In receipt of this message the original [[Node (IPv6)|node]] can now update its [[ARP cache]] and then complete sending its message.
>
> If no host responds to the ARP message - the original message is dropped.
