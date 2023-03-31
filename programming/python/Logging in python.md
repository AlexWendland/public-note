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

This library was converted from [[Java]] which is why it does not conform to the python naming  

## Logging level

There are 5 levels of severity in the logging module:
| Level name | Integer value | How to access    | how to send                 | Generally used for                                                         |
| ---------- | ------------- | ---------------- | --------------------------- | -------------------------------------------------------------------------- |
| Debug      | 10            | logging.DEBUG    | logging.debug(*message*)    | A message that will help you debug the code but not worth noting otherwise |
| Info       | 20            | logging.INFO     | logging.info(*message*)     | A message about normal running of your code the user might want to know    |
| Warning    | 30            | logging.WARNING  | logging.warning(*message*)  | A warning to the user that they are using the code incorrectly             |
| Error      | 40            | logging.ERROR    | logging.error(*message*)    | An error with the application that it can handle and keep running          |
| Critical   | 50            | logging.CRITICAL | logging.critical(*message*) | An error with the application that it can not handle and should stop       |

According to the [[pylint]] guidelines, the message should be formatted using the lazy % formatting. 

## Configuration

