---
aliases:
  - COW
checked: false
created: 2025-03-23
last_edited: 2025-03-23
publish: true
tags:
  - OS
type: definition
---
>[!tldr] Copy on write (COW)
>If two [[Process|processes]] are using the same memory the [[Operating system (OS)|operating system]] can let them share access to the same [[Memory frame|frame]]. Only needing to copy the data across if a write on the data is initialized by either process. This delays operations from the operating system until they are absolutely necessary.
>
>![[copy_on_write.png]]

