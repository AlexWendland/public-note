---
aliases:
  - TCP
checked: false
created: 2024-05-22
draft: false
last_edited: 2024-05-22
tags:
  - networks
title: Transmission Control Protocol (TCP)
type: definition
---
>[!tldr] Transmission Control Protocol (TCP)
>The transmission control protocol is a [layer 4](layer_4_transport.md) [protocol](protocol_(networks).md) that allows for [multiplexing](multiplexing.md) and a [duplex](duplex.md) communication channel. It is defined in [RFC793](https://www.ietf.org/rfc/rfc793.txt). This is a connection orientated [protocol](protocol_(networks).md) which establishes a connection with [TCP 3 way handshake](tcp_3_way_handshake.md) and closes connections with the [TCP connection teardown](tcp_connection_teardown.md). This gaurentees the following features.
>- [reliability](reliable_transmission_of_tcp_messages.md): every message will be received and acknowledge or it will be redelivered,
>- ordered delivery: messages have a sequence number and will only be parsed to the [Application layer](layer_7_application.md) in order,
>- error checking: [Checksum in layer 4](checksum_in_layer_4.md),
>- [Transmission control in TCP](transmission_control_in_tcp.md):
>	- Flow control: allow the receiver to dictate how many message it can buffer.
>	- Congestion control and fair usage: will use connection probing to determine a safe and fair transmission rate.
>
>The TCP header has the following fields:
>
>- Source [port](port.md),
>- Destination [port](port.md),
>- sequence number: the sequence number of the first data octect, this has a special role in the [TCP 3 way handshake](tcp_3_way_handshake.md),
>- Acknowledgement number: the next sequence number the receiver is expecting to get,
>- Data offset: the number of 32 [bit](bit.md) words in the TCP header,
>- Reserved: set to all 0's,
>- control bits: these are 0 or 1 for the following 6 fields Urgent, Acknowledgement, Push, Reset, Synchronise, and Finish.
>- Window: The number of data octets number of data octets the sender of this segment is willing to receive.
>- Checksum: [Checksum in layer 4](checksum_in_layer_4.md),
>- Urgent pointer,
>- Options, and
>- Padding to make the header a multiple of 32 [bits](bit.md).
>
>![Tcp Header](../../static/images/tcp_header.png)


# Flow control in [TCP](transmission_control_protocol_(tcp).md)

	Suppose [host](host_(networks).md) A is transmitting data to [host](host_(networks).md) B. When this starts up [host](host_(networks).md) B will reserve some amount of memory to buffer unprocessed packages. Lets say it can fit `RcvBuffer` bytes. Then it keeps track of `LastByteRead` and `LastByteRecieved`


