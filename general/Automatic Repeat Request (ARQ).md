---
aliases:
  - ARQ
checked: false
created: 2024-05-27
last_edited: 2024-05-27
publish: true
tags:
  - networks
type: definition
---
>[!tldr] Automatic Repeat Request (ARQ)
>This is the way [[Transmission Control Protocol (TCP)|TCP]] makes messaging reliable. This uses a combination message acknowledgements and message timeouts to determine if it needs to resend a [[Segment|segment]]. The timeout is a length of time before it reseeds the message. This will need to be fine tuned by guessing the [[Round trip time (RTT)]].