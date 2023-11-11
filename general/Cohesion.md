---
aliases: []
checked: false
created: 2023-08-05
last_edited: 2023-08-05
publish: true
tags: programming
type: meta
---
# Cohesion

When googling what this word means I got the following

>[!Quote] Google
>The action or fact of forming a united whole.

Which really does define what cohesion within code means. A class is highly cohesive if all the components of that class belong together. It has low cohesion if there are random functions or variables that don't contribute to the whole.

## Heuristic for determining Cohesion

Whenever two variables are used in the same line of code - consider these cohesive. They belong together. So if you can split your variables up based on whether they are in the same line of code your class or function has low cohesion. Normally this is indictive that your function or class can be [[Refactored]].
