# Implementation plan: `shout` function

## Steps

1. Create `shout.py` at the repository root with a single function:
   ```python
   def shout(text):
       return text.upper() + "!"
   ```

2. Create `test_shout.py` at the repository root:
   - Import `shout` from `shout`.
   - Add a test function `test_shout` that calls `shout("hello")` and asserts the result equals `"HELLO!"`.
   - Add a second test case with mixed-case input (e.g. `shout("Already Loud")` equals `"ALREADY LOUD!"`) to cover the example from the PRD.

3. Run `pytest test_shout.py` from the repository root and confirm it passes.

## Files touched

- `shout.py` (new)
- `test_shout.py` (new)
