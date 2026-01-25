---
aliases:
  - pseudo-header
created: 2024-05-27
date_checked:
draft: false
last_edited: 2024-05-27
tags:
  - networks
title: Pseudo-header
type: definition
---
>[!tldr] Pseudo-header
>The Pseudo-header is amended to the [layer 4](layer_4_transport.md) [segment](segment.md) to compute the [checksum](checksum.md). This is not sent with the [layer 4](layer_4_transport.md) segment so has to be reproducible on the receivers side. The pseudo-header contains the source and destination [IP address](internet_protocol_(ip).md) (found in the [layer 3](layer_3_network.md) header), the [protocol](protocol_(networks).md) used at [layer 4](layer_4_transport.md) (which can be determined by the header fields) and the size of the [layer 4](layer_4_transport.md) [Segment](segment.md).
>
>This breaks the independence of the [layer 3](layer_3_network.md) and [layer 4](layer_4_transport.md) headers and means you can't change the [layer 3](layer_3_network.md) header without updating the [layer 4](layer_4_transport.md) header. This exists for historic reasons - when [TCP](transmission_control_protocol_(tcp).md) and [IP](internet_protocol_(ip).md) where one [protocol](protocol_(networks).md).


