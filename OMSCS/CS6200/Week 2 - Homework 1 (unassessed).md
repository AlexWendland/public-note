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

Recursion: Set $T(j) = \bigvee_{i} T(j - i)$.

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

...

>[!question] 6.7 Palindrome *substring* (altered)
>Given a sequence $a_1, a_2, \ldots, a_n$ devise an algorithm that returns the length of the longest [[Palindrome|palindromic]] [[Substring|substring]]. Its running time should be $O(n)$.

Let $L(i,j)$ be true if $a_i \ldots a_j$ is a palindrome.

Base case: Set $L(0) = 0$.

[[Recursion]] step: Let

>[!question] 4.21 Currency exchange
>Shortest path algorithms can be applied in currency trading. Let $c_1, c_2, \ldots , c_n$ be various currencies; for instance, $c_1$ might be dollars, $c_2$ pounds, and $c_3$ lire. For any two currencies $c_i$ and $c_j$ , there is an exchange rate $r_{i,j}$ ; this means that you can purchase $r_{i,j}$ units of currency $c_j$ in exchange for one unit of $c_i$. These exchange rates satisfy the condition that $r_{i,j} \cdot r_{j,i} < 1$, so that if you start with a unit of currency $c_i$, change it into currency $c_j$ and then convert back to currency $c_i$, you end up with less than one unit of currency $c_i$ (the difference is the cost of the transaction). 
>
>(a) Give an efficient algorithm for the following problem: Given a set of exchange rates $r_{i,j}$, and two currencies $s$ and $t$, find the most advantageous sequence of currency exchanges for converting currency $s$ into currency $t$. Toward this goal, you should represent the currencies and rates by a graph whose edge lengths are real numbers. 
>
>The exchange rates are updated frequently, reflecting the demand and supply of the various currencies. Occasionally the exchange rates satisfy the following property: there is a sequence of currencies $c_{i_1} , c_{i_2} , \ldots , c_{i_k}$ such that $r_{i_1,i_2} \cdot r_{i_2,i_3} \ldots r_{i_{k−1},i_k} \cdot r_{i_k,i_1} > 1$. This means that by starting with a unit of currency $c_{i_1}$ and then successively converting it to currencies $c_{i_2} , c_{i_3} , \ldots , c_{i_k}$ , and finally back to $c_{i_1}$ , you would end up with more than one unit of currency $c_{i_1}$. Such anomalies last only a fraction of a minute on the currency exchange, but they provide an opportunity for risk-free profits. 
>
>(b) Give an efficient algorithm for detecting the presence of such an anomaly. Use the graph representation you found above.

Dynamic Programming (Chapter 6)

**6.1-6.3, 6.5** (these problems should be accesible, start here!)

**6.6** (this problem is like the Matrix Multiplication! A Y/N table should do it, but it may help to add a third dimension accounting for the symbol you wish to reduce to).

**6.7, 6.9, 6.11, 6.17** (the first making change problem)**, 6.22** (hint included in the problem).

**6.25-6.30** Note: These are a bit harder, but definitely nice problems.