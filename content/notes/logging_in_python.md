---
aliases: []
checked: false
created: 2023-03-31
draft: false
last_edited: 2023-11-11
tags:
  - programming
  - python
  - best-practices
title: Logging in python
type: module
---
# logging python

The logging module in python is used to do exactly what you would expect, it logs messages.

Some cool features it has is:
- different levels of messages for filtering of messages,
- different logger names for different parts of the application,
- different handlers to post messages such as streamed, files, http and rotating, and
- custom formatters for different handlers.

This library was converted from [Java](java.md) which is why it does not conform to the python naming conventions.

I played around with some features in a [Github repo](https://github.com/AlexWendland/python-tutorials/tree/main/logging), if you find seeing easier than reading.

## Logging level

There are 5 levels of severity in the logging module:
| Level name | Integer value | How to access    | how to send                 | Generally used for                                                         |
| ---------- | ------------- | ---------------- | --------------------------- | -------------------------------------------------------------------------- |
| Debug      | 10            | logging.DEBUG    | logging.debug(*message*)    | A message that will help you debug the code but not worth noting otherwise |
| Info       | 20            | logging.INFO     | logging.info(*message*)     | A message about normal running of your code the user might want to know    |
| Warning    | 30            | logging.WARNING  | logging.warning(*message*)  | A warning to the user that they are using the code incorrectly             |
| Error      | 40            | logging.ERROR    | logging.error(*message*)    | An error with the application that it can handle and keep running          |
| Critical   | 50            | logging.CRITICAL | logging.critical(*message*) | An error with the application that it can not handle and should stop       |

According to the [pylint](pylint.md) guidelines, the message should be formatted using the lazy % formatting.

You can set the level of the logger to filter messages of a lower level than set.

```python
logger.setLevel(logging.INFO)
```

## Basic Configuration

You can call basicConfig before logging anything to construct the root logger and set some properties of it. You can straight out of the box set the level, write to a file, format the messages.

```python
logging.basicConfig(
level = logging.DEBUG, # Set the custom level of the logger like this.
							#Defaults to Warning.
filename = "somefile.log", # Set the filename of the logger like this.
							#Defaults to stdout.
filemode = "w", # Set the filemode of the logger like this.
							#Defaults to append.
format = "%(asctime)s - %(levelname)s - %(message)s", # Set the format of
							#the logger like this.
							#Defaults to quite a nice format
datefmt = "%d-%b-%y %H:%M:%S" # Set the date format of the logger like
							#this.
)
```

Note this will effect a logger named `root` and will be the default logger that is accessed by using `logger.level(*message*)`.

## Named loggers

You can set up multiple loggers by getting one by a name, you can do this using `logging.getLogger(*name_of_logger*)` which returns you an object to write to.

It is good practice for applications to name the logger `__name__` like `logging.getLogger(__name__)`. Then when this logger is imported to other code the logger will be named with that library.

>[!question] Resetting the main logger
>It would be nice to overwrite `logger.error` to use a named logger, though I don't think you can do that.

## Logging errors

You can log errors and their trace by using the `exc_info` variable whilst logging like `logging.error(*message*, exc_info = True)` you would normally use this in code where an error has been caught.

```python
try:
	#Some error gets thrown here
except SomeError:
	logging.error("My message", exc_info = True)
```

This can be done with other severity levels also. Though with error there is a short form to do this.

```python
try:
	#Some error gets thrown here
except SomeError:
	logging.exception("My message")
```

## Handler's and formatter's

### Handler

The handler class tells logging what to do with the messages that are being written to the logger object. There are lots of useful inbuilt handlers.

| Handler class       | What it does                                                                                      |
| ------------------- | ------------------------------------------------------------------------------------------------- |
| StreamHandler       | It streams the messages to some output source, such as standard out. This is the default handler. |
| FileHandler         | This writes the messages to a file that you specify.                                              |
| RotatingFileHandler | This will rotate the log files based on their size or some form of time.                          |

Each handler has different required variables.

```python
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler("file.log")
```

### Formatter

This tells the logging object the format of how the messages should be sent. You provide this a string of the message format using the variables

| variable name | What it relates to                               |
| ------------- | ------------------------------------------------ |
| message       | The message passed to the logger                 |
| ip            | The id of the process                            |
| asctime       | The time of the message                          |
| name          | The name of the logger that was sent the message |
| levelname     | The level of the message                         |

For example a valid format type would be `"%(asctime)s - %(name)s - %(levelname)s - %(message)s"` though ... not that pretty. You can change the date format by setting the `datefmt` variable.

```python
formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")

time_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt = "%Y-%m-%d")
```

### Attaching everything

Each handler can have a formatter attached, however loggers can have multiple handlers attached.

```python
handler1.setFormatter(formatter)
handler2.setFormatter(formatter)

logger.addHandler(handler1)
logger.addHandler(handler2)

logger.critical("Hey") # This will be handled by both handler1 and 2.
```

## Advanced Configuration

Instead of defining the configuration in the code you can hand it in a file. The configuration can be passed by a dictionary - therefore you can define it in a yaml or json file - or a conf file.

### Conf file

Here is an example of such a conf file.

```conf
# Define the names for the loggers you want to use.

[loggers]

keys=root,sampleLogger

# Define the names of the handlers that output the logs

[handlers]

keys=consoleHandler,fileHandler

# Define the formatters for the handlers

[formatters]

keys=simpleFormatter,verboseFormatter

# The logger level will be the first filter that is applied.

[logger_root]

level=DEBUG

handlers=consoleHandler

# The qualname is the name of the logger that is used in the code.

[logger_sampleLogger]

level=DEBUG

handlers=fileHandler

qualname=sampleLogger

# If you want to stream to the console you need to pass it the sys.stdout

[handler_consoleHandler]

class=StreamHandler

level=DEBUG

formatter=simpleFormatter

args=(sys.stdout,)

[handler_fileHandler]

class=FileHandler

level=INFO

formatter=verboseFormatter

args=('sample.log', 'a')

[formatter_simpleFormatter]

format=%(asctime)s - %(name)s - %(levelname)s - %(message)s

[formatter_verboseFormatter]

format=%(asctime)s - %(name)s - %(levelname)s - I love pie - %(message)s
```
