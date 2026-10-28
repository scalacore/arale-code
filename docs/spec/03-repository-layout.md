# Repository Layout

This document records the clean distribution tree. The original development
workspace has a broader layout covering historical plans, research, fixtures,
diagnostics and raw trial evidence. Those paths are not part of this copy.
Only paths listed below may be created in this distribution, subject to the
active user task. Routine documentation and packaging maintenance is allowed
when the task names those files; it does not authorize client configuration,
deployment or release.

## Root

- `.gitattributes`, `.gitignore`, `.python-version`: text normalization,
  ignored local artifacts and the project Python version.
- `AGENTS.md`: agent boundaries and quality gates.
- `README.md`, `INSTALL.md`: product overview and maintained installation
  contract.
- `LICENSE`, `NOTICE`: Apache 2.0 terms and Scala Core attribution for the
  original repository materials.
- `pyproject.toml`, `uv.lock`: package metadata and locked dependencies.

## Automation

- `.github/dependabot.yml`: uv and GitHub Actions security updates; routine version-update
  pull requests are disabled.
- `.github/workflows/ci.yml`: GitHub Actions checks on Linux, macOS and
  Windows with Python 3.12, locked dependencies, the four quality gates and
  package builds and an OSV dependency audit. Runs on pushes, pull requests,
  manual dispatch and a weekly schedule.

## Product and checks

- `skills/arale/SKILL.md`: portable agent skill.
- `src/arale_code/__init__.py`, `__main__.py`, `catalog.py`,
  `procedures.py`, `server.py`: package and read-only STDIO MCP server.
- `src/arale_code/instructions/*.md`: four bundled engineering instructions.
- `src/arale_code/procedures/*.yaml`: Guide 1.7 and P01 through P20, 21
  immutable procedure resources. No runtime manifest or transport state is
  stored in these directories.
- `tests/test_catalog.py`, `test_data_integrity.py`, `test_server.py`,
  `test_server_stdio.py`: catalog, asset, in-memory MCP and STDIO checks.

## Documentation

- `docs/spec/`: maintained product, server, layout, installation, quality and
  verification specifications; `.gitkeep` and `decisions-open.md` are retained.
- `docs/plan/guide-entry-design.md` and
  `docs/plan/guide-entry-implementation-plan.md`: selected Guide 1.6 design
  and implementation record. The final installation alignment plan remains
  only in the original workspace.
- `docs/plan/consumer-harness-evidence/`: the selected compact review records
  historical Guide 1.6 pin and current `guide-entry-v17-assets.json` pin. This directory is
  historical evidence, not a self-contained raw trial archive or a release
  approval.
- `docs/assets/guide-to-procedures.webp`: original README mascot holding a
  guide and pointing to procedure cards; documentation only, outside the wheel.
  Generated for this README from a text prompt with OpenAI image generation
  on 2026-10-27, without a reference image, then resized and encoded as WebP.

The 25 bundled source assets must retain the bytes pinned by
`docs/plan/consumer-harness-evidence/guide-entry-v17-assets.json`. A fresh
offline wheel check validates the packaged copy. Client registration and live
MCP discovery are separate steps under `INSTALL.md` and
`docs/spec/09-verification-spec.md`.
