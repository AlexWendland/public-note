---
aliases:
course_code: CS8803 O08
course_name: Compilers - Theory and Practice
created: '2026-02-03'
date_checked:
draft: true
last_edited: '2026-02-03'
tags:
  - OMSCS
title: Week 5 - Top down parsing
type: lecture
week: 5
---

In the previous lecture we described a LL(1) parser that required humans to still write the functions for each expression.
In this lecture we will produce an LL(1) parser that can be automatically generated from the grammar itself.

# General overview

This algorithm will have two stacks:

- The input stack of tokens.

- The working stack of symbols it is using to build up the expression.

The first stack starts with all the input symbols.
The second stack starts with only an end-of-input marker `$` at the bottom and the start symbol on top.
The general plan of attack will be:

- Replace non-terminal symbols on the working stack using grammar rules.

- If the top of the working stack matches the top of the input stack, both are discarded - mismatches cause a syntax error.

The goal is to empty both stacks.

> [!example] Bracket matching
> Suppose we have grammar `S ::= ( S ) S | epsilon` with start symbol `S` and input `()$`. Let's run the algorithm.
> Both stacks are listed bottom to top (rightmost is the top).
> The input stack starts as `$`, `)`, `(`.
> The working stack starts as `$`, `S`.
>
> 1. Replace `S` (non-terminal) with `( S ) S` — symbols are pushed in reverse order so `(` ends up on top. Working stack: `$`, `S`, `)`, `S`, `(`.
> 2. As `(` is at the top of the input and working stack, discard both. Working: `$`, `S`, `)`, `S`. Input: `$`, `)`.
> 3. Replace `S` (top of working stack) with `epsilon`. Working: `$`, `S`, `)`.
> 4. As `)` is at the top of the input and working stack, discard both. Working: `$`, `S`. Input: `$`.
> 5. Replace `S` with `epsilon`. Working: `$`.
> 6. As `$` is at the top of the input and working stack, discard both.
>
> Both stacks are now empty so the input is syntactically valid.

# Parsing table

In the example above we decided the matching rules by hand - but generally we need to work them out beforehand.
This defines a 2-dimensional lookup table `M[X][T]` which takes a non-terminal symbol `X` at the top of the working stack and token `T` at the top of the input stack and maps to the production rule we should apply.
We call this the parsing table.

> [!example] Bracket matching parsing table
> To continue the example above we had the following parsing table:
>
> | M[X][T] | ( | ) | $ |
> | ------- | - | - | - |
> | S | S -> (S) S | S -> epsilon | S -> epsilon |
>
> This is what we applied above.

However, we said this algorithm would come from the grammar - so we need to automatically generate such a parsing table.

## LL(1) grammar

To generate such a parsing table we need a particular kind of grammar - like the ones we described in the previous lecture.

> [!definition] LL(1) grammar
> A grammar is an LL(1) grammar if the associated LL(1) parsing table has at most one production rule in each table entry.

The LL(1) grammars are a proper subset of context-free grammars.
We require the following properties:

- The grammar must not be ambiguous.

- The grammar must not be left recursive.

- The grammar must not have common prefixes (FIRST sets of alternatives for each non-terminal must be disjoint).

# Generating the parsing table

To state the algorithm to generate this parsing table we need a couple of definitions first.

## First sets

For a symbol `X` we define the first set `First(X)` to be the set of first tokens (terminal symbols) that strings derived from `X` can start with.
To generate `First(X)` we need to look at each rule for $X$ such as $X -> X_1 X_2 \ldots X_n$ (note this rule does not contain any $\vert$ in it - we take optionals to generate multiple rules) and determine which tokens could start this rule.
So we apply the following rules to generate `First(X)`:

1. If `X` is a terminal symbol (including $\epsilon$) then $First(X) = \{X\}$.
2. If `X` is a non-terminal symbol and for each rule $X \rightarrow X_1 X_2 \ldots X_n$ then $First(X_1) - \{\epsilon\} \subset First(X)$.
3. If `X` is a non-terminal symbol and for each rule $X \rightarrow X_1 X_2 \ldots X_n$ where for each $0 < i < j$ $\epsilon \in First(X_i)$ then $First(X_j) - \{\epsilon\} \subset First(X)$.
4. If `X` is a non-terminal symbol and for a rule $X \rightarrow X_1 X_2 \ldots X_n$ where $\epsilon \in First(X_i)$ for $0 < i \leq n$ then $\{\epsilon\} \subset First(X)$.

> [!example] First sets
> Suppose we have the following grammar:
> ```
> S ::= ABC
> A ::= a | epsilon
> B ::= b
> C ::= c | epsilon
> ```
> Then we get the following first sets:
>
> - First(x) = {x} for x in {a, b, c, epsilon} by the first rule.
>
> - First(A) = (First(a) - {epsilon}) $\cup$ (First(epsilon) - {epsilon}) $\cup$ {epsilon} = {a, epsilon} here as there is an alternation we express `A ::= a | epsilon` as two rules `A ::= a` and `A ::= epsilon`.
> As First(a) does not contain epsilon we stop at a.
> As First(epsilon) does contain epsilon but the rule length is only 1 by the fourth rule we add epsilon to First(A).
>
> - First(C) = {c, epsilon} similarly as above.
>
> - First(B) = First(b) - {epsilon} = {b} by the second rule.
>
> - First(S) = (First(A) - {epsilon}) $\cup$ (First(B) - {epsilon}) = {a, b} the left side comes from rule 2 and the right side comes from rule 3 but as First(B) does not contain epsilon we stop here.

