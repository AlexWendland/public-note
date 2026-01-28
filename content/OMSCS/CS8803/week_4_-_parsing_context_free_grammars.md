---
course_code: CS8803 O08
course_name: Compilers - Theory and Practice
created: '2026-01-28'
date_checked: '2026-01-28'
draft: false
last_edited: '2026-01-28'
tags:
  - OMSCS
title: Week 4 - Parsing context free grammars
type: lecture
week: 4
---

In this lecture, we will cover the parser - in particular the rules for parsing token input.
This has two major responsibilities:

- Syntax analysis: Checking the program is using the correct grammar for the programming language.

- Breaking the input into expressions: Parsing the input into a sequence of expressions.

# Derivation tree

> [!definition] Derivation tree
> A derivation tree is a tree representation of the process of parsing a program.
> The root is the starting symbol and the internal nodes represent sub-symbols.

Given a grammar $G$ we say a word $w$ is in the language, $w \in L(G)$, if there exists a derivation tree that represents the word.

> [!example] Simple example
> Lets consider the grammar given by $S \rightarrow S+S \vert S\ast S \vert (S) \vert ID$.
> We need to work out if $ID \ast ID + ID$ belongs to the language.
> We can decompose this statement using the above rules as:
> $$
> \begin{align*}
> S \Rightarrow & S + S\\
> \Rightarrow & S \ast S + S\\
> \Rightarrow & ID \ast S + S\\
> \Rightarrow & ID \ast ID + S\\
> \Rightarrow & ID \ast ID + ID
> \end{align*}
> $$
> This represents the graph below:
> ![derivation tree](../../../static/images/derivation_graph_example.png)

The natural question is how did we do this expansion?
Here we used a *left-most* derivation strategy.
That is, we took the symbol $S$ on the left-hand side and chose to expand it.
(This does not cover how we choose the rule to expand it—that is covered in the next lecture.)
We could also use a *right-most* derivation, which changes the order of expansion but should not change the resulting tree.
Whilst there are other strategies to pick which node to expand next, these are not commonly used.

> [!definition] Parse Tree
> A parse tree for a CFG $G = (V, \Sigma, R, S)$ is a derivation tree that has the following properties:
> 1. The root is labeled $S$.
> 2. Each leaf is from $\Sigma \cup \{\epsilon\}$.
> 3. Each interior node is in $V$.
> 4. If a node has a label $A \in V$ and it has children $a_1, \ldots, a_n$ (from left to right), then $G$ must have a rule $A \rightarrow a_1 \ldots a_n$ (with $a_j \in V \cup \Sigma \cup \{\epsilon\}$). A leaf labelled $\epsilon$ is a single child (has no siblings). 

> [!definition] Language
> Let $G$ be a context free grammar.
> We have $w \in L(G)$ if and only if there exists a derivation tree of $G$ that yields $w$.

# Ambiguity

> [!definition] Ambiguous word
> For a context free grammar $G$, a word $w \in L(G)$ is ambiguous if there exists two parse trees for $w$.

> [!definition] Ambiguity
> A context free grammar $G$ is called ambiguous if there exists a word $w \in L(G)$ that is ambiguous.

> [!example] Ambiguous word
> Let us consider the grammar given by $S \rightarrow 0 \mid 1 \mid S+S \mid S\ast S$.
> Now consider the word $0 \ast 1 + 1$.
> This has two parse trees given by:
> $$
> \begin{align*}
> S \Rightarrow & S + S\\
> \Rightarrow & S \ast S + S\\
> \Rightarrow & 0 \ast S + S\\
> \Rightarrow & 0 \ast 1 + S\\
> \Rightarrow & 0 \ast 1 + 1\\
> \\
> S \Rightarrow & S \ast S\\
> \Rightarrow & 0 \ast S\\
> \Rightarrow & 0 \ast S + S\\
> \Rightarrow & 0 \ast 1 + S\\
> \Rightarrow & 0 \ast 1 + 1
> \end{align*}
> $$
> These trees are different due to the starting node changing symbol.

Ambiguity is not desirable for programmatic parsing, even if it is fun in conversation!
Therefore, we deploy a couple of tricks to resolve ambiguity:

