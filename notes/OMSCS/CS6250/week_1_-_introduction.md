---
aliases:
checked: false
course: CS6250 Computer Networks
created: 2024-05-18
draft: false
last_edited: 2024-05-18
tags:
  - OMSCS
title: Week 1 - Introduction
type: lecture
week: 1
---

Here are some questions you should be able to answer to start the course:

• What are the advantages and disadvantages of a layered architecture?
Modularity, Separation of concerns, and interchange of methods at different layers.
Duplication of effort, more covert coupling, and additional overhead.
• What are the differences and similarities between the OSI model and the five-layered Internet model?
[Connection between OSI and IPS models](../../general/connection_between_osi_and_ips_models.md)
• What are sockets?
[Socket](../../general/socket.md)
• Describe each layer of the OSI model.
[OSI](../../general/open_systems_interconnection_(osi)_model.md)
• Provide examples of popular protocols at each layer of the five-layered Internet model.
[HTTP](../../general/hyper_text_transfer_protocol_(http).md)
[TCP](../../general/transmission_control_protocol_(tcp).md)
[ARP](../../general/address_resolution_protocol_(arp).md)
• What is encapsulation, and how is it used in a layered model?
[encapsulation](../../general/encapsulation.md)
• What is the end-to-end (e2e) principle?
[End to end principle](../../general/end_to_end_principle.md)
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

# Additional readings

## Important Readings

