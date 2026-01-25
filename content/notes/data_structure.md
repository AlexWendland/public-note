---
aliases:
  - data structure
  - Data structures
  - data structures
created: 2023-07-11
date_checked:
draft: false
last_edited: 2023-11-11
tags:
  - programming
title: Data structure
type: structure
---

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
