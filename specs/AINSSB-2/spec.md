# Feature Specification: Repository scaffold: README section and health-check script

**Feature Branch**: `AINSSB-2-repository-scaffold-readme-section-and-h`
**Created**: 2026-11-02
**Status**: Draft
**Input**: Story AINSSB-2 — add a "Health check" README section, a `scripts/healthcheck.py` that prints "ok" and exits 0, a pytest test for it, and a `pyproject.toml` with pytest as the only dev dependency.

## Goal

Give the repository a minimal, runnable scaffold: a trivial health-check script, a test that proves it works, and the project metadata CI needs to run that test. No web framework.

## User-visible behaviour

- A contributor reads the "Health check" section in `README.md` and learns how to run the health check.
- Running the script prints `ok` (followed by a newline) to standard output and exits with status 0.
- Running `uv run pytest` from the repository root discovers and passes a test that imports the script and asserts its output.
- CI can install the project's dev dependencies from `pyproject.toml` and run the test.

## User Scenarios & Testing

### User Story 1 - Run the health check (Priority: P1)

A developer wants a quick confirmation that the repository's tooling works.

**Independent Test**: Run the script and check its output and exit status.

**Acceptance Scenarios**:

1. **Given** a fresh clone, **When** the developer runs the script as documented in the README, **Then** `ok` is printed and the exit status is 0.

### User Story 2 - Test runs in CI (Priority: P2)

CI must have a test to run and the metadata to install its dependency.

**Independent Test**: In a clean environment, install dev dependencies and run `uv run pytest`.

**Acceptance Scenarios**:

1. **Given** `pyproject.toml` declares pytest as the only dev dependency, **When** the test suite runs, **Then** the health-check test passes.
2. **Given** the script's output were changed, **When** the suite runs, **Then** the test fails.

### Edge Cases

- The test must work when run from the repository root, without requiring `scripts/` to be installed as a package (import mechanism is a plan-stage decision).
- The script must print nothing besides `ok` and must not require any environment variables.

## Requirements

### Functional Requirements

- **FR-001**: `README.md` MUST contain a section titled "Health check" that states the command to run the health check and the expected output (`ok`, exit status 0).
- **FR-002**: `scripts/healthcheck.py` MUST print `ok` and exit with status 0.
- **FR-003**: A pytest test under `tests/` MUST import the script and assert the printed output.
- **FR-004**: `pyproject.toml` MUST exist and declare pytest as the only dev dependency.
- **FR-005**: The change MUST NOT introduce a web framework or any other runtime or dev dependency.
- **FR-006**: The change MUST NOT touch `.github/`, `.specify/`, `.claude/` or `CLAUDE.md`, and MUST contain no secrets.

## Success Criteria

- **SC-001**: A new contributor can follow the README section and see `ok` in under one minute.
- **SC-002**: `uv run pytest` passes with zero failures; `uv run ruff check .` reports no issues.
- **SC-003**: The `ci` check is green on the story's PR.

## Acceptance Criteria

- [ ] README.md has a "Health check" section with run instructions and expected output
- [ ] `scripts/healthcheck.py` prints `ok` and exits 0
- [ ] A test under `tests/` imports the script and asserts the output
- [ ] `pyproject.toml` lists pytest as the only dev dependency
- [ ] `uv run pytest` passes
- [ ] `uv run ruff check .` is clean
- [ ] No web framework or extra dependencies added

## Out of Scope

- Any web server, HTTP endpoint, or framework.
- Real health probing (dependencies, network, disk, database).
- Application code under `app/`, Docker, release, or CI workflow changes.
- Linters or other dev dependencies beyond pytest declared in `pyproject.toml`.

## Assumptions

- The script is run as `python scripts/healthcheck.py` (or via `uv run`), from the repository root.
- Python and `uv` are available to developers and CI.

## Open Questions

- `CLAUDE.md` asks for `uv run ruff check .`, but the story says pytest is the *only* dev dependency. Should ruff be run via `uvx ruff` / left to CI, or added as a second dev dependency? (Default assumed: follow the story, pytest only; ruff is not declared.)
- Which minimum Python version should `pyproject.toml` declare? (Default assumed: a currently supported 3.x, chosen at plan stage.)
