---
aliases: 
checked: false
created: 2024-07-23
last_edited: 2024-07-23
draft: false
tags:
  - networks
  - security
type: definition
---
>[!tldr] Angur
>This is a system that monitors for censorship through connectivity disruptions. It uses two internet protocols:
>
>1. **IP ID**: This uses the [[Internet Protocol (IPv4)|IPv4]] field for the packet ID. Which is a 16-[[Bit|bit]] field used to identify packets that are fragmented. (There is an analogous [[Internet Protocol (IPv6)|IPv6]] field on the fragmentation extension header - though in this protocol you should not fragment [[Packets|packets]].) Normally servers keep a count of the packets they have sent and increment the IP ID by one for each subsequent packet.
>2. **TCP RST**: When an unexpected [[Transmission Control Protocol (TCP)|TCP]] such as a [[Transmission Control Protocol (TCP)|TCP]] SYN-ACK packet without a previous SYN is sent to a host, it sends back a reset packet. (This makes some assumptions about complex behaviours not happening.)
>
>The system aims to detect if filtering exists between two hosts, *a reflector* and *a site*. A reflector is a host which maintains a global IP ID. A site is a host that may be potentially blocked. To identify if filtering exists, it makes use of a third machine called the *measurement machine*.
>
>There are two techniques it will then use:
>
>- **Probing**: The measurement machine send a SYN-ACK message to the reflector and records the IP ID of the RST message it sends back.
>- **Pertubation**: The measurement machine sends a [[Spoofing|spoofed]] packet to the site with the source IP being the reflector. The site will respond to the reflector with a SYN-ACK. Then the reflector will return a TCP RST to the site - incrementing its IP ID by 1.
>
>The reflectors IP ID will only increase by 1 if the communication from the site to the reflector is not censored. Therefore we have the three circumstances below happening.
>
>![[angur_no_blocking.png]]
>
>![[angur_inbound_blocking.png]]
>
>![[angur_outbound_blocking.png]]
>This last picture relies on the server trying to resend the SYN-ACK when it got no ACK back from the reflector. This will increment the IPID again by two on a third probe.

