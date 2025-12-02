---
aliases:
checked: false
course: 'CS7641 Machine Learning'
created: 2024-01-13
draft: false
last_edited: 2024-01-13
title: Week 1 - Chapter 1 Machine Learning
tags:
  - OMSCS
type: lecture
week: 1
---
# Week 1 - Chapter 1 Machine Learning

This is my notes from the first chapter of [MachineLearningTomMitchell.pdf](machinelearningtommitchell.pdf.md).

# 1.1 Well posed learning problems

[Machine Learning](../../general/machine_learning.md)

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

The function as you right it down might be $V$ *non-operational* definition as it is not efficiently computable (as the last condition above makes it). The goal of learning is to make an *operational* description of $V$. This might not be known perfectly however a [prediction](../../general/prediction.md) of it $\hat{V}$ will suffice.

# Choosing a representation of this target knowledge

This is equivalent to choosing a [modelling paradigm](../../general/modelling_paradigm.md).

In checkers you could represent $V$ as:
- A letteral function from board states to values,
- A neural network, or
- A function on board features that are predefined.

## A learning Mechanism

Now given a function $V: A \rightarrow B$ you need:
- [training data](../../general/training_data.md) to build $\hat{V}$ of the form $T \subset A \times B$,
- a method to evaluate this approximation - the [objective function](../../general/objective_function.md), and
- an algorithm to learn.

In the example it may be confusing how we define training data, as the training experience is it playing itself. Here we use a trick to make the training data using $\hat{V}$ itself.

The evaluation process for a linear function is commonly something like [Mean squared error (MSE)](../../general/mean_squared_error_(mse).md). Evaluating the output of the [prediction](../../general/prediction.md) $\hat{V}$ against the training data $T$.

In the example as would choose the algorithm appropriate for the representation of $V$ that we went for.

# Summary

A lot of learning systems follow the design below.

![learning_system_diagram](../../../images/excalidraw/learning_system_diagram.excalidraw.svg)

- The performance system: Runs an instance of the task and returns a new solution.
- The critic: Uses that instance to generate training data.
- Generaliser: Uses this training data to update the model.
- Experiment generator: Decides what new experience would be best for the next round of training.

Whilst not all these components are required, training systems tend to follow this cycle.

In our example:

- The performance system would play a game starting for the provided state.
- The critic would transform that game into a training data.
- The generaliser would run the learning algorithm on it.
- The experiment generator could either start a game at the beginning of the game or a state of particular confusion for the model.

Learning problems can be summarised as searching through large "Hypothesis spaces" to find the best fitting function to a given curve.

# Issues in Machine Learning

- What algorithms perform best for a given task?
- How much training data does it take to make a learning process converge?
- What is the most useful experience to next learn on?
- What function is worth learning for a given task?
- Can the learner automatically alter its representation to reduce [restriction bias](restriction_bias.md)?

