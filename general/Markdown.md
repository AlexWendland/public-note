---
created: 2023-02-24
last_edited: 2023-02-24
publish: true
tags: programming, language
type: tool
---
# Markdown

This is a [[Markup Language]] that is widely used, for example it is used in [[GitHub]] README pages and [[Obsidian]] notes. It has a fairly basic syntax, that I am going to have great fun describing in a [[Markdown]] file.

# Syntax
I am sure there is more, but this is what I have found useful so far!

| Format                | Syntax                                                                                  | Example                                              |
| --------------------- | --------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| Headings              | \# at the beginning of the line up to 6 characters.                                     | \#\# Title                                           |
| *Italic*              | \* or \_ wrapped around the statement                                                   | \*Italic\*                                           |
| **Bold**              | \*\* or \_\_ wrapped around the statement                                               | \*\*Bold\*\*                                         |
| ***Italic and Bold*** | \*\*\* or \_\_\_ wrapped around the statement                                           | \*\*\*Statement\*\*\*                                |
| Strike through        | \~\~ wrapped around the statement                                                       | \~\~statement\~\~                                    |
| Back quotes           | \> at the begining of the line, can be contined over multiple                           | \> important quote                                   |
| lists                 | \-, \* or \+ at the beginning of the line                                               | \- item                                              |
| Numbered lists        | 1., 7. a number then a dot at the start of the line[^1]                                 | 1. item                                              |
| Code blocks           | Put the code in \`\`                                                                    | \`\`Like this\`\`                                    |
| Links                 | Single square brackets on the linked text and then link in normal brackets              | \[test\]\(link\)                                     |
| Images/recall         | Put an ! before the square brackets to render the image or preview text                 | \!\[test\]\(link\)                                   |
| Horizontal line       | Use \_\_\_, \-\-\- or \*\*\* on an open line                                            | \_\_\_                                               |
| Adding titles         | In links to can add text in quotes in the link to make that a title                     | \[test\]\(link "This link"\)                         |
| Escape Characters     | The \\ allows you to put characters in text that have special meanings                  | \\\*test\\\*                                         |
| Tables                | Tables use \| and \-\-\- to separate columns and rows                                   | \| title1 \| title2\|\\n\|\-\-\-\|\-\-\-\|[^2]       |
| Alignment in tables   | This can be done using : on the side of the \-\-\- you want to align to                 | \| title1 \| title2\|\\n\|\:\-\-\-\|\:\-\-\-\:\|[^3] |
| Syntax highlighting   | Sometimes it can highlight syntax if it knows it using \`\`\` followed by the language  | \`\`\`json { "hi": "bye"}\`\`\`                      |
| Text highlighting     | \=\= wrapped around the statement                                                       | \=\=test\=\=                                         |
| Footnotes             | \[\^text\] at the point you want the foot note and \[\^text\]\: where you want the text | text\[\^1\] ... \[\^1\]: This is a foot note         |
| Tasks                 | Use unordered lists but put \[ \] after it or \[x\] to mark it done                | \- \[ \] or \- \[x\]                                                     |

[^1]: The numbers don't have to be in order!

[^2]: A larger example is here:
	\| title1 \| title2 \|
	\|\-\-\-\|\-\-\-\|
	\|row1 \| row2\|

[^3]: A larger example is here:
	\| right \| middle \| left \|
	\|\:\-\-\-\|\:\-\-\-\:\|\-\-\-\:\|
	\|right \| middle\| left \|
