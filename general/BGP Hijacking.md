---
aliases: 
checked: false
created: 2024-07-21
last_edited: 2024-07-21
publish: true
tags:
  - networks
  - security
type: definition
---
>[!tldr] BGP Hijacking
>This is a class of attacks that use the [[Boarder gateway protocol (BGP)|BGP]] [[Protocol (networks)|protocol]] as its method of attack. This falls into 3 categories:
>1. **Classification by Affected Prefix**: In this class of hijacking attacks, we are primarily concerned with the IP prefixes that are advertised by BGP.
>	1. [[Exact prefix hijacking]]
>	2. [[Sub-prefix hijacking]]
>	3. [[BGP squatting]]
>2. **Classification by AS-Path announcement**: In this class of attacks, an illegitimate [[Autonomous system (AS)|AS]] announces the AS-path for a prefix for which it doesn’t have ownership rights.
>	1. [[Type-0 hijacking]]
>	2. [[Type-N hijacking]]
>	3. [[Type-U hijacking]]
>3.  **Classification by Data-Plane traffic manipulation**: In this class of attacks, the attacker intercepts traffic between two users and manipulates it.
>	1. [[Blackholing attack]]
>	2. [[Man-in-the-middle attack (MM)]]
>	3. [[Imposture attack (IM)]]

