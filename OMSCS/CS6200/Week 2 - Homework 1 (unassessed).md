---
aliases: []
type: exercise
publish: false
created: 2023-08-28
last_edited: 2023-08-28
tags: OMSCS
course: "[[CS6200 Introduction to Graduate Algorithms]]"
week: 2
chatgpt: false
---
# Week 2 - Homework 1 (unassessed)

From [Algorithms](http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf) by S. Dasgupta, C. Papadimitriou, and U. Vazirani.

> [!question] 6.4 String of words (part 1)
> You are given a string of $n$ characters $s[1 \ldots n]$, which you believe to be a corrupted text document in which all punctuation has vanished (so that it looks something like “itwasthebestoftimes...”). You wish to reconstruct the document using a dictionary, which is available in the form of a Boolean function $dict( \cdot )$ for any string $w$,
> $$dict(w) = \begin{cases} true & \mbox{if w is a valid word}\\ false & \mbox{otherwise}\end{cases}.$$ 
> 1. Give a dynamic programming algorithm that determines whether the string $s[\cdot]$ can be reconstituted as a sequence of valid words. The running time should be at most $O(n^2)$, assuming calls to $dict$ take unit time.

Subproblem:
Let $L(k)$ = whether the subword $s[1\ldots k]$ can be split into words.

Solution:
$L(n)$.

Recursion:
$L(k) = \bigwedge_{i=0}^k L(i) \land dict(s[i+1\ldots k])$
where $L(0)$ is true.

```python
from typing import List


def string_of_words(word_dictionary: List, string: str) -> bool:
    solution = []

    for index in range(len(string)):
        potenial_solutions = [
            solution[i] and (string[i + 1 : index + 1] in word_dictionary)
            for i in range(index)
        ] + [string[: index + 1] in word_dictionary]

        solution.append(any(potenial_solutions))

    return solution[-1]


if __name__ == "__main__":
    word_dictionary = ["aba", "aa"]

    print(string_of_words(word_dictionary, "abaabaaaba")) # False
```

> [!question] 6.4 String of words (part 2)
> 2. In the event that the string is valid, make your algorithm output the corresponding sequence of words.

```python
from typing import List, Optional


def string_of_words(word_dictionary: List, string: str) -> Optional[str]:
    solutions = []

    for index in range(len(string)):
        if string[: index + 1] in word_dictionary:
            solutions.append([string[: index + 1]])
        else:
            solution = []
            for i in range(index):
                if (
	                solutions[i] 
	                and (string[i + 1 : index + 1] in word_dictionary)
	            ):
                    solution = solutions[i] + [string[i + 1 : index + 1]]
                    break
            solutions.append(solution)

    return solutions[-1]


if __name__ == "__main__":
    word_dictionary = ["aba", "abaa"]

    print(string_of_words(word_dictionary, "abaaaba"))
```


>[!question] 6.8 Longest common **substring**
>Given two strings $x = x_1x_2 \ldots x_n$ and $y = y_1y_2 \ldots y_m$, we wish to find the length of their longest common **substring**, that is, the largest $k$ for which there are integers $i$ and $j$ with $x_{i+1} x_{i+2} \ldots x_{i+k} = y_{j+1} y_{j+2} \ldots y_{j+k}$. Show how to do this, what is the time complexity of this?

Subproblem:
Let $L(i,j)$ = the longest similar suffix of $x_1x_2 \ldots x_i$ and $y_1y_2 \ldots y_j$.

Solution:
$\max\{L(i,j) \vert 1 \leq i \leq n, \ 1 \leq j \leq m\}$

Recursion:
Let $L(i,0) = L(0,j) = 0$ then
$$L(i,j) = \begin{cases} 0 & \mbox{if } x_i \not = y_j\\ 1 + L(i-1,j-1) & \mbox{otherwise}\end{cases}.$$
```python
from typing import List, Any


def common_longest_subsequence(
    first_sequence: List[Any], second_sequence: List[Any]
) -> int:
    # Set the (n+1, m+1) matrix to all 0's first.
    solutions = [
        [0] * (len(second_sequence) + 1) for _ in range(len(first_sequence) + 1)
    ]
    # This is used to track the max
    max_value = 0
    for first_index, first_value in enumerate(first_sequence):
        for second_index, second_value in enumerate(second_sequence):
            if first_value == second_value:
                solution = 1 + solutions[first_index][second_index]
                solutions[first_index + 1][second_index + 1] = solution
                max_value = max(max_value, solution)
    return max_value


if __name__ == "__main__":
    first_sequence = "BCDBABCDA"
    second_sequence = "ABECBAB"
    solution = common_longest_subsequence(first_sequence, second_sequence)
    print(
        f"The length of longest common substring of {first_sequence} "
        f"and {second_sequence} is {solution}."
    )
```

