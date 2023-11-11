---
aliases:
  - imperative programming
  - Imperative language
  - imperative language
checked: false
created: 2023-02-24
last_edited: 2023-07-14
publish: true
tags: programming, language
type: paradigm
---
# Imperative Programming

In this paradigm the language specifies a series of instructions to potentially get to an end state (*cough* [[Holting Problem]] *cough*). Lots of peoples first programs are imperative.

```python
letters = ["a","B","C","d"]
output = []

for letter in letters:
	if letter.lower() == letter:
		output.append(letter)

print(output) # ["a", "b"]
```

Here you provide the machine exact steps to what has to be done to produce the output.

There is a sub category of this called [[Procedural Programming]] that uses this with [[Function conventions|functions]].

## Advantages

- Efficient,
- Emulates low level languages,

# Disadvantages

-
