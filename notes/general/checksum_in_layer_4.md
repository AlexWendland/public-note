---
aliases:
checked: true
created: 2024-05-27
draft: false
last_edited: 2024-05-27
title: Checksum in layer 4
tags:
  - networks
type: explainer
---
# Checksum in layer 4

To compute the [checksum](checksum.md) for a [layer 4](layer_4_transport.md) header (either [TCP](transmission_control_protocol_(tcp).md) or [UDP](user_datagram_protocol_(udp).md)):
- You first construct the header with an all zeros [Checksum](checksum.md).
- Then you append the [pseudo-header](pseudo-header.md) to the message.
- You break the message down into 16-[bit](bit.md) segments potentially adding 0's if needed.
- Then compute the [ones complement](ones_complement.md) addition off all segments. If this is all 0's it is sent as all 1's. An all 0 header means that the checksum was not computed.
- Fill this in as the [checksum](checksum.md) component. (Now if you perform the [ones complement](ones_complement.md) addition of all the 16-[bit](bit.md) segments you should end up with all 1's.)
- Strip the [pseudo-header](pseudo-header.md) off the [segment](segment.md).

To verify the [checksum](checksum.md) on the receivers end they simply need to add all 16-[bit](bit.md) segments and check it results in all 1's. This makes it robust to a single [bit](bit.md) flip whilst also being robust to most double bit flips if this happens in the same position in the 16-[bit](bit.md) segments it will not be noticed.
