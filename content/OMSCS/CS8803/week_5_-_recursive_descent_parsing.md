---
aliases:
course_code: CS8803 O08
course_name: Compilers - Theory and Practice
created: '2026-02-03'
date_checked: '2026-02-05'
draft: false
last_edited: 2026-02-05
tags:
  - OMSCS
title: Week 5 - Recursive Descent Parsing
type: lecture
week: 5
---

In this lecture we are focusing on parsers.
We can classify parsers into two types:

- LR Bottom up parsers:
  - L: Scan left to right.
  - R: Traces rightmost derivation of the input string - starts from the end of the sentence.
  - This is bottom up as we start from the sentence and work our way back to the start symbol.
- LL Top down parsers:
  - L: Scan left to right.
  - L: Traces leftmost derivation of the input string - starts from the beginning of the sentence.
  - This is top down as we start from the start symbol and work our way forward to the sentence.

Within both types of parsers there is a dimension which reflects their efficiency.
This is the maximum number of tokens it needs to 'look ahead' to decide what rule to apply.
This is referred to by $k$ and appended to the end of the type like $LL(k)$ for a top down parser that looks ahead $k$ tokens.
Functionally we want to keep $k$ as low as possible to make compiling code as fast as possible.

There is another important property of a parser:

- Deterministic parser: This will not back track and if it can't apply a rule it is due to a syntax error not an incorrectly chosen rule.

- Non-deterministic parser: This will back track and try to apply a rule that it thinks will work.

In reality we will only ever use deterministic parsers.
Non-deterministic are not time efficient to be used in practice.

# Recursive Descent Parsing

During this lecture we will cover a simple parser called recursive descent parsing - this is a deterministic LL(1) parser.
For terminal symbols such as IDs, integers etc we process them using a rule that we will pick by looking ahead.
If the later tokens match this rule we consume them otherwise we throw an error.

![Recursive Descent Parsing overview](../../../static/images/recursive_descent_parsing_overview.png)

The output of the parser is an Abstract Syntax Tree (AST).

> [!definition] Abstract Syntax Tree
> A tree representation of the input text.
> The leaves of the tree are the raw values or variables.
> The internal nodes of the tree are operations.
> The order of these operations indicates the order in which they need to be applied - bottom up.

To apply this algorithm we first need to prepare the grammar. It must satisfy three properties:

- Written in Backus Naur Form (BNF).
- Only right recursive rules.
- No common prefixes between alternatives in a rule.

Each of these is covered in the sections below. All transformations must be done without introducing new ambiguities.

# Backus Naur Form (BNF)

BNF is a notation for writing down the grammar (syntax rules) of a language.
A grammar is made up of **productions** — rules that define how non-terminals can be expanded into sequences of symbols until you arrive at actual tokens.

The core symbols are:

- `<name>` - a **non-terminal**: a syntactic category that will be expanded further by another rule.
- Bare text or `"literal"` - a **terminal**: an actual token in the language (e.g. `+`, `(`, a keyword). These are the end points — they cannot be expanded further.
- `::=` - "is defined as". Separates the left-hand side (a single non-terminal) from the right-hand side (what it can expand into).
- `|` - "or". Separates alternative expansions within a rule.

> [!example] Arithmetic Expression Grammar
> ```
> <expr>   ::= <term> "+" <expr> | <term>
> <term>   ::= <factor> "*" <term> | <factor>
> <factor> ::= "(" <expr> ")" | <number>
> ```
> Reading the first rule: an expression is either a term followed by `+` and another expression, or just a term on its own.
> The first non-terminal listed (`<expr>`) is the **start symbol** - the root from which the entire input must be derivable.

A key limitation of BNF is that it has no shorthand for "optional" or "zero or more".
These common patterns must instead be encoded using recursion, which can be harder to read at a glance:

```
<list> ::= <item> "," <list> | <item>
```

This says a list is an item, optionally followed by a comma and another list - but you have to trace the recursion to see that.

# Extended Backus Naur Form (EBNF)

EBNF extends BNF with extra operators to express optionality, repetition, and grouping **directly** instead of relying on recursive rules.
It has exactly the same expressive power as BNF — every EBNF grammar can be mechanically rewritten in BNF.
It is purely syntactic sugar for readability.

The additional operators are:

- `[ X ]` — **optional**: $X$ appears zero or one times.
- `{ X }` — **repetition**: $X$ appears zero or more times.
- `( X | Y )` — **grouping**: choose between alternatives without needing a separate non-terminal rule.
- `;` — **rule terminator**: explicitly marks the end of a rule (BNF relies on end-of-line).

> [!example] Same Arithmetic Grammar in EBNF
> ```
> expr   = term { "+" term } ;
> term   = factor { "*" factor } ;
> factor = "(" expr ")" | number ;
> ```
> `{ "+" term }` directly says "zero or more occurrences of `+` followed by a term" — no recursive helper rule needed.

To make the difference concrete, here is the same comma-separated list in both forms:

```
-- BNF (requires a helper rule to express the repetition)
<list>      ::= <item> <list-tail>
<list-tail> ::= "," <item> <list-tail> | \epsilon

-- EBNF (states it directly)
list = item { "," item } ;
```

Both describe exactly the same language.
EBNF is simply faster to read and write.

# Going from EBNF to BNF

EBNF is much more convenient to write and read than BNF.
However, we will need to convert back to BNF to use it in recursive descent parsing, as each BNF production rule maps directly to a parser function.
The main rule we have to 'unwrap' is the repetition operator.
To do this we use the 'tail' notation - as shown below.

