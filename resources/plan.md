# Plan: Add `reverse_words(text)` to `words.py`

## Root cause

There is no `words.py` or `test_words.py` anywhere in the repository. This
repo currently only contains `run.py`, `run2.py`, and a symlink `sym2`, all
unrelated ZenML pipeline scratch scripts. There is no existing test setup
(no `pytest` config, no `tests/` directory, no test dependencies declared).
The issue asks for a new, self-contained utility function plus a test for
it, so this is pure net-new code, not a bug fix.

## Code changes

1. Create `words.py` at the repository root with a single function:

   ```python
   def reverse_words(text: str) -> str:
       """Reverse the order of words in the text."""
       return " ".join(text.split()[::-1])
   ```

   - Use `str.split()` with no arguments so consecutive/leading/trailing
     whitespace is collapsed and normalized (matches typical "reverse the
     words" semantics).
   - Join reversed words with a single space, returning a `str`.
   - Empty string / whitespace-only input returns `""`.

2. Create `test_words.py` at the repository root with `pytest` test
   functions covering:
   - Basic multi-word sentence reversal (e.g. `"hello world"` ->
     `"world hello"`).
   - Single word (returned unchanged).
   - Empty string input (returns `""`).
   - Input with extra/irregular whitespace between words (verifies
     whitespace normalization).

## Tests to add

In `test_words.py`:

```python
from words import reverse_words


def test_reverse_words_multiple():
    assert reverse_words("hello world foo") == "foo world hello"


def test_reverse_words_single_word():
    assert reverse_words("hello") == "hello"


def test_reverse_words_empty_string():
    assert reverse_words("") == ""


def test_reverse_words_extra_whitespace():
    assert reverse_words("  hello   world  ") == "world hello"
```

## Verification

Run `pytest test_words.py` from the repository root to confirm all new
tests pass.
