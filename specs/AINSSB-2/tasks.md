# Tasks: Repository scaffold: README section and health-check script

**Input**: [spec.md](spec.md), [plan.md](plan.md). Do not touch `.github/`, `.specify/`, `.claude/`, `CLAUDE.md`.

## Phase 1: Setup

- [ ] T001 Create `pyproject.toml` with `[project]` (name `ains-sandbox`, version `0.1.0`, `requires-python = ">=3.12"`, no runtime deps), `[dependency-groups] dev = ["pytest"]` (pytest only), and `[tool.pytest.ini_options]` with `pythonpath = ["scripts"]` and `testpaths = ["tests"]`. Files: `pyproject.toml`

## Phase 2: User Story 1 - Run the health check (P1)

- [ ] T002 [US1] Write the test first: `tests/test_healthcheck.py` with `import healthcheck`; one test using `capsys` asserting `main() == 0` and stdout == `"ok\n"`; one test running `sys.executable scripts/healthcheck.py` via `subprocess` from the repo root asserting returncode 0 and stdout `"ok\n"`. Files: `tests/test_healthcheck.py`
- [ ] T003 [US1] Implement `scripts/healthcheck.py`: `main() -> int` prints `ok`, returns 0; `if __name__ == "__main__": sys.exit(main())`; stdlib only, no env vars, no other output. Files: `scripts/healthcheck.py`
- [ ] T004 [P] [US1] Add a `## Health check` section to the README with the run command, expected output `ok`, exit status 0, how to run tests (`uv run pytest`) and lint (`uvx ruff check .`). Files: `README.md`

## Phase 3: User Story 2 - Test runs in CI (P2)

- [ ] T005 [US2] Verify the output-change guard: temporarily alter the printed text, confirm `uv run pytest` fails, then revert. Files: `scripts/healthcheck.py` (no net change)
- [ ] T006 [US2] Run `uv run pytest` from the repo root in a clean environment and confirm all tests pass (riskiest: uv handling of the non-packaged project). Files: none (may create untracked `uv.lock`, `.venv/`)
- [ ] T007 [US2] Run `uvx ruff check .` and fix any findings in the new files. Files: `scripts/healthcheck.py`, `tests/test_healthcheck.py`

## Phase 4: Final check

- [ ] T008 Confirm `git status` shows only `README.md`, `pyproject.toml`, `scripts/healthcheck.py`, `tests/test_healthcheck.py` (and optionally `uv.lock`) changed, with no secrets and no edits to protected paths. Files: none
