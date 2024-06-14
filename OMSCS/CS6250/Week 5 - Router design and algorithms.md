---
aliases: 
checked: false
course: "[[CS6250 Computer Networks]]"
created: 2024-06-11
last_edited: 2024-06-11
publish: true
tags:
  - OMSCS
type: lecture
week: 5
---
# Week 5 - Router design and algorithms

# Part 1

## Additional reading

### Important Readings

Survey and Taxonomy of IP Address Lookup Algorithms  
[https://pdfs.semanticscholar.org/71d9/018e900f99ff60653b3769160131e775873f.pdfLinks to an external site.](https://pdfs.semanticscholar.org/71d9/018e900f99ff60653b3769160131e775873f.pdf)

### Book References

Kurose-Ross, 6th Edition, Section 4.3

Kurose-Ross, 7th Edition, Section 4.2

Varghese, Network Algorithmics, Sections: 1.1.2,  2.3.2,  Chapter 11

## What is inside a router

There are two parts of a router.
- The forwarding plane, and
- The Control plane.

![[router_seperation_of_planes.png]]

The forwarding plane is responsible for getting messages forwarded when they arrive at the router. Which has 3 main components:
- **Input queue**: responsible for finishing the [[Layer 1 Physical|layer 1]] process and [[Encapsulation|de-encapsulation]] the message to get the [[Internet Protocol (IP)|IP address]]. The it looks up where it has to go and moves it onto the switching fabric.
- **Switching fabric**: Only responsible for getting messages from the input queue to the correct output queue.
- **Output queue**: The same as the input but backwards.

![[router_input_que.png]]
![[router_output_que.png]]

The control plane refers to the implementation of the [[Router|router]] [[Protocol (networks)|protocols]]. This mainly involves keeping the forwarding table up to date.

![[router_control_plane.png]]

## Router architecture

Here we depict what happens when a [[Packets|packet]] arrives at the router.

![[router_arcitecture.png]]

The most time sensitive operations are lookup, switching and scheduling.

- **Lookup**: When a packet arrives this uses the [[Internet Protocol (IP)|IP address]] to find the output link in the [[Forwarding information base (FIB)]]. It uses longest prefix matching to do this. Some routers offer more complicated lookups using [[Port|ports]] and other criteria.
- **Switching**: This involves moving from the input link to the output link. Modern routers will use crossbar switching. Though scheduling this can be complicated if multiple inputs want to go to the same output.
- **Queuing**: This is exactly what it sounds like. Some routers use a FIFO queue but they can deploy more complicated weighted queues to implement delay guarantees or fair bandwidth allocation.
- **Header validation and checksum**: Check the packet, update [[Time to live (TTL)|TTL]] and recalculate the checksum.
- **Route processing**: Building the [[Forwarding information base (FIB)]]. This uses [[Protocol (networks)|protocols]] such as [[Routing Information Protocol (RIP)|RIP]], or [[Open Shortest Path First (OSPF)|OSPF]].
- **Protocol processing**: The routers need to implement: [[Simple Network Management Protocol (SNMP)|SNMP]], [[Transmission Control Protocol (TCP)|TCP]], [[User Datagram Protocol (UDP)|UDP]], and [[Internet Control Message Protocol (ICMP)|ICMP]] for sending error messages.

## Switching fabric

This can be accomplished in one of 3 ways.

### Via Memory

Input/Output ports operate as I/O devices in an operating system, controlled by the routing processor. When an input port receives a packet, it sends an interrupt to the routing processor, and the packet is copied to the processor's memory. Then the processor extracts the destination address and looks into the forward table to find the output port, and finally, the packet is copied into that output's port buffer.

![[switching_memory.png]]

### Via bus

In this case, the routing processor does not intervene as we saw the switching via memory. When an input port receives a new packet, it puts an internal header that designates the output port, and it sends the packet to the shared bus. Then all the output ports will receive the packet, but only the designated one will keep it. When the packet arrives at the designated output port, the internal header is removed from the packet. Only one packet can cross the bus at a given time, so the speed of the bus limits the speed of the router.

![[switching_bus.png]]

### Via interconnected network (crossbar)

A crossbar switch is an interconnection network that connects $N$ input ports to $N$ output ports using $2N$ buses. Horizontal buses meet the vertical buses at crosspoints controlled by the switching fabric. For example, let's suppose that a packet arrives at port A that will need to be forwarded to output port Y, the switching fabric closes the crosspoint where the two buses intersect so that port A can send the packets onto the bus, and then the packet can only be picked up by output port Y. Crossbar network can carry multiple packets at the same time, as long as they are using different input and output ports. For example, packets can go from A-to-Y and B-to-X simultaneously.

![[switching_crossbar.png]]

## Problems facing routers

Modern routing facing a lot of problems when handling the scale of the internet.

1. **Bandwidth and Internet Population scaling**: These are caused by
	1. Increased number of devices connected to the internet.
	2. Increasing volumes of network traffic.
	3. New devices that can operate at high speeds.
2. **Services at high speeds**: New devices that need to operate at high speeds which can be effected by congestion or attacks on the network.

![[router_problems.png]]

**Longest prefix matching** Matching a packet to the [[Forwarding information base (FIB)|FIB]] can be complicated. New routers offer more complicated lookups as well.

**Service differentiation** This allows routers to offer per service guarantees such as delay insurance and fairness within services. This requires the router to inspect packets deeper than it otherwise would.

**Switching limitation** Moving packets from the input to output link has some hard limitations to it as we will see with head of line blocking.

**Bottlenecks about services** Providing performance guarantees at high speed such as measurements and security. 

## Prefix-match Lookups

Matching addresses to entries in the [[Forwarding information base (FIB)|FIB]] is one of the most time sensitive and mathematically hard operations in a router.

### Prefix notation

Here we denote prefixes in 3 ways.

- **Wildcard**: Here we just write the prefix of the address and then use a \* to denote the end of the prefix.
- **Slash notation**: We provide the [[Internet Protocol (IP)|IP address]] followed by a slash and the size of the relevant prefix in [[Bit|bits]]. i.e. 123.0.0.0/8.
- **Masking**: We provide the [[Internet Protocol (IP)|IP address]] with the [[Network mask|network mask]].

### Variable length prefixes

In the early days of the [[Internet]] there were fixed length prefixes. Though this drove the problem that [[We are running out of IPv4 addresses on the pubic internet|we are running out of IPv4 addresses on the pubic internet]].

### Better lookup algorithms

There are many problems that just the lookup process faces.

1. Measurement studies on network traffic had shown a large number (in the order of hundreds of thousands - 250,000 according to a measurement study in the earlier days of the Internet) of concurrent flows of short duration. This already large number has only been increasing, and as a consequence, caching solutions will not work efficiently. 
2. The important element of any lookup operation is how fast it is done (lookup speed). A large part of the cost of computation for lookup is accessing memory.
3. An unstable routing protocol may adversely impact the update time in the table: add, delete or replace a prefix. Inefficient routing protocols increase this value up to additional milliseconds.
4. A vital trade-off is memory usage. We can use expensive fast memory (cache in software, SRAM in hardware) or cheaper but slower memory (e.g., DRAM, SDRAM).

![[lookup_problems.png]]

## Unibit Tries

![[Trie]]

We can use [[Subnets|subnet]] to form a [[Trie|trie]] over the alphabet of $\{0, 1\}$ with values being the [[Subnets|subnets]]. To generate the [[Trie|trie]] we build a path from the root for every address in our table and label the end node with that [[Subnets|subnet]]. 

> [!example] Prefix-match lookup
> Suppose we have the following table
> ![[prefix_table.png]]
> then we use these strings to construct the following [[Trie|trie]].
> ![[prefix_trie.png]]
> we do not include the left branch of this [[Trie|trie]]. We also compress one-way branches for example in P9.

Then we use this [[Trie|trie]] as the description entails.

## Multibit tries

Whilst unibit [[Trie|tries]] is very efficient in terms of space they can be slow in terms of memory lookups. For a substring of length $n$ you may need to look up $n$ times. Instead we can increase the length of the "stride" and go for a longer alphabet.

We have two approaches here.
- Fix stride length $k$ generating $2^k$ children.
- Variable length stride depending on the number of children, like P9 above.

### Fixed length multibit tries

Here we pick a length of stride $k$ and then cut our [[Subnets|subnets]] into multiples of $k$. If a [[Subnets|subnet]] length is not a multiple of $k$ then we expand it to all the address of the next multiple of $k$ that would be covered b it. If no other longer address clashes with it, we label that address with the [[Subnets|subnet]] it came from.

> [!example] Prefix expansion
> Suppose we set $k=3$ then using the table from the previous example lets do prefix expansion.
> ![[prefix_expansion.png]]

Then we construct the multibit [[Trie|trie]] the same way as the unibit [[Trie|trie]] with the expanded addresses but with the alphabet set to bit strings of length $k$.

![[fixed_length_multibit_trie.png]]

Notice here we only needed to have at most 3 lookups whereas before it was 5.

### Variable length multibit tries

In the previous example we can see by choosing length 3 words the table to the left is much larger than we needed it to be. P3 was only length 2 and we had no other entries in that table. This wastes space - so we can let the length of that string be 2 instead.

![[variable_length_trie.png]]

The optimal stride length can be chosen using [[Dynamic Programming|dynamic programming]]. Though they do not say how.

# Part 2

## Additional readings

### Book References

Varghese, Network Algorithmics, Chapters 12, 13, 14

Kurose-Ross, 6th Edition, Section 7.5.2

Kurose-Ross, 7th Edition, Section 9.5.2

## Packet classification

To guarantee more features within a [[Router|router]] such as quality of service, security and protocol based handling of [[Packets|packets]] we need to classify packets on more than just their destination [[Internet Protocol (IP)|IP]].

These further classifications can be based on source [[Internet Protocol (IP)|IP address]], TCP flags, ect. We refer to this as packet classification. This is deployed by many applications such as:
- Firewalls,
- Resource reservation protocols, and
- Routing based on traffic type.

![[packet_classification.png]]

**Example for traffic type sensitive routing.** The above figure shows an example topology where networks are connected through router R. Destinations are shown as S1, S2, X, Y, and D. L1 and L2 denote specific connection points for router R. The table shows some examples of packet classification rules. The first rule is for routing video traffic from S1 to D via L1. The second rule drops all traffic from S2, for example, in the scenario that S2 was an experimental site. Finally, the third rule reserves 50 Mbps of traffic from prefix X to prefix Y, which is an example of a rule for resource reservation.

## Simple solutions

