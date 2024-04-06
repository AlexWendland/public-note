---
aliases: 
checked: false
created: 2024-04-06
last_edited: 2024-04-06
publish: true
tags:
  - game-theory
type: example
---
>[!example] Prisoner's dilemma
> Two people are caught mid crime and put in separate cells where they can't talk to each other. They are both offered a plea deal if they testify against their companion, where:
> - If neither of them testify they both get sent away for one month,
> - If one of them testifies and the other doesn't whoever testify gets off whilst the other stays in jail for 3 months, however
> - If they both testify they both get sent away for 2 months.
> 
> This can be summarised in the following matrix
> $$
> \begin{array}{c|cc}
> \ \mbox{A \\ B} & \mbox{silent} & \mbox{testify}\\ \hline 
> \mbox{silent} & (1,1) & (3,0) \\
> \mbox{testify} & (0,3) & (2,2) \\
> \end{array}
> $$
> If the player stays silent they pay an expected cost of 2, whereas if they testify they pay an expected cost of 1. So the optimum strategy is to testify. However by other testifying combined they are paying the largest cost.


