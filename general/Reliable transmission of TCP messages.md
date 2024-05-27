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
# Reliable transmission of [[Transmission Control Protocol (TCP)|TCP]] messages

[[Transmission Control Protocol (TCP)|TCP]] uses sequence numbers with acknowledgements to increase the reliability of messages. If a message was corrupted or not received it will resend that [[Segment|segment]]. 