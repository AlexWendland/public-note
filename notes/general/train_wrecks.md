---
aliases:
  - train wreck
  - train wrecks
checked: false
created: 2023-08-05
draft: false
last_edited: 2023-11-11
title: Train Wrecks
tags:
  - programming
  - clean-code
type: terminology
---
# Train Wrecks

This is a line of code which repeatedly calls different functions on return variables. Like the following:

```python
object.get_settings().get_graphics_config().get_makers_url().get_abs_path()
```

Note that they must return a different object, if they are doing permuting objects this a [pipe](pipe.md) and is more acceptable when doing data manipulation.
