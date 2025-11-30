---
aliases: 
checked: false
created: 2024-04-06
last_edited: 2024-04-06
draft: false
tags:
  - game-theory
type: example
---
>[!example] Prisoner's dilemma
> Two people are caught mid crime and put in separate cells where they can't talk to each other. They are both offered a plea deal if they testify against their companion, where:
> - If they both cooperate with each other and stay silent they both get one month in jail,
> - If one of them defects and testifies and the other doesn't whoever testify gets off free whilst the other stays in jail for 3 months, however
> - If they both defect and testify they both get sent away for 2 months.
> 
> This can be summarised in the following matrix
> $$
> \begin{array}{c|cc}
> \ \mbox{A \\ B} & \mbox{cooperate} & \mbox{defect}\\ \hline 
> \mbox{cooperate} & (1,1) & (0,3) \\
> \mbox{defect} & (3,0) & (2,2) \\
> \end{array}
> $$
> If the player stays silent they pay an expected cost of 2, whereas if they testify they pay an expected cost of 1. So the optimum strategy is to testify. However by other testifying combined they are paying the largest cost.
