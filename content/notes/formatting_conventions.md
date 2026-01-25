---
aliases:
  - formatting
  - code formatting
  - formatting conventions
created: 2023-07-01
date_checked:
draft: false
last_edited: 2023-11-11
tags:
  - programming
  - clean code
  - ''
title: Formatting conventions
type: convention
---

Here formatting means the spacing and organisation of files in your code base. This is about communication and leaving a well organised desk space for others to use after you.

The main metaphor used for formatting is a news paper. Nearly all code is read left to right and top to bottom.   You documents, should start with a head line, then as you go down slowly increase in the level of detail. The code should be in nice columns and no story should be too long. It shouldn't use too much indentation but should be nicely spaced to make it easy to read. You should use paragraphs to break up concepts.

# Document length

Given you are keeping to the [Class conventions](class_conventions.md) your documents shouldn't be very long (between 500-800 lines).

Documents should try to keep concepts that are related to one another, whilst separating out code that is nearly completely unrelated to the main point of the file.

# Vertical space

Each line should represent a single expression or clause. Every group lines should  represent a single concept or thought. Then you should separate each thought with a single line.

The vertical distance between thoughts should represent (as much as possible) the level of relatedness of the concepts. If some code is completely unrelated to anything - it might not belong in this file.

# Variables

Generic variables should be declare as close to their point of use as possible. Whereas instance variables should be declared at the top of the class and not hidden in the code.

# Functions

Dependent functions should be below the function that calls them. This keeps to the newspaper metaphor, and means we descends in abstraction as the file goes on.

# Horizontal space

Historically there was a quite tight line limit to allow for smaller screens (80 characters). Whilst screens have now gotten bigger, having long lines is most probably indicative of a single line trying to do too much or excessive indentation. The normal cause of long times are [comments](comment_conventions.md) or strings, which should be broken up to make it easier to read. Trying to stick to 80 characters isn't hard and pretty standard in most code formatters. It also makes code easy to read on a side by side comparison which people will use for [Pull Requests](pull_requests.md) or handling [Merge conflicts](merge_conflicts.md).

Some people like horizontal alignment of assignment of variables. Personally I don't and I think it takes more effort to maintain that benefit given to the reader.

# Indentation

Whilst sticking to indenting class and function definitions [try not to nest functions](function_conventions.md#functions-shouldnt-be-too-nested).
