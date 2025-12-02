---
aliases:
checked: false
created: 2024-07-23
draft: false
last_edited: 2024-07-23
tags:
  - networks
  - security
title: Angur
type: definition
---
>[!tldr] Angur
>This is a system that monitors for censorship through connectivity disruptions. It uses two internet protocols:
>
>1. **IP ID**: This uses the [IPv4](internet_protocol_(ipv4).md) field for the packet ID. Which is a 16-[bit](bit.md) field used to identify packets that are fragmented. (There is an analogous [IPv6](internet_protocol_(ipv6).md) field on the fragmentation extension header - though in this protocol you should not fragment [packets](packets.md).) Normally servers keep a count of the packets they have sent and increment the IP ID by one for each subsequent packet.
>2. **TCP RST**: When an unexpected [TCP](transmission_control_protocol_(tcp).md) such as a [TCP](transmission_control_protocol_(tcp).md) SYN-ACK packet without a previous SYN is sent to a host, it sends back a reset packet. (This makes some assumptions about complex behaviours not happening.)
>
>The system aims to detect if filtering exists between two hosts, *a reflector* and *a site*. A reflector is a host which maintains a global IP ID. A site is a host that may be potentially blocked. To identify if filtering exists, it makes use of a third machine called the *measurement machine*.
>
>There are two techniques it will then use:
>
>- **Probing**: The measurement machine send a SYN-ACK message to the reflector and records the IP ID of the RST message it sends back.
>- **Pertubation**: The measurement machine sends a [spoofed](spoofing.md) packet to the site with the source IP being the reflector. The site will respond to the reflector with a SYN-ACK. Then the reflector will return a TCP RST to the site - incrementing its IP ID by 1.
>
>The reflectors IP ID will only increase by 1 if the communication from the site to the reflector is not censored. Therefore we have the three circumstances below happening.
>
>![Angur No Blocking](../../static/images/angur_no_blocking.png)
>
>![Angur Inbound Blocking](../../static/images/angur_inbound_blocking.png)
>
>![Angur Outbound Blocking](../../static/images/angur_outbound_blocking.png)
>This last picture relies on the server trying to resend the SYN-ACK when it got no ACK back from the reflector. This will increment the IPID again by two on a third probe.

