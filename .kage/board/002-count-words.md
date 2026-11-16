---
id: 002
title: Add a word counter
status: todo
kind: guided
area: text helpers
critical: no
screen: no
---

## What you will see
A new function `count_words(text)` in textkit.py that gives the number of words in the text, where words are separated by any white space.

## How we know it works
New tests in test_textkit.py check that `count_words("one two  three")` gives 3 and `count_words("")` gives 0, and all tests pass with `python3 -m unittest -q`.

## What must not change
The existing functions and their tests.
