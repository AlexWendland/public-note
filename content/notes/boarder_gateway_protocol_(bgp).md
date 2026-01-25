---
aliases:
  - BGP
  - BGPs
  - iBGP
  - eBGP
created: 2024-06-08
date_checked:
draft: false
last_edited: 2024-06-08
tags:
  - networks
title: Boarder gateway protocol (BGP)
type: definition
---
>[!tldr] Boarder gateway protocol (BGP)
>This is a class of [protocols](protocol_(networks).md) that are used for [interdomain routing](interdomain_routing.md). That is sharing subnets between [AS](autonomous_system_(as).md). Two [routers](router.md) connected over [BGP](boarder_gateway_protocol_(bgp).md) are called BGP peers. They open a semi-permanent [TCP](transmission_control_protocol_(tcp).md) connection where they exchange routes. There are two varieties of this class.
>- **iBGP**: For internal to the [AS](autonomous_system_(as).md) communication between boarder routers.
>- **eBGP**: For two routers who are in different [AS](autonomous_system_(as).md).
>The difference between iBGP and [IGP](interior_gateway_protocol_(igp).md) is that iBGP is communicating about what external subnets are available from that router wheres [IGP](interior_gateway_protocol_(igp).md) is communicating about what internal subnets there are.

