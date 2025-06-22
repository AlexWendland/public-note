---
aliases: 
checked: false
created: 2024-07-22
last_edited: 2024-07-22
draft: false
tags:
  - networks
type: definition
---
>[!tldr] DNS injection
>This is a form of [[DNS censorship]]. It uses a ruleset for which [[Domain Name System (DNS)|DNS]] entries are unacceptable and fakes the replies from a [[Domain Name System (DNS)|DNS]] lookup so the requester can not resolve the [[Internet Protocol (IP)|IP address]]. The works in the following way:
>1. DNS probe is sent to the open DNS resolvers
>2. The probe is checked against the blocklist of domains and keywords
>3. For domain-level blocking, a fake [[DNS records|DNS A record]] response is sent back. There are two levels of blocking domains: the first one is by directly blocking the domain, and the second one is by blocking it based on keywords present in the domain

