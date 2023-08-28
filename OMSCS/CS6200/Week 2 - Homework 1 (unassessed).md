---
aliases: []
type: exercise
publish: false
created: 2023-08-28
last_edited: 2023-08-28
tags: OMSCS
course: [[CS6200 Introduction to Graduate Algorithms]]
week: 2
chatgpt: false
---
# Week 2 - Homework 1 (unassessed)

> [!question] 6.4 String of words
> You are given a string of $n$ characters $s[1 \ldots n]$, which you believe to be a corrupted text document in which all punctuation has vanished (so that it looks something like “itwasthebestoftimes...”). You wish to reconstruct the document using a dictionary, which is available in the form of a Boolean function $dict( \cdot )$ for any string $w$,
> $$dict(w) = \begin{cases} true & \mbox{if w is a valid word}\\ false & \mbox{otherwise}\end{cases}.$$ 
> 1. Give a dynamic programming algorithm that determines whether the string $s[\cdot]$ can be reconstituted as a sequence of valid words. The running time should be at most $O(n^2)$, assuming calls to $dict$ take unit time.
> 2. In the event that the string is valid, make your algorithm output the corresponding sequence of words.

Question 1)

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

Question 2)

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

Let $T(i)$ be the set of coin permutations that make up $i$ (potentially empty). 