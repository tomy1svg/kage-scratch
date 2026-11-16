---
id: 001
title: Add a whisper helper
status: todo
kind: guided
area: text helpers
critical: no
screen: no
---

## What you will see
A new function `whisper(text)` in textkit.py that gives the text back in lower case.

## How we know it works
A new test in test_textkit.py checks that `whisper("HeLLo")` gives `"hello"`, and all tests pass with `python3 -m unittest -q`.

## What must not change
The existing `shout` function and its test.
