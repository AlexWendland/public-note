---
aliases:
checked: false
created: 2024-05-27
draft: false
last_edited: 2024-05-27
tags:
  - networks
title: Reliable transmission of TCP messages
type: explainer
---
# Reliable transmission of [TCP](transmission_control_protocol_(tcp).md) messages

[TCP](transmission_control_protocol_(tcp).md) uses sequence numbers with acknowledgements to increase the reliability of messages. If a message was corrupted or not received it will resend that [segment](segment.md).

[Automatic Repeat Request (ARQ)](automatic_repeat_request_(arq).md)

The most basic implementation of [ARQ](automatic_repeat_request_(arq).md) stops and waits to check if the message was received.

[Stop and wait ARQ](stop_and_wait_arq.md)

In [TCP](transmission_control_protocol_(tcp).md) the acknowledgement header is set to be the next sequence number the receiver is waiting to get. There are different ways you can handle unacknowledged messages.

[Go back N](go_back_n.md)

[Fast retransmit](fast_retransmit.md)