This can be formalised into an algorithm as below.

```pseudocode
generateFirstSets(G) {
  for each terminal X set First(X) = {X}
  for each non-terminal X set First(X) = {}
  while there are changes to any First(X) {
    for each rule X -> X_1 X_2 ... X_n {
      k := 1
      while k <= n {
        First(X) = First(X) U (First(X_k) - {epsilon})
        if epsilon not in First(X_k) then break
        k := k + 1
      }
      if k > n then First(X) = First(X) U {epsilon}
    }
  }
  return First
}
```

## Follow sets

Intuitively, the follow set of a symbol `Follow(X)` is the set of tokens that can follow `X` in the input.
These are used to determine if a rule such as `A -> epsilon` should be used to remove `A` from the stack.
This is defined using the following rules:

1. If `X` is the start symbol then `$` $\in Follow(X)$.

2. If there is a rule $B \rightarrow \alpha X \beta$, then $First(\beta) - \{\epsilon\} \subset Follow(X)$ (where $\beta$ is the remaining string after $X$, which could be empty).

3. If there is a rule $B \rightarrow \alpha X \beta$, and $\epsilon \in First(\beta)$ then $Follow(B) \subset Follow(X)$ (where $\beta$ is the remaining string after $X$, which could be empty).

Note that, by definition, $\epsilon$ is never in $Follow(X)$.
Also $Follow(X)$ is only defined for non-terminals.

> [!example] Follow sets
> Suppose we have the following grammar (like before):
> ```
> S ::= ABC
> A ::= a | epsilon
> B ::= b
> C ::= c | epsilon
> ```
> Then we get the following follow sets:
>
> - Follow(S) = {$} by the first rule.
>
> - Follow(A) = First(B) - {epsilon} =  {b} by the second rule.
>
> - Follow(B) = (First(C) - {epsilon}) U Follow(S) = {c, $} by the second and third rule.
>
> - Follow(C) = Follow(S) = {$} by the third rule.

Quite often when resolving these you will get that multiple follow sets are the same.
We have included the code to generate this below.

```pseudocode
generateFollowSets(G, First) {
  for each non-terminal X {
    set Follow(X) = {} if X is not the start symbol else {$}
  }
  while there are changes to any Follow(X) {
    for each rule X -> X_1 X_2 ... X_n {
      for i = 1 to n {
        Follow(X_i) = Follow(X_i) U (First(X_i+1 ... X_n) - {epsilon})
        if epsilon in First(X_i+1 ... X_n) {
          Follow(X_i) = Follow(X_i) U Follow(X)
        }
      }
    }
  }
  return Follow
}
```

## The algorithm

Putting both the ideas above into practice we can now generate the parsing table.

```pseudocode
parsingTable(G, First, Follow) {
  for each non-terminal X {
    for each terminal t {
      Parsing(X,t) = Null
    }
  }
  for each rule X -> w {
    for each token t in First(w) {
      Parsing(X,t) = (X -> w)
    }
    if epsilon in First(w) {
      for each token t in Follow(X) {
        Parsing(X,t) = (X -> w)
      }
    }
  }
  return Parsing
}
```

The algorithm above is fairly simple - if a rule for $X$ can start with symbol $t$ then when we have $X$ at the top of the working stack and $t$ at the top of the input stack we can apply that rule.
If $X$ is nullable (`First(w)` contains `epsilon`) and the token $t$ can follow $X$ then we can apply the rule also - by nullifying it.

> [!example] Parsing table
> Suppose we have the following grammar:
> ```
> S ::= ABC
> A ::= a | epsilon
> B ::= b
> C ::= c | epsilon
> ```
> Then we get the following parsing table:
>
> | M[X][T] | a | b | c | $ |
> | ------- | - | - | - | - |
> | A | (A -> a) | (A -> epsilon) | - | - |
> | B | - | (B -> b) | - | - |
> | C | - | - | (C -> c) | (C -> epsilon) |
> | S | (S -> ABC) | (S -> ABC) | - | - |

Sometimes when calculating this it can be handy to use a 3rd concept called `Predict` which is all the tokens a rule can be applied to.

$$
\text{Predict}(X \rightarrow w) = \begin{cases}
\text{First}(w) & \text{if } \epsilon \not \in \text{First}(w) \\
(\text{First}(w) - \{\epsilon\}) \cup \text{Follow}(X) & \text{otherwise}
\end{cases}
$$

Then we can say that $M[X][t] = (X \rightarrow w)$ for all $t \in \text{Predict}(X \rightarrow w)$.
