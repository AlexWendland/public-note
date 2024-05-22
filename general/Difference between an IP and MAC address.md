---
aliases: 
checked: false
created: 2024-05-22
last_edited: 2024-05-22
publish: true
tags:
  - networks
type: explainer
---
# Difference between an IP and MAC address

For any [[Packets|packet]] we attach the source and destination [[IP address]]. This [[Packets|packet]] may need to travel through many different [[Network|networks]]. For each different [[Network|network]] it will get a new [[Layer 2 Data Link|layer 2]] header with the [[MAC address]] of the [[Router|router]] it entered the [[Network|network]] on and the [[Router|router]] it needs to leave the [[Network|network]] on.

[[MAC address]] are really only there for a single network hop whereas the [[IP address]] is there for the whole journey.
