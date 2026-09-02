# Plan: Add `slugify(text)` to `slug.py`

## Root cause

There is no bug to fix — this is a net-new feature request. The repository
currently contains no `slug.py`, no `test_slug.py`, and no test
infrastructure at all (no `pytest.ini` / `pyproject.toml` / `conftest.py`).
`pytest` (9.1.1) is available in the environment, so a bare test file at the
repo root is sufficient to run with `pytest`.

## Code changes

1. **Create `slug.py`** at the repository root with a single public function:

   ```python
   import re


   def slugify(text: str) -> str:
       """Lower-case text and collapse runs of non-alphanumeric chars into single dashes."""
       text = text.lower()
       text = re.sub(r"[^a-z0-9]+", "-", text)
       return text.strip("-")
   ```

   Design notes:
   - Use `re.sub(r"[^a-z0-9]+", "-", text)` after lower-casing so *runs* of
     one or more non-alphanumeric characters collapse to a *single* dash
     (satisfies "replaces runs ... with single dashes").
   - Strip leading/trailing dashes produced when the input starts/ends with
     non-alphanumeric characters (e.g. `" Hello World! "` → `hello-world`,
     not `-hello-world-`). This matches common slugify semantics; call this
     out as a design choice in the PR description since the issue doesn't
     specify edge-of-string behavior.
   - Only ASCII alphanumerics are treated as "alphanumeric" (matches typical
     slug usage); no unicode/transliteration handling is required by the
     issue.

2. **No changes needed to `run.py` / `run2.py` / `sym2`** — unrelated ZenML
   pipeline scaffolding, not part of this feature.

## Tests to add (`test_slug.py`, repo root)

Use plain `pytest` (no extra fixtures/config needed):

```python
from slug import slugify


def test_lowercases_text():
    assert slugify("HELLO") == "hello"


def test_replaces_single_non_alphanumeric_char():
    assert slugify("hello world") == "hello-world"


def test_collapses_runs_of_non_alphanumeric_chars():
    assert slugify("Hello   World!!!") == "hello-world"


def test_mixed_punctuation_and_whitespace():
    assert slugify("Hello, World -- Foo_Bar") == "hello-world-foo-bar"


def test_strips_leading_and_trailing_dashes():
    assert slugify("  Hello World!  ") == "hello-world"


def test_preserves_numbers():
    assert slugify("Room 42B") == "room-42b"


def test_empty_string():
    assert slugify("") == ""


def test_only_non_alphanumeric_characters():
    assert slugify("!!!") == ""
```

## Verification steps

1. `python -m pytest test_slug.py -v` — all new tests pass.
2. Manually sanity-check a couple of examples via `python -c "from slug import slugify; print(slugify('Hello, World!'))"`.