This algorithm takes $O(nm)$ time, first to set up the initial matrix and to fill the values.

>[!question] 6.17 Making change I
>Given an unlimited supply of coins of denominations $x_1, x_2, \ldots , x_n$, we wish to make change for a value $v$; that is, we wish to find a set of coins whose total value is $v$. This might not be possible: for instance, if the denominations are $5$ and $10$ then we can make change for $15$ but not for $12$. Give an $O(nv)$ dynamic-programming algorithm for the following problem. 
>
>Input: $x_1, \ldots , x_n; v$. 
>Question: Is it possible to make change for $v$ using coins of denominations $x_1, \ldots , x_n$?

Let $T(i)$ be true or false if we can make $i$ using the coins $x_i$. 

Base: Set $T(-i)$ = False for $1 \leq i \leq \max\{x_i \ \vert \ 1 \leq i \leq n\}$. With $T(0)$ = True.

Recursion: Set $T(j) = \bigvee_{i} T(j - x_i)$.

Solution: $T(v)$.

```python
def coin_problem(coins, amount):
    solutions = [0]
    for i in range(1, amount + 1):
        if any(i - coin in solutions for coin in coins):
            solutions.append(i)
    return amount in solutions


if __name__ == "__main__":
    print(coin_problem([5, 3], 8))
```

This takes $O(nv)$ time. 

>[!question] 6.18 Making change II
>Consider the following variation on the change-making problem (Exercise 6.17). Given coin denominations $x_1, x_2, \ldots , x_n$, we wish to make change for a value $v$ but you are only allowed to use each denomination *at most once*. For instance, if the denominations are 1, 5, 10, 20, then you can make change for 16 = 1 + 15 and for 31 = 1 + 10 + 20 but not for 40 (because you can’t use 20 twice).
>
>Input: $x_1, \ldots , x_n; v$. 
>Question: Is it possible to make change for $v$ using coins of denominations $x_1, \ldots , x_n$ only once?
>
>Show how to solve this problem in time O(nv).

Let $T(i,j)$ be a [[Boolean variable|boolean]] on weather you can make $0 \leq j \leq v$ using the first $0 \leq i \leq n$ coins.

Base: Set $T(i,0) =$ True for $0 \leq i \leq n$ and $T(0,j) =$ false for $1 \leq j \leq v$.

Recursion: Set 
$$T(i,j) = \begin{cases} T(i-1, j) & \mbox{if } j < x_i\\ T(i-1, j) \lor T(i-1, j-x_i) & \mbox{otherwise} \end{cases}$$

Solution: $T(n, v)$.

```python
from typing import List


class Change2Solver:
    _solution_array: List[List[int]]
    _coins: List[int]
    _number_of_coins: int
    _value: int

    def solve(self, coins: List[int], value: int) -> bool:
        self._setup_problem(coins, value)
        self._setup_solution_array()
        self._fill_array()
        return self._solution_array[-1][-1]

    def _setup_problem(self, coins: List[int], value: int) -> None:
        self._coins = coins
        self._number_of_coins = len(coins)
        self._value = value

    def _setup_solution_array(self) -> None:
        self._solution_array = [
            ([True] + [False for _ in range(self._value)])
            for _ in range(self._number_of_coins + 1)
        ]

    def _fill_array(self) -> None:
        for coin_index in range(self._number_of_coins):
            for sub_value in range(1, self._value + 1):
                self._solution_array[coin_index + 1][
                    sub_value
                ] = self._solve_for_single_value(coin_index, sub_value)

    def _solve_for_single_value(self, coin_index: int, sub_value: int) -> bool:
        current_coin = self._coins[coin_index]
        lower_solution = self._solution_array[coin_index][sub_value]
        if current_coin > sub_value:
            return lower_solution
        else:
            return any(
                [
                    lower_solution,
                    self._solution_array[coin_index][sub_value - current_coin],
                ]
            )


if __name__ == "__main__":
    solver = Change2Solver()
    assert solver.solve([1, 5, 10], 16)
    assert solver.solve([1, 5, 10], 11)
    assert not solver.solve([1, 5, 10], 12)
```

