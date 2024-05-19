---
aliases: 
checked: false
course: "[[CS6250 Computer Networks]]"
created: 2024-05-19
last_edited: 2024-05-19
publish: true
tags:
  - OMSCS
type: lecture
week: 0
---
# Week 0 - Assumed knowledge

## Notes from Fundamentals course

I followed this [Fundamentals course](https://www.youtube.com/playlist?list=PLIFyRwBY_4bRLmKfP1KnZA6rZbRHtxmXi) to understand the basics.

### Lecture 1: Hosts and devices

Some terminology first:

- Hosts: Any device that sends or revives traffic.
	- Client: Initialises a request
	- Server: Responds to that request.

> [!Note] 
> These terms are relative to a single request a host can be a client in another request.

- Server: Is just a host that has software to serve specific kinds of requests.
- IP Address: Identity for a host on a network. This is 32-[[Bit|bits]] long.
	- These 32 bits are normally broken down into 4 8-bit chunks and written in decimal format as the human readable address. 
	- Subnetting: Normally host names a hierarchical. With sub networks owned by different teams having a given prefix.
- Networks: Are just logical groupings of hosts with similar connectivity requirements.
- Internet: Is just a massive interconnected network.

Signal strength decays over long distances.

- Repeater: Just repeats a signal to increase signal distance.

When joining lots of computers together there is a scaling problem if they all need to connect to one another. So instead we us a single entity to act as an intermediary.

- Hub: This is a multi-port repeater. I.e. everything it receives it sends to all connected devices.
- Bridges: Only have two ports but they know which devices are on either side. They will only repeat signals if the destination host is on the opposite side of the bridge.
- Switch: A multi-port bridge. This facilitates communication within a network.
	- Hosts on a switch normally all belong to a subnet and will have the same IP address prefix.
- Router: facilitates communication between networks.
	- Provides a traffic control point between networks. This is a good place to apply security filtering or redirecting.
	- Routing table: Routers keep a table of which addresses belong to which connection for redirecting messages like a switch.
	- Gateway: In addition to the routing table routers have an IP address on each network it is connected to, this is called the gateway address.
	- Routers make the hierarchy on the internet possible by owning the prefix for that sub network.

Whilst these devices are called routers and switches there is a more abstract concept here.

- Switching: The process of moving data within networks.
- Routing: The process of moving data between networks.

Many other devices can perform switching and routing other than a switch and a router.

### Lesson 2: OSI model

The ultimate goal of networking is to let hosts share data with one another. For this purpose the OSI model breaks down networking into 7 layers.

1. Physical
2. Data Link
3. Network
4. Transport
5. Session
6. Presentation
7. Application

#### 1 Physical

Tools that help transport the physical 10 bits from one host to another. For example:
- Cables,
- Wifi,
- Repeaters, or
- Hubs.

#### 2 Data Link

These are tools that put data on or off the physical transport layer. For example:
- Network Interface Cards (NIC),
- Wifi access cards, or
- Switches.

These devices all have unique MAC addresses. 

>[!tip] MAC Addresses
>These are 48-bit addresses that represent physical devices. These are made human readable by representing them as 12 hex digits (these are grouped into 2 characters and separated by - for windows : for Linux and in groups of 4 separated by a . SISCO routers and switches)

#### 3 Network

This layer works with entities identified by an IP address. Devices at level 3 are:
- Hosts, or
- Routers.

What is the difference between MAC addresses and IP addresses?

For any packet of data we attach the source and destination IP address. This packet may need to travel through different networks. For this purpose within a network we attach the source and destination MAC address for where it has to go within that network. This is then removed when it goes through a router.

Address Resolution Protocols (ARP) combine layer 2 MAC addresses and layer 3 IP
addresses.

#### 4 Transport

This layer is responsible for getting data going between two hosts to go to the correct service. It does this using ports. There are two different types of ports.
- 0-65535 TCP, which favours reliability, or
- 0-65535 UDP, which favours efficiency.

A packet sent to a server will also contain a layer 4 header including the port.

#### 5 Session

Layer 5 is responsible for separating out users who might be connecting through the same lower levels of the OSI model or the same user who is switching between different networks to connect to the same server.

Browser cookies is an example of a layer 5 technology as it allows users to switch networks without having to login again.

#### 6 Presentation

Layer 6 is responsible for telling us the form the data is in. How should we break down the long binary expression into something the application can understand.

For example in HTTP it says characters are grouped into 8 bit sequences and interpreted as extended asci characters.

#### 7 Application

This layer determines what to do with this data. In a HTTP web server these would be the key words get, post, head ect.

#### 567 Session, Presentation, and Application

The roles and responsibilities of the last 3 layers get very mixed and end up being combined into one in other. Some applications might not implement some of them.

For example HTTP uses cookies for layer 5, extended ASCII for layer 6, and keywords for layer 7. Whereas FTP doesn't have a way to implement layer 5, uses the same extended ASCII for layer 6 but different commands for layer 7.

This mix of these layers is normally dependent on the protocol - so normally rolled up into one thing.

#### TCP/IP Model (4 Layer)

This is a more modern model of networks that has 4 layers.

1. Network access
	1. Combines layer 1 and 2 of the OSI model
2. Internet
	1. The same as layer 3 of the OSI model
3. Host to host
	1. The same as layer 4 of the OSI model
4. Application
	1. The same as layer 5, 6, and 7 of the OSI model.

![[model-comparison.png]]

#### Encapsulation: Process of sending data

For an application to send data to another application across a network it needs to encapsulate it.

Layer 4 takes the data and adds the source and destination ports to the data to make it a *segment*.

Layer 3 takes the segment and adds a source and destination IP address to make it a *packet*.

Layer 2 takes the packet and adds a source and destination MAC address to make it a *frame*.

This is moved onto layer two to be passed along to its destination.

The reverse process is called de-encapsulation.

![[osci-model-summary.png]]

### Lesson 3: How do hosts talk to one another

There are two important different cases to cover.

1. How host talk to one another on the same network, and
2. How hosts talk to one another on different networks.

#### Talking on the same network

When hosts talk to each other on the same network they need 3 identifying bits of information.
- MAC Address,
- IP Address, and
- subnet mask (this tells the host how many computers are on this network).

Suppose we need host A to send data to host B.

As host A is already part of the network it has the subnet mask already.

We will assume host A already has host B's IP address through a DNS entry or an act of god.

The only further information about host B host A needs is its mac address. To do this it will need to use the Address Resolution Protocol (ARP) as discussed before.

Every host has an ARP cache that stores the MAC address against each IP address it knows in the network. If host B's address is already in host A's ARP cache it can use that to generate the layer 2 and 3 headers.

If not it will need to make an ARP request to the network. It broadcasts its IP and MAC address on the network asking for the host at host B's IP address to respond. It does this by setting in the layer 2 header the all f's MAC address - an address reserved for the purpose of broadcasting to the local network.

Once host B gets this ARP request it can populate its ARP cache entry for host A then send an ARP response directly back (Unicast) to host A with its MAC address.

Now with host B's MAC address host A can now safely send the data directly to host B.

This is how computers on the same network communicate with each they use ARP to populate their ARP cache so they can directly communicate with one another.

#### Talking to computers on different networks

In this set up host A needs to send data to host C but there is a router in-between them. We assume host A already has host C's IP address.

It will know this IP is on a foreign network using host C's IP address and its own sub-net mask.

The first step for host A to send data to host C is to get it to its local router. It will know the address of that router as it will be set to the default gateway for host A. If this is the first time host A has connected to the router it can use ARP to find the routers IP address.

Host A now constructs the frame to send to the router it sets the layer 3 header using its IP address and host C's IP address. The it sets the layer 2 header using its MAC address and the routers MAC address and sends it off unicast to the network.

At this point the router takes the frame it receives strips out the layer 2 header to get a packet then it uses it's own ARP table to attach a new layer 2 header to send it further on. This could be directly to host C or to another router.

### Lesson 4: Everything switches do to communicate within a network

#### Rules of a switch

These are the rules for switching so applies to anything that can do switching.

When performing switching they only care about the layer 2 data so they don't know anything about IP addresses - only MAC addresses.

In a switch each device connects to a different port. The switch will maintain a MAC address table that maps different ports to MAC addresses. There are then 3 operations a switch can do.

- Learn,
- Flood, and
- Forward.

When a switch gets a frame from a new host it can *learn* that hosts MAC address as it will be the source MAC address of that frame. So it can add this to its MAC address table.

If the switch gets a message for a MAC address it doesn't know it will *flood* the network with that frame to make sure it gets to the intended host. This involves duplicating the frame and sending it on all ports that wasn't the port the package came from.

The idea is that hosts that do not match that MAC address throw away the frame as it is not for them.

If the switch already knows the hosts port in its MAC address table it *forwards* that frame on to the associated port for the destination.

As this all works on layer 2 and doesn't involve IP addresses the router on the network is just another host from the switches perspective.

>[!note] Switches MAC address
>Traffic going through a switch does not use a switches MAC address or IP address. However switches are hosts on that network so have an IP address and MAC address. These only get used if you are looking to connect directly to the switch to configure it.

#### Unicast flooding vs Brodcasts

Flooding is an action the switch takes when it does not know the port for a provided MAC address. This replicates the frame and sends it on all available ports. 

Broadcast is a type of frame that has the destination MAC address set as all f's. These will always get flooded by the switch as it will not have a port for the MAC address of all f's.

#### Virtual Local Area Networks (VLAN's)

VLAN's let you break a large physical switch into multiple virtual switches. It does this by breaking up its ports into small groups that each will be a virtual switch. This means messages within one port range can only go out to ports within that range.

#### Multiple switches

When multiple switches are on the same network - nothing really changes about the switches rules.

### Lesson 5: Everything a router does to communicate between networks

In RFC2460: Internet Protocol, Version 6 (IPv6) Specification it defines what a node, host, and router is.

- Node: A devise that implements IPv6.
- Router: A node that forwards IPV6 packets not explicitly addressed to itself.
- Host: Any node that is not a router.

In otherwards the only difference between a router and a host is that a host will drop a packet not matching its own IP address whereas a router will do its best to get that packet to its home.

A router keeps a table of all networks it knows about in its *routing table*. Different networks are identified by the part of the IP space associated to that network. The router will bind these different network spaces to interfaces of the router.

> [!note] Unknown packet address
> If a router gets a packet it does not know the address of it will just drop that packet.

#### Routing table

There are 3 ways a router can populate its routing table
1. Directly connected: This is for networks directly connected to the router.
2. Static route: This is a route that has been manually configured on a router. Instead on set of subdomains mapping to an interface it will instead have an IP address to forward that packet on to.
3. Dynamic routing: This is the same in structure to the static rout but instead of being manually added this gets populated by routers sharing known addresses with one another.

There are many different Dynamic routing protocols RIP, OSPF, BGP, EIGRP, IS-IS, ect They differ in how they discover new routers, what addresses they share, and how they share thous addresses.

#### Difference between an ARP table and a Router table

As routers have IP addresses on the networks associated to their interfaces they therefor have to have ARP tables for these networks.

The main difference between ARP tables and router tables is that ARP tables always start empty and can be fully populated through ARP. If the router gets a frame it doesn't have an ARP entry for it will use ARP to discover it - wheras if a router gets a packet it doesn't have a routing entry for it will drop that packet. 

#### Hierarchy helps with scaling

If you use a tree like network to connect routers the longest path grows like $\log(n)$ instead of linear designs that will grown as $n$. However there are more reasons to use a Hierarchy a base on the IP address.

With the entries in the routing table the subnet mask indicates what part of the IP address you need to match on. For example the routing table may look something like



### Lesson 6: 
## Preparation questions

- What is a “protocol”? What are some of the most well-known and used protocols?


- What is an ISP? What is an AS?
    
- What is the OSI layer model? What is the primary responsibility of each layer?
    
- How does the layered architecture of the internet allow fundamentally different technologies (such as WiFi vs. Ethernet) to be used together?
    
- What is the client-server model? What is the peer-to-peer model? What are the strengths and weaknesses of each?
    
- What is a port (number)? How is it used?
    
- What’s the difference between a well-known port number and an ephemeral port?
    
- What is TCP? What is UDP? What are some of the major differences between them?
    
- If you were developing a brand new application layer protocol, what aspects of TCP would make it more appealing to use? What aspects of UDP would make it more appealing to use?
    
- What is a socket? How is it used?
    
- Can you generally describe how HTTP works in an example (how the HTTP request is initiated, how the webserver receives the request, how the content is returned, etc.)?
    
- What is an IP address? How is it different than a MAC Address?
    
- What is a switch? What is a router? What are the major differences between the roles that they play in a network, classically?
    
- What is a default gateway?
    
- What happens to a message as it gets sent across a network, as far as encapsulation and protocol headers?
    
- What is DNS? At a high level, how does it work?