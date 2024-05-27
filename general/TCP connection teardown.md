---
aliases: 
checked: false
created: 2024-05-27
last_edited: 2024-05-27
publish: true
tags:
  - networks
type: definition
---
>[!tldr] TCP connection teardown
> When either [[Host (networks)|host]] wants to end a [[Transmission Control Protocol (TCP)|TCP]] connection they follow a teardown [[Protocol (networks)|protocol]]:
> - The [[Client|client]] sends an empty finish message with the FIN [[Bit|bit]] set to 1.
> - The [[Server|server]] sends an acknowledgement message for that closing message.
> - After the [[Server|server]] has closed off the connection it sets an empty finish message with the FIN [[Bit|bit]] set to 1.
> - Lastly the [[Client|client]] sends an empty acknowledgement message for that finish message. This is sent again after short delay to increase the chance that is received. 