The function `_setup_problem` takes $O(1)$. Though `_setup_solution_array` takes $O(nv)$.

As `_solve_for_single_value` just checks two values it is $O(1)$ with `_fill_array` running this function $nv$ times, making that $O(nv)$.

This gives the overall run time to be $O(1) + O(nv) + O(nv) = O(nv)$.

>[!question] 6.19 Making change III
>Consider the following variation on the change-making problem (Exercise 6.17). Given coin denominations $x_1, x_2, \ldots , x_n$, we wish to make change for a value $v$ but you can only use a *at most $k$ coins* (with repeats). For instance, if the denominations are $5$, $10$ with $k=6$ then you can make change for 55 with $5 \times 10 + 1 \times 5$ but not $65$.
>
>Input: $x_1, \ldots , x_n; k; v$. 
>Question: Is it possible to make change for $v$ using at most $k$ coins of denominations $x_1, \ldots , x_n$?

Let $T(i,j)$ be a [[Boolean variable|boolean]] on weather you can make $0 \leq j \leq v$ using $0 \leq i \leq k$ coins.

Base: Set $T(i,0) =$ True for $0 \leq i \leq n$ and $T(0,j) =$ False for $1 \leq j \leq v$.

Recursion: Set 
$$T(i,j) = T(i, j-1) \lor \bigvee_{\substack{\rho \in \{1,2, \ldots, n\}\\x_{\rho} \geq i}} T(i - x_{\rho}, j-1)$$

Solution: $T(v, k)$.

```python
from typing import List


class Change3Solver:
    _solution_array: List[List[int]]
    _coins: List[int]
    _number_of_coins: int
    _value: int
    _coin_limit: int

    def solve(self, coins: List[int], coin_limit: int, value: int) -> bool:
        self._setup_problem(coins, coin_limit, value)
        self._setup_solution_array()
        self._fill_array()
        return self._solution_array[-1][-1]

    def _setup_problem(self, coins: List[int], coin_limit: int, value: int):
        self._coins = coins
        self._number_of_coins = len(coins)
        self._coin_limit = coin_limit
        self._value = value

    def _setup_solution_array(self):
        self._solution_array = [
            ([True] + [False for _ in range(self._value)])
            for _ in range(self._coin_limit + 1)
        ]

    def _fill_array(self) -> None:
        for sub_coin_limit in range(1, self._coin_limit + 1):
            for sub_value in range(1, self._value + 1):
                self._solution_array[sub_coin_limit][
                    sub_value
                ] = self._solve_for_single_value(sub_coin_limit, sub_value)

    def _solve_for_single_value(
	    self, 
	    sub_coin_limit: int, 
	    sub_value: int
	) -> bool:
        previous_solutions = self._solution_array[sub_coin_limit - 1]

        if previous_solutions[sub_value]:
            return True

        return any(
            [
                previous_solutions[sub_value - current_coin]
                for current_coin in self._coins
                if current_coin <= sub_value
            ]
        )


if __name__ == "__main__":
    solver = Change3Solver()
    assert solver.solve([5, 10], 6, 55)
    assert not solver.solve([1, 5, 10], 6, 65)
```

The function `_setup_problem` takes $O(1)$. Though `_setup_solution_array` takes $O(nk)$.

As `_solve_for_single_value` just checks at most $n$ values it is $O(n)$ with `_fill_array` running this function $nk$ times, making that $O(nvk)$.

This gives the overall run time to be $O(1) + O(nk) + O(nvk) = O(nvk)$.

>[!question] 6.20 Optimal BST
>Suppose you are given a list of words $w_1, w_2, \ldots, w_n$ and their frequencies $f_1, f_2, \ldots f_n$. We want to design a [[Binary search tree|binary search tree]] such that at any node with word $w$ on the tree all child nodes to the left of the node have words that are alphabetically lower than $w$ whereas all child nodes to the right of the node have words that are alphabetically greater than it. We want to design such a tree where the average access time with respect to $f_i$ is minimised. i.e. if word $w_i$ has depth $d_i$ we want to minimise
>$$ \sum_{i = 1}^k d_i*f_i.$$
>Write a dynamic program that solves this problem efficiently with the following:
>
>Input: words $w_1, \ldots, w_n$ (in sorted order); frequencies $f_1, \ldots, f_n$.
>Output: The binary search tree of lowest cost.  (Not just the cost!)  

