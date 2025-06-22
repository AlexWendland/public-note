---
aliases: 
checked: false
created: 2024-05-27
last_edited: 2024-05-27
draft: false
tags:
  - networks
type: explainer
---
# Reliable transmission of [[Transmission Control Protocol (TCP)|TCP]] messages

[[Transmission Control Protocol (TCP)|TCP]] uses sequence numbers with acknowledgements to increase the reliability of messages. If a message was corrupted or not received it will resend that [[Segment|segment]]. 

![[Automatic Repeat Request (ARQ)]]

The most basic implementation of [[Automatic Repeat Request (ARQ)|ARQ]] stops and waits to check if the message was received.

![[Stop and wait ARQ]]

In [[Transmission Control Protocol (TCP)|TCP]] the acknowledgement header is set to be the next sequence number the receiver is waiting to get. There are different ways you can handle unacknowledged messages.

![[Go back N]]

![[Fast retransmit]]

