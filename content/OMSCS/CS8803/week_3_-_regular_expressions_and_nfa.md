---
aliases:
course_code: CS8803 O08
course_name: Compilers - Theory and Practice
created: '2026-01-16'
date_checked: 2026-01-25
draft: false
last_edited: 2026-01-19
tags:
  - OMSCS
title: Week 3 - Regular expressions and NFA
type: lecture
week: 3
---

This lecture focuses on how to construct a DFA from a given RegEx algorithmically.
To do this we will:

1. Introduce an easier object to work with called a Non-deterministic Finite Automaton (NFA).

2. Show that operations in RegEx can be converted into ways to combine NFAs together.

3. We will prove that an NFA can be converted into a DFA.

4. We will try to minimise this representation.

This will give us the algorithm to go from RegEx to a minimal DFA.

# Non-deterministic Finite Automata (NFA)

> [!definition] Non-deterministic Finite Automata (NFA)
> A non-deterministic finite automaton (NFA) is defined by the following:
> - A finite set of states $Q$.
> - A finite set of input symbols $\Sigma$.
> - A transition function $\delta: Q \times (\Sigma \cup \{\epsilon\}) \rightarrow \mathcal{P}(Q)$.
> - A start state $q_0 \in Q$.
> - A set of accepting states $A \subseteq Q$.

The two largest differences between a DFA and NFA are:

- An input symbol can send you to multiple states or NO states.
In the no states case, the computation path terminates.

- There are epsilon-transitions ($\epsilon$-transitions), which means when at a state with an $\epsilon$-transition you can move to any state connected by an $\epsilon$-transition without consuming input.

This non-determinism means we need to change perspective about how we traverse these automata.
Whenever presented with multiple options or an $\epsilon$-edge, think of the computation 'forking' to explore all possible paths simultaneously.
A word is accepted by an NFA if any of these forked computation paths end in an accepting state. In other words, a word is accepted if there exists at least one way to read the word such that it reaches an accepting state.

> [!example] Simple NFA
> Consider the following NFA:
> ```
>        1       0,e       1
> -> A -----> B -----> C ----> <D>
>   ^ |
>   +-+
>   0,1
> ```
> This can be formalised as:
> - We have $Q = \{A, B, C, D\}$.
> - We have $\Sigma = \{0, 1\}$.
> - We define $\delta$ by:
> $$
> \begin{aligned}
> \delta(A, 0) &= \{A\} \\
> \delta(A, 1) &= \{A, B\} \\
> \delta(A, e) &= \{\} \\
> \delta(B, 0) &= \{C\} \\
> \delta(B, 1) &= \{\} \\
> \delta(B, e) &= \{C\} \\
> \delta(C, 0) &= \{\} \\
> \delta(C, 1) &= \{D\} \\
> \delta(C, e) &= \{\} \\
> \delta(D, -) &= \{\} \\
> \end{aligned}
> $$
> - The start state is $A$.
> - The accepting states are $\{D\}$.
> In this example, when considering the word 1011, we can track the states it could currently be in.
> - 1 -> {A, B, C}
> - 10 -> {A, C}
> - 101 -> {A, B, C, D}
> - 1011 -> {A, B, C, D}
> Therefore, since this word contains an accepting state in its final states, we accept it.
> Generally, the accepted words are $(0|1)^*(11|101)$.

# Going from a RegEx to an NFA

To construct an NFA from a regular expression we need to show how the regular expression operations can be expressed as combinations of other NFAs.

## The | operation

