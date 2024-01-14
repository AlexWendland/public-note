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

In what follows we use Checkers to provide an example of the process you go through to design a learning system.
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
- Student lead learning - The student can ask questions about particularly confusing positions and get the correct decision.
	- In the checkers example, this might be from allowing the machine to play itself.

Lastly how representative the test samples are. 
- If a computer only plays itself it might not be able to bit the common ways a human plays.
- It is often assumed the training data follows the same distribution as the testing data. 
	- However, one of the goals of machine learning is to generalise beyond this.
	- In practice this is one of the most violated assumptions from the theory.

# Designing a learning system

Now we must make 3 more choices:
1. the exact type of knowledge to be learned,
2. a representation for this target knowledge, and 
3. a learning mechanism.

## Type of knowledge to be learnt

This normally comes in the form of a target function. 

For example, in the checkers example you may think the best thing to learn would be a function that choose the best move for a given state of the board $ChooseMove: B \rightarrow B$, where $B$ is the set of legal board states. However, in practice this is quite complicated. The preferred option is the board evaluation function $V: B \rightarrow \mathbb{R}$, that assigns a score to each state of the board for one player. 

It is important to be specific with the target function, as it may help simplify design decisions later.

In the example above we can may explicit expectations on $V$ such as $b \in B$ 
- if it is won then $V(b) = 100$,
- if it is lost then $V(b) = -100$,
- if it is drawn then $V(b) = 0$, and
- else $V(b) = V(b')$ where $b'$ is the end state assuming optimum play.

The function as you right it down might be $V$ *non-operational* definition as it is not efficiently computable (as the last condition above makes it). The goal of learning is to make an *operational* description of $V$. This might not be known perfectly however a [[Prediction|prediction]] of it $\hat{V}$ will suffice. 

# Choosing a representation of this target knowledge

This is equivalent to choosing a [[Modelling paradigm|modelling paradigm]].

In checkers you could represent $V$ as:
- A letteral function from board states to values,
- A neural network, or
- A function on board features that are predefined.

## A learning Mechanism

Now given a function $V: A \rightarrow B$ you need: 
- [[Training data|training data]] to build $\hat{V}$ of the form $T \subset A \times B$, 
- a method to evaluate this approximation - the [[Objective function|objective function]], and 
- an algorithm to learn.

In the example it may be confusing how we define training data, as the training experience is it playing itself. Here we use a trick to make the training data using $\hat{V}$ itself.

The evaluation process for a linear function is commonly something like [[Mean squared error (MSE)]]. Evaluating the output of the [[Prediction|prediction]] $\hat{V}$ against the training data $T$.

In the example as would choose the algorithm appropriate for the representation of $V$ that we went for.




