---
aliases:
checked: false
course_code: CS6250
course_name: Computer Networks
created: 2024-06-11
draft: false
last_edited: 2024-06-11
tags:
  - OMSCS
title: Week 5 - Router design and algorithms
type: lecture
week: 5
---
 Part 1

# Additional reading

## Important Readings

Survey and Taxonomy of IP Address Lookup Algorithms
[https://pdfs.semanticscholar.org/71d9/018e900f99ff60653b3769160131e775873f.pdfLinks to an external site.](https://pdfs.semanticscholar.org/71d9/018e900f99ff60653b3769160131e775873f.pdf)

## Book References

Kurose-Ross, 6th Edition, Section 4.3

Kurose-Ross, 7th Edition, Section 4.2

Varghese, Network Algorithmics, Sections: 1.1.2,  2.3.2,  Chapter 11

# What is inside a router

There are two parts of a router.
- The forwarding plane, and
- The Control plane.

![Router Seperation Of Planes](../../../static/images/router_seperation_of_planes.png)

The forwarding plane is responsible for getting messages forwarded when they arrive at the router. Which has 3 main components:
- **Input queue**: responsible for finishing the [layer 1](../../general/layer_1_physical.md) process and [de-encapsulation](../../general/encapsulation.md) the message to get the [IP address](../../general/internet_protocol_(ip).md). The it looks up where it has to go and moves it onto the switching fabric.
- **Switching fabric**: Only responsible for getting messages from the input queue to the correct output queue.
- **Output queue**: The same as the input but backwards.

![Router Input Que](../../../static/images/router_input_que.png)
![Router Output Que](../../../static/images/router_output_que.png)

The control plane refers to the implementation of the [router](../../general/router.md) [protocols](../../general/protocol_(networks).md). This mainly involves keeping the forwarding table up to date.

![Router Control Plane](../../../static/images/router_control_plane.png)

# Router architecture

Here we depict what happens when a [packet](../../general/packets.md) arrives at the router.

![Router Arcitecture](../../../static/images/router_arcitecture.png)

The most time sensitive operations are lookup, switching and scheduling.

- **Lookup**: When a packet arrives this uses the [IP address](../../general/internet_protocol_(ip).md) to find the output link in the [Forwarding information base (FIB)](../../general/forwarding_information_base_(fib).md). It uses longest prefix matching to do this. Some routers offer more complicated lookups using [ports](../../general/port.md) and other criteria.
- **Switching**: This involves moving from the input link to the output link. Modern routers will use crossbar switching. Though scheduling this can be complicated if multiple inputs want to go to the same output.
- **Queuing**: This is exactly what it sounds like. Some routers use a FIFO queue but they can deploy more complicated weighted queues to implement delay guarantees or fair bandwidth allocation.
- **Header validation and checksum**: Check the packet, update [TTL](../../general/time_to_live_(ttl).md) and recalculate the checksum.
- **Route processing**: Building the [Forwarding information base (FIB)](../../general/forwarding_information_base_(fib).md). This uses [protocols](../../general/protocol_(networks).md) such as [RIP](../../general/routing_information_protocol_(rip).md), or [OSPF](../../general/open_shortest_path_first_(ospf).md).
- **Protocol processing**: The routers need to implement: [SNMP](../../general/simple_network_management_protocol_(snmp).md), [TCP](../../general/transmission_control_protocol_(tcp).md), [UDP](../../general/user_datagram_protocol_(udp).md), and [ICMP](../../general/internet_control_message_protocol_(icmp).md) for sending error messages.

# Switching fabric

This can be accomplished in one of 3 ways.

## Via Memory

Input/Output ports operate as I/O devices in an operating system, controlled by the routing processor. When an input port receives a packet, it sends an interrupt to the routing processor, and the packet is copied to the processor's memory. Then the processor extracts the destination address and looks into the forward table to find the output port, and finally, the packet is copied into that output's port buffer.

![Switching Memory](../../../static/images/switching_memory.png)

## Via bus

In this case, the routing processor does not intervene as we saw the switching via memory. When an input port receives a new packet, it puts an internal header that designates the output port, and it sends the packet to the shared bus. Then all the output ports will receive the packet, but only the designated one will keep it. When the packet arrives at the designated output port, the internal header is removed from the packet. Only one packet can cross the bus at a given time, so the speed of the bus limits the speed of the router.

![Switching Bus](../../../static/images/switching_bus.png)

## Via interconnected network (crossbar)

A crossbar switch is an interconnection network that connects $N$ input ports to $N$ output ports using $2N$ buses. Horizontal buses meet the vertical buses at crosspoints controlled by the switching fabric. For example, let's suppose that a packet arrives at port A that will need to be forwarded to output port Y, the switching fabric closes the crosspoint where the two buses intersect so that port A can send the packets onto the bus, and then the packet can only be picked up by output port Y. Crossbar network can carry multiple packets at the same time, as long as they are using different input and output ports. For example, packets can go from A-to-Y and B-to-X simultaneously.

![Switching Crossbar](../../../static/images/switching_crossbar.png)

# Problems facing routers

Modern routing facing a lot of problems when handling the scale of the internet.

1. **Bandwidth and Internet Population scaling**: These are caused by
	1. Increased number of devices connected to the internet.
	2. Increasing volumes of network traffic.
	3. New devices that can operate at high speeds.
2. **Services at high speeds**: New devices that need to operate at high speeds which can be effected by congestion or attacks on the network.

![Router Problems](../../../static/images/router_problems.png)

**Longest prefix matching** Matching a packet to the [FIB](../../general/forwarding_information_base_(fib).md) can be complicated. New routers offer more complicated lookups as well.

**Service differentiation** This allows routers to offer per service guarantees such as delay insurance and fairness within services. This requires the router to inspect packets deeper than it otherwise would.

**Switching limitation** Moving packets from the input to output link has some hard limitations to it as we will see with head of line blocking.

**Bottlenecks about services** Providing performance guarantees at high speed such as measurements and security.

# Prefix-match Lookups

Matching addresses to entries in the [FIB](../../general/forwarding_information_base_(fib).md) is one of the most time sensitive and mathematically hard operations in a router.

## Prefix notation

Here we denote prefixes in 3 ways.

- **Wildcard**: Here we just write the prefix of the address and then use a \* to denote the end of the prefix.
- **Slash notation**: We provide the [IP address](../../general/internet_protocol_(ip).md) followed by a slash and the size of the relevant prefix in [bits](../../general/bit.md). i.e. 123.0.0.0/8.
- **Masking**: We provide the [IP address](../../general/internet_protocol_(ip).md) with the [network mask](../../general/network_mask.md).

## Variable length prefixes

In the early days of the [Internet](../../general/internet.md) there were fixed length prefixes. Though this drove the problem that [we are running out of IPv4 addresses on the pubic internet](../../general/we_are_running_out_of_ipv4_addresses_on_the_pubic_internet.md).

## Better lookup algorithms

There are many problems that just the lookup process faces.

1. Measurement studies on network traffic had shown a large number (in the order of hundreds of thousands - 250,000 according to a measurement study in the earlier days of the Internet) of concurrent flows of short duration. This already large number has only been increasing, and as a consequence, caching solutions will not work efficiently.
2. The important element of any lookup operation is how fast it is done (lookup speed). A large part of the cost of computation for lookup is accessing memory.
3. An unstable routing protocol may adversely impact the update time in the table: add, delete or replace a prefix. Inefficient routing protocols increase this value up to additional milliseconds.
4. A vital trade-off is memory usage. We can use expensive fast memory (cache in software, SRAM in hardware) or cheaper but slower memory (e.g., DRAM, SDRAM).

![Lookup Problems](../../../static/images/lookup_problems.png)

# Unibit Tries

[Trie](../../general/trie.md)

We can use [subnet](../../general/subnets.md) to form a [trie](../../general/trie.md) over the alphabet of $\{0, 1\}$ with values being the [subnets](../../general/subnets.md). To generate the [trie](../../general/trie.md) we build a path from the root for every address in our table and label the end node with that [subnet](../../general/subnets.md).

> [!example] Prefix-match lookup
> Suppose we have the following table
> ![Prefix Table](../../../static/images/prefix_table.png)
> then we use these strings to construct the following [trie](../../general/trie.md).
> ![Prefix Trie](../../../static/images/prefix_trie.png)
> we do not include the left branch of this [trie](../../general/trie.md). We also compress one-way branches for example in P9.

Then we use this [trie](../../general/trie.md) as the description entails.

# Multibit tries

Whilst unibit [tries](../../general/trie.md) is very efficient in terms of space they can be slow in terms of memory lookups. For a substring of length $n$ you may need to look up $n$ times. Instead we can increase the length of the "stride" and go for a longer alphabet.

We have two approaches here.
- Fix stride length $k$ generating $2^k$ children.
- Variable length stride depending on the number of children, like P9 above.

## Fixed length multibit tries

Here we pick a length of stride $k$ and then cut our [subnets](../../general/subnets.md) into multiples of $k$. If a [subnet](../../general/subnets.md) length is not a multiple of $k$ then we expand it to all the address of the next multiple of $k$ that would be covered b it. If no other longer address clashes with it, we label that address with the [subnet](../../general/subnets.md) it came from.

> [!example] Prefix expansion
> Suppose we set $k=3$ then using the table from the previous example lets do prefix expansion.
> ![Prefix Expansion](../../../static/images/prefix_expansion.png)

Then we construct the multibit [trie](../../general/trie.md) the same way as the unibit [trie](../../general/trie.md) with the expanded addresses but with the alphabet set to bit strings of length $k$.

![Fixed Length Multibit Trie](../../../static/images/fixed_length_multibit_trie.png)

Notice here we only needed to have at most 3 lookups whereas before it was 5.

## Variable length multibit tries

In the previous example we can see by choosing length 3 words the table to the left is much larger than we needed it to be. P3 was only length 2 and we had no other entries in that table. This wastes space - so we can let the length of that string be 2 instead.

![Variable Length Trie](../../../static/images/variable_length_trie.png)

The optimal stride length can be chosen using [dynamic programming](../../general/dynamic_programming.md). Though they do not say how.

 Part 2

# Additional readings

## Book References

Varghese, Network Algorithmics, Chapters 12, 13, 14

Kurose-Ross, 6th Edition, Section 7.5.2

Kurose-Ross, 7th Edition, Section 9.5.2

# Packet classification

To guarantee more features within a [router](../../general/router.md) such as quality of service, security and protocol based handling of [packets](../../general/packets.md) we need to classify packets on more than just their destination [IP](../../general/internet_protocol_(ip).md).

These further classifications can be based on source [IP address](../../general/internet_protocol_(ip).md), TCP flags, ect. We refer to this as packet classification. This is deployed by many applications such as:
- Firewalls,
- Resource reservation protocols, and
- Routing based on traffic type.

![Packet Classification](../../../static/images/packet_classification.png)

**Example for traffic type sensitive routing.** The above figure shows an example topology where networks are connected through router R. Destinations are shown as S1, S2, X, Y, and D. L1 and L2 denote specific connection points for router R. The table shows some examples of packet classification rules. The first rule is for routing video traffic from S1 to D via L1. The second rule drops all traffic from S2, for example, in the scenario that S2 was an experimental site. Finally, the third rule reserves 50 Mbps of traffic from prefix X to prefix Y, which is an example of a rule for resource reservation.

# Simple solutions

## Linear search

Firewalls do a linear search through a rules table like above and keep track of the best match. This is fine for a small number of rules but scales linearly in the number of rules.

## Caching

If you are going to get a lot of similar [packets](../../general/packets.md) then caching could be used on top of another search algorithm. This has two problems
1. The cache-hit rate can be high (80-90%) but still need to perform searches on the misses,
2. If the underlying search like linear has poor performance this can still have low overall performance.

## Passing labels

This involves the sender attaching labels to the header that determine when happens to it. This means that intermediary routers do not need to reclassify packets on a path to the destination. Though this will require security to ensure bad actors can not abuse this. This is deployed in [Multiprotocol label switching (MPLS)](../../general/multiprotocol_label_switching_(mpls).md) and [DiffServ](../../general/diffserv.md).

# More [tries](../../general/trie.md)

Assume we are in a position where we need to use the destination and source [IP address](../../general/internet_protocol_(ip).md) to determine the rule. The address must match both the [subnets](../../general/subnets.md) and ties are broken first by the longest matching destination [subnet](../../general/subnets.md) then by the longest matching source [subnet](../../general/subnets.md).

A simple way to do this would be to construct the destination [trie](../../general/trie.md) then at the [leaf](../../general/leaf_(graph).md) nodes attach source [tries](../../general/trie.md).

>[!example] Set-Pruning [tries](../../general/trie.md)
> Suppose we have the following rule table.
> ![Set Pruning Trie Table](../../../static/images/set_pruning_trie_table.png)
> Then we attach the following [tries](../../general/trie.md) to the destination [trie](../../general/trie.md).
> ![Set Pruning Trie Example](../../../static/images/set_pruning_trie_example.png)
> Note that for the 00\* source trie we need to include all rules that could match that prefix in particular even rules that only match the 0\*.
>

The need to match all rules that could fit with the prefix means we have to repeat the same rule in multiple branches. This leads to a memory explosion in large examples.

> [!note] This prefers the longest matching source [subnet](../../general/subnets.md)
> This can be mitigated by switching the order of source and destination when constructing the [trie](../../general/trie.md).

# Backtracking

We could get around the memory problem by letting each rule only appear in one source [trie](../../general/trie.md). Then if you don't match in current source [trie](../../general/trie.md) you backtrack on the destination [trie](../../general/trie.md) and go to the next source [trie](../../general/trie.md). In the example above we get the following [trie](../../general/trie.md).

![Set Pruning Tries Backtrack](../../../static/images/set_pruning_tries_backtrack.png)

Whilst this reduces memory the downside to this approach is the time to compute the answer. If a [packet](../../general/packets.md) has lots of backtracking you have lots of memory lookups which is slow.

# Grid of [tries](../../general/trie.md)

We can get the best of both worlds if we precompute where the misses land in the backtracked [trie](../../general/trie.md). This means we don't need to recalculate the source path we had already walked. In the example above we would get the following.

![Grid Of Tries Example](../../../static/images/grid_of_tries_example.png)

# Scheduling and head of line blocking

## Scheduling

Assume we have an $N \times M$ crossbar switch with $N$ inputs and $M$ outputs, and $NM$ cross points. Each cross point needs to switched on and off so one input line only connects to one output line. We also would like to maximise input/output lines that are connected for better parallelism.

## Take-a-ticket algorithm

This is analogise to input lines taking a ticket to wait to be served by a given output line. The output lines serve the requests in order. This has rounds that follow the pattern.
1. Input ques make requests to output ques to send a message if needed.
2. The output queues grant tickets to the input queues.
3. The holder of the latest ticket for each output queue connects and passes its transaction on.

![Take A Ticket Example](../../../static/images/take_a_ticket_example.png)

However this algorithm has a clear problem if all the inputs want to connect to the same output.

[Head of line (HOL) blocking](../../general/head_of_line_(hol)_blocking.md)

If we can avoid [HOL blocking](../../general/head_of_line_(hol)_blocking.md) we achieve a big speedup. In the example above we could do the same message passing but in only 3 iterations. Though for this we sacrifice "fairness".

## Knockout scheme

This uses output queuing to get around [HOL blocking](../../general/head_of_line_(hol)_blocking.md). If our switching fabric operates $k$ times faster than outputs we can ... This is really not clear what on earth is going on here.

## Parallel iterative matching

Here we let input lines request access for each output line they have a packet for. This goes as follows:
1. Input lines request a route for each output lines they have a [packet](../../general/packets.md) for.
2. Output lines randomly select an input line to complete a transaction with.
3. If an input line has more than one offer it randomly selects a transaction to complete.
4. Connection happens.

![Parallel Iterative Matching](../../../static/images/parallel_iterative_matching.png)

# Custom Scheduling

Scheduling can allow different types of packets to get different services. This is done in real time so will need to be done at inter packet times.

## [FIFO](../../general/first_in_first_out_(fifo)_queue.md) with tail drop

Traditional schedule approach. Each input link is a [FIFO](../../general/first_in_first_out_(fifo)_queue.md) queue where if the queue is full any new additions get dropped.

## Need for Quality of Service (QoS)

If you have some QoS guarantees such as maximum delay or a given bandwidth you employ smarter scheduling techniques. Here it is useful to think of network flows - [packets](../../general/packets.md) that are all following the same route from source to destination. This flow will need to be recognisable from a header.

In the following examples you might want to make smarter routing decisions:
- Router support for congestion.
- Providing QoS guarantees to flows.
- Fair sharing of links among competing flows.

# Round Robin

This is a method to control bandwidth reservations in schedulers for multiple flows.

## Bit-by-bit round robin

If we could split [packets](../../general/packets.md) into bits we could employ absolute fairness by switching from flow to flow delivering each [bit](../../general/bit.md). This is a round robin.

We can not split packets up so we will simulate this by making a "round number" delivering packets based on this value assigned to each request.

Let $R(t)$ be the round number at time $t$. If the router can deliver packets at $\mu$ [bits](../../general/bit.md) a second and we have $N$ flows then
$$
\frac{dR}{dt} = \frac{\mu}{N}.
$$
For the $i$th packet in a flow of size $p(i)$ (in [bits](../../general/bit.md)) we will assign $S(i)$ and $F(i)$ to be the start and finish round number for that packet when it arrives in a queue at time $t$. We set $S(i) = \max(R(t), F(i-1))$ and $F(i) = S(i) + p(i)$ i.e. if there are no packets waiting for that flow the start round number should be now - otherwise it should start after the last packet is sent.

Though when do we send packets using this scheme?

## Packet-level fair queueing

This is a method that uses bit-by-bit round robin framework to make fair queues.

It achieves this by sending the packet that has the smallest finish time $F(i)$. It iteratively does this and increments the current round number to the finish time of the last packet whilst doing it.

![Rr 1](../../../static/images/rr_1.png)

![Rr 2](../../../static/images/rr_2.png)

![Rr 3](../../../static/images/rr_3.png)

![Rr 4](../../../static/images/rr_4.png)

Whilst this guarantees fairness keeping track of all the finishing time would require a propitiatory queue method which has time complexity of $\log(N)$. This makes it hard to operate at gigabit speeds.

## Deficit Round Robin (DRR)

Whilst the bit-by-bit round robin was completely fair and ensured bandwidth and delay guarantees the time complexity made it infeasible.

Instead we can use round robin to given each flow some allocation to use for packets. If the next packet size is less than their current allowance we send it reducing their allowance by that size. For this we set some *quantum size* for each flow $Q_i$ (this can be the same or different for each flow) and we have a deficit counter $D(i)$ for each flow. Then we do the following procedure.

```psuedo code
1. Loop forever
2. for each flow i
	1. Increment D(i) += Q_i
	2. While there is a next packet of size p such that p < D(i):
		1. Decremet D(i) -= p
		2. Send p
```

![Drr Example](../../../static/images/drr_example.png)

Deficit Round robin has one fail condition. If a flow has not had any packets for a while it allowance may build up which then could release a burst of packets. This might not be desirable if you want to guarantee a constant rate to other flows.

# Token bucket

Token bucket shaping is similar to Deficit round robin but here we limit the number of tokens in the counter by $B$ and restrict the inflow to a rate $R$ per second this enables:
1. limiting the average rate, and
2. limiting the maximum burst size.

![Token Bucket Shaping](../../../static/images/token_bucket_shaping.png)

If a packet arrives and the bucket does not have enough tokens we have two options:
1. Put it into a buffer and wait for that bucket to have enough tokens, this is traditional token bucket shaping, or
2. Drop the packet, this is called bucket policing.

This leads to very different traffic throughput on the router.

![Token Bcuket Traffic](../../../static/images/token_bcuket_traffic.png)

# Leaky bucket

There is a middle ground between policing and shaping that combines the benefits of both. Instead of having tokens added to the bucket instead think of it being the [packets](../../general/packets.md) we need to send. If there is room in the bucket we add the packet to the buffer and wait to send it. If the packet is too big to fit in the bucket we discard it. We then send packets at a constant rate in terms of size - thus the leak.

![Leaky Bucket](../../../static/images/leaky_bucket.png)

This can take a irregular flow and regularise it. This has the benefit of having a controlled size of buffer which can offset overflow.
