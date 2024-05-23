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

![[Host (networks)]]

![[Client]]

![[Server]]

> [!Note] 
> These terms are relative to a single request a host can be a client in another request.

![[IP address]]

![[Subnets]]

![[Network]]

![[Internet]]

Signal strength decays over long distances.

![[Repeater]]

When joining lots of computers together there is a scaling problem if they all need to connect to one another. So instead we us a single entity to act as an intermediary.

![[Hub]]

![[Bridge]]

![[Switch]]

![[Router]]

![[Gateway]]

[[Router|Routers]] make the hierarchy on the internet possible by owning the prefix for that [[Subnets|subnet]].

Whilst these devices are called [[Router|routers]] and [[Switch|switches]] there is a more abstract concept here.

- [[Switching]]: The process of moving data within networks.
- [[Routing]]: The process of moving data between networks.

Many other devices can perform switching and routing other than a switch and a router.

### Lesson 2: [[Open Systems interconnection (OSI) model]]

![[Open Systems interconnection (OSI) model]]

![[Layer 1 Physical]]

![[Layer 2 Data Link]]

![[MAC address]]

![[Layer 3 Network]]

![[Difference between an IP and MAC address]]

![[Layer 4 Transport|layer 4]]

![[Layer 5 Session]]

![[Layer 6 Presentation]]

![[Layer 7 Application]]

The main other model of the internet is [[Internet Protocol Stack (IPS) 5 layers|IPS model]]

![[Internet Protocol Stack (IPS) 5 layers|IPS model]]

![[Connection between OSI and IPS models]]

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

In [[RFC2460 Internet Protocol, Version 6 (IPv6) Specification]] it defines what a node, host, and router is.

![[Node (IPv6)]]

![[Router (IPv6)]]

![[Host (networks)]]

In other words the only difference between a router and a host is that a host will drop a packet not matching its own IP address whereas a router will do its best to get that packet to its home.

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

The main difference between ARP tables and router tables is that ARP tables always start empty and can be fully populated through ARP. If the router gets a frame it doesn't have an ARP entry for it will use ARP to discover it - whereas if a router gets a packet it doesn't have a routing entry for it will drop that packet. 

#### Hierarchy helps with scaling

If you use a tree like network to connect routers the longest path grows like $\log(n)$ instead of linear designs that will grown as $n$. However there are more reasons to use a Hierarchy a base on the IP address.

With the entries in the routing table the subnet mask indicates what part of the IP address you need to match on. For example the routing table may look something like

| IP address | Subnet mask | Interface |
| ---------- | ----------- | --------- |
| 10.40.55.0 | 24          | R1        |
| 10.20.0.0  | 16          | R2        |

the first entry would say any IP address matching the first 24 bits or the first 3 decimals of the IP address go here whereas the second entry says any address matching the first 16 bits or 2 decimals then go here. The second entry is called router summerization. It is actually referring to a lot of sub nets but groups them all index one entry as the first step is always to go to a single router. This can only be done if you arrange your IP addresses in a hierarchical manner.

You can set a default route - this is one that matches on 0 bits. Then instead of dropping any unknown address you instead send it to the default route.

>[!note] Matching criteria
>If you have a default gateway then it will match with all addresses which might cause a conflict. By default the more specific a routing entry the higher priority that rule. Though rules can get more complicated than this.

### Lesson 6: Protocols

Protocol: Set of rules and messages that form an Internet standard.

Some were already described above. Such as [[Address Resolution Protocol (ARP)|ARP]] (RFC 826).

![[File Transfer Protocol (FTP)|FTP]]

#### Simple Mail Transfer Protocol (SMTP)

This is the mail mail servers communicate with users.

![[Hyper Text Transfer Protocol (HTTP)]]

#### Secure Sockets Layer (SSL) and Transport Layer Security (TLS)

Methods to establish secure communication between hosts.

#### Domain Name System (DNS)

This is the way you convert the name of your favourite website to their IP address.

#### Dynamic Host Configuration Protocol (DHCP)

To connect to the internet you need 4 bits of information:
- Your IP address,
- Your subnet mask,
- The default network of your local network, and
- The domain name server you will use.

The DHCP will provide you all the above information once you connect to a new network. When you first join you send DHCP discover message first and be provided with all your information.

## Preparation questions

- What is a “protocol”? What are some of the most well-known and used protocols?

A protocol is a set of messages and rules that are an internet standard. They can be found defined in RFC's. Some popular protocols are ARP, HTTP, TLS, and DNS.

- What is an ISP? What is an AS?

A ISP is an internet service provider. The offer connectivity to their network.

A Autonomous system (AS) is a collection of IP addresses with a common prefix all controlled by a single administrative entity or domain.

- What is the OSI layer model? What is the primary responsibility of each layer?

