---
aliases: 
checked: false
course: "[[CS6250 Computer Networks]]"
created: 2024-07-27
last_edited: 2024-07-27
publish: true
tags:
  - OMSCS
type: lecture
week: 11
---
# Week 11 - CDNs and overlay networks

## Reading

### Important Readings

The Akamai Network: A Platform for High-Performance Internet Applications  
[https://dl.acm.org/doi/10.1145/1842733.1842736Links to an external site.](https://dl.acm.org/doi/10.1145/1842733.1842736)

Open Connect Everywhere: A Glimpse at the Internet Ecosystem through the Lens of the Netflix CDN  
[https://arxiv.org/pdf/1606.05519.pdf Links to an external site.](https://arxiv.org/pdf/1606.05519.pdf)

### Book References

Kurose-Ross, 7e, Section 2.4, DNS—The Internet’s Directory Service

Kurose-Ross, 7e, Section 2.6, Video Streaming and Content Distribution Networks

### Optional Readings

**Server Selection**

C3: Internet-Scale Control Plane for Video Quality Optimization  
[https://www.usenix.org/system/files/conference/nsdi15/nsdi15-paper-ganjam.pdf Links to an external site.](https://www.usenix.org/system/files/conference/nsdi15/nsdi15-paper-ganjam.pdf)

Shedding Light on the Structure of Internet Video Quality Problems in the Wild  
[https://conferences.sigcomm.org/co-next/2013/program/p357.pdfLinks to an external site.](https://conferences.sigcomm.org/co-next/2013/program/p357.pdf)

Where Do You “Tube”? Uncovering YouTube Server Selection Strategy  
[https://ieeexplore.ieee.org/document/6006028Links to an external site.](https://ieeexplore.ieee.org/document/6006028)

Google Data Centers  
[https://www.google.com/about/datacenters/inside/locations/index.htmlLinks to an external site.](https://www.google.com/about/datacenters/inside/locations/index.html)

Understanding Hybrid CDN-P2P: Why Limelight Needs Its Own Red Swoosh,  
[https://dl-acm-org.prx.library.gatech.edu/doi/10.1145/1496046.1496064Links to an external site.](https://dl-acm-org.prx.library.gatech.edu/doi/10.1145/1496046.1496064)

**User-perceived application experience**

Shedding Light on the Structure of Internet Video Quality Problems in the Wild  
[https://conferences.sigcomm.org/co-next/2013/program/p357.pdfLinks to an external site.](https://conferences.sigcomm.org/co-next/2013/program/p357.pdf)

EONA: Experience-Oriented Network Architecture  
[https://conferences.sigcomm.org/hotnets/2014/papers/hotnets-XIII-final121.pdfLinks to an external site.](https://conferences.sigcomm.org/hotnets/2014/papers/hotnets-XIII-final121.pdf)

Assessing Affinity Between Users and CDN Sites  
[https://www.isi.edu/~johnh/PAPERS/Fan15a.pdfLinks to an external site.](https://www.isi.edu/~johnh/PAPERS/Fan15a.pdf)

Developing a Predictive Model of Quality of Experience for Internet Video  
[https://www.cs.cmu.edu/~srini/papers/2013.Balachandran.sigcomm.pdf Links to an external site.](https://www.cs.cmu.edu/~srini/papers/2013.Balachandran.sigcomm.pdf)

Chord: A Scalable Peer-to-peer Lookup Service for Internet Applications  
[https://pdos.csail.mit.edu/papers/chord:sigcomm01/chord_sigcomm.pdf Links to an external site.](https://pdos.csail.mit.edu/papers/chord:sigcomm01/chord_sigcomm.pdf)

Reverse Engineering the Youtube Video Delivery Cloud  
[https://pdfs.semanticscholar.org/4c48/501e2aa3e9c3e2507617f8cec2db16b01490.pdf Links to an external site.](https://pdfs.semanticscholar.org/4c48/501e2aa3e9c3e2507617f8cec2db16b01490.pdf)

**On CDNs and ISPs Interplay**

Pushing CDN-ISP Collaboration to the Limit  
[https://www.akamai.com/content/dam/site/en/documents/research-paper/pushing-cdn-isp-collaboration-to-the-limit-technical-publication.pdf Links to an external site.](https://www.akamai.com/content/dam/site/en/documents/research-paper/pushing-cdn-isp-collaboration-to-the-limit-technical-publication.pdf)

**P2P and Gaming:** 

[http://ccr.sigcomm.org/online/files/p315.pdf Links to an external site.](http://ccr.sigcomm.org/online/files/p315.pdf)  
[https://conferences.sigcomm.org/sigcomm/2011/papers/sigcomm/p474.pdf Links to an external site.](https://conferences.sigcomm.org/sigcomm/2011/papers/sigcomm/p474.pdf)  
[http://ccr.sigcomm.org/online/files/p2p_gaming.pdf Links to an external site.](http://ccr.sigcomm.org/online/files/p2p_gaming.pdf)  
[https://www.cs.cmu.edu/~junchenj/c3.pdfLinks to an external site.](https://www.cs.cmu.edu/~junchenj/c3.pdf)

## [[Content delivery network (CDN)|CDN]] revisited

The classic way to make a service available on the internet was to host it on a single machine and let users find that IP. This has a number of draw backs for larger service providers:
- Your users might be dispersed over a large geographical area causing:
	- Latency for clients a long way away.
	- Excessive use of bandwidth if multiple users far away are accessing the same data. (Literally the same packets are being transmitted multiple times across the same path.)
	- Relying on multiple [[Internet Service Provider (ISP)|ISPs]] to route your traffic to your consumers.
- Your single server is a massive single point of failure.

Therefore large content providers use [[Content delivery network (CDN)|CDNs]].

![[Content delivery network (CDN)|CDN]]

However even using [[Content delivery network (CDN)|CDNs]] there are still massive challenges content providers face:
- **Peering point congestion**: There is financial motives to speed up the "first mile" to web hosts and "last mile" to customers. However, the real bottleneck appears in the middle mile with peering points between networks.
- **Inefficient routing protocols**: [[Boarder gateway protocol (BGP)|BGP]] was not built for modern demands - it only uses [[Autonomous system (AS)|AS]] hop count not factors like congestion and latency and well-documented security vulnerabilities for misconfiguration and malicious attacks.
- **Unreliable networks**: You rely on everyone in-between you and your consumer. So natural disaster, configuration failures, severing of underwater cables are all problems that might effect you.
- **Inefficient communication protocols**: [[Transmission Control Protocol (TCP)|TCP]] is also not designed for the modern internet with its over head of ACKing packets and congestion control. Although a lot of research has been put into replacing it - it is slow to take on.
- **Scalability**: Scaling up infrastructure is expensive and takes time. Therefore responding to random surges in current demand or scheduled increases can be hard.
- **Application limitation and slow adaption**: As there is so much old infrastructure it takes a long time for new [[Protocol (networks)|protocols]] to be adopted by internet browsers, routers and firewalls.

There have been two massive shifts in the internet infrastructure recently:
1. The sheer scale of users - this has pushed old [[Protocol (networks)|protocols]] and infrastructure to its limits.
2. The flattening of the internet - the rise of [[Internet Exchange Points (IXPs)|IXPs]] has shifted us from having [[Internet Service Provider (ISP)|ISPs]] as the backbone of the internet with a few connection points into a more flat well connected structure. 

Both these changes mean that more traffic is exchanged locally instead of traversing the whole hierarchy of the internet. This has been driven by large players such as google, facebook, and netfilx. For example see below netflixs [[Content delivery network (CDN)|CDN]] infrastructure across the globe.

![[netflix_infra.png]]

[[Content delivery network (CDN)|CDNs]] can be privately owned like in Netflix's case or owned by a third party such as Akamai and Limelight. 

Owning a [[Content delivery network (CDN)|CDN]] comes with many challenges:
- Owning lots of real-estate and physical hardware.
- Consuming a lot of power and requiring a lot of cooling.
- Staying well-connected to the internet.
- Managing performance and upgrading your infrastructure.

## [[Content delivery network (CDN)|CDN]] server placement

There is a spectrum with the philosophy on server placement. With the extremes represented below.

- **Enter deep**: Using lots of [[Content delivery network (CDN)|CDN]] access points close to end users.
	- This has the advantage of always being close to end users reducing latency and bandwidth usage.
	- This has the disadvantage of maintaining lots of different locations and distributing your content to them all quickly.
![[enter_deep.png]]
- **Bring home**: Using a few larger server clusters at key points.
	- Much easier to maintain and keep synchronised.
	- Larger latency and bandwidth use to get to end consumers. 

There are lots of hybrid approaches. Such as Google with 16 mega data-centers and 50 smaller clusters deeper into the network.

