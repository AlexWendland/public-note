---
aliases:
  - TCP
checked: false
created: 2024-05-22
last_edited: 2024-05-22
publish: true
tags:
  - networks
type: definition
---
>[!tldr] Transmission Control Protocol (TCP)
>This is reliable and verified way to send data. The guarantees data integrity on the other end. This starts with a 3 way handshake:
>1. The server sends a syn (synchronising) message.
>2. The client sends a syn-ach message (synchronising-acknowledgement)
>3. Lastly the server sends an ach (acknowledgement) back to that.
>This opens a connection between the two hosts.
>
>Then data is sent with sequence numbers which has a checksum to verify the data is correct on the other side. The client returns ach messages with these sequence number to inform the host it was received. The client also checks the check sum on their side. If the check sum doesn't match it asks for the data again.
>
>Lastly they close the session with a similar 3 way handshake as before.

