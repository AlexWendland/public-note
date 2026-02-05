---
aliases:
created: 2024-07-21
date_checked:
draft: false
last_edited: 2026-02-05
tags:
  - networks
  - security
title: BGP Hijacking
type: definition
---
>[!definition] BGP Hijacking
>This is a class of attacks that use the [BGP](border_gateway_protocol_(bgp).md) [protocol](protocol_(networks).md) as its method of attack. This falls into 3 categories:
>1. **Classification by Affected Prefix**: In this class of hijacking attacks, we are primarily concerned with the IP prefixes that are advertised by BGP.
>	1. [Exact prefix hijacking](exact_prefix_hijacking.md)
>	2. [Sub-prefix hijacking](sub-prefix_hijacking.md)
>	3. [BGP squatting](bgp_squatting.md)
>2. **Classification by AS-Path announcement**: In this class of attacks, an illegitimate [AS](autonomous_system_(as).md) announces the AS-path for a prefix for which it doesn’t have ownership rights.
>	1. [Type-0 hijacking](type-0_hijacking.md)
>	2. [Type-N hijacking](type-n_hijacking.md)
>	3. [Type-U hijacking](type-u_hijacking.md)
>3.  **Classification by Data-Plane traffic manipulation**: In this class of attacks, the attacker intercepts traffic between two users and manipulates it.
>	1. [Blackholing attack](blackholing_attack.md)
>	2. [Man-in-the-middle attack (MM)](man-in-the-middle_attack_(mm).md)
>	3. [Imposture attack (IM)](imposture_attack_(im).md)