The Open System Interconnection model is the 7 conceptual layers of how connected systems work.

1. Physical: Cables and transportation of data.
2. Data Link: Devices that move data on and off the physical layer. Identifies actors by MAC addresses.
3. Network: Devices that work as the ultimate destination for data within a network. Uses IP addresses to distinguish actors.
4. Transport: The passes data going to the same host to different processes. This uses ports to distinguish entities.
5. Session: This allows users using the same process to be distinguished.
6. Presentation: This determines how the data should be interpreted.
7. Application: How the data will be used to run commands.

- How does the layered architecture of the internet allow fundamentally different technologies (such as WiFi vs. Ethernet) to be used together?

It established clear separation of concerns and the interfaces in which the operate by. For example for ethernet or Wifi as long as the data has been encapsulated properly these Physical layers are only responsible for getting data to the next entity in the network. 

- What is the client-server model? What is the peer-to-peer model? What are the strengths and weaknesses of each?

The client-server model is a distributed application structure with two roles. There are servers providing resources and clients requesting them. For example, a web-server follows the client server model. The user of the browser is the client and the server providing web-pages is the server.

Advantages
- A service that is centrally managed is easier to monitor.
- Easier to apply access controls and security to the system.
- With a centralised system you can gaurentee data integrity more easily.

Disadvantages
- Single point of failure if the server goes down.
- Higher start up cost as you require the infrastructure in the first place.
- Scaling can become complex as the server can become a big bottle neck.

The peer-to-peer model is a decentralised application architecture which has each participant being both consumer and provider of resources. Each peer offers some of its resources up to the network for other peers to use without central coordination. An example of this is Torrent file sharing.

Advantages
- Naturally scales as more people use the system.
- Cost effective as there is no centrally managed servers.
- Fault tolerant as any number of nodes going down does not stop the system working.

Disadvantages
- Security challenges as no central authority is dictating who is allowed into the network.
- Can not gaurentee data integrity of assets on the network. 
- Hard to manage and monitor as there is no central place collecting logs.

- What is a port (number)? How is it used?

A port number is how Layer 4 distinguishes different applications. It is used to separate up messages going to the same host.

- What’s the difference between a well-known port number and an ephemeral port?

![[Port]]

- What is TCP? What is UDP? What are some of the major differences between them?

![[Transmission Control Protocol (TCP)]]

![[User Datagram Protocol (UDP)]]

- If you were developing a brand new application layer protocol, what aspects of TCP would make it more appealing to use? What aspects of UDP would make it more appealing to use?

I would use TCP if I wanted to gaurentee integrity of the data and didn't care about latency whereas I would use UDP if I wanted a fast connection where packet replay was not important.

- What is a socket? How is it used?

![[Socket]]

- Can you generally describe how HTTP works in an example (how the HTTP request is initiated, how the webserver receives the request, how the content is returned, etc.)?

Yes I think so but that is a lot of writing.

- What is an IP address? How is it different than a MAC Address?

An IP address is the unique identifier for a host. This works for hosts that are not not the same network. This will be added to the message at Layer 3 and is responsible for checking the message is going to the correct host. MAC addresses are encapsulated at layer 2 and are only responsible for getting the frame to the correct host within a network.

- What is a switch? What is a router? What are the major differences between the roles that they play in a network, classically?

Switches are responsible for getting data between hosts on the same network. The have an ARP table and can do 3 operations, learn, flood and forward. These allow for the switch to learn about new hosts that are connected to its ports and find their MAC addresses. This device only cares about the layer 2 information of the message.

Routing on the other hand is responsible for getting packets to hosts that are not on their network. The maintain a route table that informs them about the IP addresses it knows where to route packets to. This operates on the Layer 3 information of the packet.

- What is a default gateway

The default gateway is the address of the main router in that network it is IP address that hosts add the MAC address of if the IP address is not in this network.

- What happens to a message as it gets sent across a network, as far as encapsulation and protocol headers?

Suppose we have a message we need to send to an application first we encode that information using the specification of layer 6 of the target application. We add headers to identify this user session in layer 5. Then we add the randomly assigned source port of the application sending the data and the destination port of the application we need to send the information to. Now we add the IP address of the machine sending the data and the IP address of the machine we want to send the data to. Then we use that IP address and the subnet mask to determine if the machine is on our network or a foriegn network. Then we either uses its address or the default gateway's address to look a MAC address of the next hop in the network in our ARP table - if we don't have it we use ARP to determine that MAC address in the network.

- What is DNS? At a high level, how does it work?

Domain Name Service map domain names to IP addresses. When connecting to a domain name like www.example.com first you go to your domain name provider to look up the associated IP address then once you have done that you can send the message to the server. Note this doesn't resolve the port of the application this would need to be known before hand. Lots of standard protocols use default ports.