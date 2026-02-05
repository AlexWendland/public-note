---
aliases:
  - ARQ
created: 2024-05-27
date_checked:
draft: false
last_edited: 2026-02-05
tags:
  - networks
title: Automatic Repeat Request (ARQ)
type: definition
---
>[!definition] Automatic Repeat Request (ARQ)
>This is the way [TCP](transmission_control_protocol_(tcp).md) makes messaging reliable. This uses a combination message acknowledgements and message timeouts to determine if it needs to resend a [segment](segment.md). The timeout is a length of time before it reseeds the message. This will need to be fine tuned by guessing the [Round trip time (RTT)](round_trip_time_(rtt).md).
