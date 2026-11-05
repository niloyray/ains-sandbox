# Feature Specification: Version command

**Story**: AINSSB-3 — Version command: print the package version from pyproject.toml
**Status**: Draft

## Goal

Give developers and scripts a one-line command that reports the project's current version, using `pyproject.toml` as the single source of truth so the number never drifts from the package metadata.

## User-visible behaviour

- Running `python scripts/version.py` prints the value of the `version` field in `pyproject.toml` (currently `0.1.0`) as a single line on standard output, then exits with status 0.
- The output contains only the version string plus a trailing newline: no label, prefix or extra text.
- The README has a "Version" section showing this one-line command.

## Acceptance criteria

- [ ] `scripts/version.py` exists and prints exactly one line: the `version` value from `pyproject.toml`.
- [ ] The command exits with status 0 on success.
- [ ] A pytest test under `tests/` runs the script and asserts its printed value equals the version read from `pyproject.toml`.
- [ ] `README.md` has a section titled "Version" containing the one-line command.
- [ ] The script uses only the Python standard library; no dependency is added to `pyproject.toml`.
- [ ] `uv run pytest` and `uv run ruff check .` pass.

## Out of scope

- Bumping or editing the version, or any release tooling.
- Reading the version from installed package metadata or from anywhere other than `pyproject.toml`.
- Command-line flags, alternative output formats, or a packaged console entry point.
- Changes to CI or to anything under `.github/`, `.specify/` or `.claude/`.

## Open questions

- None blocking. Assumed: the script is run from the repository root, and it finds `pyproject.toml` relative to its own location, so the working directory does not matter.
- Assumed: if `pyproject.toml` or its `version` field is missing, the script exits non-zero with a message on stderr. The story does not specify this case, so it is not an acceptance criterion.
