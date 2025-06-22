---
aliases: 
checked: false
course: "[[CS6250 Computer Networks]]"
created: 2024-05-24
last_edited: 2024-05-24
draft: false
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

## [[Layer 4 Transport|Transport layer]] summary

During [[Encapsulation|encapsulation]] the [[Layer 7 Application|Application layer]] parses the [[Layer 4 Transport|Transport layer]] a message. It appends some headers to make into a [[Segment|segment]]. This then gets parsed to the [[Layer 3 Network|Network layer]] to make a best effort of delivery. The purpose of the [[Layer 4 Transport|Transport layer]] to bridge the gap between the [[Layer 3 Network|Network layers]] best effort delivery and something more reliable for the application to depend upon.

The two main [[Protocol (networks)|protocols]] here are [[User Datagram Protocol (UDP)|UDP]] and [[Transmission Control Protocol (TCP)|TCP]]. These both offer the application different payoffs. Currently [[Transmission Control Protocol (TCP)|TCP]] is the most dominant out of these and is pretty ubiquitous in the internet.

## Multiplexing

![[Multiplexing]]

![[Port]]

## UDP

![[User Datagram Protocol (UDP)|UDP]]

![[Checksum in layer 4]]

![[Pseudo-header]]

![[Ones complement]]

## TCP

![[Transmission Control Protocol (TCP)|TCP]]

![[TCP 3 way handshake]]

![[TCP connection teardown]]

### Reliable Transmission

![[Reliable transmission of TCP messages]]

### Transmission control

![[Transmission control in TCP]]

![[Flow control in TCP]]

![[Congestion control in TCP]]