---
aliases: 
checked: false
created: 2024-05-27
last_edited: 2024-05-27
publish: true
tags:
  - networks
type: explainer
---
# Transmission control in [[Transmission Control Protocol (TCP)|TCP]]

There are two main components of transmission control. These tackle two distinct problems that a connection may have:
- [[Flow control in TCP]]: Allows the receiver to control how much data gets sent to it in one go, and
- [[Congestion control in TCP]]: Allows probing of the network to guarantee maximum network utilisation without disruption to service.

These both ultimately effect the number of unacknowledged messages allowed to be sent in [[Automatic Repeat Request (ARQ)|ARQ]]. This will be the minimum of the two window sizes provided by the above controls.

[[User Datagram Protocol (UDP)|UDP]] lets the [[Layer 7 Application|Application layer]] hand transmission control. Whereas [[Transmission Control Protocol (TCP)|TCP]] sees this a a widely shared feature that it can abstract away.