1. Rule precedence: We put different rules in order of precedence; for example, always multiply or divide before we add or subtract.

2. Left-associativity: Perform operations from left to right.

3. Full parenthesisation: Always enclose sub-expressions in parentheses.

> [!warning] Applying precedence rules
> A little counter-intuitively we apply operations with lower precedence closer to the root of the tree and operations with higher precedence closer to the leaves.

> [!example] Precedence example
> Suppose we put the rules of the grammar in order of precedence (lowest precedence at the top—these get applied first when making a parsing tree).
> - $\text{expression} \rightarrow \text{expression} \, \text{addop} \, \text{expression} \mid \text{term}$
> - $\text{addop} \rightarrow + \mid -$
> - $\text{term} \rightarrow \text{term} \, \text{mulop} \, \text{term} \mid \text{factor}$
> - $\text{mulop} \rightarrow \ast \mid /$
> - $\text{factor} \rightarrow \text{number} \mid ( \text{expression} )$
> Now suppose we want to parse the expression $4 \ast 5 + 6$.
> $$
> \begin{align*}
> \langle\text{exp}\rangle \Rightarrow & \langle\text{exp}\rangle \, \langle\text{addop}\rangle \, \langle\text{exp}\rangle\\
> \Rightarrow & \langle\text{term}\rangle \, \langle\text{addop}\rangle \, \langle\text{exp}\rangle\\
> \Rightarrow & \langle\text{term}\rangle \, \langle\text{mulop}\rangle \, \langle\text{term}\rangle \, \langle\text{addop}\rangle \, \langle\text{exp}\rangle\\
> \Rightarrow & 4 \, \langle\text{mulop}\rangle \, \langle\text{term}\rangle \, \langle\text{addop}\rangle \, \langle\text{exp}\rangle\\
> \Rightarrow & 4 \ast \langle\text{term}\rangle \, \langle\text{addop}\rangle \, \langle\text{exp}\rangle\\
> \Rightarrow & 4 \ast 5 \, \langle\text{addop}\rangle \, \langle\text{exp}\rangle\\
> \Rightarrow & 4 \ast 5 + \langle\text{exp}\rangle\\
> \Rightarrow & 4 \ast 5 + \langle\text{term}\rangle\\
> \Rightarrow & 4 \ast 5 + 6\\
> \end{align*}
> $$
> Notice that here we could not go directly to $\langle\text{term}\rangle$ as there would be no way back to $\langle\text{exp}\rangle$ without using parentheses.
> This eliminates the ambiguity between the $\ast$ and $+$ operators.

We can use left-associativity to eliminate ambiguity in expressions such as $1-1-1$.

The last large family of ambiguity stems from the 'dangling else' problem.
For example:

> if a < b if c < d c = d else a = b

In this case, does the else belong to the first or second if?
This can be resolved using an endif statement or by bracketing.
Here the grammar would change as follows:

- $\text{statement} \rightarrow \text{matched-stmt} \mid \text{unmatched-stmt}$
- $\text{matched-stmt} \rightarrow \text{if} \, (exp) \, \text{matched-stmt} \, \text{else} \, \text{matched-stmt} \mid \text{other}$
- $\text{unmatched-stmt} \rightarrow \text{if} \, (exp) \, \text{statement} \mid \text{if} \, (exp) \, \text{matched-stmt} \, \text{else} \, \text{unmatched-stmt}$

This derivation means that as soon as you resolve the if statement, you must designate it as either a matched or unmatched statement.
This forces the resolution of the else at that point.

In the example above, we would get:

![dangling else](../../../static/images/dangling_else_resolution.png)

If we used a matched-statement initially, it can only have matched child statements.
However, in our example above, the outer if contains the else, but the inner if has no else—which means it cannot be a matched statement.

# Abstract Syntax Trees

> [!definition] Abstract Syntax Tree
> An abstract syntax tree (AST) is a tree representation of the structure of a program.
> For a CFG $G = (V, \Sigma, R, S)$, the AST is a tree where all inner vertices are operations and leaf nodes are values.

We can convert our parse tree into an AST for the statement by contracting any internal nodes.
For example, see below.

![AST](../../../static/images/parse_tree_to_ast.png)
