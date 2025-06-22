---
aliases: []
checked: false
created: 2023-08-05
last_edited: 2023-11-11
draft: true
tags: []
type: planning
---
# Your pages in reverse order

It is good to review old pages and update their last_edited value.

```dataview
TABLE last_edited, created
FROM -"templates"
SORT last_edited ASC, created ASC
WHERE last_edited
```
