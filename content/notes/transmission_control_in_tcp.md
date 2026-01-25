---
aliases:
created: 2024-05-27
date_checked:
draft: false
last_edited: 2024-05-27
tags:
  - networks
title: Transmission control in TCP
type: explainer
---
# Transmission control in [TCP](transmission_control_protocol_(tcp).md)

There are two main components of transmission control. These tackle two distinct problems that a connection may have:
- [Flow control in TCP](flow_control_in_tcp.md): Allows the receiver to control how much data gets sent to it in one go, and
- [Congestion control in TCP](congestion_control_in_tcp.md): Allows probing of the network to guarantee maximum network utilisation without disruption to service.

These both ultimately effect the number of unacknowledged messages allowed to be sent in [ARQ](automatic_repeat_request_(arq).md). This will be the minimum of the two window sizes provided by the above controls.

[UDP](user_datagram_protocol_(udp).md) lets the [Application layer](layer_7_application.md) hand transmission control. Whereas [TCP](transmission_control_protocol_(tcp).md) sees this a a widely shared feature that it can abstract away.



