---
aliases: []
type: terminology
publish: true
created: 2023-08-05
last_edited: 2023-08-05
tags: programming
chatgpt: false
---
# Pipe

This is where you do multiple manipulations to a data object in 'one line' but break it up over multiple. This is commonly used in [[Python]] with the [[Pandas]] library. 

```python
data_frame.group_by(["animals"])
	.mean()
	.reset_index()
	.rename({"height": "mean_height", "weight": "mean_weight"})
```

This operations are naturally grouped together and effect the same object. This is not to be confused with a [[Train Wrecks|train wreck]].