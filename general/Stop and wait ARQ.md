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
>[!tldr] Stop and wait ARQ
>This is an implementation of [[Automatic Repeat Request (ARQ)|ARQ]] that sends some messages and wait for an acknowledgement before sending more. It uses a window size determined by the [[Transmission control in TCP]]. It will only send the window size worth of unacknowledged message before stopping to wait for a new acknowledgement message or the timeout window to be exceeded. 


