---
aliases: 
checked: false
course: "[[CS6250 Computer Networks]]"
created: 2024-05-18
last_edited: 2024-05-18
publish: true
tags:
  - OMSCS
type: lecture
week: 1
---
# Week 1 - Introduction

Here are some questions you should be able to answer to start the course:

• What are the advantages and disadvantages of a layered architecture?
Modularity, Separation of concerns, and interchange of methods at different layers.
Duplication of effort, more covert coupling, and additional overhead.
• What are the differences and similarities between the OSI model and the five-layered Internet model?  
![[Connection between OSI and IPS models]]
• What are sockets?  
![[Socket]]
• Describe each layer of the OSI model.  
![[Open Systems interconnection (OSI) model|OSI]]
• Provide examples of popular protocols at each layer of the five-layered Internet model.  
[[Hyper Text Transfer Protocol (HTTP)|HTTP]]
[[Transmission Control Protocol (TCP)|TCP]]
[[Address Resolution Protocol (ARP)|ARP]]
• What is encapsulation, and how is it used in a layered model?  
![[Encapsulation|encapsulation]]
• What is the end-to-end (e2e) principle? 
![[End to end principle]]
• What are the examples of a violation of e2e principle? 

1. **Network Address Translation (NAT)**: NAT modifies the IP address information in packet headers while they are in transit, which breaks the end-to-end connectivity and transparency. This complicates end-to-end communication protocols that rely on unique IP addresses.
2. **Firewalls and Deep Packet Inspection (DPI)**: Firewalls and DPI devices inspect and sometimes modify the content of data packets as they pass through the network. This interferes with end-to-end encryption and data integrity checks.
3. **Content Delivery Networks (CDNs)**: CDNs cache content closer to users to improve performance and reduce latency. While this benefits performance, it introduces intermediary nodes that alter the direct path between the source and destination, which can complicate end-to-end control and data integrity.
4. **QoS (Quality of Service) Mechanisms**: QoS techniques prioritize certain types of traffic over others within the network. While this can improve performance for specific applications, it introduces complexity and control within the network itself, rather than at the endpoints.
5. **Proxy Servers**: Proxy servers act as intermediaries for requests from clients seeking resources from other servers. They can modify requests and responses, breaking the direct communication path and potentially interfering with end-to-end data handling.

• What is the EvoArch model?  
• Explain a round in the EvoArch model.  
• What are the ramifications of the hourglass shape of the internet?  
• Repeaters, hubs, bridges, and routers operate on which layers?  
• What is a bridge, and how does it “learn”?  
• What is a distributed algorithm?  
• Explain the Spanning Tree Algorithm.  
• What is the purpose of the Spanning Tree Algorithm?

## Additional readings

### Important Readings

