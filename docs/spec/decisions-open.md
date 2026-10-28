# Open Decisions

This document tracks all design and implementation decisions requiring user feedback or explicit approval.

## Decision Log

All architecture, naming, packaging, runtime, and transport parameters for Phase 2A were fixed prior to specification writing:
- Name: `arale-code`
- Python package: `arale_code`
- Console command: `arale-code`
- Runtime: Python 3.12 (`>=3.12,<3.13`)
- Dependencies: `fastmcp>=4.1,<4.2`, `PyYAML>=6.0,<7`
- Tooling: `uv`, `ruff`, `mypy`, `pytest`, `pytest-asyncio`, `uv_build`
- Transport: STDIO only, read-only, stateless, offline
- Procedure IDs: `p01` through `p20` plus `guide`
- Instruction documents: `design-spec`, `implementation-plan`, `code-quality`, `testing`
- Line endings: LF
- Asset counts: 4 instruction Markdown files, 21 procedure YAML files (0 occurrences of old name in YAML text)

---

## Phase 2B Items

### Item 1: Skill Distribution Packaging
- **Question**: Should the `arale` agent skill folder be distributed primarily as a source folder inside the repository (e.g. `<REPO_ROOT>/skills/arale/SKILL.md`) copied during install, or should it additionally be packaged and bundled inside Python package data or an optional release zip artifact?
- **Resolution**: `skills/arale/` stays in the repository and is copied at install; INSTALL.md states "after every repository update, repeat the skill copy".
- **Status**: CLOSED by user.

---

## Phase 2C Open Items

### Item 2: Virtual Environment Exclusion and Lockfile Tracking
- **Question**: Confirm that `.venv/` is listed in `.gitignore` and `uv.lock` is committed to git tracking?
- **Current Assessment**: In repository layout and gitignore specification, `.venv/` must be ignored to prevent committing local virtual environment binaries, and `uv.lock` must be committed to guarantee deterministic dependency resolution.
- **Status**: DECISION NEEDED.
