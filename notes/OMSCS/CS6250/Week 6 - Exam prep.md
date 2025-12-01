---
aliases:
checked: false
course: '[[CS6250 Computer Networks]]'
created: 2024-06-15
draft: false
last_edited: 2024-06-15
tags:
  - OMSCS
type: lecture
week: 6
---
# Week 6 - Exam prep

## Lesson 1: Introduction, History, and Internet Architecture

- What are the advantages and disadvantages of a layered architecture?

- What are the differences and similarities between the OSI model and the five-layered Internet model?

- What are sockets?

- Describe each layer of the OSI model.

- Provide examples of popular protocols at each layer of the five-layered Internet model.

- What is encapsulation, and how is it used in a layered model?

- What is the end-to-end (e2e) principle?

- What are the examples of a violation of e2e principle?

- What is the EvoArch model?

- Explain a round in the EvoArch model.

- What are the ramifications of the hourglass shape of the internet?

- Repeaters, hubs, bridges, and routers operate on which layers?

- What is a bridge, and how does it “learn”?

- What is a distributed algorithm?

- Explain the Spanning Tree Algorithm.

- What is the purpose of the Spanning Tree Algorithm?

## Lesson 2: Transport and Application Layers

- What does the transport layer provide?

- What is a packet for the transport layer called?

- What are the two main protocols within the transport layer?

- What is multiplexing, and why is it necessary?

- Describe the two types of multiplexing/demultiplexing.

- What are the differences between UDP and TCP?

- When would an application layer protocol choose UDP over TCP?

- Explain the TCP Three-way Handshake.

- Explain the TCP connection tear down.

- What is Automatic Repeat Request or ARQ?

- What is Stop and Wait ARQ?

- What is Go-back-N?

- What is selective ACKing?

- What is fast retransmit?

- What is transmission control, and why do we need to control it?

- What is flow control, and why do we need to control it?

- What is congestion control?

- What are the goals of congestion control?

- What is network-assisted congestion control?

- What is end-to-end congestion control?

- How does a host infer congestion?

- How does a TCP sender limit the sending rate?

- Explain Additive Increase/Multiplicative Decrease (AIMD) in the context of TCP.

- What is a slow start in TCP?

- Is TCP fair in the case where connections have the same RTT? Explain.

- Is TCP fair in the case where two connections have different RTTs? Explain.

- Explain how TCP CUBIC works.

- Explain TCP throughput calculation.

## Lesson 3: Intradomain Routing

- What is the difference between forwarding and routing?

- What is the main idea behind a link-state routing algorithm?

- What is an example of a link-state routing algorithm?

- Walk through an example of the link-state routing algorithm.

- What is the computational complexity of the link-state routing algorithm?

- What is the main idea behind the distance vector routing algorithm?

- Walk through an example of the distance vector algorithm.

- When does the count-to-infinity problem occur in the distance vector algorithm?

- How does poison reverse solve the count-to-infinity problem?

- What is the Routing Information Protocol (RIP)?

- What is the Open Shortest Path First (OSPF) protocol?

- How does a router process advertisements?

- What is hot potato routing?

## Lesson 4: AS Relationships and Interdomain Routing

- Describe the relationships between ISPs, IXPs, and CDNs.

- What is an AS?

- What kind of relationship does AS have with other parties?

- What is BGP?

- How does an AS determine what rules to import/export?

- What were the original design goals of BGP? What was considered later?

- What are the basics of BGP?

- What is the difference between iBGP and eBGP?

- What is the difference between iBGP and IGP-like protocols (RIP or OSPF)?

- How does a router use the BGP decision process to choose which routes to import?

- What are the 2 main challenges with BGP? Why?

- What is an IXP?

- What are four reasons for IXP's increased popularity?

- Which services do IXPs provide?

- How does a route server work?
    ``
## Lesson 5: Router Design and Algorithms (Part 1)

- What are the basic components of a router?

- Explain the forwarding (or switching) function of a router.

- The switching fabric moves the packets from input to output ports. What are the functionalities performed by the input and output ports?

- What is the purpose of the router’s control plane?

- What tasks occur in a router?

- List and briefly describe each type of switching. Which, if any, can send multiple packets across the fabric in parallel?

- What are two fundamental problems involving routers, and what causes these problems?

- What are the bottlenecks that routers face, and why do they occur?

- Convert between different prefix notations (dot-decimal, slash, and masking).

- What is CIDR, and why was it introduced?

- Name 4 takeaway observations around network traffic characteristics. Explain their consequences.

- Why do we need multibit tries?

- What is prefix expansion, and why is it needed?

- Perform a prefix lookup given a list of pointers for unibit tries, fixed-length multibit ties, and variable-length multibit tries.

- Perform a prefix expansion. How many prefix lengths do old prefixes have? What about new prefixes?

- What are the benefits of variable-stride versus fixed-stride multibit tries?

## Lesson 6: Router Design and Algorithms (Part 2)

- Why is packet classification needed?

- What are three established variants of packet classification?

- What are the simple solutions to the packet classification problem?

- How does fast searching using set-pruning tries work?

- What’s the main problem with the set pruning tries?

- What is the difference between the pruning approach and the backtracking approach for packet classification with a trie?

- What’s the benefit of a grid of tries approach?

- Describe the “Take the Ticket” algorithm.

- What is the head-of-line problem?

- How is the head-of-line problem avoided using the knockout scheme?

- How is the head-of-line problem avoided using parallel iterative matching?

- Describe FIFO with tail drop.

- What are the reasons for making scheduling decisions more complex than FIFO?

- Describe Bit-by-bit Round Robin scheduling.

- Bit-by-bit Round Robin provides fairness; what’s the problem with this method?

- Describe Deficit Round Robin (DRR).

- What is a token bucket shaping?

- In traffic scheduling, what is the difference between policing and shaping?

- How is a leaky bucket used for traffic policing and shaping?
