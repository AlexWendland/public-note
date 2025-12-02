---
aliases:
checked: false
created: 2024-05-27
draft: false
last_edited: 2024-05-27
title: TCP connection teardown
tags:
  - networks
type: definition
---
>[!tldr] TCP connection teardown
> When either [host](host_(networks).md) wants to end a [TCP](transmission_control_protocol_(tcp).md) connection they follow a teardown [protocol](protocol_(networks).md):
> - The [client](client.md) sends an empty finish message with the FIN [bit](bit.md) set to 1.
> - The [server](server.md) sends an acknowledgement message for that closing message.
> - After the [server](server.md) has closed off the connection it sets an empty finish message with the FIN [bit](bit.md) set to 1.
> - Lastly the [client](client.md) sends an empty acknowledgement message for that finish message. This is sent again after short delay to increase the chance that is received.
