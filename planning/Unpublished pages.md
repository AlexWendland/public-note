---
aliases: []
type: planning
publish: false
created: 2023-08-05
last_edited: 2023-08-05
---
# Unpublished pages

```dataview
TABLE created
FROM -"templates" and -"planning"
WHERE !publish and created
SORT created DESC
```