Let $C(i,j)$ with $1 \leq i \leq j \leq n$ be the minimum cost of a binary search tree on $x_{i+1} x_{i} \ldots x_j$.

The solution to the problem will be $C(0,n)$.

The base case will be $C(i,i) = f_i$.

The [[Recursion|recursion]] step will be
$$ C(i,j) = \min\{C(i+1, j), \ C(i, j-1), \ C(i,k-1) + C(k+1,j) \ \vert \ i < k < j\} + \sum_{k = 1}^j f_k.$$
To calculate $C(i,j)$ we need to [[Iterative algorithms|iteratively]] increase the difference between $j - i$, the base case is $0$ the last case will be $n-1$.

```python
from __future__ import annotations
from typing import List, Optional
from dataclasses import dataclass


class UpperDiagonalMatrix:
    _matrix_size: int
    _matrix_values: List

    def __init__(self, matrix_size: int):
        self._matrix_size = matrix_size
        self._matrix_values = [0] * int((matrix_size * (matrix_size + 1)) / 2)

    def get(self, row: int, column: int) -> int:
        self._check_row_column(row, column)
        return self._matrix_values[self._get_index(row, column)]

    def set(self, row: int, column: int, value: int) -> None:
        self._check_row_column(row, column)
        self._matrix_values[self._get_index(row, column)] = value

    def _get_index(self, row: int, column: int) -> int:
        return self._get_column_offset(column) + (row - 1)

    def _get_column_offset(self, column: int) -> int:
        return int((column * (column - 1)) / 2)

    def _check_row_column(self, row: int, column: int) -> None:
        if row > column:
            raise ValueError("Row must be less than or equal to column")
        if row < 1:
            raise ValueError("Row must be greater than or equal to 0")
        if column > self._matrix_size:
            raise ValueError("Column must be less than matrix size")


@dataclass
class WordWithFrequency:
    word: str
    frequency: float


class ChainMultiplySolver:
    _solution_array: UpperDiagonalMatrix
    _words: List[str]
    _frequencies: List[float]
    _number_of_words: int

    def solve(self, words: List[WordWithFrequency]) -> Node:
        self._setup_problem(words)
        self._fill_matrix_diagonally()
        return self._solution_array.get(1, self._number_of_words)

    def _setup_problem(self, words: List[WordWithFrequency]) -> None:
        self._words = words
        self._number_of_words = len(words)
        self._solution_array = UpperDiagonalMatrix(self._number_of_words)
        for i in range(self._number_of_words):
            self._solution_array.set(i + 1, i + 1, self._words[i].frequency)

    def _fill_matrix_diagonally(self) -> None:
        for difference in range(1, self._number_of_words):
            for lower_index in range(1, self._number_of_words - difference + 1):
                upper_index = lower_index + difference
                self._solution_array.set(
                    lower_index,
                    upper_index,
                    self._solve_for_single_value(lower_index, upper_index),
                )

    def _solve_for_single_value(self, lower_index: int, upper_index: int) -> float:
        return self._get_sum_of_frequencies(
            lower_index, upper_index
        ) + self._get_minimum_cost_of_sub_binary_forest(lower_index, upper_index)

    def _get_sum_of_frequencies(self, lower_index: int, upper_index: int) -> float:
        return sum(
            [word.frequency for word in self._words[lower_index - 1 : upper_index]]
        )

    def _get_minimum_cost_of_sub_binary_forest(
        self, lower_index: int, upper_index: int
    ) -> float:
        return min(
            [
                self._solution_array.get(lower_index + 1, upper_index),
                self._solution_array.get(lower_index, upper_index - 1),
            ]
            + [
                self._solution_array.get(lower_index, split_index - 1)
                + self._solution_array.get(split_index + 1, upper_index)
                for split_index in range(lower_index + 1, upper_index)
            ]
        )


if __name__ == "__main__":
    words = [
        WordWithFrequency("a", 0.25),
        WordWithFrequency("b", 0.5),
        WordWithFrequency("b", 0.25),
    ]
    solver = ChainMultiplySolver()
    print(solver.solve(words))
```

