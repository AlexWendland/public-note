---
aliases: 
checked: false
course: "[[CS6200 Introduction to Graduate Algorithms]]"
created: 2024-01-13
last_edited: 2024-01-13
publish: true
tags:
  - OMSCS
type: lecture
week: 1
---
# Week 1 - Chapter 1 Machine Learning

This is my notes from the first chapter of [[MachineLearningTomMitchell.pdf]].

# 1.1 Well posed learning problems

![[Machine Learning]]

>[!example] Checkers
>If we want a programme to learn at checkers we simply need to define $T$, $P$, and $E$!
>- Task $T$: playing checkers,
>- Performance measure $P$: percentage of games won against opponents, and
>- Training experience $E$: playing practice games against itself.

# Training experience

There are important classifications of training experience.

For example when the pay off comes:
- Direct training examples - examples of exactly the correct thing at the time of a decision. 
	- In the checkers example, given a board position the right move to make. 
	- Normally the best training but harder to get.
- Indirect training examples - examples that leads to a positive outcome but not at the point of the decision. 
	- In the checkers example, a previous game where it knows a sequence of moves that leads to a win or loss.
	- Indirect training faces the problem of *credit assignment*, which moves where correct?

Or how much autonomy the learner has over this process:
- Leader lead learning - A sequence of training examples built by the teacher.
	- In the checkers example, if you feed it a selection of games or game states.
- Student lead learning - The student can 