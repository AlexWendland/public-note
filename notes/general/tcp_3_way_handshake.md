---
aliases:
checked: false
created: 2024-05-27
draft: false
last_edited: 2024-05-27
title: TCP 3 way handshake
tags:
  - networks
type: definition
---
>[!tldr] TCP 3 way handshake
>[TCP](transmission_control_protocol_(tcp).md) starts a connection with a 3 way handshake to parse enough information to start the [duplex](duplex.md) communication:
>- The connecting [host](host_(networks).md) sends an empty synchronise message with the SYN [bit](bit.md) set to 1. It sets the initial sequence for the messages this host will be sending `client_isn`.
>- The receiving [host](host_(networks).md) sends an empty synchronise-acknowledgement message with the SYN and ACK [bit](bit.md) set to 1. It sets the initial sequence number for the messages this host will be sending `server_isn` with the acknowledgement header set to `client_isn + 1`.
>- Lastly the connecting [host](host_(networks).md) sends an empty acknowledgement message with the ACK [bit](bit.md) set to 1. The acknowledgement header is set to `server_isn + 1`.