How to Read a Paper  
[https://people.cs.umass.edu/~phillipa/CSE390/paper-reading.pdfLinks to an external site.](https://people.cs.umass.edu/~phillipa/CSE390/paper-reading.pdf) 

How to Read a Research Paper  
[https://www.cs.tufts.edu/comp/150PLD/ReadingPapers.pdfLinks to an external site.](https://www.cs.tufts.edu/comp/150PLD/ReadingPapers.pdf)

The Design Philosophy of the DARPA Internet Protocols  
[http://ccr.sigcomm.org/archive/1995/jan95/ccr-9501-clark.pdfLinks to an external site.](http://ccr.sigcomm.org/archive/1995/jan95/ccr-9501-clark.pdf) 

The Evolution of Layered Protocol Stacks Leads to an Hourglass-Shaped Architecture [https://www.cc.gatech.edu/~dovrolis/Papers/evoarch.pdfLinks to an external site.](https://www.cc.gatech.edu/~dovrolis/Papers/evoarch.pdf)

### Book References

If you have access to the Kurose-Ross book and the Peterson book, you can find the chapters discussed in this lecture. As mentioned in the course schedule, purchasing the books is not required.

1. Kurose 1.5.1 (Edition 6): Layered Architecture
2. Kurose 1.5.2 (Edition 6): Encapsulation
3. Computer Networks: A Systems Approach - Edition 4, Section 3 and 3.1 (Interconnecting hosts and networks)
4. Computer Networks: A Systems Approach - Edition 4, Section 3.2.1 (Learning Bridges)
5. Computer Networks: A Systems Approach - Edition 4, Section 3.2.2 (The looping problem and the spanning tree algorithm)

### Optional Readings

Brief History of the Internet (1997)  
[https://www.internetsociety.org/wp-content/uploads/2017/09/ISOC-History-of-the-Internet_1997.pdfLinks to an external site.](https://www.internetsociety.org/wp-content/uploads/2017/09/ISOC-History-of-the-Internet_1997.pdf)

Rethinking the design of the Internet  
[https://dspace.mit.edu/bitstream/handle/1721.1/1519/TPRC_Clark_Blumenthal.pdf?sequence=1&origin=publication_detailLinks to an external site.](https://dspace.mit.edu/bitstream/handle/1721.1/1519/TPRC_Clark_Blumenthal.pdf?sequence=1&origin=publication_detail)

The End-To-End Argument  
[http://web.mit.edu/Saltzer/www/publications/endtoend/ANe2ecomment.htmlLinks to an external site.](http://web.mit.edu/Saltzer/www/publications/endtoend/ANe2ecomment.html)  
[http://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdfLinks to an external site.](http://web.mit.edu/Saltzer/www/publications/endtoend/endtoend.pdf)

Internet Clean-Slate Design: What and Why?  
[https://citeseerx.ist.psu.edu/pdf/700ba413874b914557742ab688cf4c7a445e7c47Links to an external site.](https://citeseerx.ist.psu.edu/pdf/700ba413874b914557742ab688cf4c7a445e7c47)

A Clean Slate 4D Approach to Network Control and Management [https://www.cs.princeton.edu/~jrex/papers/ccr05-4d.pdfLinks to an external site.](https://www.cs.princeton.edu/~jrex/papers/ccr05-4d.pdf)

Holding the Internet Accountable  
[https://conferences.sigcomm.org/hotnets/2007/papers/hotnets6-final71.pdfLinks to an external site.](https://conferences.sigcomm.org/hotnets/2007/papers/hotnets6-final71.pdf)

An Algorithm for Distributed Computation of a Spanning Tree in an Extended LAN [https://www.it.uu.se/edu/course/homepage/datakom/ht06/slides/sta-perlman.pdfLinks to an external site.](https://www.it.uu.se/edu/course/homepage/datakom/ht06/slides/sta-perlman.pdf)

## Layer architecture of the internet

The internet stack is a layered stack of protocols where each layer depends loosely on the layer below and is requried by the layer above. This allows doe scalability molecularity and the flexibility to add or remove components.

The first version of this structure was the [[Open Systems interconnection (OSI) model|OSI model]] - though later refinements came about such as [[Internet Protocol Stack (IPS) 5 layers|IPS model]] which combined some layers.

![[Open Systems interconnection (OSI) model|OSI model]]

[[Layer 7 Application|Application layer]]

This is where a lot of the popular [[Protocol (networks)|protocols]] operate such as [[Hyper Text Transfer Protocol (HTTP)|HTTP]], [[Simple Mail Transfer Protocol (SMTP)|SMTP]], [[File Transfer Protocol (FTP)|FTP]], or [[Domain Name System (DNS)|DNS]]. This controls the application specific command.

[[Layer 6 Presentation|Presentation layer]]

This is responsible for converting data from its encoded format to one understood by the application. This might be as simple as converting [[Bit|bits]] to [[American Standard Code for Information Interchange (ASCII)|ASCII]].

[[Layer 5 Session|Session layer]]

This is responsible for merging different transport streams that are intended for the same user. For example the audio and video streams for a call.

[[Layer 4 Transport|Transport layer]]

This is responsible for getting the data correctly from one end to another. It uses protocols such as [[User Datagram Protocol (UDP)|UDP]] and [[Transmission Control Protocol (TCP)|TCP]]. This attaches source and destination [[Port|ports]] to the message to make it a [[Segment|segment]].

Note that [[Transmission Control Protocol (TCP)|TCP]] adds
- multiplexing, 
- congestion control and 
- reliable, in-order delivery.

Though for this is slower and more complex to implement.

[[Layer 3 Network|Network layer]]

The network layer is responsible for getting the data to the correct host in the internet. It wraps the [[Segment]] up with the [[IP address|IP addresses]] to make a [[Packets|datagram]]. This uses the [[Internet Protocol (IP)|IP]] to do this.

[[Layer 2 Data Link|Data Link layer]]

This layer uses [[MAC address|MAC addresses]] and bind this to the [[Packets|datagram]] to make a [[Frame (networks)|frame]]. This is used to safely pass [[Segment|segment]] through [[Network|networks]].

[[Layer 1 Physical|Physical layer]]

This facilitates communicate these [[Frame (networks)|frames]] through the physical hardware associated to the network be that cables or wifi.

![[Encapsulation]]

The end hosts have to implement encapsulation and de-encapsulation however intermediary don't need to. This is summarised by the [[End to end principle]].

![[End to end principle]]

In simple terms this states that the network core should be simple and minimal, while the end systems should carry the intelligence. Any feature in the core of the network should be shared by all applications. Therefore there could be error checking at the physical layer if that error checking was done without needing to know the structure of the original message.

### Violations of the end to end principle

![[Network Address Translation (NAT)]]

Most home [[Router|routers]] have a [[Network Address Translation (NAT)|NAT]] in them this means your home internet will have a single [[IP address]] to the outside world.

![[Firewall]]

## Shape of the internet

![[Internet protocol stack hourglass shape]]




