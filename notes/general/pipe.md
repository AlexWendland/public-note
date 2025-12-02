---
aliases: []
checked: false
created: 2023-08-05
draft: false
last_edited: 2023-11-11
title: Pipe
tags:
  - programming
type: terminology
---
# Pipe

This is where you do multiple manipulations to a data object in 'one line' but break it up over multiple. This is commonly used in [Python Index](python_index.md) with the [Pandas](pandas.md) library.

```python
data_frame.group_by(["animals"])
	.mean()
	.reset_index()
	.rename({"height": "mean_height", "weight": "mean_weight"})
```

This operations are naturally grouped together and effect the same object. This is not to be confused with a [train wreck](train_wrecks.md).
