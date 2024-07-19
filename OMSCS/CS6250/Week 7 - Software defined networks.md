---
aliases: 
checked: false
course: "[[CS6250 Computer Networks]]"
created: 2024-07-19
last_edited: 2024-07-19
publish: true
tags:
  - OMSCS
type: lecture
week: 7
---
# Week 7 - Software defined networks

![[Software defined networks (SDN)]]

## Additional reading

### Important Readings

The Road to SDN: An Intellectual History of Programmable Networks  
[https://www.sigcomm.org/sites/default/files/ccr/papers/2014/April/0000000-0000012.pdfLinks to an external site.](https://www.sigcomm.org/sites/default/files/ccr/papers/2014/April/0000000-0000012.pdf "Link")

### Book References

Kurose-Ross, 7th Edition. Section 4.1.1

Kurose-Ross, 7th Edition. Chapter 5

### Optional Readings

SDN Controllers: Benchmarking & Performance Evaluation  
[https://arxiv.org/pdf/1902.04491.pdfLinks to an external site.](https://arxiv.org/pdf/1902.04491.pdf)

SDN Architecture  
[https://www.opennetworking.org/wp-content/uploads/2013/02/TR_SDN_ARCH_1.0_06062014.pdfLinks to an external site.](https://www.opennetworking.org/wp-content/uploads/2013/02/TR_SDN_ARCH_1.0_06062014.pdf)

### Optional Activity

OpenDaylight Application Developer’s Tutorial

## History

There was two main factors in the drive to switch to [[Software defined networks (SDN)|SDNs]]:
- Diversity of device types: after [[Router|routers]] and [[Switch|switches]] the introduction of  [[Middleboxes|middleboxes]] caused an explosion of devices network mangers had to look after.
- Proprietary Technologies: A lot of the software ran on [[Router|routers]], [[Switch|switches]], and [[Middleboxes|middleboxes]] was closed and configuration interfaces varied between vendors.
Therefore we needed to separate tasks up and define a well defined and consistent interface between the control plane and data plane of these devices.

There were 3 main steps in the journey to the definition of an [[Software defined networks (SDN)|SDN]].

### 1. Active Networks (Mid-1990s to Early 2000s)

**Goal:** Introduce a programmable network interface (network API) to customise packet handling and innovate network services despite the slow standardisation process by [[IETF]].

**Approaches:**

- **Capsule Model:** In-band code carried in data packets.
- **Programmable Router/Switch Model:** Code carried via out-of-band mechanisms.

**Contributions:**

- Lowering innovation barriers through programmability.
- Enabling network virtualisation for experimentation.
- Proposing unified control over [[Middleboxes|middleboxes]].

**Challenges:** Too ambitious, requiring end-user programming and facing trust, performance, and security issues.

### 2. Control and Data Plane Separation (2001 to 2007)

**Goal:** Improve network reliability, predictability, and performance by separating the control and data planes in response to increasing traffic volumes.

**Innovations:**

- **Open Interface:** Between control and data planes.
- **Centralised Control:** Logically centralised network control.

**Contributions:**

- Path selection based on traffic load.
- Minimising routing change disruptions.
- Handling attack traffic and enabling customer control.

**Challenges:** Initial scepticism about separating control and data planes, leading to foundational concepts for [[OpenFlow]] API.

### 3. OpenFlow API and Network Operating Systems (2007 to 2010)

**Goal:** Facilitate scalable network experimentation and practical deployment through programmable networks.

**Innovations:**

- **OpenFlow Switches:** Use tables of packet-handling rules to manage traffic.

**Contributions:**

- Supported large-scale network experimentation.
- Improved data-centre network traffic management.
- Encouraged investment in control program development over proprietary switches.

**Effects:**

- Generalised network device functions.
- Introduced the vision of a network operating system.
- Developed distributed state management techniques.

## [[Software defined networks (SDN)|SDN]] functionality

### Separation of Data and Control Plane

There were two main pushes for this:
1. Independent evolution and development.
2. Control from higher-level software.

This led to developments in many areas such as: Data centres, routing, enterprise networks, and research networks. Through the ability to control the behaviour of all devices through a single centralised point.

The main role of the data plane is the forwarding of packets based on some [[Forwarding information base (FIB)|FIB]], whereas the main role of the control plane is [[Routing|routing]] which mainly involves updating the [[Forwarding information base (FIB)|FIB]] once it has computed the route a particular packet should take. 

A [[Software defined networks (SDN)|SDN]] moves the control plane from being on the device to being located somewhere else on the network. It defines a clean API on how this networked control plane can interact and update the [[Forwarding information base (FIB)|FIB]] on the device.

![[snd_example.png]]

## Architecture

There are 3 separate layers to the architecture:

- **SDN-controlled network elements**: The SDN-controlled network elements, sometimes called the infrastructure layer, is responsible for the forwarding of traffic in a network based on the rules computed by the SDN control plane. 
- **SDN controller**: The **SDN controller** is a logically centralized entity that acts as an **interface between the network elements and the network-control applications.** 
- **Network-control applications**: The network-control applications are programs that manage the underlying network by collecting information about the network elements with the help of SDN controller.

![[sdn_arciteture.png]]

These components have two important interfaces.
- Southbound API: Connecting the SDN controller to the SDN-Controlled switches.
- NorthboundAPI: Allowing other network applications to interface with the SDN controller.

There are 4 important features of this architecture:

1. **Flow-based forwarding:** The rules for forwarding packets in the SDN-controlled switches can be computed based on any number of header field values in various layers such as the transport-layer, network-layer and link-layer. This differs from the traditional approach where only the destination IP address determines the forwarding of a packet. For example, [[OpenFlow]] allows up to 11 header field values to be considered. 
2. **Separation of data plane and control plane:** The SDN-controlled switches operate on the data plane and they only execute the rules in the flow tables. Those rules are computed, installed, and managed by software that runs on separate servers. 
3. **Network control functions:** The SDN control plane, (running on multiple servers for increased performance and availability) consists of two components: the controller and the network applications. The controller maintains up-to-date network state information about the network devices and elements (for example, hosts, switches, links) and provides it to the network-control applications. This information, in turn, is used by the applications to monitor and control the network devices. 
4. **A programmable network:** The network-control applications act as the “brain” of SDN control plane by managing the network. Example applications can include network management, traffic engineering, security, automation, analytics, etc. For example, we can have an application that determines the end-to-end path between sources and destinations in the network using Dijkstra’s algorithm.

### Controller Architecture

The controller itself is broken down into a further 3 layers. These handle each of its separate responsibilities. 

1. **Communication Layer**: This layer consists of a protocol through which the SDN controller and the network controlled elements communicate. Using this protocol, the devices send locally observed events to the SDN controller providing the controller with a current view of the network state. For example, these events can be a new device joining the network, heartbeat indicating the device is up, etc. The communication between SDN controller and the controlled devices is known as the “southbound” interface. [[OpenFlow]] is an example of this protocol, which is broadly used by SDN controllers today.
2. **Network-wide state-management layer**: This layer is about the network-state that is maintained by the controller. The network-state includes any information about the state of the hosts, links, switches and other controlled elements in the network. It also includes copies of the flow tables of the switches. Network-state information is needed by the SDN control plane to configure the flow tables.
3. **The interface to the network-control application layer:** This layer is also known as the controller’s “northbound” interface using which the SDN controller interacts with network-control applications. Network-control applications can read/write network state and flow tables in controller’s state-management layer. The SDN controller can notify applications of changes in the network state, based on the event notifications sent by the SDN-controlled devices. The applications can then take appropriate actions based on the event. A REST interface is an example of a northbound API.

![[sdn_controller_architecture.png]]

The SDN controller, although viewed as a monolithic service by external devices and applications, is implemented by distributed servers to achieve fault tolerance, high availability and efficiency. Despite the issues of synchronization across servers, many modern controllers such as OpenDayLight and ONOS have solved it and prefer distributed controllers to provide highly scalable services.

## Readings for part 2

### Important Readings

Software-Defined Networking: A Comprehensive Survey  
[https://arxiv.org/pdf/1406.0440.pdfLinks to an external site.](https://arxiv.org/pdf/1406.0440.pdf "Link")

ONOS: Towards an Open, Distributed SDN OS  
[https://www-cs-students.stanford.edu/~rlantz/papers/onos-hotsdn.pdf Links to an external site.](https://www-cs-students.stanford.edu/~rlantz/papers/onos-hotsdn.pdf)

P4: Programming Protocol-Independent Packet Processors  
[https://www.sigcomm.org/sites/default/files/ccr/papers/2014/July/0000000-0000004.pdfLinks to an external site.](https://www.sigcomm.org/sites/default/files/ccr/papers/2014/July/0000000-0000004.pdf)

A Software-Defined Internet Exchange  
[https://dl.acm.org/doi/pdf/10.1145/2740070.2626300?download=trueLinks to an external site.](https://dl.acm.org/doi/pdf/10.1145/2740070.2626300?download=true)

### Optional Readings

P4 Language tutorial  
[https://github.com/p4lang/tutorials/tree/master/exercises/basicLinks to an external site.](https://github.com/p4lang/tutorials/tree/master/exercises/basic)

An Industrial-Scale Software Defined Internet Exchange Point  
[https://www.usenix.org/system/files/conference/nsdi16/nsdi16-paper-gupta.pdfLinks to an external site.](https://www.usenix.org/system/files/conference/nsdi16/nsdi16-paper-gupta.pdf)

 _As you go through this lesson, there will be links for optional tutorials on various SDN technologies._

## Advantages of [[Software defined networks (SDN)|SDN]]s

1. **Shared abstractions:** These middlebox services (or network functionalities) can be programmed easily now that the abstractions provided by the control platform and network programming languages can be shared.
2. **Consistency of same network information**: All network applications have the same global network information view, leading to consistent policy decisions while reusing control plane modules
3. **Locality of functionality placement:** Previously, the location of middleboxes was a strategic decision and big constraint. However, in this model, the middlebox applications can take actions from anywhere in the network.
4. **Simpler integration:** Integrations of networking applications are smoother. For example, load balancing and routing applications can be combined sequentially.

![[sdn_advantages.png]]



