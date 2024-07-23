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

There are multiple different techniques to use here. 

1. **Packet dropping**: For a specific set of [[Internet Protocol (IP)|IP addresses]] you drop packets going to or from that address.
	- Strengths:
		- Easy to implement
		- Low cost
	- Weaknesses:
		- Maintaining a block list can be hard if users rotate their [[IP addresses]].
		- Overblocking if multiple services use the same [[Internet Protocol (IP)|IP address]].
2. **DNS poisoning**: For a [[Domain Name System (DNS)|DNS]] lookup you do not respond or respond with a fake address.
	- Strength: No over blocking since we are using the domain name.
	- Weakness: Blocks the whole domain - no possible to allow different [[Protocol (networks)|protocols]] through.
3. **Content inspection**
	1. **Proxy-based content inspection**: This censorship technique is more sophisticated in that it allows for all network traffic to pass through a proxy where the traffic is examined for content, and the proxy rejects requests that serve objectionable content.
		- Strengths:
			- Precise censorship: A very precise level of censorship can be achieved, down to the level of single web pages or even objects within the web page.
			- Flexible: Works well with hybrid security systems. E.g., with a combination of other censorship techniques like packet dropping and DNS poisoning.
		- Weakness:
			- Not scalable: They are expensive to implement on a large-scale network as the processing overhead is large (through a proxy).
	2. **[[Intrusion detection systems (IDS)]] based content inspection**: An alternative approach is to use parts of an IDS to inspect network traffic. An IDS is easier and more cost-effective to implement than a proxy-based system as it is more responsive than reactive in nature in that it informs the firewall rules for future censorship.
4. **Blocking with Resets**: This technique sends a [[Transmission Control Protocol (TCP)|TCP]] reset (RST) to block individual connections that contain requests with objectionable content. We can see this by packet capturing of requests that are normal and requests that contain potentially flaggable keywords. Let’s look at one such example of packet capture.
Ok request
```
cam(53382)  → china(http) [SYN]   
china(http) → cam(53382) [SYN, ACK]   
cam(53382)  → china(http) [ACK]   
**cam(53382)  → china(http) GET / HTTP/1.0**   
**china(http) → cam(53382) HTTP/1.1 200 OK (text/html) etc...  
china(http) → cam(53382) ..._more of the web page_**   
**cam(53382)  → china(http) [ACK]  
            ..._and so on until the page was complete_**
```
Blocked request
```
cam(54190)  → china(http) [SYN]   
china(http) → cam(54190) [SYN, ACK] TTL=39   
cam(54190)  → china(http) [ACK]   
cam(54190)  → china(http) GET /?falun HTTP/1.0   
**china(http) → cam(54190) [RST] TTL=47, seq=1, ack=1**  
**china(http) → cam(54190) [RST] TTL=47, seq=1461, ack=1**   
**china(http) → cam(54190) [RST] TTL=47, seq=4381, ack=1**   
china(http) → cam(54190) HTTP/1.1 200 OK (text/html) _etc..._  
cam(54190)  → china(http) [RST] TTL=64, seq=25, ack zeroed   
china(http) → cam(54190) ..._more of the web page_   
cam(54190)  → china(http) [RST] TTL=64, seq=25, ack zeroed   
china(http) → cam(54190) [RST] TTL=47, seq=2921, ack=25
```
After the client (cam54190) sends the request containing flaggable keywords, it receives 3 TCP RSTs corresponding to one request, possibly to ensure that the sender receives a reset. The RST packets received correspond to the sequence number of 1460 sent in the GET request.

5. **Immediate Reset of Connections**: In addition to inspecting content, to suspend traffic coming from a source immediately for a  short period of time.

After the request above
```
cam(54191)  → china(http) [SYN]  
china(http) → cam(54191) [SYN, ACK] TTL=41  
cam(54191)  → china(http) [ACK]  
china(http) → cam(54191) [RST] TTL=49, seq=1
```
The reset packet received by the client is from the firewall. It does not matter that the client sends out legitimate GET requests following one “questionable” request. It will continue to receive resets from the firewall for a particular duration. Running different experiments suggests that this blocking period is variable for “questionable” requests.

