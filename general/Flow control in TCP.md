---
aliases: 
checked: false
created: 2024-05-28
last_edited: 2024-05-28
draft: false
tags:
  - networks
type: explainer
---
# Flow control in [[Transmission Control Protocol (TCP)|TCP]]

Suppose [[Host (networks)|host]] A is transmitting data to [[Host (networks)|host]] B. When this starts up [[Host (networks)|host]] B will reserve some amount of memory to buffer unprocessed packages. Lets say it can fit `RcvBuffer` bytes. Then it keeps track of `LastByteRead` and `LastByteRecieved`.

When returning an acknowledgement message to [[Host (networks)|host]] A for a [[Segment|segment]] it populates the window field with `RcvBuffer - [LastByteRecieved - LastByteRead]`. This informs [[Host (networks)|host]] A how much buffer [[Host (networks)|host]] B has left. 

[[Host (networks)|Host]] A will use this as one input to its [[Transmission control in TCP|Transmission control]].

>[!attention] What if the window size is 0?
>If the window size is 0 on the last Acknowledgement message then we could have a deadlock if [[Host (networks)|host]] B doesn't want to send anything to [[Host (networks)|host]] A. It will process its messages but never send another ACK message to [[Host (networks)|host]] A to tell it, it has more buffer available.
>To solve this problem [[Host (networks)|host]] A will periodically send [[Host (networks)|host]] B a single byte of data. Then it gets the new buffer size in the ACK message.