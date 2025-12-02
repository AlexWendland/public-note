---
aliases:
  - naming variables
  - naming conventions
checked: false
created: 2023-03-18
draft: false
last_edited: 2023-11-11
title: Naming conventions
tags:
  - programming
type: convention
---
# Naming conventions

When coding we repeatedly have to name things. So having some go to standards for how to do this makes writing code quickly but it easier to read. The key thing is for the name to be fully expansive about what the variable is doing, if you can't do this maybe this variable is doing too much.

> [!quote] [Clean Code](../references/books/clean_code.md)
> One difference between a smart programmer and a professional programmer is that the professional understands that clarity is king. Professionals use their powers for good and write code that others can understand.

These are the following principles I try to follow:
- [Use intention-revealing names](naming_conventions.md#use-intention-revealing-names)
- [Don't include the type in the name](naming_conventions.md#dont-include-the-type-in-the-name)
- [No two names should look a like](naming_conventions.md#no-two-names-should-look-a-like)
- [Use pronounceable names](naming_conventions.md#use-pronounceable-names)
- [Avoid mental mappings](naming_conventions.md#avoid-mental-mappings)
- [Be consistent](naming_conventions.md#be-consistent)
- [Use solution and problem domain names](naming_conventions.md#use-solution-and-problem-domain-names)
- [Use the correct level of context](naming_conventions.md#use-the-correct-level-of-context)
- [Don't be afraid to rename something](naming_conventions.md#dont-be-afraid-to-rename-something)

## Use intention-revealing names

>[!quote] [Clean Code](../references/books/clean_code.md)
>The name of a variable, function, or class, should answer all the big questions. It should tell you why it exists, what it does, and how it is used.

Using intention-revealing names is easier when you adhere to the [Single Responsibility Principle (SRP)](single_responsibility_principle_(srp).md).

Here's an example to illustrate the concept:
```python
# Unclear variable name
d = 86400

# Intention-revealing variable name
seconds_in_a_day = 86400
```

In this example, `d` doesn't reveal its purpose, while `seconds_in_a_day` clearly indicates what the variable represents.

Remember this heuristic to evaluate if you've chosen a good name:

> [!quote] [Clean Code](../references/books/clean_code.md)
> If a name requires a comment, then the name does not reveal its intent.

## Don't include the type in the name

As a [Python Index](python_index.md) programmer working in [Data](data.md), it's tempting to include data types in variable names, such as `df_football_results_data`.

There are several reasons to avoid this practice:

1.  **Redundancy**: Variable names should be indicative of their structure. If you have `football_results`, it's likely you would store it in a DataFrame anyway, so specifying the type is unnecessary. There might be exceptions to this rule for example time being saved as a datetime object or unix timestamp (thus an integer).
2.  **Confusion**: Including the type in a variable name can make it harder to understand. For example, `write_to_cloud_boolean` may lead to confusion about whether it represents a boolean variable or a storage account with a provider named "boolean".
3.  **Misinformation**: Inconsistency in naming conventions can lead to misunderstandings. If you've been using types in variable names and someone else names a variable `accounts_list` when it's actually a dictionary, this can cause confusion for others working on the codebase.
4.  **IDE Suggestions**: Including types in variable names can make it more challenging to find the desired variable in your IDE's suggestions, leading to extra clicks and wasted time.
5.  **Lengthy Names**: Including types in variable names makes them unnecessarily long, which can negatively impact readability.
6. **Refactoring and maintenance**: If you include data types in variable names and later decide to change the data structure or type, you will need to update the variable name throughout the codebase to maintain consistency. This can be time-consuming and potentially introduce new bugs if not done carefully. (Though with modern IDE's this should not be a huge issue.)
7.  **Language features**: Modern programming languages and development environments often provide features such as type hinting, linting, and autocompletion that make it easier to understand and work with variables of different data types. Relying on these features instead of including data types in variable names can lead to cleaner and more maintainable code.

Though also a couple of reasons to include them:

1.  **Self-documenting code**: Including data types in variable names can make the code more self-explanatory, reducing the need for additional comments. This could be beneficial for developers who are new to the codebase or when working in a team with varying levels of expertise.
2.  **Reduced ambiguity**: In certain situations, including data types in variable names can clarify the intended use of a variable, making it easier to understand the code's purpose and reducing the likelihood of bugs or misunderstandings.
3.  **Language limitations**: In dynamically-typed languages like Python, including data types in variable names can help mitigate the lack of static type checking. This can make it easier for developers to understand the expected data types without relying on explicit type hints or external documentation.
4.  **Type conversion**: When working with multiple data types that require frequent type conversions, including data types in variable names can provide a clear indication of which variables need conversion and reduce the risk of type-related errors.
5.  **Consistency**: In some development environments or organisations, including data types in variable names might be a standard practice. Following such conventions can improve consistency and maintainability across the codebase.

Balancing these all against one another. I think it is best not to include the variable type in the name. If you are struggling to identify the type of the variable, it is indicative of the code being too long, the name of the variable needing to be changed or the variable is doing too much work.

## No two names should look a like

Using distinct variable names makes your code easier to read and scan. To prevent confusion, avoid creating variable names that look similar in the following ways:

1.  **Long prefixes**: Names that look similar due to long, shared prefixes can be confusing.
    - Example: `XYZControllerForEfficientHandlingOfStrings` and `XYZControllerForEfficientStorageOfStrings`
2.  **Numbers or noise words**: Adding numbers or noise words to variable names can make it difficult to differentiate between them.
    - Example: `data1` and `data2` or `the_data`
    - Example: having the root class as `ReaderBase` or `AbstractReader`, instead of using `Base` or `Abstract` why not specify the child classes further.
1.  **Similar suffixes**: Using words with similar meanings at the end of variable names can cause confusion.
    - Example: `ProductInfo` and `ProductData`

By ensuring that variable names are distinct and easy to differentiate.

## Use pronounceable names

Modern IDEs make it easy to work with longer, more descriptive variable names. Therefore, there's no need to use:
1.  **Single-letter characters**: Avoid using single-letter characters for variable names, as they can be ambiguous and hard to discuss.
2.  **Acronyms**: Using acronyms for variable names can be confusing and difficult to understand, especially for those unfamiliar with the acronym.
3.  **Abbreviations**: Abbreviations in variable names can be unclear and challenging to pronounce.
4. **Name hard coded variables**: If you turn numbers or strings into variables with pronounceable names, it will make the code easier to read, the variable more searchable, and easier to abstract. i.e. don't add a 7 to the code instead why not add ``DAYS_IN_THE_WEEK``.
By using pronounceable names for your variables, you can facilitate more meaningful conversations when discussing your code with others, such as during code reviews.

## Avoid mental mappings

Mental mapping occurs when readers have to interpret or translate names in the code to understand their meaning. This makes the code harder to read and understand. To avoid mental mapping, use clear and descriptive names that don't require any additional interpretation. This includes not making in-jokes within the code or needing to have read your favourite reddit to understand what a variable is doing.

Avoid vague words such as `thing`, acronyms, or single letter variables. For example:

```python
for i, fbt in enumerate(list_names):
	value = do_thing(fbt)
	print(f'Case {i} completed with {fbt} and output {value}')
```

Requires more context to know what is going on. You could use more descriptive names such as:

```python
for index, football_team in enumerate(football_premiership_teams):
	average_goals_per_game = calculate_goals_per_game(football_team)
	print(f'Team {index} completed with {football_team} and output {average_goals_per_game}')
```

>[!warning] Include units in the variable name
> You might know that all timestamps in your code are unix second timestamps. However you in 5 days or another coder might not. So instead of `start_time` why not `start_unix_timestamp_seconds`

## Be consistent

Consistency is key when naming classes, methods, and concepts in your code. Using a single word for an abstract concept and sticking to a naming convention for classes and methods ensures a better understanding of the code.

Choose one word for each abstract concept and use it consistently throughout your code. Having multiple words for the same concept can be confusing. For example, using `fetch`, `retrieve`, and `get` as equivalent methods in different classes can make it difficult to remember which method belongs to which class.

Class names should be nouns or noun phrases, such as `Customer`, `WikiPage`, `Account`, or `AddressParser`. Avoid using words like `Manager`, `Processor`, `Data`, or `Info` in class names, as they are less descriptive. A class name should not be a verb.

Method names should be verbs or verb phrases, like `postPayment`, `deletePage`, or `save`. Accessors, mutators, and predicates should be named for their value and prefixed with `get`, `set`, and `is`.

By maintaining consistency in your naming conventions, your code will be easier to read, understand, and maintain.

## Use solution and problem domain names

When naming variables, methods, and classes in your code, it's important to strike a balance between using solution domain names and problem domain names. This ensures that your code is both understandable to fellow programmers and accurately represents the real-world concepts it models.

### Solution Domain Names

Solution domain names come from computer science, algorithms, design patterns, and mathematics. They are familiar to programmers and help communicate the underlying structure and logic of your code. Don't shy away from using solution domain names, as they allow your colleagues to understand your code without needing to constantly ask for clarification.

For example, use names like `Singleton`, `Factory`, or `Observer` when implementing design patterns, or `QuickSort` and `BinarySearch` for algorithms.

### Problem Domain Names

Problem domain names come from the specific field or industry your software is addressing, like finance, healthcare, or e-commerce. They represent the real-world concepts and entities your software is modelling.

When there's no suitable solution domain name, use a problem domain name. This way, programmers who maintain your code can consult domain experts to understand the meaning behind these names.

For instance, if you're building a finance application, you might use names like `InterestRate`, `LoanAmount`, or `MortgageCalculator`.

By using both solution and problem domain names, your code will be more understandable and maintainable for your team, while also accurately representing the concepts and entities it models.

## Use the correct level of context

When naming variables, methods, and classes in your code, it's essential to use the appropriate level of context. Providing the right amount of context helps make your code more readable and understandable, while avoiding unnecessary confusion or verbosity.

In some cases, you may need to add context to your names to make them more meaningful. For example, if you have variables like `firstName`, `lastName`, `street`, `houseNumber`, `city`, `state`, and `zipcode`, it's clear they form an address when combined. However, when used individually, some variables might lose their context. To add context, you can use prefixes like `addrFirstName`, `addrLastName`, `addrState`, and so on.

On the other hand, adding too much context can make your names unnecessarily long and harder to read. When naming variables, methods, or classes, only include the necessary context to make the name clear and understandable. For example, if you're working within a `Customer` class, it's unnecessary to prefix every variable with `customer`, such as `customerName`, `customerEmail`, etc. Instead, use simpler names like `name` and `email`, as the context is already provided by the class.

Striking the right balance between context and readability is key. If a name is too short or lacks context, it becomes unclear and difficult to understand. If it's too long or includes too much context, it can be cumbersome and challenging to read.

## Don't be afraid to rename something

If something is named poorly and when you come to the code base you don't understand it. Rename that variable!

You should keep to the repositories standards but if you are worried about this, get the person who is maintaining this area to code review it and let them know in that why you are renaming it. (Worst case, you find out your understanding of the code was wrong.)
