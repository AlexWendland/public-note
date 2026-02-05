---
aliases:
course_code: CS8803 O08
course_name: Compilers - Theory and Practice
created: '2026-02-05'
date_checked:
draft: true
last_edited: '2026-02-05'
tags:
  - OMSCS
title: Week 6 - Semantic Analysis
type: lecture
week: 6
---

Next we move on to the Semantic analysis stage of the compiler.
This answers questions like:

- Has a variable $x$ been declared?

- Does $x$ have the correct type?

- Are there variables that are declared but not used?

- Do two variables reference the same memory location?

The answers to these question are beyond the scope of what a CFG can check.
These questions rely on information such as:

- The value of a variable.

- Requires non-local information such as the type it was assigned before or the result type of a computation.

- Answers may involve computation and more complex logic.

There are two methods used to answer these questions within modern compilers:

- Attribute grammars.

- Ad-hoc techniques, such as:

  - Symbol tables.

  - Ad-hoc code for particular operations.

  - Use of a semantic stack to speed up analysis.

We will focus on the formalised version of attribute grammars, this is a specification on how to structure solutions to these questions.
This separates the what needs to be done from how it is done.
Though with this comes some issues - such as too much overhead in compilers, information that is not needed being passed around.
In reality, both attribute grammars and ad-hoc techniques are used in practice.

# Attribute grammars

> [!definition] Attribute grammar
> A attribute grammar consists of the following information:
> - A context-free grammar $G$ that describes the language of the program.
> - Each symbol in $G$ is associated with a set of named values or attributes.
> - For each value or attribute a rule on how to compute it using the values of their parent or children.
> - Attribute rules are functional; they uniquely define the value.

> [!example] Evaluating a signed binary number
