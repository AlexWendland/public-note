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
>The transmission control protocol is a [[Layer 4 Transport|layer 4]] [[Protocol (networks)|protocol]] that allows for [[Multiplexing|multiplexing]] and a [[Duplex|duplex]] communication channel. It is defined in [RFC793](https://www.ietf.org/rfc/rfc793.txt). This is a connection orientated [[Protocol (networks)|protocol]] which establishes a connection with [[TCP 3 way handshake]] and closes connections with the [[TCP connection teardown]]. This gaurentees the following features. 
>- [[Reliable transmission of TCP messages|reliability]]: every message will be received and acknowledge or it will be redelivered,
>- ordered delivery: messages have a sequence number and will only be parsed to the [[Layer 7 Application|Application layer]] in order,
>- error checking: [[Checksum in layer 4]],
>- [[Transmission control in TCP]]:
>	- Flow control: allow the receiver to dictate how many message it can buffer.
>	- Congestion control and fair usage: will use connection probing to determine a safe and fair transmission rate.
>
>The TCP header has the following fields:
>
>- Source [[Port|port]],
>- Destination [[Port|port]],
>- sequence number: the sequence number of the first data octect, this has a special role in the [[TCP 3 way handshake]],
>- Acknowledgement number: the next sequence number the receiver is expecting to get,
>- Data offset: the number of 32 [[Bit|bit]] words in the TCP header,
>- Reserved: set to all 0's,
>- control bits: these are 0 or 1 for the following 6 fields Urgent, Acknowledgement, Push, Reset, Synchronise, and Finish.
>- Window: The number of data octets number of data octets the sender of this segment is willing to receive. 
>- Checksum: [[Checksum in layer 4]],
>- Urgent pointer,
>- Options, and
>- Padding to make the header a multiple of 32 [[Bit|bits]].
>
>![[tcp_header.png]]


