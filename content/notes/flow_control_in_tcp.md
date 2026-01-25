---
aliases:
created: 2024-05-28
date_checked:
draft: false
last_edited: 2024-05-28
tags:
  - networks
title: Flow control in TCP
type: explainer
---
# Flow control in [TCP](transmission_control_protocol_(tcp).md)

Suppose [host](host_(networks).md) A is transmitting data to [host](host_(networks).md) B. When this starts up [host](host_(networks).md) B will reserve some amount of memory to buffer unprocessed packages. Lets say it can fit `RcvBuffer` bytes. Then it keeps track of `LastByteRead` and `LastByteRecieved`.

When returning an acknowledgement message to [host](host_(networks).md) A for a [segment](segment.md) it populates the window field with `RcvBuffer - [LastByteRecieved - LastByteRead]`. This informs [host](host_(networks).md) A how much buffer [host](host_(networks).md) B has left.

[Host](host_(networks).md) A will use this as one input to its [Transmission control](transmission_control_in_tcp.md).

>[!attention] What if the window size is 0?
>If the window size is 0 on the last Acknowledgement message then we could have a deadlock if [host](host_(networks).md) B doesn't want to send anything to [host](host_(networks).md) A. It will process its messages but never send another ACK message to [host](host_(networks).md) A to tell it, it has more buffer available.
>To solve this problem [host](host_(networks).md) A will periodically send [host](host_(networks).md) B a single byte of data. Then it gets the new buffer size in the ACK message.
