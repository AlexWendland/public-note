---
aliases: null
checked: false
created: 2024-05-23
last_edited: 2024-05-23
publish: false
tags: []
type: definition
---
>[!tldr] Encapsulation
>Once an application has generated some data *encapsulation* is the process of wrapping that data with headers so it can traverse through the internet to make it to it's destination. 
>
>[[Layer 4 Transport|layer 4]] takes the data and adds the source and destination [[Port|ports]] to the data to make it a [[segment]].
>
>Layer 3 takes the segment and adds a source and destination IP address to make it a *packet*.
>
>Layer 2 takes the packet and adds a source and destination MAC address to make it a *frame*.
>
>This is moved onto layer one to be passed along to its destination.
>
>The reverse process is called de-encapsulation.
>
>![[osci-model-summary.png]]


