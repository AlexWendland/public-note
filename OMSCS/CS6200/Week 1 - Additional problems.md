---
aliases: []
type: exercises
publish: false
created: 2023-08-27
last_edited: 2023-08-27
tags: OMSCS
course: [[CS6200 Introduction to Graduate Algorithms]]
week: int
chatgpt: false
---
# Substring with max sum

>[!question] 6.1 Contiguous Subsequence
>A contiguous subsequence of a list $S$ is a subsequence made up of consecutive elements of $S$. 
>
>For instance, if $S$ is 
>$$5, 15, −30, 10, −5, 40, 10,$$ 
>then 15, −30, 10 is a contiguous subsequence but 5, 15, 40 is not. Give a linear-time algorithm for the following task: 
>
>Input: A list of numbers, $a_1, a_2, \ldots , a_n$. 
>
>Output: The contiguous subsequence of maximum sum (a subsequence of length zero has sum zero). 
>
>For the preceding example, the answer would be 10, −5, 40, 10, with a sum of 55.
>
>(Hint: For each $j \in \{1, 2, \ldots , n\}$, consider contiguous subsequences ending exactly at position $j$.)

Subproblem:
Let $L(i)$ = the largest positive contiguous subsequence end with $a_i$ (if non-empty).

Solution: 
The max of $L(i)$.

Recursion:
$L(i) = \max\{0, L(i-1) + a_i\}$
where $L(0) = 0$.

This runs in $O(n)$ time.

>[!question] 6.2 hotel stops
>You are going on a long trip. You start on the road at mile post 0. Along the way there are $n$ hotels, at mile posts $a_1 < a_2 < \ldots < a_n$, where each $a_i$ is measured from the starting point. The only places you are allowed to stop are at these hotels, but you can choose which of the hotels you stop at. You must stop at the final hotel (at distance $a_n$), which is your destination. 
>
>You’d ideally like to travel 200 miles a day, but this may not be possible (depending on the spacing of the hotels). If you travel $x$ miles during a day, the penalty for that day is $(200 − x)^2$. You want to plan your trip so as to minimize the total penalty —that is, the sum, over all travel days, of the daily penalties. 
>
>Give an efficient algorithm that determines the optimal sequence of hotels at which to stop.

Subproblem:
Let $L(i)$ = minimum penalty stopping at hotel $a_i$.

Solution: 
$L(n)$.

Recursion:
$L(k) = \min \{ L(i) + (200 - (a_k-a_i))^2 \vert 1 \leq i \leq k \}$

This runs in $O(n^2)$ time.

