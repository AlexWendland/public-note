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
>[!tldr] TCP 3 way handshake
>[[Transmission Control Protocol (TCP)|TCP]] starts a connection with a 3 way handshake to parse enough information to start the [[Duplex|duplex]] communication:
>- The connecting [[Host (networks)|host]] sends an empty synchronise message with the SYN [[Bit|bit]] set to 1. It sets the initial sequence for the messages this host will be sending `client_isn`.
>- The receiving [[Host (networks)|host]] sends an empty synchronise-acknowledgement message with the SYN and ACK [[Bit|bit]] set to 1. It sets the initial sequence number for the messages this host will be sending `server_isn` with the acknowledgement header set to `client_isn + 1`.
>- Lastly the connecting [[Host (networks)|host]] sends an empty acknowledgement message with the ACK [[Bit|bit]] set to 1. The acknowledgement header is set to `server_isn + 1`.

