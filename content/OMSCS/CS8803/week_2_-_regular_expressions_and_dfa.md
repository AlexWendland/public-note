---
aliases:
course_code: CS8803 O08
course_name: Compilers - Theory and Practice
created: '2026-01-16'
date_checked: '2026-01-28'
draft: false
last_edited: 2026-01-28
tags:
  - OMSCS
title: Week 2 - Regular expressions and DFA
type: lecture
week: 2
---

In the lexical analysis phase of the compiler we need to convert a sequence of characters into tokens.
First, let's define formally what a token is.

> [!definition] Token
> A token is a tuple consisting of:
> - A type, such as `VAR`, `FloatConst`, etc. This is defined by the language.
>
> - A value associated to that type, e.g. the name of the variable, or the value of a constant.

Some examples of tokens are:

- A float: (FloatConst, 123.45)

- A variable: (VAR, string = DaysOfWeek)

- An operator: (Operator, +)

This lesson will focus on the conversion from strings to tokens.

# Regular expressions

A regular expression describes a string pattern to match against.
A regular expression matches (or accepts) a set of strings that satisfy the pattern.
To do this, first we start with an alphabet $\Sigma$.
This can be any set of characters, for example lowercase English letters.

- *Alphabet* - A set of valid symbols $\Sigma$.

- *Symbol* - A valid character $s$ in the alphabet $s \in \Sigma$.

Within a regular expression, we not only have symbols in our alphabet but also `meta-characters/meta-symbols` which relate to the regular expression itself.
These are special characters that allow us to express a pattern.
For example, `|` means or (`a | b` is a or b), `()` allow grouping, `*`/`+` allow repetition.

To distinguish between symbols and meta-symbols we escape them with a `\`.
For example if $\vert \in \Sigma$ to represent `|` as a symbol we will use `\|`.

- *Meta-symbol* - A symbol that is used to express a pattern.

- *Escape* - To express a symbol that is also a meta-symbol we use the escape character `\`.

- *Empty string* - There is a special character $\epsilon$ that matches the empty string.

> [!warning] Non-standard definition
> In this course we use Unix regex but there are many varieties that all have slightly different syntax.
> Whilst the core of regex is the same, some meta-symbols may vary between implementations.

## Regular operators

The key operators to understand in regular expressions are the following:

### Concatenation

In regular expressions, symbols following one another is concatenation.
Therefore `abc` is `a` followed by `b` followed by `c`.

### Alternation

An alternation allows us to offer options for what could come next.
There are two major ways to do this.

- *Pipe* - The pipe operator can be used to form an alternation.
For example `a | b` is `a` or `b`.

- *Character classes* - Square brackets `[]` allow to specify a set of characters to match.
For example `[ab]` is `a` or `b`.

- *Ranges* - Whilst still a character class, a range allows for characters between the matches.
For example `[a-z]` is any lowercase letter, or `[0-9]` is any digit.

- *Negation* - The negation operator allows us to negate a character class.
For example `[^a]` is any symbol in our alphabet that is not `a`.

- *Any* - We use `.` to denote any symbol in our alphabet.

### Repetition

Repetition characters operate on the previous symbol or grouped expression.
They allow for some number of the previous symbol to be repeated.
For example, `a*` repeats `a`, while `(ab)*` repeats the entire sequence `ab`.

- *Zero or more* - The asterisk `*` denotes zero or more repetitions.

- *One or more* - The plus sign `+` denotes one or more repetitions.

- *Zero or one* - The question mark `?` denotes zero or one repetitions.

### Precedence

When reading a regular expression we need precedence rules to determine which operator is applied first.

- *Brackets* - Brackets `()` have the highest precedence.

- *Repetition* - Repetition operators have the next highest precedence.

- *Concatenation* - Concatenation operators have the next highest precedence.

- *Alternation* - Alternation operators have the lowest precedence.

Therefore `a | b*` is `a`, $\epsilon$, `b`, `bb`, ... as the repetition gets applied before the alternation.
Whereas `(a | b)*` is $\epsilon$, `a`, `b`, `aa`, `ab`, `ba`, ... as the brackets apply the alternation first.

### Special symbols

There are some special symbols that help with structuring the expression.

- *Beginning of line* - The caret `^` denotes the beginning of the string.

- *End of line* - The dollar sign `$` denotes the end of the string.

## Examples

Below are simple but common examples.

> [!example] Signed integers
> `[+-]?[1-9][0-9]*|0`
>
> Matches integers like `+123`, `-456`, `0` (but not leading zeros like `007`).

> [!example] Floats
> `[+-]?[0-9]+(\.[0-9]+)?([eE][+-]?[0-9]+)?`
>
> Matches floating point numbers like `3.14`, `-2.5e10`, `+0.5E-3`.

# Deterministic Finite Automata (DFA)

We define a DFA as follows:

> [!definition] Deterministic Finite Automata
> A deterministic finite automaton (DFA) is defined by the following:
> - A finite set of states $Q$.
> - A finite set of input symbols $\Sigma$.
> - A transition function $\delta: Q \times \Sigma \rightarrow Q$.
> - A start state $q_0 \in Q$.
> - A set of accepting states $A \subseteq Q$.

A DFA defines what a regular language is.

> [!definition] Regular language
> A language $L$ is regular if DFA recognises it.

This DFA will have symbols $\Sigma$, with a map from $p: W_{\Sigma} \rightarrow Q$ from the words in $\Sigma$ to the states of the automaton, which defines $\delta$.
The start state $q_0 = p(\epsilon)$ and the accepting states will be the allowed words in this language.

> [!example] Words ending in `1`
> Suppose $\Sigma = \{0, 1\}$.
> Then let our language be defined by `.*1`, i.e. words that end in 1.
> Then we can define our DFA as follows:
>
> ```
>         1        1
> -> q0 ----- <q1> -+
>   ^| ^      |  ^  |
>   ++ +------+  +--+
>   0      0
> ```
>
> Formally this would be:
> - We have $Q = \{q_0, q_1\}$.
> - We have $\Sigma = \{0, 1\}$.
> - We have $\delta(q_j, i) = q_i$.
> - The start state is $q_0$.
> - The accepting states are $\{q_1\}$.

Due to the finite limitation of the DFA it cannot recognise all possible strings.
For example, if you wanted to accept words that have an equal number of `0` and `1` you would need to track all possible values of `0` and `1` which would lead to an infinite number of states.
