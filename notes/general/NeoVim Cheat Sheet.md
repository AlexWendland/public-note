---
aliases: 
checked: false
created: 2024-03-08
last_edited: 2024-03-08
draft: false
tags:
  - personal
type:
---
# NeoVim Cheat Sheet

Every NeoVim set up is personal, I am using my website it document how I have it set up - not universally true. :) 

## Basics

- Normal mode: Esc
- Beginners guide: :Tutor
- Edit setup: :e $MYVIMRC
- Quit: :q! or :wq (with save)
- Delete letter: x
- Insert text: i / a
- Delete text: d *motion*
	- Everything deleted goes into a buffer for put.
- Delete whole line: dd
- Undo: u
- Undo all changes to one line: U
- Put: p/P (after/before)
- replace: r/R (R is for multiple characters)
- Change: c *motion* (deletes and puts you in edit mode)
- Move to line number: *number* G (defaults to end of file)
- Move to start of file: gg
- Search: / *search word* (n/N to go through options)
- Back: C-o
- Forward: C-i
- Switch to match parenthesis: %
- Replace: :s/old/new/g
- Replace between line number n,m : :n,ms/old/new/g
- Replace in whole file: :%s/old/new/g(c) (c allows you to decide)
- External commands: :!
- Save as: :w
- Visual selector: v
- Retrieve: :r
- Open/insert new line: o/O (below/above)
- Copy: y *motion* (use in visual mode too)
- Set an option: :set
- Edit different file: :e
## Motions
- Start of the next word: w
- End of current word: e
- End of line: $
- Start of line: 0
- Use numbers to do it multiple times.
## Lazy
- Directory tree: leader e
	- Help: ?
	- New file: a
	- 
- Search in files: leader s g
- Switch colour scheme: leader u C
- Search key maps: leader s k
- Search and replace: leader s r
	- accept: leader s r
	- reject: dd
	- accept all: leader R
- Lazygit: leader gg
