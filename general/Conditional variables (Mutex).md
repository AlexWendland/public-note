---
aliases:
  - conditional variables
  - Conditional variables
checked: false
created: 2024-09-04
last_edited: 2024-09-04
publish: true
tags:
  - OS
type: definition
---
>[!tldr] Conditional variables (Mutex)
> A [[Mutex|mutex]] may need special operations applied upon some condition being met. (For example processing a list when it is full.) To implement this we use [[Data structure|data structure]] called conditional variable that holds at least:
> - A reference to the [[Mutex|mutex]] it is related to, and
> - A list of waiting [[Thread|threads]].
> 
> Then an [[Operating system (OS)|OS]] will offer 3 calls on the [[Application Programming Interface (API)|API]]:
> - wait(*mutex*, *condition*): [[Mutex|mutex]] is released and reacquired when the condition is met (i.e. they are notified about the condition).
> - signal(*condition*): notify a single [[Thread|thread]] waiting on the condition it has been met.
> - broadcast(*condition*): notify all [[Thread|threads]] waiting on the condition. (Though as they are all waiting on the [[Mutex|mutex]] they only activate one at a time.)