> [!Note] This will solve for the cost
> To get back the tree we will make $C(i,j)$ a tuple with the second coordinate being the break point. 

The run time of this algorithm is $O(n^3)$.

>[!question] 6.7 Palindrome subsequence
>Given a sequence $a_1, a_2, \ldots, a_n$ devise an algorithm that returns the length of the longest [[Palindrome|palindromic]] [[Subsequence|subsequence]]. Its running time should be $O(n^2)$.

Algorithm:

Define an array $A(i,j)$ which will be the longest Palindromic subsequence in $a_i, a_{i+1}, \ldots, a_{j}$.

Base case: $A(i,i) = 1$ and
$$A(i,i+1) = \begin{cases} 2 & \mbox{if } a_i = a_{i+1}\\ 1 & \mbox{otherwise}\end{cases}.$$

Iterative step: Recursively calculate $A(i,j)$ by increasing $j-i$. Set
$$A(i,j) = \begin{cases} 2 + A(i+1, j-1) & \mbox{if } a_i = a_j\\ \max\{A(i+1,j), A(i,j-1)\} & \mbox{otherwise}\end{cases}.$$

>[!question] 6.7 Palindrome *substring* (altered)
>Given a sequence $a_1, a_2, \ldots, a_n$ devise an algorithm that returns the length of the longest [[Palindrome|palindromic]] [[Substring|substring]]. Its running time should be $O(n)$.

Manacher's algorithm .. big brain shit.

>[!question] 4.21 Currency exchange
>Shortest path algorithms can be applied in currency trading. Let $c_1, c_2, \ldots , c_n$ be various currencies; for instance, $c_1$ might be dollars, $c_2$ pounds, and $c_3$ lire. For any two currencies $c_i$ and $c_j$ , there is an exchange rate $r_{i,j}$ ; this means that you can purchase $r_{i,j}$ units of currency $c_j$ in exchange for one unit of $c_i$. These exchange rates satisfy the condition that $r_{i,j} \cdot r_{j,i} < 1$, so that if you start with a unit of currency $c_i$, change it into currency $c_j$ and then convert back to currency $c_i$, you end up with less than one unit of currency $c_i$ (the difference is the cost of the transaction). 
>
>(a) Give an efficient algorithm for the following problem: Given a set of exchange rates $r_{i,j}$, and two currencies $s$ and $t$, find the most advantageous sequence of currency exchanges for converting currency $s$ into currency $t$. Toward this goal, you should represent the currencies and rates by a graph whose edge lengths are real numbers. 
>
>The exchange rates are updated frequently, reflecting the demand and supply of the various currencies. Occasionally the exchange rates satisfy the following property: there is a sequence of currencies $c_{i_1} , c_{i_2} , \ldots , c_{i_k}$ such that $r_{i_1,i_2} \cdot r_{i_2,i_3} \ldots r_{i_{k−1},i_k} \cdot r_{i_k,i_1} > 1$. This means that by starting with a unit of currency $c_{i_1}$ and then successively converting it to currencies $c_{i_2} , c_{i_3} , \ldots , c_{i_k}$ , and finally back to $c_{i_1}$ , you would end up with more than one unit of currency $c_{i_1}$. Such anomalies last only a fraction of a minute on the currency exchange, but they provide an opportunity for risk-free profits. 
>
>(b) Give an efficient algorithm for detecting the presence of such an anomaly. Use the graph representation you found above.

Duplicate in [[Week 3 - Homework 2 (unassessed)]]

## Dynamic Programming (Chapter 6) - filtered

> [!question] 6.5 Pebbling a checkerboard.
> We are given a checkerboard which has $4$ rows and $n$ columns, and has an integer written in each square. We are also given a set of $2n$ pebbles, and we want to place some or all of these on the checkerboard (each pebble can be placed on exactly one square) so as to maximize the sum of the integers in the squares that are covered by pebbles. There is one constraint: for a placement of pebbles to be legal, no two of them can be on horizontally or vertically adjacent squares (diagonal adjacency is fine). 
> 
> (a) Determine the number of legal patterns that can occur in any column (in isolation, ignoring the pebbles in adjacent columns) and describe these patterns. 
> 
> Call two patterns compatible if they can be placed on adjacent columns to form a legal placement. Let us consider subproblems consisting of the first $k$ columns $1 \leq k \leq n$. Each subproblem can be assigned a type, which is the pattern occurring in the last column. 
> 
> (b) Using the notions of compatibility and type, give an $O(n)$-time dynamic programming algorithm for computing an optimal placement.

