---
id: 001
title: Add a whisper helper
status: built
kind: guided
area: text helpers
critical: no
screen: no
commit: 1faf97e7e3807bac5221a2a7865f51ecea90dd21
screenshots: runs/20261116-032201/screenshots/001
branch: 
---

## What you will see
A new function `whisper(text)` in textkit.py that gives the text back in lower case.

## How we know it works
A new test in test_textkit.py checks that `whisper("HeLLo")` gives `"hello"`, and all tests pass with `python3 -m unittest -q`.

## What must not change
The existing `shout` function and its test.