```
-- EBNF
list = item { "," item } ;

-- EBNF to BNF
<list>      ::= <item> <list-tail>
<list-tail> ::= "," <item> <list-tail> | \epsilon
```

Here we just set whatever optional ending we have to be a new symbol which is either what is in the brackets or empty.

> [!example] EBNF to BNF
> Suppose our language is described by the regular expression $a^* b \mid c^+$. How can we write this in BNF?
> ```
> <S> ::= <A> <B> | <C>
> <A> ::= a <A> | \epsilon
> <B> ::= b
> <C> ::= c <D>
> <D> ::= c <D> | \epsilon
> ```
> We break the expression into its smallest components and apply the tail rule to each repetition ($a^*$ and $c^+$).

# Left and Right Recursion

So far in all our examples we have right recursion.
This means we have examples like $A \to a A$ where the recursive element is on the right.
This helps us writing a parser as we can process all the tokens before we reach the recursive element.
Whereas with left recursion (e.g. $A \to A a$) we would hit an infinite loop of a function calling itself (this will become clearer later on).
Therefore we need a way to convert left recursive statements into right recursive ones.
To do this we 'shift' the expression by one - creating a new intermediate symbol.

> [!example] Simple left recursion
> Suppose we have a left recursive statement like $E \to E \text{ } '+' \text{ } T \mid T$ - how can we rewrite this as a right recursive statement?
> ```
> E -> T E'
> E' -> '+' T E' | \epsilon
> ```
> Just like the tail before we get the 'terminal' component of the recursion and set that first.
> Then we get out the recursive component pulling one iteration out of it onto the left hand side.

# Common prefix contraction

Lastly to limit the lookahead needed to determine the rule we need to collapse common prefixes.
To do this we again use a substitution rule.

> [!example] Common prefix contraction
> Suppose we have a rule like $A \to uv \mid uw$ - how can we rewrite this to remove the common prefix?
> ```
> A -> u A'
> A' -> v | w
> ```
> This ensures that we only need a single look ahead to disambiguate the two cases.

# The Parsing Algorithm

The setup of a parser is that there is a stack of tokens that we need to apply rules to.
The rules will be function calls which will proceed down the stack until we hit the end or have an error.
To assist this we can 'peek' at the next token of the stack without removing it.
We will also be able to call 'matchToken' which will look at the next token on the stack and match it to a provided token.
In the lectures the algorithm was not provided directly but instead motivated by examples.

> [!example] Converting a sequential rule
> Suppose we have a grammar as follows:
> ```
> expr -> term e_tail
> e_tail -> "+" term e_tail | \epsilon
> term -> ...
> ```
> This can be converted into two functions for expr and e_tail as follows:
> ``` pseudocode
> void expr() {
>   term();
>   e_tail();
> }
>
> void e_tail() {
>   Token token = peekToken();
>   if (token == "+") {
>     matchToken("+");
>     term();
>     e_tail();
>   }
> }
> ```

The conversion literally comes from the grammar rule.
When there is an option between two choices you use the next symbol to decide the path.
If there is a terminal symbol such as an operation then you check it is there.
Otherwise you call the next rule.

> [!example] Converting a branching rule
> Suppose we have a grammar as follows:
> ```
> factor -> "(" expr ")" | number | id
> ```
> This can be converted into a function as follows:
> ``` pseudocode
> void factor() {
>   Token token = peekToken();
>   if (token == "(") {
>     matchToken("(");
>     expr();
>     matchToken(")");
>   } else if (token == "number") {
>     matchToken("number");
>   } else if (token == "id") {
>     matchToken("id");
>   } else {
>     throw new Error("Expected '(' or 'number' or 'id'");
>   }
> }
> ```

Putting this all together, let's run through an example of it being applied to a simple grammar:

```
expr -> term e_tail
e_tail -> "+" term e_tail | \epsilon
term -> factor t_tail
t_tail -> "*" factor t_tail | \epsilon
factor -> "(" expr ")" | number | id
```

Let's assume we always start with an expr and our input is `1 + 2 * 3`.
Each level of nesting below is one function call deeper on the call stack.
`match` consumes a token, `peek` looks ahead to decide a branch, and `→ ε` means the empty production was taken.
The remaining input is shown in parentheses after each action:

```
expr()
├── term()
│   ├── factor(): match "1"                (stack: + 2 * 3)
│   └── t_tail(): peek "+", not "*" → ε    (stack: + 2 * 3)
└── e_tail(): peek "+"
    ├── match "+"                          (stack: 2 * 3)
    ├── term()
    │   ├── factor(): match "2"            (stack: * 3)
    │   └── t_tail(): peek "*"
    │       ├── match "*"                  (stack: 3)
    │       ├── factor(): match "3"        (stack: ε)
    │       └── t_tail(): peek ε → ε       (stack: ε)
    └── e_tail(): peek ε → ε               (stack: ε)
```

This outputs us a parse tree below:

![Recursive Descent Parsing Example](../../../static/images/recursive_descent_parsing_example.png)

# Parse tree to AST

The last step is to go from a parse tree to an AST.
This involves applying the following operations to the parse tree.

1. Contracting $\epsilon$ nodes: Remove them as leaves and then contract the branches they are on until all leaves are now non-epsilon terminal nodes.
2. Contract operations into nodes: Take the operations that are currently leaf nodes and merge them into the internal node they are connected to.
Then contract that nodes parent branches until it has the appropriate number of children.
3. Contract terminal symbols: Lastly contract the branches so that the terminal nodes (numbers, IDs) connect directly to an operation node.

The remaining tree represents the AST - it will only contain internal nodes with operations and children that are either numbers or IDs.
