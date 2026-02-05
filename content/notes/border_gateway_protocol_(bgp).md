---
aliases:
  - BGP
  - BGPs
  - iBGP
  - eBGP
created: 2024-06-08
date_checked: 2026-02-05
draft: false
last_edited: 2026-02-05
tags:
  - networks
title: Border gateway protocol (BGP)
type: definition
---
>[!definition] Border gateway protocol (BGP)
>This is a class of [protocols](protocol_(networks).md) that are used for [interdomain routing](interdomain_routing.md). That is sharing subnets between [AS](autonomous_system_(as).md). Two [routers](router.md) connected over [BGP](border_gateway_protocol_(bgp).md) are called BGP peers. They open a semi-permanent [TCP](transmission_control_protocol_(tcp).md) connection where they exchange routes. There are two varieties of this class.
>- **iBGP**: For internal to the [AS](autonomous_system_(as).md) communication between border routers.
>- **eBGP**: For two routers who are in different [AS](autonomous_system_(as).md).
>The difference between iBGP and [IGP](interior_gateway_protocol_(igp).md) is that iBGP is communicating about what external subnets are available from that router whereas [IGP](interior_gateway_protocol_(igp).md) is communicating about what internal subnets there are.

