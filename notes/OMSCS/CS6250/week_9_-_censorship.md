---
aliases:
checked: false
course: 'CS6250 Computer Networks'
created: 2024-07-22
draft: false
last_edited: 2024-07-22
title: Week 9 - Censorship
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

[DNS censorship](../../general/dns_censorship.md)

[Great Firewall of China (GFW)](../../general/great_firewall_of_china_(gfw).md)

Researchers have tried to reverse engineer the GFW and to understand how it works. Researchers have started to identify some of the properties:

1. _Locality of [GFW](../../general/great_firewall_of_china_(gfw).md) nodes_: There are two differing notions on whether the GFW nodes are present only at the edge [ISPs](../../general/internet_service_provider_(isp).md) or whether they are also present in non-bordering Chinese [ASs](../../general/autonomous_system_(as).md). The majority view is that censorship nodes are present at the edge.
2. _Centralized management_: Since the blocklists obtained from two distinct GFW locations are the same, there is a high possibility of a central management (GFW Manager) entity that orchestrates blocklists.
3. _Load balancing_: GFW load balances between processes based on source and destination IP address. The processes are clustered together to collectively send injected DNS responses.

## DNS injection

[DNS injection](../../general/dns_injection.md)

To detect [DNS injection](../../general/dns_injection.md) you can use probing techniques to search for injected paths.

There are multiple different techniques to use here.

1. **Packet dropping**: For a specific set of [IP addresses](../../general/internet_protocol_(ip).md) you drop packets going to or from that address.
	- Strengths:
		- Easy to implement
		- Low cost
	- Weaknesses:
		- Maintaining a block list can be hard if users rotate their [IP addresses](ip_addresses.md).
		- Overblocking if multiple services use the same [IP address](../../general/internet_protocol_(ip).md).
2. **DNS poisoning**: For a [DNS](../../general/domain_name_system_(dns).md) lookup you do not respond or respond with a fake address.
	- Strength: No over blocking since we are using the domain name.
	- Weakness: Blocks the whole domain - no possible to allow different [protocols](../../general/protocol_(networks).md) through.
3. **Content inspection**
	1. **Proxy-based content inspection**: This censorship technique is more sophisticated in that it allows for all network traffic to pass through a proxy where the traffic is examined for content, and the proxy rejects requests that serve objectionable content.
		- Strengths:
			- Precise censorship: A very precise level of censorship can be achieved, down to the level of single web pages or even objects within the web page.
			- Flexible: Works well with hybrid security systems. E.g., with a combination of other censorship techniques like packet dropping and DNS poisoning.
		- Weakness:
			- Not scalable: They are expensive to implement on a large-scale network as the processing overhead is large (through a proxy).
	2. **[Intrusion detection systems (IDS)](../../general/intrusion_detection_systems_(ids).md) based content inspection**: An alternative approach is to use parts of an IDS to inspect network traffic. An IDS is easier and more cost-effective to implement than a proxy-based system as it is more responsive than reactive in nature in that it informs the firewall rules for future censorship.
4. **Blocking with Resets**: This technique sends a [TCP](../../general/transmission_control_protocol_(tcp).md) reset (RST) to block individual connections that contain requests with objectionable content. We can see this by packet capturing of requests that are normal and requests that contain potentially flaggable keywords. Let’s look at one such example of packet capture.
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

## Measuring DNS manipulation

It is believed over 60 countries are impacted by some form of [DNS censorship](../../general/dns_censorship.md) byt there is little comprehensive knowledge of what is blocked in which country because of the following issues:

- **Diverse Measurements**
    - **Geographic and Political Variation:**
        - Different geographic regions, [ISPs](../../general/internet_service_provider_(isp).md), and countries exhibit diverse political dynamics affecting censorship.
        - Censorship techniques can vary even within regions of the same country.
    - **Different Filtering Techniques:**
        - ISPs may employ various methods, such as IP address blocking or keyword-based web request blocking.
    - **Need for Longitudinal Studies:**
        - Continuous and widespread measurements are necessary to understand the global scope and diversity of [DNS](../../general/domain_name_system_(dns).md) manipulation.
- **Need for Scale**
    - **Limitations of Volunteer-Based Methods:**
        - Initial methods relied on volunteers installing and running measurement software.
        - This approach lacks the scale needed for comprehensive analysis.
    - **Automation and Independence:**
        - There is a need for automated measurement tools that do not depend on human intervention.
- **Identifying Intent to Restrict Content Access**
    - **Complexity in Detection:**
        - Inconsistent or anomalous DNS responses may be due to various causes, including misconfigurations.
    - **Intent Detection:**
        - Detecting DNS manipulation involves discerning intent to block access, which is inherently challenging.
    - **Reliance on Multiple Indications:**
        - It is essential to identify multiple signals to infer deliberate DNS manipulation.
- **Ethics and Minimizing Risks**
    - **Risks to Citizens:**
        - Participation in censorship measurement can pose risks, especially in countries penalising access to censored content.
    - **Safer Alternatives:**
        - Avoid using home network DNS resolvers or forwarders.
        - Prefer open DNS resolvers within Internet infrastructure, such as those hosted by ISPs or cloud providers.

Good method to measure censorship require different vantage points on the internet. Some of these did use servers to rent such as CensMon others such as OpenNet used volunteers - though this can be difficult in exactly the places where you would want to measure it.

[Iris](../../general/iris.md)

## Censorship through connectivity disruptions

The most direct way of censorship is to block access to the whole or parts of the internet at the [IP](../../general/internet_protocol_(ip).md) level. The main methods to do this are:
- **Physically disconnecting infrastructure**: If the network is sufficiently small then you could take down the access points to the internet. This is hard however, as normally this infrastructure is distributed.
- **Router disruption**: Abusing the [BGP](../../general/boarder_gateway_protocol_(bgp).md) to change the routes that are offered or removing them completely. This is fairly easy to detect as you would be able to notice the change in routing behaviour.
- **Packet filtering**: Such as what a [firewall](../../general/firewall.md) or a [switch](../../general/switch.md) does but on the level on of the whole network. This can be harder to detect as you would need to probe for these [IP address](../../general/internet_protocol_(ip).md) or the paths packets follow.

[Angur](../../general/angur.md)
