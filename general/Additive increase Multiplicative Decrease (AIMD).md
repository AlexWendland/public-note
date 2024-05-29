---
aliases:
  - AIMD
checked: false
created: 2024-05-29
last_edited: 2024-05-29
publish: true
tags:
  - networks
type: definition
---
>[!tldr] Additive increase Multiplicative Decrease (AIMD)
>This is a method of probe-and-adjust that some [[Transmission Control Protocol (TCP)|TCP]] implementations use.
>-  Every [[Round trip time (RTT)|RTT]] it wants to increase the window size by 1.
>- If there is congestion on the network it halves the window size.
>
>As the window size is really in [[Byte|bytes]] rather than packets and we would like incremental progress rather than waiting for a full [[Round trip time (RTT)|RTT]]. We increment the window size using the maximum segment size (MSS) proportionally to the current CongestionWindow size on every acknowledged packet using the formula:
>$$ CongestionWindow += MSS \times (MSS/CongestionWindow).$$

