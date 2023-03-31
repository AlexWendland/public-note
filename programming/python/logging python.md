---
aliases: []
type: module
publish: true
created: 2023-03-31
last_edited: 2023-03-31
tags: programming, python, best-practices
chatgpt: false
---
# logging python

The logging module in python is used to do exactly what you would expect, it logs messages.

Some cool features it has is:
- different levels of messages for filtering of messages,
- different logger names for different parts of the application,
- different handlers to post messages such as streamed, files, http and rotating, and
- custom formatters for different handlers.

## Logging level

There are 5 levels of severity in the logging module:
| Level name | Integer value | How to access | Generally used for |
| ---------- | ------------- | ------------- | ------------------ |
| Debug      | 10            | logging.DEBUG |                    |
1. debug,
2. info,
3. warning,
4. error, and
5. critical.

These levels are actually given 