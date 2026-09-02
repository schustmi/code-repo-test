# Plan: Add `count_vowels(text)` to `vowels.py` with pytest coverage

## Root cause

This is a feature request, not a bug fix — there is no root cause to diagnose.
The repository currently contains no `vowels.py` module and no test suite at
all (only `run.py`, `run2.py`, a symlink `sym2`, and `.gitignore` at the repo
root; no `tests/` directory, no `pytest.ini`/`pyproject.toml` test config).
The task is simply to add the missing module and its test file from scratch,
at the repository root, matching the flat layout the repo already uses for
`run.py`/`run2.py`.

## Code changes

1. **Create `vowels.py`** at the repository root with a single function:

   ```python
   def count_vowels(text: str) -> int:
       """Return the number of vowels (a, e, i, o, u, case-insensitive) in text."""
       return sum(1 for char in text.lower() if char in "aeiou")
   ```

   Design notes:
   - Case-insensitive matching (`'A'` and `'a'` both count).
   - Only count `a, e, i, o, u` — do not count `y`, since the issue doesn't
     mention it and "vowel" without qualification conventionally excludes `y`.
   - No special handling needed for empty strings or non-letter characters —
     the generator expression naturally returns `0` for them without extra
     branching.

2. **Create `test_vowels.py`** at the repository root (co-located with
   `vowels.py`, consistent with the flat repo layout), importing and testing
   `count_vowels`.

## Tests to add (`test_vowels.py`)

Use plain `pytest` functions (no unittest classes), matching the pytest
version already installed (`pytest==9.1.1`, confirmed via `pip show pytest`).

- `test_count_vowels_basic`: `count_vowels("hello world") == 3`
- `test_count_vowels_all_vowels`: `count_vowels("aeiou") == 5`
- `test_count_vowels_no_vowels`: `count_vowels("xyz") == 0`
- `test_count_vowels_empty_string`: `count_vowels("") == 0`
- `test_count_vowels_case_insensitive`: `count_vowels("AEIOU") == 5` and a
  mixed-case sentence, e.g. `count_vowels("Hello World") == 3`
- `test_count_vowels_with_punctuation_and_numbers`: e.g.
  `count_vowels("Testing 1, 2, 3!") == 3` — confirms non-letter characters
  are simply ignored.

Consider `@pytest.mark.parametrize` to combine these cases into one compact
test function instead of several near-duplicate ones, e.g.:

```python
import pytest
from vowels import count_vowels


@pytest.mark.parametrize(
    "text, expected",
    [
        ("hello world", 3),
        ("aeiou", 5),
        ("AEIOU", 5),
        ("xyz", 0),
        ("", 0),
        ("Hello World", 3),
        ("Testing 1, 2, 3!", 3),
    ],
)
def test_count_vowels(text, expected):
    assert count_vowels(text) == expected
```

## Verification

- Run `pytest test_vowels.py -v` from the repository root and confirm all
  cases pass.
