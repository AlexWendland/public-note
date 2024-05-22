---
aliases:
  - ports
  - port
  - well known ports
  - ephemeral ports
  - registered ports
checked: false
created: 2024-05-21
last_edited: 2024-05-21
publish: true
tags:
  - networks
type: definition
---
>[!tldr] Port
>A port is just a number that the [[Host (networks)|host]] associates to an application. Ports break down into 3 groups
>1. 0-1023 are well known ports,
>2. 1024-49151 are user or registered ports, and
>3. 49152-65535 are ephemeral ports.
>
>Well known ports are used for system processes and protocols. For example port 80 is used by webservers for [[Hyper Text Transfer Protocol (HTTP)|HTTP]].
>
>Registered ports are used for user applications that need a port to work off of.
>
>The ephemeral ports or dynamic ports are used for private or temporary uses for example to connect to a web browser and receive a web page. 