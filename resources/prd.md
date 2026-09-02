# PRD: `shout` function

## Problem

There is no utility function for transforming text into an emphatic, upper-cased form with a trailing exclamation mark. Callers who want this behavior have to write it inline, ad hoc, wherever it's needed.

## Desired behavior

Add a function `shout(text)` in `shout.py` at the repository root. It takes a string and returns that string upper-cased with an exclamation mark appended.

Example:
- `shout("hello")` returns `"HELLO!"`
- `shout("Already Loud")` returns `"ALREADY LOUD!"`

Add a corresponding pytest test suite in `test_shout.py` at the repository root that verifies this behavior.

## Acceptance criteria

- `shout.py` defines a function `shout(text)` that returns `text.upper() + "!"`.
- `test_shout.py` contains at least one pytest test that calls `shout` with a sample string and asserts the returned value is upper-cased with `!` appended.
- Running `pytest test_shout.py` passes.
