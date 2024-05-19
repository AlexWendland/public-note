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

### Lesson 3: OSI model

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

#### 567 Session, Presentation, and Application

When first created these layers had distinct purposes but now the distinction is a bit vague. Applications are free to control all of them.

These are what the applications do with the data once they have got it.

#### TCP/IP Model

This is a more modern model of networks that has 4 layers.

1. Network access
	1. Combines layer 1 and 2 of the OSI model
2. Internet
	1. The same as layer 3 of the OSI model
3. Host to host
	1. The same as layer 4 of the OSI model
4. Application
	1. The same as layer 5, 6, and 7 of the OSI model.

#### Encapsulation: Process of sending data

For an application to send data to another application across a network it needs to encapsulate it.

Layer 4 takes the data and adds the source and destination ports to the data to make it a *segment*.

Layer 3 takes the segment and adds a source and destination IP address to make it a *packet*.

Layer 2 takes the packet and adds a source and destination MAC address to make it a *frame*.

This is moved onto layer two to be passed along to its destination.

The reverse process is called de-encapsulation.



There is a competing model to the 

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