a) There are 7 legal positions of pebbles. We represent the positions by the row numbers with a pebble, they are $P = \{p_{\emptyset}, p_{0}, p_{1}, p_2, p_3, p_{0,2}, p_{1,3}\}$. Then the legal following positions given the column to the right are

$$P_p = \begin{cases} P & \mbox{if } p = p_{\emptyset}\\ P \backslash \{p_i, p_{i, i\pm2}\} & \mbox{if } p = p_i\\ P \backslash\{p_{i,j}, p_i, p_j\} & \mbox{if } p = p_{i,j}\end{cases}.$$
b) Suppose we have a weight function $\hat{W}: [1, \ldots, n] \times [1,2,3,4] \rightarrow \mathbb{Z}$ which describes the weights, with $w(i,j)$ being the number on the $(i,j)$ checkerboard. Define a function $W: [1, \ldots, n] \times P \rightarrow \mathbb{Z}$ where $W(i,p_S) = \sum_{j \in S} \hat{W}(j)$.

Define $T(i,p)$ with $i \in [1, \ldots, n]$ and $p \in P$ to be a maximum value in the checkerboard using the first $i$ columns with position $p$ in the $i$'th column.

Base case: Set $T(1,p) = W(1,p)$.

Recursion: Set $T(i,p) = \max_{q \in P_p}\{T(i-1,q)\} + W(i,p)$ for $1 < i \leq n$ and $p \in P$.

Solution: $\max_{p \in P} \{T(n,p)\}$  

## Correctness

Prove by induction. 

If $i =1$ then $T(1,p)$ as it has to use $p$ in the first column and that is the only column it is $W(1,p)$.

Suppose it is true for $k-1$ lets prove for $k$.

As $T(k,p)$ must use $p$ in the $k$'th column the solution is going to be $W(k,p)$ with a solution to the $k-1$'th problem.

The only valid possibilities for the $k-1$'th column are $P_p$ therefore it must use a maximal solution to $k-1$'th problem with one of the $q \in P_p$ in that column. These are exactly $T(i-1,q)$ by the induction hypothesis. 

So
$$T(k,p) = \max_{q \in P_p}\{T(i-1,q)\} + W(i,p)$$
giving the correctness of our solution at the $k$'th column.

By induction $T(i,p)$ is correct for all columns.

The correct solution to the problem must use one of $p \in P$ for the $n$'th column. Which would mean it would be a maximal solution for the $k$'th problem.

Therefore this is one of $T(n,p)$ by the correctness of $T$ giving our algorithm is correct on the whole problem.

## Pseudocode

```pseudocode
Checkerboard solver
Input: Function W: [1..n] x [1..4] -> Z.
Output: The maximum value putting the stones on the board.
	Define P to be the set of valid position
	Define P_p to be the set of compatible positions for an adjacent column 
		when it is next to a column with p in P in it.
	Set up T as a map from [1..n], P into Z.
	Set T[1,p] = sum_(i in p) W(1,i)
	for i = 2 -> n
		for p in P
			T[i, p] = sum_(j in p) W(i,j) + max_q in P_p T[i-1,q]
	return max_p in P T[n,p]
```

Lets analyse the run time of this algorithm.

Making the sets $P$ and $P_p$ take $O(1)$ time as they are the same for every run.

Defining $T[1,p]$ for each $p$ takes at most 2 looks ups and this is carried out $7$ times so takes $O(1)$ time.

We loop over $i$ being $2$ to $n$ which is $n-1$ steps. We loop over $p \in P$ which is 7 steps. We calculate the sum of elements in $p$ which takes at most 2 loops ups. Then we calculate the max over $P_p$ which takes at most $7$ look ups.

In total this loop is at most $(n-1) \cdot 7 \cdot (2 + 7)$ look ups which is $O(n)$.

