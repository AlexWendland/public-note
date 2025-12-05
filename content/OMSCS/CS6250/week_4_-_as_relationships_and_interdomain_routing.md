---
aliases:
checked: false
course_code: CS6250
course_name: Computer Networks
created: 2024-06-08
draft: false
last_edited: 2024-06-08
tags:
  - OMSCS
title: Week 4 - AS relationships and interdomain routing
type: lecture
week: 4
---

[Interdomain routing](../../notes/interdomain_routing.md)

# Additional reading

## Important Readings

Interdomain Internet Routing
[https://web.mit.edu/6.829/www/currentsemester/papers/AS-bgp-notes.pdfLinks to an external site.](https://web.mit.edu/6.829/www/currentsemester/papers/AS-bgp-notes.pdf)

BGP routing policies in ISP networks
[https://www.cs.princeton.edu/~jrex/papers/policies.pdfLinks to an external site.](https://www.cs.princeton.edu/~jrex/papers/policies.pdf)

On the importance of Internet eXchange Points for today’s Internet ecosystem
[https://cryptome.wikileaks.org/2013/07/ixp-importance.pdfLinks to an external site.](https://cryptome.wikileaks.org/2013/07/ixp-importance.pdf)

Peering at Peerings: On the Role of IXP Route Servers
[https://people.csail.mit.edu/richterp/imc238-richterA.pdfLinks to an external site.](https://people.csail.mit.edu/richterp/imc238-richterA.pdf "Link")

## Book References

Kurose-Ross

**6th Edition**: Section 1.3.3 (A Network of Networks), Section 4.6.3 (Inter-AS Routing: BGP)

**7th Edition**: Section 1.3.3 (A Network of Networks), Section 5.4.1 (The Role of BGP)

## Optional Readings

Investigating Interdomain Routing Policies in the Wild
[https://people.cs.umass.edu/~phillipa/papers/AnwarIMC15.pdfLinks to an external site.](https://people.cs.umass.edu/~phillipa/papers/AnwarIMC15.pdf)

BGP Communities: Even more Worms in the Routing Can
[https://people.mpi-inf.mpg.de/~fstreibelt/preprint/communities-imc2018.pdfLinks to an external site.](https://people.mpi-inf.mpg.de/~fstreibelt/preprint/communities-imc2018.pdf)

On the scalability of BGP: the roles of topology growth and update rate-limiting
[https://www.cc.gatech.edu/home/dovrolis/Papers/bgp-scale-conext08.pdfLinks to an external site.](https://www.cc.gatech.edu/home/dovrolis/Papers/bgp-scale-conext08.pdf)

O Peer, Where Art Thou? Uncovering Remote Peering Interconnections at IXPs
[https://www.inspire.edu.gr/wp-content/pdfs/uncovering_remote_peering_interconnections_v1.pdfLinks to an external site.](https://www.inspire.edu.gr/wp-content/pdfs/uncovering_remote_peering_interconnections_v1.pdf)

Detecting BGP Configuration Faults with Static Analysis
[https://www.usenix.org/legacy/events/nsdi05/tech/feamster/feamster.pdfLinks to an external site.](https://www.usenix.org/legacy/events/nsdi05/tech/feamster/feamster.pdf)

# Ecology of the internet

The internet has 3 major players:

[Internet Service Provider (ISP)](../../notes/internet_service_provider_(isp).md)

[Content delivery network (CDN)](../../notes/content_delivery_network_(cdn).md)

[Internet Exchange Points (IXPs)](../../notes/internet_exchange_points_(ixps).md)

Each of these may operate as one [AS](../../notes/autonomous_system_(as).md) or as multiple to allow different protocols to be used in different parts of the network.

# Cooperation and competition among networks

Whilst [ISPs](../../notes/internet_service_provider_(isp).md) are in direct competition with eachother they also can not operate without cooperating with each other also. The [ISP](../../notes/internet_service_provider_(isp).md) business model is based off selling access to internet - this is normally calculated via bandwidth used either for a fixed price with a cap or by taking the 95th percentile of measurements normally taken every 5 minutes. Either of these mean the [ISP](../../notes/internet_service_provider_(isp).md) has incentives to make you use their service more. This relies on you having low latency connections to as many other [hosts](../../notes/host_(networks).md) as possible.

The cost to [ISPs](../../notes/internet_service_provider_(isp).md) is maintaining a network with sufficient capacity to handle all that traffic. Therefore unless traffic is going to a [host](../../notes/host_(networks).md) paying them they will need a commercial incentive to carry it.

Therefore two types of relationships form between [ISPs](../../notes/internet_service_provider_(isp).md)
- **Peering relationships**: If two providers see [hosts](../../notes/host_(networks).md) exchange traffic between there networks in roughly equal quantities they may agree to share traffic directly at no cost between the [ISPs](../../notes/internet_service_provider_(isp).md).
- **Customer-Provider relationships**: If one [ISP](../../notes/internet_service_provider_(isp).md) has considerably more [hosts](../../notes/host_(networks).md) receiving traffic then they can sell access to these hosts to other [ISPs](../../notes/internet_service_provider_(isp).md). Here the larger [ISP](../../notes/internet_service_provider_(isp).md) becomes the provider to the smaller customer [ISP](../../notes/internet_service_provider_(isp).md) and picks up a fee.

This has been the model since the beginning of the internet and was one of the main drivers for the hierarchical nature of [ISPs](../../notes/internet_service_provider_(isp).md) and the internet as a whole. However [IXPs](../../notes/internet_exchange_points_(ixps).md) are changing this. [IXPs](../../notes/internet_exchange_points_(ixps).md) mean that [ISPs](../../notes/internet_service_provider_(isp).md) don't need to go through eachother and instead can trade traffic directly. This is making the internet more flat. This is in part driven by [CDNs](../../notes/content_delivery_network_(cdn).md) using [IXPs](../../notes/internet_exchange_points_(ixps).md) to have the lowest latency connections to their consumers.

# Address exchange

First consider which addresses [AS](../../notes/autonomous_system_(as).md) want to exchange with other internet entities.

## Exporting routes

First lets look at what routes an [AS](../../notes/autonomous_system_(as).md) would want to tell other internet entities about. This has financial repercussions as you will then have to carry that traffic on your network.

- **Routes form customers**: These are profitable for an [ISP](../../notes/internet_service_provider_(isp).md) to share as they generate revenue from more traffic going to these. These are shared willingly to all.
- **Routes from peers**: Whilst there is the network cost of carrying this traffic sharing these addresses keeps the free agreements in place or can turn peers into customers. It may make sense to share routes learnt from peers but it is circumstantial.
- **Routes from providers**: A provider is paying for access to the provider. It has very little commercial incentive to share routes learnt from the provider.

## Importing routes

When an [AS](../../notes/autonomous_system_(as).md) decides which route to send its traffic down this again is a symmetric decision to exporting. The goal of the [AS](../../notes/autonomous_system_(as).md) is for the traffic of its customers to travel through the fewest other [AS](../../notes/autonomous_system_(as).md) as possible as each one will generate it some cost and potentially reduce capacity of the route.

- **Route offered by peer or customer**: These in the short term are completely free and so will preferably use these.
- **Route offered by provider**: These cost the [AS](../../notes/autonomous_system_(as).md) money so will be used as a last resort.

## [Protocols](../../notes/protocol_(networks).md)

[Interdomain routing](../../notes/interdomain_routing.md)

[Boarder gateway protocol (BGP)](../../notes/boarder_gateway_protocol_(bgp).md)

The goals of [BGP](../../notes/boarder_gateway_protocol_(bgp).md) are:
- **Scalability**: How do you maintain a routing table when the size of the internet is expanding.
- **Expressing route policies**: How do we allow for [AS](../../notes/autonomous_system_(as).md) to control which routes to use and to broadcast.
- **Cooperation**: To let [AS](../../notes/autonomous_system_(as).md) to make local decisions with the information they are provided.
- **Security**: Whist not an initial design goal [BGP](../../notes/boarder_gateway_protocol_(bgp).md) did not include security as the internet has expanded it has become more important. This needs to protect [AS](../../notes/autonomous_system_(as).md) from malicious attacks, misconfiguration, and faults. This includes different protocols, registries for the domains an [AS](../../notes/autonomous_system_(as).md) owns, private keys for [AS](../../notes/autonomous_system_(as).md).

# The [BGP](../../notes/boarder_gateway_protocol_(bgp).md) [protocol](../../notes/protocol_(networks).md)

Two [routers](../../notes/router.md) connected over [BGP](../../notes/boarder_gateway_protocol_(bgp).md) are called BGP peers. They open a semi-permanent [TCP](../../notes/transmission_control_protocol_(tcp).md) connection where they exchange routes. There are two different varieties.
- iBGP: For internal communication about what external routes are available.
- eBGP: For communicating with other [AS](../../notes/autonomous_system_(as).md).

There are three important messages [BGP](../../notes/boarder_gateway_protocol_(bgp).md) has.
1. The **OPEN** message to start the conversation.
2. The  **UPDATE** message that contains a change of available routes. This has two forms:
	1. *Announcements* about new routes or updates to old routes.
	2. *Withdrawls* messages about routes no longer available.
3. The **KEEPALIVE** messages that keep the connection going.

In the [BGP](../../notes/boarder_gateway_protocol_(bgp).md) the [routers](../../notes/router.md) exchange [IP prefixes](../../notes/subnets.md) that represent [subnets](../../notes/subnets.md) or collections of [subnets](../../notes/subnets.md) if the [router](../../notes/router.md) is using [route summarization](../../notes/route_summarization.md). For the routes agreed by the [AS](../../notes/autonomous_system_(as).md) the [router](../../notes/router.md) offers theses over [eBGP](../../notes/boarder_gateway_protocol_(bgp).md) and then shares the routes it has been offered over [iBGP](../../notes/boarder_gateway_protocol_(bgp).md).

Messages passed between [AS](../../notes/autonomous_system_(as).md) have some special properties, two of which are:
- **ASPATH**: A list of [ASN](../../notes/autonomous_system_number_(asn).md) for each [AS](../../notes/autonomous_system_(as).md) the route has passed through. This is helpful to avoid loops.
- **NEXTHOP**: The [IP address](../../notes/internet_protocol_(ip).md) of the next router in the hop.

# The router process

We can model a [router](../../notes/router.md) running [BGP](../../notes/boarder_gateway_protocol_(bgp).md) as follows.

![Router Diagram](../../../static/images/router_diagram.png)

This has 3 main steps.
1. Receive and store neighbours routing tables.
2. Decides its best routing options and updates the forwarding table.
3. Decides which routes it wants to advertise and updates neighbouring routers.

How a router decides which route to use depends on many factors. It ranks these and then compares routes.

| Step | Attribute                                            | Controller? |
| ---- | ---------------------------------------------------- | ----------- |
| 1    | Highest LocalPref                                    | local       |
| 2    | Lowest AS path length                                | neighbour   |
| 3    | Lowest origin type                                   | neither     |
| 4    | Lowest MED                                           | neighbour   |
| 5    | eBGP-learned over iBGP-learned                       | neither     |
| 6    | Lowest [IGP](interior_gateway_protocol_(igp)\.md) cost | local       |
| 7    | Lowest router ID (break ties)                        | neither     |

There are two main ways [AS](../../notes/autonomous_system_(as).md) can control which routes it uses and its neighbours uses.

## LocalPref

This is how an [AS](../../notes/autonomous_system_(as).md) expresses its commercial best interest. It will set a value to neighbouring [AS](../../notes/autonomous_system_(as).md) based on the financial relationship it has with it. These normally are:

| Relationship to advertising [AS](autonomous_system_(as)\.md) | LocalPerf value |
| ---------------------------------------------------------- | --------------- |
| Customer                                                   | 90-99           |
| Peer                                                       | 80 - 89         |
| Provider                                                   | 70 - 79         |
| Backup links                                               | 60-69           |

This reflects the preferences we discussed above, customer then peer then provider.j

## Multi-exit Discriminator (MED)

If an [AS](../../notes/autonomous_system_(as).md) has two routers connecting to a neighbours [AS](../../notes/autonomous_system_(as).md) which are offering some of the same routes. Knowing the forwarding tables of these routers may give a preference for how a neighbouring [AS](../../notes/autonomous_system_(as).md) forwards traffic through your network. This is controlled by setting a MED value (for example as the [IGP](../../notes/interior_gateway_protocol_(igp).md) cost to forward that traffic).

# Challenges with [BGP](../../notes/boarder_gateway_protocol_(bgp).md): Misconfiguration and scalability

Routers are vulnerable to misconfiguration and faults. This can lead to an excessively large number of updates leading to further faults from overloading the network. This can be mediated by limiting the size of the routing table.

To limit the size of the routing table it can filter out routes that are too specific. This encourages [route summarization](../../notes/route_summarization.md). The act of [route summarization](../../notes/route_summarization.md) protects the whole network from getting overloaded and help with scalability. Small [AS](../../notes/autonomous_system_(as).md) sometimes just use a default gateway where they redirect all traffic without further knowledge.

If a route is repeatedly updated due to some route instability this can risk messages getting sent in error or a patchy connection. Routers can implement **flap damping** where it tracks the number of updates to a prefix. If this goes over a certain threshold in a time interval it will suppress that route until it stabilises.

Routers can be strategic about what addresses it does this too and how sensitive it is. If it has addresses it needs to have high availability for it can have a much higher threshold whereas other addresses it can be much lower.

# Peering at an [IXP](../../notes/internet_exchange_points_(ixps).md)

[IXP](../../notes/internet_exchange_points_(ixps).md)

Below is an example of such and [IXP](../../notes/internet_exchange_points_(ixps).md) is Frankfurt.

![Ixp Example](../../../static/images/IXP_example.png)

This shows how an [IXP](../../notes/internet_exchange_points_(ixps).md) is a massive set of switches creating a giant [network](../../notes/network.md). It is normally distributed over a region or globally with different connection points such as DE-CIX1,2,3,4,7 all connecting in to a fault tolerant core Core 1 with backup Core2.

To exchange with an [IXP](../../notes/internet_exchange_points_(ixps).md) a [AS](../../notes/autonomous_system_(as).md) needs to physically connect with it. Which is why being distributed makes this easier though carries technical cost to it.

## [IXPs](../../notes/internet_exchange_points_(ixps).md) have become increasingly popular, why?

1. [IXP](../../notes/internet_exchange_points_(ixps).md) can handle large quantities of traffic rivalling that of tier-1 [ISPs](../../notes/internet_service_provider_(isp).md).
2. [IXP](../../notes/internet_exchange_points_(ixps).md) can mitigate [DDoS](../../notes/distributed_denial-of-service_(ddos).md) attacks by monitoring traffic to particular [ASs](../../notes/autonomous_system_(as).md).
3. They provide excellent research hubs due to their open and large scale nature.
4. They are active marketplaces offering services to the [ASs](../../notes/autonomous_system_(as).md) that participate in them. This offering is expanding as more research happens providing innovation to the internet.

## How to peer at an [AS](../../notes/autonomous_system_(as).md)

An [AS](../../notes/autonomous_system_(as).md) must have an [ASN](../../notes/autonomous_system_number_(asn).md) to peer at an [IXP](../../notes/internet_exchange_points_(ixps).md). Then they will need to physically collocate a router in the [AS](../../notes/autonomous_system_(as).md) to one of the [IXP](../../notes/internet_exchange_points_(ixps).md) access points. Lastly they must agree to the terms and conditions of using the [IXP](../../notes/internet_exchange_points_(ixps).md). To do this they pay:
- A one off access cost to locate the router at the access point,
- A monthly fee for renting a port - this cost normally scales based on the speed/capacity of that [port](../../notes/port.md).
- Sometimes there is a yearly subscription fee.

Once connected to the [IXP](../../notes/internet_exchange_points_(ixps).md) there is normally no cost to publicly peer there. That means getting access to all the other networks also publicly peering there.

Normally the terms of accessing do not forbid reselling of access to the [IXP](../../notes/internet_exchange_points_(ixps).md). Therefore some providers link with an [IXP](../../notes/internet_exchange_points_(ixps).md) the resale access to that [IXP](../../notes/internet_exchange_points_(ixps).md) if it is too hard for another [AS](../../notes/autonomous_system_(as).md) to collocate a router there. This is called remote peering and is an active area of study.

## Why peer in an [IXP](../../notes/internet_exchange_points_(ixps).md)

- Keeps traffic local which is more reliable and faster.
- Lower costs than negotiating with other [ASs](../../notes/autonomous_system_(as).md) such as [ISP](../../notes/internet_service_provider_(isp).md) for access.
- Incentives - large content providers prefer use of [IXP](../../notes/internet_exchange_points_(ixps).md) as it guarantees more control of how their users receive their content. Therefore they connect via [IXPs](../../notes/internet_exchange_points_(ixps).md) which motivates other actors to use them.

## Services offered by an [IXP](../../notes/internet_exchange_points_(ixps).md)

1. **Public peering**: This allows you to directly connect with any other participant who is also public peering opening up a massive number of new routes but also direct connections with other [ASs](../../notes/autonomous_system_(as).md).
2. **Private peering**: This allows for direct connection between two parties who know eachother at the [IXP](../../notes/internet_exchange_points_(ixps).md). This won't use the pubic peering infrastructure. Though provides a high capacity stable connection.
3. **Route servers and Service level agreements**: Normally the [IXP](../../notes/internet_exchange_points_(ixps).md) will offer free access to a route server which is a giant public route table. The [IXP](../../notes/internet_exchange_points_(ixps).md) will also offer [SLAs](../../notes/service_level_agreements_(slas).md) with the services they offer.
4. **Mobile peering**: This is a scalable solution to mobile networks.
5. **DDoS black-holing**: This is a customer triggered black-holing of traffic coming towards their [AS](../../notes/autonomous_system_(as).md) to relieve the stress from [DDoS](../../notes/distributed_denial-of-service_(ddos).md) attacks.
6. **Free value add services**: Services that are for the public good like bandwidth testing, Internet Routing Registries,[DNS](../../notes/domain_name_system_(dns).md) servers, ect.

## How do route servers work

Two [ASs](../../notes/autonomous_system_(as).md) in a [IXP](../../notes/internet_exchange_points_(ixps).md) to transfer route information need to establish a bilateral [BGP](../../notes/boarder_gateway_protocol_(bgp).md) connection. However with so many participants at an [IXP](../../notes/internet_exchange_points_(ixps).md) the number of open connections would be massive - which would not scale.

![Route Server Example](../../../static/images/route_server_example.png)

Instead if the [IXP](../../notes/internet_exchange_points_(ixps).md) offers a route server [ASs](../../notes/autonomous_system_(as).md) connect to this single entity instead. This offers the following services:
- It collects and shares routing information from its peers.
- It execute [BGP](../../notes/boarder_gateway_protocol_(bgp).md) decisions and re-advertises the resulting information.

The collection of addresses is called a Routing Information Base (RIB) which contains all [BGP](../../notes/boarder_gateway_protocol_(bgp).md) paths. There is a master RIB with all the information and an [AS](../../notes/autonomous_system_(as).md) specific RIB for each participant.

Route servers maintain two types of route filters. Import route filters that allow [ASs](../../notes/autonomous_system_(as).md) to only advertise routes they should advertise. Export route filters which are triggered by member [ASs](../../notes/autonomous_system_(as).md) to restrict which other [IXP](../../notes/internet_exchange_points_(ixps).md) members can receive their routes.

For example suppose AS X and AS Y exchange routes through a multi-lateral peering session through a route server. This happens in the following steps.
1. First AS X advertises a prefix p1 to the route server, which is added to the route server's RIB for that [AS](../../notes/autonomous_system_(as).md).
2. The route server checks AS X import filters to see if it wants to advertise p1 - if so it is added to the master RIB.
3. The route server checks AS X's export filters to see if AS Y is allowed to recieve p1. If so it adds it to AS Y's RIB.
4. Lastly the route server advertises p1 to AS Y with AS X as the next hop.

![Route Server Process](../../../static/images/route_server_process.png)

