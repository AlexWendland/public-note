---
aliases:
checked: true
created: 2024-05-27
draft: false
last_edited: 2024-05-27
tags:
  - networks
type: explainer
---
# Checksum in layer 4

To compute the [[Checksum|checksum]] for a [[Layer 4 Transport|layer 4]] header (either [[Transmission Control Protocol (TCP)|TCP]] or [[User Datagram Protocol (UDP)|UDP]]):
- You first construct the header with an all zeros [[Checksum]].
- Then you append the [[Pseudo-header|pseudo-header]] to the message.
- You break the message down into 16-[[Bit|bit]] segments potentially adding 0's if needed.
- Then compute the [[Ones complement|ones complement]] addition off all segments. If this is all 0's it is sent as all 1's. An all 0 header means that the checksum was not computed.
- Fill this in as the [[Checksum|checksum]] component. (Now if you perform the [[Ones complement|ones complement]] addition of all the 16-[[Bit|bit]] segments you should end up with all 1's.)
- Strip the [[Pseudo-header|pseudo-header]] off the [[Segment|segment]].

To verify the [[Checksum|checksum]] on the receivers end they simply need to add all 16-[[Bit|bit]] segments and check it results in all 1's. This makes it robust to a single [[Bit|bit]] flip whilst also being robust to most double bit flips if this happens in the same position in the 16-[[bit]] segments it will not be noticed.
