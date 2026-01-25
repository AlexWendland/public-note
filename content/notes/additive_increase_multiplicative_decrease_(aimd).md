---
aliases:
  - AIMD
created: 2024-05-29
date_checked:
draft: false
last_edited: 2024-05-29
tags:
  - networks
title: Additive increase Multiplicative Decrease (AIMD)
type: definition
---
>[!tldr] Additive increase Multiplicative Decrease (AIMD)
>This is a method of probe-and-adjust that some [TCP](transmission_control_protocol_(tcp).md) implementations use.
>-  Every [RTT](round_trip_time_(rtt).md) it wants to increase the window size by 1.
>- If there is congestion on the network it halves the window size.
>
>As the window size is really in [bytes](byte.md) rather than packets and we would like incremental progress rather than waiting for a full [RTT](round_trip_time_(rtt).md). We increment the window size using the maximum segment size (MSS) proportionally to the current CongestionWindow size on every acknowledged packet using the formula:
>$$ CongestionWindow += MSS \times (MSS/CongestionWindow).$$

