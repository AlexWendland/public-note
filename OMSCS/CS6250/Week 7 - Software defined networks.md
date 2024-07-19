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