---
aliases: [naming variables]
type: notation
publish: true
created: 2023-03-18
last_edited: 2023-03-18
tags: programming
---
# Naming conventions

When coding we repeatedly have to name things. So having some go to standards for how to do this makes writing code quickly but it easier to read. The key thing is for the name to be fully expansive about what the variable is doing, if you can't do this maybe this variable is doing too much.

> [!quote] [[Clean Code]]
> One difference between a smart programmer and a professional programmer is that the professional understands that clarity is king. Professionals use their powers for good and write code that others can understand.

These are the following principles I try to follow:
- [[Naming conventions#Use intention-revealing names|Use intention-revealing names]]
- [[Naming conventions#Don't include the type in the name|Don't include the type in the name]]
- [[Naming conventions#No two names should look a like|No two names should look a like]]
- [[Naming conventions#Use pronounceable names|Use pronounceable names]]
- [[Naming conventions#Avoid mental mappings|Avoid mental mappings]]
- [[Naming conventions#Be consistent|Be consistent]]
- [[Naming conventions#Use solution and problem domain names|Use solution and problem domain names]]
- [[Naming conventions#Use the correct level of context|Use the correct level of context]]
- [[Naming conventions#Don't be afraid to rename something|Don't be afraid to rename something]]

## Use intention-revealing names

>[!quote] [[Clean Code]]
>The name of a variable, function, or class, should answer all the big questions. It should tell you why it exists, what it does, and how it is used.

Using intention-revealing names is easier when you adhere to the [[Single Responsibility Principle (SRP)]].

Here's an example to illustrate the concept:
```python
# Unclear variable name
d = 86400

# Intention-revealing variable name
seconds_in_a_day = 86400
```

In this example, `d` doesn't reveal its purpose, while `seconds_in_a_day` clearly indicates what the variable represents.

Remember this heuristic to evaluate if you've chosen a good name:

> [!quote] [[Clean Code]] 
> If a name requires a comment, then the name does not reveal its intent.

## Don't include the type in the name

As a [[Python]] programmer working in [[Data]], it's tempting to include data types in variable names, such as `df_football_results_data`. 

There are several reasons to avoid this practice:

1.  **Redundancy**: Variable names should be indicative of their structure. If you have `football_results`, it's likely you would store it in a DataFrame anyway, so specifying the type is unnecessary.
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
    -   Example: `XYZControllerForEfficientHandlingOfStrings` and `XYZControllerForEfficientStorageOfStrings`
2.  **Numbers or noise words**: Adding numbers or noise words to variable names can make it difficult to differentiate between them.
    -   Example: `data1` and `data2` or `the_data`
3.  **Similar suffixes**: Using words with similar meanings at the end of variable names can cause confusion.
    -   Example: `ProductInfo` and `ProductData`

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

## Be consistent

Use noun or noun phrases for class names and verb or verb phrases for method names.

## Use solution and problem domain names

Use computer science terms and pattern names when appropriate, and problem domain names when there's no suitable "programmer-eese" term.

## Use the correct level of context

## Don't be afraid to rename something

If something is named poorly and when you come to the code base you don't understand it. Rename that variable!

You should keep to the repositories standards but if you are worried about this, get the person who is maintaining this area to code review it and let them know in that why you are renaming it. (Worst case, you find out your understanding of the code was wrong.)
