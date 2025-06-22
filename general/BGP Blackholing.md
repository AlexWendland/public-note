---
aliases: 
checked: false
created: 2024-07-21
last_edited: 2024-07-21
draft: false
tags:
  - networks
  - security
type: definition
---
>[!tldr] BGP Blackholing
>This is a method of initiating [[Blackholing (BH)|blackholing]] in the event of a [[Distributed Denial-of-Service (DDoS)|DDoS]] attack using an upstream service.
>
>This works in the following stages:
>1. **Announcement**: The victim [[Autonomous system (AS)|AS]] under attack announces the targeted destination [[Internet Protocol (IP)|IP]] or prefix to its upstream provider or Internet Exchange Point (IXP).
>2. **Propagation**: The upstream provider or [[Internet Exchange Points (IXPs)|IXP]] then advertises a more specific prefix and modifies the next-hop address to divert the traffic to a null interface.
>3. **Blackhole Community**: The blackholing message is tagged with a specific [[BGP Communities]] attribute to differentiate it from regular routing updates. This is normally the community 666.
>
>There are two main ways this is implement.
>
>1. **Using an Upstream Provider**:
>    - The victim network announces a blackholing message to its upstream provider, specifying the attacked IP and the blackholing community.
>    - The provider then recognises this message and sets the next-hop field to a blackholing IP, effectively discarding all traffic to the attacked IP.
>    
>![[bgp_bh_provider.png]] 
>
>2. **Using an Internet Exchange Point (IXP)**:  
>    - If the victim network is part of an IXP, it sends a blackholing message to the IXP route server.
>    - The route server then propagates this message to all connected IXP member networks, which drop the traffic to the blackholed IP.
> 
>![[bgp_bh_ixp.png]]
>
>Key Benefits of BGP Blackholing:
>- **Effective Mitigation**: Stops high-volume attacks close to their source, preventing them from reaching and overwhelming the target.
>- **Scalability**: Can be implemented quickly by upstream providers or [[Internet Exchange Points (IXPs)|IXPs]] to protect multiple networks.
>- **Cost-Efficiency**: Reduces the need for expensive [[Distributed Denial-of-Service (DDoS)|DDoS]] mitigation services by leveraging existing [[Boarder gateway protocol (BGP)|BGP]] infrastructure.
>
>Challenges and Considerations:
>
>- **Collateral Damage**: Legitimate traffic to the blackholed IP is also dropped, which can disrupt normal operations.
>- **Coordination**: Effective implementation requires coordination and trust between the victim network and its upstream providers or IXPs.
>- **Community Attributes**: The blackhole community attributes must be publicly available and correctly implemented to ensure proper functioning.

