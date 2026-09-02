import importlib
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_run_module_imports():
    sys.path.insert(0, str(REPO_ROOT))
    try:
        importlib.import_module("run")
    finally:
        sys.path.remove(str(REPO_ROOT))


def test_run_script_exits_cleanly():
    result = subprocess.run(
        [sys.executable, "run.py"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr
