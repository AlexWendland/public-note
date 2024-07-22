---
aliases: 
checked: false
course: "[[CS6250 Computer Networks]]"
created: 2024-07-22
last_edited: 2024-07-22
publish: true
tags:
  - OMSCS
type: lecture
week: 9
---
# Week 9 - Censorship

## Additional reading

### Important Readings

Towards a Comprehensive Picture of the Great Firewall’s DNS Censorship  
[https://www.usenix.org/system/files/conference/foci14/foci14-anonymous.pdfLinks to an external site.](https://www.usenix.org/system/files/conference/foci14/foci14-anonymous.pdf)

Ignoring the Great Firewall of China  
[https://www.cl.cam.ac.uk/~rnc1/ignoring.pdfLinks to an external site.](https://www.cl.cam.ac.uk/~rnc1/ignoring.pdf)

Global Measurement of DNS Manipulation  
[https://www.cc.gatech.edu/~pearce/papers/dns_usenix_2017.pdfLinks to an external site.](https://www.cc.gatech.edu/~pearce/papers/dns_usenix_2017.pdf)

Analysis of Country-wide Internet Outages Caused by Censorship  
[https://www.caida.org/publications/papers/2011/outages_censorship/outages_censorship.pdfLinks to an external site.](https://www.caida.org/publications/papers/2011/outages_censorship/outages_censorship.pdf)

Augur: Internet-Wide Detection of Connectivity Disruptions  
[https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7958591Links to an external site.](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=7958591)

Adapting Social Spam Infrastructure for Political Censorship  
[https://www.icir.org/vern/papers/kremlin-bots.leet11.pdfLinks to an external site.](https://www.icir.org/vern/papers/kremlin-bots.leet11.pdf)

Five incidents, one theme: Twitter spam as a weapon to drown voices of protests   
[https://www.usenix.org/system/files/conference/foci13/foci13-verkamp.pdfLinks to an external site.](https://www.usenix.org/system/files/conference/foci13/foci13-verkamp.pdf)

## DNS censorship

![[DNS censorship]]

![[Great Firewall of China (GFW)]]

Researchers have tried to reverse engineer the GFW and to understand how it works. Researchers have started to identify some of the properties: 

1. _Locality of [[Great Firewall of China (GFW)|GFW]] nodes_: There are two differing notions on whether the GFW nodes are present only at the edge [[Internet Service Provider (ISP)|ISPs]] or whether they are also present in non-bordering Chinese [[Autonomous system (AS)|ASs]]. The majority view is that censorship nodes are present at the edge.
2. _Centralized management_: Since the blocklists obtained from two distinct GFW locations are the same, there is a high possibility of a central management (GFW Manager) entity that orchestrates blocklists.
3. _Load balancing_: GFW load balances between processes based on source and destination IP address. The processes are clustered together to collectively send injected DNS responses.

## DNS injection

![[DNS injection]]

To detect [[DNS injection]] you can use probing techniques to search for injected paths. 