# Plan: Add `truncate(text, max_length)` utility

## Root cause / context

This is a feature request, not a bug fix — the repository currently contains
only two ZenML pipeline example scripts (`run.py`, `run2.py`) and a symlink
(`sym2`). There is no `truncate.py`, no `test_truncate.py`, and no existing
test infrastructure (no `pytest.ini` / `pyproject.toml` / `requirements.txt`).
`pytest` (9.1.1) is available in the environment, so tests can be added and
run with a plain `pytest` invocation from the repo root.

Because there's no existing package structure to fit into, both files will
be created as new, standalone top-level modules at the repo root, following
the naming the issue specifies.

## Code changes

1. **Create `truncate.py`** at the repo root with a single function:

   ```python
   def truncate(text: str, max_length: int) -> str:
       """..."""
   ```

   Behavior:
   - If `len(text) <= max_length`, return `text` unchanged (no ellipsis
     appended).
   - If `len(text) > max_length`, cut the text down and append an ellipsis
     (`"..."`) such that the **total returned length equals `max_length`**
     (i.e. truncate to `max_length - 3` characters of original text, then
     add `"..."`). This is the conventional definition of "truncate to N
     chars with ellipsis" and avoids the result exceeding `max_length`.
   - Edge case: if `max_length` is small (e.g. `<= 3`), truncating to
     `max_length - 3` would be negative/zero. Handle this by clamping — if
     `max_length <= 3`, just return `"."[:max_length]`-style truncated
     ellipsis (i.e. the first `max_length` characters of `"..."`), so the
     result never exceeds `max_length` and never raises.
   - Validate `max_length` is a non-negative int; raise `ValueError` if
     negative (defensive boundary check since this is a public utility
     function with an external-ish contract).

2. No changes needed to other files — this is an additive, self-contained
   utility with no integration points in the current codebase.

## Tests to add

Create **`test_truncate.py`** at the repo root using `pytest`, importing
`from truncate import truncate`. Cases:

1. `test_no_truncation_when_shorter` — text shorter than `max_length` is
   returned unchanged, no ellipsis appended.
2. `test_no_truncation_when_equal` — text exactly `max_length` long is
   returned unchanged.
3. `test_truncates_and_appends_ellipsis` — text longer than `max_length`
   is cut and ends with `"..."`; assert the returned string's length
   equals `max_length` and it starts with the expected prefix of the
   original text.
4. `test_truncate_result_length_never_exceeds_max_length` — parametrized
   over several `(text, max_length)` pairs to confirm
   `len(truncate(text, max_length)) <= max_length` always holds.
5. `test_small_max_length_edge_case` — `max_length` smaller than the
   ellipsis length (e.g. `0`, `1`, `2`, `3`) still returns a string no
   longer than `max_length` without raising.
6. `test_empty_string` — `truncate("", max_length)` returns `""`.
7. `test_negative_max_length_raises` — calling with a negative
   `max_length` raises `ValueError`.

## Steps

1. Add `truncate.py` implementing `truncate(text, max_length)` per the
   behavior above.
2. Add `test_truncate.py` with the pytest cases listed above.
3. Run `pytest test_truncate.py -v` from the repo root and confirm all
   tests pass.
4. (Optional/no-op here) No other files reference truncation logic, so no
   further integration changes are required.
