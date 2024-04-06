---
aliases: 
checked: false
course: "[[CS6200 Introduction to Graduate Algorithms]]"
created: 2024-04-06
last_edited: 2024-04-06
publish: true
tags:
  - OMSCS
type: lecture
week: 13
---
# Week 13 - Game theory

![[Game theory]]

## 2-player zero-sum finite game of perfect information

This is a lot of words but these games are like tick tack toe or noughts and crosses. Whilst these are fun they all boil down to a payoff matrix for the different strategies you take. Like the following
$$
\begin{array}{c|ccc}
 \ 1 & a & b & c\\ \hline 
x & 1 & 0 & -1 \\
y & -1 & 0 & 1 \\
\end{array}
$$
to read this table, if the first player at the top picks action $a$ and the second player on the rows picks $x$ then player one gets 1 point whereas player two gets -1 point. This is the [[Zero-sum game|zero-sum]] aspect to the game. (Note the game could be non-deterministic but we just take [[Expected value|expectation]] to find the values in the grid.)

We call the options $a$, $b$, $c$, $x$ and $y$ strategies.

![[Minmax decision]]

![[Optimum play exists for 2-player zero-sum games with perfect information]]

This means we can determine the value of the game by both players following their best strategy we can work out the value of the game.  

>[!warning]
>I don't really understand what happens in the case
>$$
> \begin{array}{c|cc}
>  \ 1 & a & b \\ \hline 
> x & 1 &  -1 \\
> y & -1 &  1 \\
> \end{array}
> $$
> What would be the optimal pure strategy?

## No more perfect information

[[Perfect information]] means that all the knowledge is known by all players at the start of the game. A good example where this is not the case is poker.

>[!example] Mini-poker
>Suppose we are in a game where the following happens: 
>1. Player one is dealt a card, 50% of the time it is red and the other 50% it is black.
>2. If player one is dealt a black card they can resign or keep playing. If they are dealt a red card they have to keep playing. If they resign they get -20 score.
>3. Player two then gets to choose to resign or for player one to show them their card.
>	1. If player two resigns player one gets 10 points.
>	2. If player one shows their card and it is back they get -40 points.
>	3. If player one shows their card and it is red they get 30 points.
>
>What is the optimum play for either party?

In this case we can still calculate the payoff matrix. Note if player one chooses a resign strategy by they get dealt a red card they have to keep going.
$$
\begin{array}{c|cc}
 \ \mbox{red} & \mbox{resign} & \mbox{hold}\\ \hline 
\mbox{resign} & -20 & 10 \\
\mbox{show} & -20 & -40\\
\end{array} \ \ \ \ \
\begin{array}{c|cc}
 \ \mbox{black} & \mbox{resign} & \mbox{hold}\\ \hline 
\mbox{resign} & 10 & 10 \\
\mbox{show} & 30 & 30\\
\end{array}  \ \ \ \ \
\begin{array}{c|cc}
 \ \mbox{either} & \mbox{resign} & \mbox{hold}\\ \hline 
\mbox{resign} & -5 & 10 \\
\mbox{show} & 5 & -5\\
\end{array}
$$
