---
aliases:
  - NAT boxes
  - NAT
checked: false
created: 2024-05-23
draft: false
last_edited: 2024-05-23
name: Network Address Translation (NAT)
tags:
  - networks
type: definition
---
>[!tldr] Network Address Translation (NAT)
>A Network Address Translation boxs are used to solve the issue of limited [IP addresses](internet_protocol_(ipv4).md) on the public [Internet](internet.md). They present a single public [Internet Protocol (IPv4)](internet_protocol_(ipv4).md) and remap internal [IP addresses](internet_protocol_(ipv4).md) and [ports](port.md) to that [Internet Protocol (IPv4)](internet_protocol_(ipv4).md) and allocate it a [port](port.md). To do this these boxes maintain a mapping table.
>This violates the [End to end principle](end_to_end_principle.md) as a host that [packets](packets.md) pass through has to change the [layer 3](layer_3_network.md) and [layer 4](layer_4_transport.md) header before it has arrived at the host.