> [!lemma] Suppose we have two NFAs representing $A$ and $B$ (RegEx) (on the same alphabet $\Sigma$) then there is an NFA that represents $A \vert B$.
> Let $X$ be represented by $(Q_X, \Sigma, \delta_X, q_X, A_X)$ then we will need to construct $C$ similarly.
>
> Let $Q_C = Q_A \cup Q_B \cup \{start\}$, where $q_C = start$ and $A_C = A_A \cup A_B$.
>
> Then let $\delta_C(q,s) = \delta_X(q,s)$ for all $q \in Q_X$.
> So all that remains to be defined is on $start$.
> $$
> \begin{aligned}
> \delta_C(start, \epsilon) &= \{q_A, q_B\}\\
> \delta_C(start, s) &= \{\} & \mbox{for all } s \in \Sigma
> \end{aligned}
> $$
>
> To show $C$ generates the same language as $A \vert B$ we need to show both $L_{C} \subset L_{A \vert B}$ but also $L_{A\vert B} \subset L_{C}$.
>
> Take a word $w \in L_{C}$ and pick a single path $p$ that realises $w$.
> This path must start with $(start, q_X, \epsilon)$ as they are the only paths from $start$.
> Though as $Q_A$ and $Q_B$ are disconnected in $Q_C$ this means $p$ must only traverse nodes in $Q_X$.
> Therefore $p$ without the first edge is a path that realises $w$ in $X$.
> So $w \in L_{A \vert B}$.
>
> Suppose we have $w \in L_{A \vert B}$ then let $p$ be a path that realises $w$ in $X$.
> Append $(start, q_X, \epsilon)$ to $p$ and we have a path that realises $w$ in $C$.
> So $w \in L_{C}$.
>
> Therefore we have $L_{C} = L_{A \vert B}$.


## Concatenation

> [!lemma] Suppose we have two NFAs representing $A$ and $B$ (RegEx) (on the same alphabet $\Sigma$) then there is an NFA that represents $AB$.
> Let $X$ be represented by $(Q_X, \Sigma, \delta_X, q_X, A_X)$ then we will need to construct $C$ similarly.
>
> Let $Q_C = Q_A \cup Q_B$ with start state $q_A$ and accepting states $A_C=A_B$.
>
> Let $\delta_C(q,-) = \delta_X(q,-)$ for all $q \in Q_C \backslash A_A$.
> Then define $\delta_C$ on $A_A$ as:
> $$
> \begin{aligned}
> \delta_C(q, s) &=\delta_A(q,s) & \mbox{for } q \in A_A \mbox{ and } s \in \Sigma\\
> \delta_C(q, \epsilon) &= \delta_A(q,\epsilon) \cup \{q_B\} & \mbox{for } q \in A_A
> \end{aligned}
> $$
>
> Then $L_{AB} \subset L_C$ as any concatenated word of $AB$ can follow their paths in A and B with a joining $(a, q_B, \epsilon)$ edge for $a \in A_A$.
> Similarly any word in $L_C$ must use a $(a, q_B, \epsilon)$ edge at which point all nodes before this edge use only nodes in $Q_A$ and after only nodes in $Q_B$ giving us our concatenation point.
> This shows $L_{AB} = L_C$.

## The * operation

> [!lemma] Suppose we have an NFA representing $A$ (RegEx) then there is an NFA that represents $A*$.
> Let $A$ be represented by $(Q_A, \Sigma, \delta_A, q_A, A_A)$ then we will need to construct $B$ to represent $A*$.
> (For simplicity, I am going to assume $q_A \not \in A_A$ - this construction works if it is but you have to be more careful with $\delta_B$ to check what you are building is valid.)
>
> Let $Q_B = Q_A$ with start state $q_B = q_A$ and accepting states $A_B = A_A$.
>
> Now define $\delta_B(q,-) = \delta_A(q,-)$ for all $q \in Q_B \backslash (A_A \cup \{q_A\})$ then define:
> $$
> \begin{aligned}
> \delta_B(q_A, s) &= \delta(q_A, s) & \mbox{for } s \in \Sigma\\
> \delta_B(q_A, \epsilon) &= \delta(q_A, \epsilon) \cup A_A\\
> \delta_B(q, s) &= \delta(q, s) & \mbox{for } q \in A_A \mbox{ and } s \in \Sigma\\
> \delta_B(q, \epsilon) &= \delta(q, \epsilon) \cup \{q_A\} & \mbox{for } q \in A_A
> \end{aligned}
> $$
>
> Suppose we have a word in $A*$; then we can realize all subwords in $A$ as paths in $Q_A$.
> We can glue these together using edges $(q, q_A, \epsilon)$ for $q \in A_A$.
> (For the empty word, we can use a path with one edge $(q_A, q, \epsilon)$ for $q \in A_A$.)
> Thus showing $L_{A*} \subset L_B$.
>
> Instead suppose we have a word in $B$ let it be realised by a minimal path $p$ in the number of edges.
> If the word this path represents is not empty then we can show it does not use any of the $(q_A, q, \epsilon)$ edges - otherwise we could contract the path further to get a smaller path.
> Therefore we can cut this path up by the $(q, q_A, \epsilon)$ edges to get subwords in $A$.
> Thus showing $L_B \subset L_{A*}$ and giving us equality.

