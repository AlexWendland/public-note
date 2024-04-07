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

![[Zero-sum game|zero-sum]]

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
>[!warning] Don't understand
>I don't really get how this situation is any different to the above ones. The lecturers say now the value of the game differ for both players but it still boils down to a matrix that you could have gotten with a normal game?

## Mix strategies

![[Pure strategy]]

However you can have non-deterministic strategies.

![[Mixed strategy]]

In the game above, if player one holds with probability $p$ then we get expected return $15p- 5$ if player two resigns otherwise we get $5 - 10p$ profit if player two sees the card. Therefore if we choose $p = 0.4$ we can get expected profit of $1$ no matter what player $B$ does. 

If you do the same for player two, picking to see with probability $q$ then we get expected return $10q - 5$ if player one resigns but $10 - 15q$ if they hold. Then we get optimum $q = 3/5$ which also gives player one a profit of 1.

## Removing [[Zero-sum game|zero-sum]]

![[Prisoner's dilemma]]

In the [[Prisoner's dilemma]] the dominating strategy is for them both to testify. Even if any player could change their decision after finding out the outcome they wouldn't want to.

![[Nash equilibrium]]

This works for both pure or mixed strategies. 

## Dominating strategies

![[Strictly dominated strategy]]

This could be used to get [[Nash equilibrium]].

![[Elimination and Nash Equilibrium]]

Though this doesn't guarantee finding it. Though there is always a [[Nash equilibrium]] in finite games.

![[Existance of Nash equilibrium]]

>[!Note]
>Normally the best way to get out of the prisoners dilemma is to change the structure of the game.

## Multiple rounds

Suppose now you are in a situation where you are playing iterative rounds of a game with the same player.

## Known number of rounds

One approach to solving this issue is to combine possible series of strategies as a new series and to investigate the composite game. Though an easier solution to this situation can be found be thinking of them separately.

If the number of rounds are known beforehand, then consider the last round. As there are no games afterwards - there is no incentive to not behave rationally, so we will use the [[Nash equilibrium]] strategy.

Though given this last game is already decided we might as well consider playing one less game. Though this inductively gives that each player will play a [[Nash equilibrium]] strategy at each step of the game.

However, which [[Nash equilibrium]] is an interesting problem!

## Unknown number of rounds

At the end of a round suppose there is a $\gamma$ chance you play again and a $1-\gamma$ chance you end. This stays constant and you use [[Discounted rewards|discounted rewards]] to evaluate performance.

>[!Note]
>[[Discounted rewards]] is perfectly built for this. Suppose $G$ is the random variable for the value of playing this game, let $g_i$ be the reward for the $i'th$ round then
>$$\mathbb{E}[G] = g_i + \gamma \mathbb{E}[G] + (1-\gamma) 0 = g_i + \gamma \mathbb{E}[G].$$
>Therefore if we pick a strategy that would pay off $g_i$ in round $i$ if it were played then the total expected value of this strategy would be
>$$\mathbb{E}[G] = \sum_{i \in \mathbb{N}} g_i \gamma^i.$$

The expected number of round in this set up is $\frac{1}{1-\gamma}$.

## Tit for Tat

When in the above situation there are some meta strategies you can adopt. For example you can always choose one option - like in the known number of rounds example. However, you can now adopt strategies that depend on the opponents move.

![[Tit for Tat]]

>[!example] [[Prisoner's dilemma]]
>Suppose we do this with the prisoners dilemma. Now lets consider 3 strategies, always stay silent (silent), always testify (testify) or tit for tat (tft) where we look at the two different start points silent and testify. Lets consider the strategy matrix (to simplify things I took a factor of $\frac{1}{1 - \gamma}$ out)
> $$
> \begin{array}{c|cc}
> \ \mbox{A \\ B} & \mbox{silent} & \mbox{testify} & \mbox{tft-silent} & \mbox{tft-testify}\\ \hline 
> \mbox{silent} & (1,1) & (3,0) & (1,1) & (3-2\gamma, \gamma) \\
> \mbox{testify} & (0,3) & (2,2) & (2 \gamma, 3 - \gamma) & (2,2) \\
> \mbox{tft-silent} & (1,1) & (3 - \gamma, 2 \gamma) & (1,1) & (\frac{3}{1 + \gamma}, \frac{3 \gamma}{1 + \gamma})\\
> \mbox{tft-testify} & (\gamma, 3-2\gamma) & (2,2) & (\frac{3\gamma}{1+\gamma}, \frac{3}{1 + \gamma}) & (2,2)\\
> \end{array}
> $$

Lets consider the preferred strategy when your opponent has already picked (this depends on $\gamma$).

| Opponent    | $\gamma < 0.5$       | $\gamma = 0.5$       | $\gamma > 0.5$       |
| ----------- | -------------------- | -------------------- | -------------------- |
| Silent      | Testify              | Testify              | Testify              |
| Testify     | Testify, tft-testify | Testify, tft-testify | Testify, tft-testify |
| tft-silent  | testify              | Any                  | tft-silent, silent   |
| tft-testify | Testify, tft-testify | Any                  | silent               |

Here no matter what $\gamma$ we have that testify is a [[Nash equilibrium]]. Though we have additional equilibrium depending on $\gamma$
- for $\gamma \leq 0.5$ tft-testify is also a [[Nash equilibrium]], and
- for $\gamma \geq 0.5$ tft-silent is also a [[Nash equilibrium]].

