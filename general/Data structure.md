---
aliases: [data structure, Data structures, data structures]
type: structure
publish: true
created: 2023-07-11
last_edited: 2023-07-11
tags: programming
chatgpt: false
---
# Data structure

A data structure is simply a container of information. All its variables are public and can be depended on by other actors in the code base. It could contain some functions that present the data in a nicer format but it can't rely on private data holding internal state (like a boolean has_printed).

In python data structures are really easy to define.
```python
from dataclasses import dataclass

@dataclass
class point:
	x : float
	y : float
```

Normally, a single data structure will have lots of implementations as it is just a way to group data together in a meaningful way.