Returning the solution involves $7$ look ups which is $O(1)$.

The run time of this algorithm is $O(1) + O(1) + O(n) + O(1) = O(n)$.

> [!question] 6.6 Multiplication operation
> Let us define a multiplication operation on three symbols $a, b, c$ according to the following table; thus $ab = b,\ ba = c$, and so on. Notice that the multiplication operation defined by the table is neither associative nor commutative.
> $$\begin{array}{c|ccc} \cdot & a & b & c\\\hline a & b & b & a\\ b & c & b & a\\ c & a & c & c \end{array}$$
> Find an efficient algorithm that examines a string of these symbols, say $bbbbac$, and decides whether or not it is possible to parenthesize the string in such a way that the value of the resulting expression is $a$. For example, on input $bbbbac$ your algorithm should return yes because $((b(bb))(ba))c = a$.

Take input a sequence $a_i$ for $1 \leq i \leq n$ of symbols. 

## Algorithm

Let $T(i,j,s)$ record if it is possible with sequence $a_i, a_{i+1}, \ldots, a_j$ it is possible to make $s$.

Define the an upper diagonal table $T(i,j,s)$ where $1 \leq i \leq j \leq n$ and $s \in S :=\{a,b,c\}$ which has values $True$ and $False$. Let the table start with all values being $False$. 

Let $T(i,i,a_i)$ be True.

Iteratively fill $T(i,j,s)$ based on the difference between $i,j$ starting with $j - i = 1$.

For some $k$ such that $i \leq k < j$  let 
$$S_{Left} = \{s \in S \vert T(i,k,s)\} \mbox{ and } S_{Right} = \{s \in S \vert T(k+1,j,s)\}.$$
Then set $T(i,j,s_{left} \cdot s_{right})$ True for all $s_{left} \in S_{Left}$ and $s_{right} \in S_{Right}$. 

Return $T(1,n,a)$. 

## Correctness

We prove $T(i,j,s)$ is correct by induction on $j-i$. 

Note that as $T(i,i,s)$ records if $a_i$ can be bracketed to make $s$ the only correct solution is $a_i$.

Suppose $T(i,j,s)$ is correct for all $j-i < k$. 

Suppose we pick $i < j$ such that $j-i = k$. 

Note that if $T(i',j',s)$ is correct when $j'-i' < k$. Then $T(i,j,s)$ can never be True when there is no bracketing of $a_i, \ldots a_j$ that equals $s$ as by definition it can only be true when $T(i,k,s_{left})$ and $T(k+1,j,s_{right})$ are true and $s = s_{left} \cdot s_{right}$.

Similarly if there is some bracketing of $a_i, \ldots, a_j$ such that it equals $s$ there must be some outer bracket that partitions $a_i, \ldots, a_k$ and $a_{k+1}, \ldots, a_j$ such that the bracketing on the left equals $s_{left}$ and the right $s_{right}$ with $s_{left} \cdot s_{right} = s$ with $i \leq k < j$. Therefore as $T(i,k,s_{right})$ is all correct and $T(k+1,j,s_{left})$ is all correct we have these must be $True$ and so $T(i,j,s)$ is True.

This shows by induction each $T(i,j,s)$ is correct.

The final solution is correct as $a$ would have to be some bracketing of $a_1, \ldots a_n$ to make $a$ which is exactly $T(1,n,a)$.

## Running time

Making the table initially takes $O(n^2)$ time as there are $3 \cdot n(n+1)/2$ entries to fill.

Filling the bottom row takes $O(n)$ time as there are $n$ entries to fill one for each $a_i$.

Filling entries $T(i,j,s)$ for all $s \in S$ takes $(j-i) \cdot 3^2 \cdot 2$ checks for each $i \leq k < j$ you need to check each pair of elements and compute the multiplication. This is $O(n)$.

There are $O(n^2)$ entries in the table as explained in the first step.

Therefore filling the table takes $O(n^2)O(n)$ steps making it $O(n^3)$.

Returning the value is a single look up so is $O(1)$.

Thus making the algorithmic look up time $O(n^2) + O(n) + O(n^3) + O(1) = O(n^3)$.

## UNSOLVED PROBLEMS

6.7, 6.9, 6.22 (hint included in the problem).

**6.25-6.30** Note: These are a bit harder, but definitely nice problems.