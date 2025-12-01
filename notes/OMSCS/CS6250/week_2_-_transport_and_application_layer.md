---
aliases:
checked: false
course: '[CS6250 Computer Networks](../cs6250_computer_networks.md)'
created: 2024-05-24
draft: false
last_edited: 2024-05-24
name: Week 2 - Transport and application layer
tags:
  - OMSCS
type: lecture
week: 2
---
# Week 2 - Transport and application layer

## Important Readings

CUBIC: A New TCP-Friendly High-Speed TCP Variant
[https://www.cs.princeton.edu/courses/archive/fall16/cos561/papers/Cubic08.pdfLinks to an external site.](https://www.cs.princeton.edu/courses/archive/fall16/cos561/papers/Cubic08.pdf)

## Book References

Kurose-Ross (Edition 6): Sections 3.1.1, 3.2, 3.3, 3.4, 3.5.5, 3.6

Peterson Section 6.3

## Optional Readings

Congestion Avoidance and Control
[https://ee.lbl.gov/papers/congavoid.pdfLinks to an external site.](https://ee.lbl.gov/papers/congavoid.pdf)

A Protocol for Packet Network Intercommunication
[https://www.cs.princeton.edu/courses/archive/fall06/cos561/papers/cerf74.pdfLinks to an external site.](https://www.cs.princeton.edu/courses/archive/fall06/cos561/papers/cerf74.pdf)

End-to-End Internet Packet Dynamics
[https://people.eecs.berkeley.edu/~sylvia/cs268-2019/papers//pktdynamics.pdfLinks to an external site.](https://people.eecs.berkeley.edu/~sylvia/cs268-2019/papers//pktdynamics.pdf)

Data Center TCP (DCTCP)
[https://people.csail.mit.edu/alizadeh/papers/dctcp-sigcomm10.pdfLinks to an external site.](https://people.csail.mit.edu/alizadeh/papers/dctcp-sigcomm10.pdf "Link") [(Links to an external site.)](https://people.csail.mit.edu/alizadeh/papers/dctcp-sigcomm10.pdf)

TIMELY: RTT-based Congestion Control for the Datacenter
[https://conferences.sigcomm.org/sigcomm/2015/pdf/papers/p537.pdfLinks to an external site.](https://conferences.sigcomm.org/sigcomm/2015/pdf/papers/p537.pdf "Link")

Design, implementation and evaluation of congestion control for multipath TCP
[https://www.usenix.org/legacy/events/nsdi11/tech/full_papers/Wischik.pdfLinks to an external site.](https://www.usenix.org/legacy/events/nsdi11/tech/full_papers/Wischik.pdf)

Sizing Router Buffers
[https://web.archive.org/web/20210120232627/http://yuba.stanford.edu/techreports/TR04-HPNG-060800.pdfLinks to an external site.](https://web.archive.org/web/20210120232627/http://yuba.stanford.edu/techreports/TR04-HPNG-060800.pdf)

## [Transport layer](../../general/layer_4_transport.md) summary

During [encapsulation](../../general/encapsulation.md) the [Application layer](../../general/layer_7_application.md) parses the [Transport layer](../../general/layer_4_transport.md) a message. It appends some headers to make into a [segment](../../general/segment.md). This then gets parsed to the [Network layer](../../general/layer_3_network.md) to make a best effort of delivery. The purpose of the [Transport layer](../../general/layer_4_transport.md) to bridge the gap between the [Network layers](../../general/layer_3_network.md) best effort delivery and something more reliable for the application to depend upon.

The two main [protocols](../../general/protocol_(networks).md) here are [UDP](../../general/user_datagram_protocol_(udp).md) and [TCP](../../general/transmission_control_protocol_(tcp).md). These both offer the application different payoffs. Currently [TCP](../../general/transmission_control_protocol_(tcp).md) is the most dominant out of these and is pretty ubiquitous in the internet.

## Multiplexing

[Multiplexing](../../general/multiplexing.md)

[Port](../../general/port.md)

## UDP

[UDP](../../general/user_datagram_protocol_(udp).md)

[Checksum in layer 4](../../general/checksum_in_layer_4.md)

[Pseudo-header](../../general/pseudo-header.md)

[Ones complement](../../general/ones_complement.md)

## TCP

[TCP](../../general/transmission_control_protocol_(tcp).md)

[TCP 3 way handshake](../../general/tcp_3_way_handshake.md)

[TCP connection teardown](../../general/tcp_connection_teardown.md)

### Reliable Transmission

[Reliable transmission of TCP messages](../../general/reliable_transmission_of_tcp_messages.md)

### Transmission control

[Transmission control in TCP](../../general/transmission_control_in_tcp.md)

[Flow control in TCP](../../general/flow_control_in_tcp.md)

[Congestion control in TCP](../../general/congestion_control_in_tcp.md)
