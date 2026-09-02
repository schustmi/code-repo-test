# Plan: Add `word_count(text)` to `wc.py`

## Root cause

There is no word-counting utility in the repository. The repo currently
only contains `run.py` / `run2.py` (ZenML pipeline examples) and a
symlink; there is no `wc.py` or `test_wc.py`, and no test infrastructure
beyond `pytest` being available in the environment (`pytest` 9.1.1 is
installed, no `pytest.ini`/`pyproject.toml`/`setup.cfg` exists yet). This
is a net-new feature request, not a bug fix — the "root cause" is simply
that the function doesn't exist yet.

## Code changes

1. Create `wc.py` at the repository root with a single function:

   ```python
   def word_count(text: str) -> int:
       """Return the number of words in text."""
       return len(text.split())
   ```

   - Use `str.split()` with no arguments so it splits on any run of
     whitespace (spaces, tabs, newlines) and ignores leading/trailing
     whitespace, which matches the common-sense definition of "word
     count."
   - An empty string or a whitespace-only string returns `0` naturally
     since `"".split()` / `"   ".split()` both yield `[]`.
   - No third-party dependencies needed.

## Tests

2. Create `test_wc.py` at the repository root with pytest tests covering:
   - Basic case: `"hello world"` → `2`
   - Single word: `"hello"` → `1`
   - Empty string: `""` → `0`
   - Whitespace-only string: `"   "` → `0`
   - Multiple/irregular whitespace between words (tabs, multiple spaces,
     newlines): `"hello   world\tfoo\nbar"` → `4`
   - Leading/trailing whitespace: `"  hello world  "` → `2`

   Example structure:

   ```python
   from wc import word_count


   def test_word_count_basic():
       assert word_count("hello world") == 2


   def test_word_count_single_word():
       assert word_count("hello") == 1


   def test_word_count_empty_string():
       assert word_count("") == 0


   def test_word_count_whitespace_only():
       assert word_count("   ") == 0


   def test_word_count_irregular_whitespace():
       assert word_count("hello   world\tfoo\nbar") == 4


   def test_word_count_leading_trailing_whitespace():
       assert word_count("  hello world  ") == 2
   ```

## Verification

3. Run `pytest test_wc.py -v` from the repository root and confirm all
   tests pass.
