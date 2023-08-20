---
aliases: []
type: practice
publish: true
created: 2023-08-20
last_edited: 2023-08-20
tags: programming, list[str]
chatgpt: false
---
# Wrap 3rd party libraries

It is a good practice to wrap 3rd party libraries before putting them into your system. This will allow you to:
- Control the API on how your library interacts with it.
- If you need to change provider there is only one place to go in the code to change that usage.
- Allows you to handle [[Exception|exceptions]] in a more useful way for your code. 

## Natural opposition between library providers and users

When people write 3rd party libraries, they want them to be as widely applicable as possible. However, when you use a library to solve a problem you may only need part of its functionality. This is a natural opposition that exists between 3rd party libraries and its consumers. (We have all had it when you go buy a tool and it boasts an impressive array of features you secretly know you are never going to use.)