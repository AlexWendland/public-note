---
aliases: 
checked: false
created: 2024-05-21
last_edited: 2024-05-21
publish: true
tags:
  - networks
type: definition
---
>[!tldr] Routing
>The process of routing is getting a [[Packets|packet]] the network associated to its [[IP address]]. To do this all routers store a [[Routing table|routing table]] which maps the tuple of an IP address and a [[Network mask|network mask]] to either a interface or a IP address.
>There are 3 ways a router can populate its routing table
>1. Directly connected: This is for networks directly connected to the router. It adds an entry for that networks and the interface of the [[Router|router]] it is connected to.
>2. Static route: This is a route that has been manually configured on a router. Instead of an interface it will have an IP address to forward that packet on to.
>3. Dynamic routing: This is the same in structure to the static rout but instead of being manually added this gets populated by routers sharing known addresses with one another.
>
>This table might grow very large but routers use [[Route summarization|route summarization]] to keep the tables shorter.
>
>Once a router has been configured when it receives a [[Packets|packet]] it looks at its [[Layer 3 Network|layer 3]] header containing the destination IP address. It compares that again the known address, using the [[Network mask|network mask]] and finds the most precise match (matching on the longest [[Network mask|network mask]]) then forwards it to that interface or IP address.

