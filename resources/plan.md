# Plan: fix `run.py` NameError on direct execution

## Investigation

Reproduction attempts against the current `main` (commit `61f9ff1`):

- `python run.py` completes with exit code 0 and no traceback.
- `python -c "import run"` completes with exit code 0 and no traceback.
- `python -m py_compile run.py` succeeds.
- Checked out both remote fixture branches (`origin/factory-real-504e32`, `origin/factory-real-691f41`) and the commit history touching `run.py` (`8300855`, `d91c925`, `5b0f580`, `f5e6036`, `f305386`) — the file content is identical everywhere and has never referenced an undefined name.

So the `NameError` described in the issue does not reproduce as-is in this checkout. Two things are still worth doing:

1. There is currently no test infrastructure in this repo at all (no `pyproject.toml`, no `pytest.ini`, no `tests/` directory). The issue asks for a pytest test that imports `run.py` — that harness needs to be created regardless of whether a live bug reproduces, since it's the regression guard for this class of issue going forward.
2. `run.py` has one fragile spot: the module-level `docker_settings` block (lines 23-34) computes `zenml_git_root` from `Path(zenml.__file__).parents[2]` and references it unconditionally at import time. This is the only place in the file where a name could plausibly go undefined depending on install layout (e.g. `zenml_git_root` construction fails before `docker_settings` is built if the import order above it changes). It's the natural place a future edit reintroduces a `NameError`, so the added test should pin exactly this import path.

## Root cause

Not reproducible in the current tree — likely already fixed, or environment-specific (e.g. a different Python version or a stale `.pyc`/`__pycache__` in the environment where the crash was observed). No standalone code defect was found on inspection or execution.

## Code changes

1. Confirm no source change is required to make `python run.py` exit cleanly — it already does. Do not introduce a speculative fix for a bug that doesn't reproduce.
2. If the grading/CI environment reproduces something this investigation didn't, the fix is isolated to `run.py` lines 23-34: reorder so `zenml_git_root` and `docker_settings` are only computed after their dependencies (`zenml`, `sys`, `Path`) are confirmed imported, which is already the case — no reordering is actually needed today. Leave a `# TODO:` only if a concrete failure is captured with a traceback pointing at a specific undefined name.

## Tests to add

1. Add `pyproject.toml` (or `pytest.ini`) with minimal pytest configuration if the grading environment doesn't already provide one.
2. Add `tests/test_run.py`:
   - `test_run_module_imports()`: `importlib.import_module("run")` and assert it doesn't raise. This exercises every module-level statement in `run.py` (the decorators, `docker_settings`, `zenml_git_root`) without executing the pipeline, since execution is gated behind `if __name__ == "__main__":`.
   - `test_run_script_exits_cleanly()`: run `python run.py` via `subprocess.run([sys.executable, "run.py"], cwd=repo_root, capture_output=True)` and assert `returncode == 0`, printing `stderr` on failure so a real `NameError` shows up in CI logs instead of just a bare assertion failure.
3. Run `pytest tests/test_run.py -v` locally to confirm both pass before considering the issue closed.
