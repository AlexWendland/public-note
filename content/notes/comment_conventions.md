---
aliases:
  - comments
  - comment
  - comment conventions
created: 2023-07-01
date_checked:
draft: false
last_edited: 2023-11-11
tags:
  - programming
  - clean-code
title: Comment conventions
type: convention
---

Comments in code are a necessary evil. As they are not the code, there is no way to check their integrity. As code gets changed the comments may not be updated and can easily cause more confusion that good. Comments also take some thought to process as you need to understand what the person who wrote the comment meant - which is far easier to do in code.

There are good use cases like a public API or todo notes - though they are mainly there to compensate for our failure to express ourselves in code. They do not make up for bad code!

The goal is to express yourself in code so clearly you will never really need to use them to help other coders. If you follow the other convention notes - there will only be a few usecases for comments.

# Good comments

- **API docstrings**: If you exposing some functions to others, provide a full doc string so they don't have to read your code to understand what is going on.
- **Legal comments**: If you are required to add a comments by the legal team.
- **Warning of consequences**: If you want to highlight a particular consequence like irreparably changing a database.
- **TODO comments**: Tag for some task to extend the code. These shouldn't be an excuse to write shoddy code.
- **Amplification**: To highlight some aspect of the code that might be overlooked.

# Bad comments

- **Redundant comments**: Ones that just explain the code - which could be understood by just reading the code instead.
- **Misleading comments**: Have inaccuracies that cause confusion instead of clarify the situation.
- **Mandated comments**: In some companies they are required to provide comments in certain places. These just take up screen space as people will ignore them.
- **Journal comments**: Sometimes changes to a file need to be recorded at the top of the file. With modern version control this should be stored somewhere else.
- **Position markers**: People can use position markers in code, like sections. If you need these it might indicate that the file is doing too much.
- **Attribution and bylines**: Want to say you made this file? This can be handled by the source control.
- **Commented out code**: No one will delete this as they will worry that it is important. If you aren't going to use it delete it. If you want to keep the version, try using the version control system instead.
- **Docstrings in non-public functions**: If the function isn't exposed to an outside user, docstrings are not required. The function should be short enough so the signature is easily understood.

# Practices

## Don't use comments when you could just use a function or variable name

Regularly if you want to write a comment to explain a variable or function - that comment is a better reflection of its name and should be used for that instead.

## Only use local information

If you write a comment, make sure it describes code close to it. If it uses information outside that context you can't guarantee the comment will be updated when that changes.

## Try to keep any comments concise

Don't include historical discussion or irrelevant details in the comment. If there was some research applied in picking a certain approach write that up somewhere else and include a link.

## Make the connection to the code obvious

If the connection to the code isn't obvious, it will either be ignored or you will confuse the next developer to look at it. Making the comment unhelpful.
