---
aliases:
created: 2024-07-27
date_checked: 2026-02-05
draft: false
last_edited: 2026-02-05
tags:
  - networks
title: IP Anycast
type: definition
---
> [!definition] IP Anycast
>This is a [protocol](protocol_(networks).md) that uses [Hot potato routing](hot_potato_routing.md) in the [BGP](border_gateway_protocol_(bgp).md). It broadcasts the same [IP address](internet_protocol_(ip).md) from multiple different locations and records the path that gets advertised to a given [AS](autonomous_system_(as).md). This is a cheap way to calculate the shortest path in terms of [AS](autonomous_system_(as).md)-paths from a set of locations to your [AS](autonomous_system_(as).md). This is used in server selection within [CDNs](content_delivery_network_(cdn).md).

