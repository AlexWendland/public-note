---
aliases: null
checked: false
course: '[[CS6200 Introduction to Graduate Algorithms]]'
created: 2023-10-10
last_edited: 2023-11-11
publish: false
tags:
  - OMSCS
type: exercise
week: 8
---
# Week 8 - Quiz 5

>[!question] Question 1
>What is $2^{345}$ mod 31?

Note $2^5 = 32 = 1$ (mod $31$) so $2^{345} = 1$ (mod 31).

>[!question] Question 2
>A new Computer Science algorithms course takes 32 weeks to complete. The CS
teacher offers to assign you just one second of homework the first week of
school, two seconds the second week, four seconds the third, and so on.
 >
>How long would the homework take for the last week of school?
>
> Provide your answer in seconds mod 11.

For week $i$ the length of the homework is $2^{i-1}$ so the length of homework is $2^{31}$ seconds in the 32nd week of the course. So we are left to compute
$$2^{31} \ (mod \ 11)$$ Which as $11$ is prime by [[Fermat's little theorem]] we have $2^{10} = 1$ (mod $11$) giving
$$ 2^{31} = 2 \ (mod \ 11).$$
>[!question] Question 3
>What is the value $3^{2003}$ mod $5$?

By [[Fermat's little theorem]] as $5$ is prime we have $3^4 = 1$ mod $5$. So
$$ 3^{2003} = 3^3 = 3^{-1} = 2 \ (mod \ 5).$$
>[!question] Question 4
>What is $13^{-1}$ mod $22$?

We run the [[Extended Euclidean algorithm|extended Euclidean algorithm]] on 13 and 22.

| x   | y   | c   | a   | b   |
| --- | --- | --- | --- | --- |
| 22  | 13  | 1   | 3   | -5    |
| 13  | 9   | 1   | -2  | 3   |
| 9   | 4   | 2   | 1   | -2  |
| 4   | 1   | 4   | 0   | 1   |
| 1   | 0   | -   | 1   | 0   |

So the inverse to $13^{-1} = -5 = 17$ mod $22$.

>[!question] Question 5
>What is the value of $(2^{20} + 4^{40} + 5^{50} + 6^{60})$ mod $7$?

As $6 = -1$ mod $7$ and $5 = -2$ mod $7$ we have
$$ (2^{20} + 4^{40} + 5^{50} + 6^{60}) = (2^{20} + 2^{80} + 2^{50} + 1) \ mod \ 7$$
From [[Fermat's little theorem]] we have $2^6 = 4^6 = 1$ mod $7$ so
$$(2^{20} + 2^{80} + 2^{50} + 1) = (2^{2} + 2^{2} + 2^{2} + 1) = 4 + 4 + 4 + 1 = 13 = 6 \ mod \ 7$$
>[!question] Question 6
>How many numbers in the range $1, \ldots, 143$ are relatively prime with $143$?

As $143 = 11 \times 13$ we have $10 \times 12 = 120$ relatively prime numbers between $1$ and $143$.

>[!question] Question 7
>A red ribbon spool has 22,608 inches of ribbon and a blue ribbon spool has 10,206  inches of ribbon. The ribbons on both spools are to be evenly divided (with no  leftover) into pieces of the same length so that the pieces are as long as possible.  What is the length of each piece? (Provide an integer value without any units)

So find the length of the ribbons we need to calculate the [[Greatest common divisor|greatest common divisor]] using the [[Euclidean algorithm]].

| x     | y     | c   |
| ----- | ----- | --- |
| 22608 | 10206 | 2   |
| 10206 | 2196  | 4   |
| 2196  | 1422  | 1   |
| 1422  | 774   | 1   |
| 774   | 648   | 1   |
| 648   | 126   | 5   |
| 126   | 18    | 7   |
| 18    | 0     | 0   |

Therefore the length of ribbon is 18.

>[!question] Question 8
>Your younger brother posts his RSA public key ($N = 133, e = 7$). You decide to show him that he needs to pick a stronger key. Find your brother’s private key (the value of d). (Provide an integer value)

We have $133 = 7 \times 19$ so we need to find the inverse of $7$ in $6 \times 18 = 108$

| x   | y   | c   | a   | b   |
| --- | --- | --- | --- | --- |
| 108 | 7   | 15  | -2  | 31  |
| 7   | 3   | 2   | 1   | -2  |
| 3   | 1   | 3   | 0   | 1   |
| 1   | 0   | 4   | 1   | 0   |

So $7^{-1} = 31$ mod $108$.

>[!question] Question 9
>Using your brother’s RSA Public Key (N=133,e=7), one of his friends sends him the  encrypted message “5� (the number 5 is the complete message). Decrypt the message to your brother. (Provide an integer value)

This will be $5^{31}$ mod $133$

$$ 5^{31} = 5 \times (25)^{15} = 5 \times 25 \times (93)^7 = -8 \times 93 \times 4^3 = -8 \times 93 \times 64 = 131 \ (mod \ 133).$$
So his message was 131.

>[!question] Question 10
>Using p = 3, q = 11, d = 7 and e = 3 in the RSA algorithm, provide the result of encrypting the number 5. (Provide an integer value)

The public key would be $(33, 3)$ so to encode the message $5$ we look at $5^3$ mod $33$.
$$ 5^3 = 125 = 26 \ (mod \ 33).$$
So the encrypted value is 26.
