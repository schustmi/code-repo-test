# Plan: Add `is_palindrome(text)` with pytest coverage

## Root cause

This is a feature request, not a bug fix — there is no `palindrome.py` or any
palindrome-related code anywhere in the repository (confirmed via a full
recursive search for `*palindrome*`). The repo currently only contains two
unrelated ZenML pipeline example scripts (`run.py`, `run2.py`) at the root,
plus a symlink (`sym2`). There is also no existing test suite, `pytest`
config (`pytest.ini` / `pyproject.toml` / `setup.cfg`), or dependency
manifest in the repo, so both the implementation and its test need to be
created from scratch, and `pytest` must be available in the environment
used to run the new test.

## Files to add

Both new files go at the repository root, next to `run.py`/`run2.py`, since
that's the only convention this repo currently has (flat scripts, no `src/`
layout or package).

### 1. `palindrome.py`

Add a single public function:

```python
def is_palindrome(text: str) -> bool:
    """Return True if text is a palindrome, ignoring case and spaces."""
    normalized = text.replace(" ", "").lower()
    return normalized == normalized[::-1]
```

Notes on behavior to preserve:
- Ignores case (`"Racecar"` → palindrome).
- Ignores spaces only, per the issue wording (not all whitespace/punctuation —
  keep scope limited to what was asked).
- Empty string and single-character strings are trivially palindromes.

### 2. `test_palindrome.py`

Add a pytest test module at the repo root that imports `is_palindrome` from
`palindrome` and covers:

- `assert is_palindrome("racecar") is True` — plain palindrome.
- `assert is_palindrome("RaceCar") is True` — mixed case.
- `assert is_palindrome("nurses run") is True` — spaces ignored.
- `assert is_palindrome("A man a plan a canal Panama") is True` — case + spaces combined.
- `assert is_palindrome("hello") is False` — non-palindrome.
- `assert is_palindrome("") is True` — empty string edge case.
- `assert is_palindrome("a") is True` — single character edge case.

Can be written either as individual `assert` statements in one test function
or via `@pytest.mark.parametrize` over `(text, expected)` pairs — parametrize
is preferable for readability given the number of cases.

## Steps

1. Create `palindrome.py` at repo root with the `is_palindrome` implementation above.
2. Create `test_palindrome.py` at repo root with the pytest cases above.
3. Run `pytest test_palindrome.py -v` from the repo root and confirm all cases pass.
4. If `pytest` is not installed in the environment, install it (e.g. `pip install pytest`) before running step 3 — no repo dependency manifest currently references it, so no manifest update is needed unless the project later adds one.