We can use a similar construction to get $A^+$ by not including the edges $(q_A, q, \epsilon)$ for $q \in A_A$.
Similarly, we can construct $A?$ by removing the $(q, q_A, \epsilon)$ edges for $q \in A_A$.

# Equivalence of DFA and NFA

We say that two finite automata are equivalent if they recognise the same set of words.

> [!lemma] DFA and NFA are equivalent
> As DFA are a subset of NFA, we just need to show that for every NFA we can construct a DFA that recognises the same set of words.
>
> Let $A$ a NFA be represented by $(Q_A, \Sigma, \delta_A, q_A, A_A)$ then we will need to construct $B$ a DFA to represent $A$.
> To define $B$ we need to define a map called the $\epsilon$-closure:
> $$
> \epsilon: \mathcal{P}(Q_A) \rightarrow \mathcal{P}(Q_A)
> $$
> $$
> \epsilon: X \mapsto \{q \in Q_A \mid \text{there exists a path } p_{x,q} \text{ for some } x \in X \text{ using only } \epsilon \text{ edges}\}.
> $$
> Note that $X \subset \epsilon(X)$ by the empty path.
> Let $Q_B = \mathcal{P}(Q_A)$ with $q_B = \epsilon(\{q_A\})$, and $A_B = \{X \in \mathcal{P}(Q_A) \mid X \cap A_A \neq \emptyset\}$.
> Then define $\delta_B(X,s) = \epsilon(\bigcup_{x \in X} \delta_A(x,s))$.
>
> Intuitively, this graph is exactly how we traverse an NFA as described earlier.
> Note it may not be connected - but that does not matter.
>
> As this graph is exactly how you traverse an NFA, paths in $Q_A$ can be projected into $Q_B$ where $\epsilon$ edges are removed.
> Therefore $L_{A} \subset L_{B}$.
>
> Similarly, for a word $w \in L_{B}$ we can expand a path $p$ that realises $w$ in $Q_B$ to a path in $Q_A$ by adding $\epsilon$ edges at each node.
> Therefore $L_{B} \subset L_{A}$.
> Giving us $L_{A} = L_{B}$.

While the construction above works, it is not very efficient in practice.
So instead, in algorithms we build $B$ by traversing $A$ using breadth-first search.

```
1. q_B <- \epsilon({q_A})
2. Q_B <- {q_B}
3. W <- {q_B}
4. while W is not empty:
5.   q <- pop(W)
6.   for each s in \Sigma:
7.     t <- \epsilon(\delta_A(q,s))
8.     \delta_B(q,s) <- t
9.     if t \not in Q_B then:
10.       Q_B <- Q_B \cup {t}
11.       W <- W \cup {t}
```

This technically completes our move from RegEx to DFA but this could still be very large.
Therefore, we do one last step to try to minimise this DFA representation.

# Minimal DFA

Notice that within the DFA construction we naturally collapse states that have a similar prefix, as these paths will be tracked together and collapsed similarly.
However, similar suffixes on the other hand are not collapsed as this algorithm only looks forward.
So to collapse these similar suffixes, we first run the construction backwards before running it forwards.
To do this we define 3 functions on NFAs:

1. Subset(A): This is the operation we defined in the above section to go from an NFA to a DFA.

2. Reverse(A): We take an NFA and reverse all the edges and switch the start and end states.
As there are multiple accepting states, we add a new start state and connect it to each of the accepting states using an $\epsilon$ edge.

3. Reachable(A): We remove all states that are not reachable from the start state.

Then the minimal DFA for some NFA $A$ is defined by the sequence of operations:

```
Min_DFA(A) = reachable[subset[reverse[reachable[subset[reverse[A]]]]]]
```

This is just `reachable \cdot subset \cdot reverse` applied twice.
The first iteration gets rid of common suffixes, the second iteration gets rid of common prefixes.
