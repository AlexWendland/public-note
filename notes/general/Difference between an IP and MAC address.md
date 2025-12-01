---
aliases:
checked: false
created: 2024-05-22
draft: false
last_edited: 2024-05-22
tags:
  - networks
type: explainer
---
# Difference between an IP and MAC address

For any [[Packets|packet]] we attach the source and destination [[Internet Protocol (IPv4)]]. This [[Packets|packet]] may need to travel through many different [[Network|networks]]. For each different [[Network|network]] it will get a new [[Layer 2 Data Link|layer 2]] header with the [[MAC address]] of the [[Router|router]] it entered the [[Network|network]] on and the [[Router|router]] it needs to leave the [[Network|network]] on.

[[MAC address]] are really only there for a single network hop whereas the [[Internet Protocol (IPv4)]] is there for the whole journey.
