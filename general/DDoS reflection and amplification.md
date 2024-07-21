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
>[!tldr] DDoS reflection and amplification
>Instead of attacking your target directly in [[Distributed Denial-of-Service (DDoS)|DDoS]] attack - you can instead find legitimate services that respond to requests (for example when opening a [[Transmission Control Protocol (TCP)|TCP]] connection). You can make requests to such services where you [[DDoS Spoofing|spoof]] the source [[Internet Protocol (IP)|IP]] as your target. This has two advantages:
>- It is hard to block as the servers sending the request to the target could be services it relies upon or would need to talk to.
>- The services that could blocks the requests are not the same as the one that is suffering the damage causing a coordination issue.
>![[ddos_reflection.png]]

