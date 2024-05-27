---
aliases:
  - pseudo-header
checked: false
created: 2024-05-27
last_edited: 2024-05-27
publish: true
tags:
  - networks
type: definition
---
>[!tldr] Pseudo-header
>The Pseudo-header is amended to the [[Layer 4 Transport|layer 4]] [[Segment|segment]] to compute the [[Checksum|checksum]]. This is not sent with the [[Layer 4 Transport|layer 4]] segment so has to be reproducible on the receivers side. The pseudo-header contains the source and destination [[Internet Protocol (IP)|IP address]] (found in the [[Layer 3 Network|layer 3]] header), the [[Protocol (networks)|protocol]] used at [[Layer 4 Transport|layer 4]] (which can be determined by the header fields) and the size of the [[Layer 4 Transport|layer 4]] [[Segment]]. 
>
>This breaks the independence of the [[Layer 3 Network|layer 3]] and [[Layer 4 Transport|layer 4]] headers and means you can't change the [[Layer 3 Network|layer 3]] header without updating the [[Layer 4 Transport|layer 4]] header. This exists for historic reasons - when [[Transmission Control Protocol (TCP)|TCP]] and [[Internet Protocol (IP)|IP]] where one [[Protocol (networks)|protocol]].


