import subprocess
import sys
from pathlib import Path

import healthcheck

ROOT = Path(__file__).resolve().parent.parent


def test_main_prints_ok(capsys):
    assert healthcheck.main() == 0
    assert capsys.readouterr().out == "ok\n"


def test_script_runs_and_exits_zero():
    result = subprocess.run(
        [sys.executable, "scripts/healthcheck.py"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert result.stdout == "ok\n"
