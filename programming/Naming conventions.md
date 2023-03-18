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

These are the following principles I try to follow:
- [[Naming conventions#Use intention-revealing names|Use intention-revealing names]]
- [[Naming conventions#Don't include the type in the name|Don't include the type in the name]]
- [[Naming conventions#No two names should look a like|No two names should look a like]]
- 

## Use intention-revealing names

>[!quote] [[Clean Code]]
>The name of a variable, function, or class, should answer all the big questions. It should tell you why it exists, what it does, and how it is used.

This should be easy to do as long as you have followed the [[Single Responsibility Principle (SRP)]]. 

Following is a nice heuristic to see if you have succeeded.

>[!quote] [[Clean Code]]
>If a name requires a comment, then the name does not reveal its intent.

## Don't include the type in the name

Being predominantly a [[Python]] programmer working in [[Data]] it is awfully tempting to call something `df_football_results_data` here are some reasons to do this:
- The variable name should be indicative of what structure it is in.
	- `df_football_results_data` if it was `football_results` would you not keep this in a data frame anyway? 
- It makes the variable name harder to understand
	- `write_to_cloud_boolean` do we have a storage account with the provider boolean or is this variable a boolean?
- If you don't keep the standard of including the type in the name, it can lead to disinformation.
	- If you have been using types in the variables names then someone else names something `accounts_list` but you actually using a dictionary to key accounts to their holdings. This could lead to a surprise if someone else were to edit the code base.
- It can make it harder to find the variable in the IDE's suggestions.
	- Got lots of data frames, it is going to take 3 extra clicks to find the variable you want.
- It makes variable names even longer than they have to be.

You might want to do it for the following reason:
- It makes the type easy to find without having to look through my code.
	- This is a red flag that your code is too long and it is working on too many different levels of abstraction.

## No two names should look a like

This makes your code far easier to read, if they all have a different shape or ideally use very distinct words then it is far easier to scan. Similar names can occur in a number of ways that we should avoid:

- Two names that look very similar due to a long prefix.
	- e.g. `XYZControllerForEfficientHandlingOfStrings` and `XYZControllerForEfficientStorageOfStrings`
- Adding numbers or noise words to variable names.
	- e.g. `data1` and `data2` or `data_left` `data_right`
- Using similar meaning words at the end.
	- e.g. `ProductInfo` and `ProductData`