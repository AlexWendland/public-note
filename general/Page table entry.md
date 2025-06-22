---
aliases:
  - page table entry
checked: false
created: 2025-03-22
last_edited: 2025-03-22
draft: false
tags:
  - OS
type: definition
---
>[!tldr] Page table entry
>A *page table entry* is indexed by the [[Virtual page number (VPN)|virtual page number]] and contains the [[Physical Frame Number (PFN)|physical frame number]] which is how the mapping between the two is carried out. However, the entry also contains some other management fields such as:
>- Present: If mapping is still valid or not. As the [[Memory frame|frame]] may have been reclaimed.
>- Dirty: If the [[Memory frame|frame]] has been written too. For example if it represents something on disk we know it still need to be copied down to disk.
>- Access: If the [[Memory frame|frame]] has been accessed by the [[Process|process]] for read or write operations.
>- Protection: If the [[Process|process]] has read/write/execute permissions on the memory.
>
>Though these differ by architecture. See below for a particular example.
>![[page_table_entry.png]]

