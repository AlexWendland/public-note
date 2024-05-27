---
aliases:
  - encapsulation
  - de-encapsulation
  - encapsulate
checked: false
created: 2024-05-23
last_edited: 2024-05-23
publish: false
tags: 
type: definition
---
>[!tldr] Encapsulation
>Once an application has generated some data *encapsulation* is the process of wrapping that data with headers so it can traverse through the internet to make it to it's destination. 
>
>[[Layer 4 Transport|Layer 4]] takes the data and adds the source and destination [[Port|ports]] to the data to make it a *[[Segment|segment]]*.
>
>[[Layer 3 Network|Layer 3]] takes the [[Segment|segment]] and adds a source and destination [[Internet Protocol (IPv4)]] to make it a *[[Packets|packet]]*.
>
>[[Layer 2 Data Link|Layer 2]] takes the [[Packets|packet]] and adds a source and destination [[MAC address]] to make it a *[[Frame (networks)|frame]]*.
>
>This is moved onto [[Layer 1 Physical|layer 1]] to be passed along to its destination.
>
>The reverse process is called *de-encapsulation*.
>
>![[osci-model-summary.png]]


