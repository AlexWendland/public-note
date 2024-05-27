---
aliases: 
checked: true
created: 2024-05-27
last_edited: 2024-05-27
publish: true
tags:
  - networks
type: explainer
---
# Checksum in layer 4

To compute the [[Checksum|checksum]] for a [[Layer 4 Transport|layer 4]] header (either [[Transmission Control Protocol (TCP)|TCP]] or [[User Datagram Protocol (UDP)|UDP]]): 
- You first construct the header with an all zeros [[Checksum]]. 
- Then you append the [[Pseudo-header|pseudo-header]] to the message. 
- You break the message down into 16-[[Bit|bit]] segments potentially adding an all 0 component if needed.
- 