How to Read a Paper
[https://people.cs.umass.edu/~phillipa/CSE390/paper-reading.pdfLinks to an external site.](https://people.cs.umass.edu/~phillipa/CSE390/paper-reading.pdf)

How to Read a Research Paper
[https://www.cs.tufts.edu/comp/150PLD/ReadingPapers.pdfLinks to an external site.](https://www.cs.tufts.edu/comp/150PLD/ReadingPapers.pdf)

The Design Philosophy of the DARPA Internet Protocols
[http://ccr.sigcomm.org/archive/1995/jan95/ccr-9501-clark.pdfLinks to an external site.](http://ccr.sigcomm.org/archive/1995/jan95/ccr-9501-clark.pdf)

The Evolution of Layered Protocol Stacks Leads to an Hourglass-Shaped Architecture [https://www.cc.gatech.edu/~dovrolis/Papers/evoarch.pdfLinks to an external site.](https://www.cc.gatech.edu/~dovrolis/Papers/evoarch.pdf)

## Book References

If you have access to the Kurose-Ross book and the Peterson book, you can find the chapters discussed in this lecture. As mentioned in the course schedule, purchasing the books is not required.

1. Kurose 1.5.1 (Edition 6): Layered Architecture
2. Kurose 1.5.2 (Edition 6): Encapsulation
3. Computer Networks: A Systems Approach - Edition 4, Section 3 and 3.1 (Interconnecting hosts and networks)
4. Computer Networks: A Systems Approach - Edition 4, Section 3.2.1 (Learning Bridges)
5. Computer Networks: A Systems Approach - Edition 4, Section 3.2.2 (The looping problem and the spanning tree algorithm)

## Optional Readings

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

# Layer architecture of the internet

The internet stack is a layered stack of protocols where each layer depends loosely on the layer below and is requried by the layer above. This allows doe scalability molecularity and the flexibility to add or remove components.

The first version of this structure was the [OSI model](../../general/open_systems_interconnection_(osi)_model.md) - though later refinements came about such as [IPS model](../../general/internet_protocol_stack_(ips)_5_layers.md) which combined some layers.

[OSI model](../../general/open_systems_interconnection_(osi)_model.md)

[Application layer](../../general/layer_7_application.md)

This is where a lot of the popular [protocols](../../general/protocol_(networks).md) operate such as [HTTP](../../general/hyper_text_transfer_protocol_(http).md), [SMTP](../../general/simple_mail_transfer_protocol_(smtp).md), [FTP](../../general/file_transfer_protocol_(ftp).md), or [DNS](../../general/domain_name_system_(dns).md). This controls the application specific command.

[Presentation layer](../../general/layer_6_presentation.md)

This is responsible for converting data from its encoded format to one understood by the application. This might be as simple as converting [bits](../../general/bit.md) to [ASCII](../../general/american_standard_code_for_information_interchange_(ascii).md).

[Session layer](../../general/layer_5_session.md)

This is responsible for merging different transport streams that are intended for the same user. For example the audio and video streams for a call.

[Transport layer](../../general/layer_4_transport.md)

This is responsible for getting the data correctly from one end to another. It uses protocols such as [UDP](../../general/user_datagram_protocol_(udp).md) and [TCP](../../general/transmission_control_protocol_(tcp).md). This attaches source and destination [ports](../../general/port.md) to the message to make it a [segment](../../general/segment.md).

Note that [TCP](../../general/transmission_control_protocol_(tcp).md) adds
- multiplexing,
- congestion control and
- reliable, in-order delivery.

Though for this is slower and more complex to implement.

[Network layer](../../general/layer_3_network.md)

The network layer is responsible for getting the data to the correct host in the internet. It wraps the [Segment](../../general/segment.md) up with the [IP addresses](../../general/internet_protocol_(ipv4).md) to make a [datagram](../../general/packets.md). This uses the [IP](../../general/internet_protocol_(ip).md) to do this.

[Data Link layer](../../general/layer_2_data_link.md)

This layer uses [MAC addresses](../../general/mac_address.md) and bind this to the [datagram](../../general/packets.md) to make a [frame](../../general/frame_(networks).md). This is used to safely pass [segment](../../general/segment.md) through [networks](../../general/network.md).

[Physical layer](../../general/layer_1_physical.md)

This facilitates communicate these [frames](../../general/frame_(networks).md) through the physical hardware associated to the network be that cables or wifi.

[Encapsulation](../../general/encapsulation.md)

The end hosts have to implement encapsulation and de-encapsulation however intermediary don't need to. This is summarised by the [End to end principle](../../general/end_to_end_principle.md).

[End to end principle](../../general/end_to_end_principle.md)

In simple terms this states that the network core should be simple and minimal, while the end systems should carry the intelligence. Any feature in the core of the network should be shared by all applications. Therefore there could be error checking at the physical layer if that error checking was done without needing to know the structure of the original message.

## Violations of the end to end principle

[Network Address Translation (NAT)](../../general/network_address_translation_(nat).md)

Most home [routers](../../general/router.md) have a [NAT](../../general/network_address_translation_(nat).md) in them this means your home internet will have a single [Internet Protocol (IPv4)](../../general/internet_protocol_(ipv4).md) to the outside world.

[Firewall](../../general/firewall.md)

# Shape of the internet

[Internet protocol stack hourglass shape](../../general/internet_protocol_stack_hourglass_shape.md)

There is a model that was purposed to explain this shape.

[Evolutionary Architecture model (EvoArch)](../../general/evolutionary_architecture_model_(evoarch).md)

In some set ups of this model the width of the layers tend to follow that of the internet with a similar hourglass shape. Implying there might not be anything particularly special about [Internet Protocol (IP)](../../general/internet_protocol_(ip).md), [UDP](../../general/user_datagram_protocol_(udp).md), or [TCP](../../general/transmission_control_protocol_(tcp).md) but more there was always going to be a bottle neck here.

These [protocols](../../general/protocol_(networks).md) do defend one another for a replacement to [IP](../../general/internet_protocol_(ip).md) to come about it would have to rival being used by both [TCP](../../general/transmission_control_protocol_(tcp).md) and [UDP](../../general/user_datagram_protocol_(udp).md).

This is good to keep in mind for development for any layered system - if you don't want monopolies to form you need to garentee a variety of non-competing protocols at each layer.

# Devices

[layer 1](../../general/layer_1_physical.md)

[Repeater](../../general/repeater.md)

[Hub](../../general/hub.md)

[layer 2](../../general/layer_2_data_link.md)

[Bridge](../../general/bridge.md)

[Switch](../../general/switch.md)

[layer 3](../../general/layer_3_network.md)

[Router](../../general/router.md)

# Spanning tree algorithm

There is a problem with [Switching](../../general/switching.md) when there are multiple [switches](../../general/switch.md) that form loops. A message may go round infinitely. To get around this the switches in a [network](../../general/network.md) try to form a spanning tree amongst themselves so they stop infinite cycles.

[Spanning Tree Protocol (STP)](../../general/spanning_tree_protocol_(stp).md)
