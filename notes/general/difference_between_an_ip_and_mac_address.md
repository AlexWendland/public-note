---
aliases:
checked: false
created: 2024-05-22
draft: false
last_edited: 2024-05-22
title: Difference between an IP and MAC address
tags:
  - networks
type: explainer
---
# Difference between an IP and MAC address

For any [packet](packets.md) we attach the source and destination [Internet Protocol (IPv4)](internet_protocol_(ipv4).md). This [packet](packets.md) may need to travel through many different [networks](network.md). For each different [network](network.md) it will get a new [layer 2](layer_2_data_link.md) header with the [MAC address](mac_address.md) of the [router](router.md) it entered the [network](network.md) on and the [router](router.md) it needs to leave the [network](network.md) on.

[MAC address](mac_address.md) are really only there for a single network hop whereas the [Internet Protocol (IPv4)](internet_protocol_(ipv4).md) is there for the whole journey.
