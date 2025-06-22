---
aliases:
  - DNS
  - root DNS server
  - TLD
  - top level domain server
  - authoritative DNS server
  - LDNS
checked: false
created: 2024-05-23
last_edited: 2024-05-23
draft: false
tags:
  - networks
type: definition
---
>[!tldr] Domain Name System (DNS)
>The domain name systems main function is to translate a human readable domain name into an [[Internet Protocol (IP)|IP address]]. It is in essence a massive distributed database across many server.
>This distributed database uses different [[DNS records]] and a hierarchy of servers.
>- **Root DNS servers**: There are 13 mainly located in North America which are a network of replicated servers.
>- **Top level domain (TLD) server**: These are responsible for top level domains such as .com, .org, ect.
>- **Authoritative servers**: An organisations DNS server that control their domain.
>- **Local DNS (LDNS) servers**: This can be owned my users or [[Internet Service Provider (ISP)|ISPs]] and act as a proxy to the root servers. 
>![[dns_hierarchy.png]]
>When querying DNS servers requests can either be **iterative** meaning that the host that sends them keeps getting back another location to go to or **recursive** which means the host requested for the information goes directly to the next server.
>An example of a typical request can be seen below.
>![[dns_request.png]]
>DNS servers also offer other services such as:
>- Mail server,
>- Load distribution,
>- Certificate authorisation,
>- Others that can be found in the [[DNS records]].

