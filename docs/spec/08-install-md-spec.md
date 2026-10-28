# Installation Specification

`INSTALL.md` is the maintained installation contract and the sole source of
client-specific commands, paths, permission boundaries and verification steps.
Do not duplicate its exact text here. Review any installation change against
the official references linked there and update this specification only when
the contract itself changes.

## Required behavior

- Inspect repository identity, Git state, `pyproject.toml`, `uv.lock`, `uv`,
  and local Python 3.12 before invoking `uv run` or `uv sync`.
- Prepare the lockfile environment offline first. The lockfile stays unchanged.
  Missing packages, `uv` or Python require a separate, explicit authorization
  for a precisely stated download.
- At client startup, use the prepared environment without synchronization,
  network requests or automatic Python downloads.
- Register only the user-selected client. Preserve other configuration entries,
  back up before manual edits, re-parse after edits and restore on parse errors.
- Use only documented commands and paths for the installed client version.
  Cursor uses its documented `mcp.json` flow. OpenCode's interactive flow and
  manual schema depend on version. Antigravity CLI and IDE paths differ and
  require verification against the installed surface.
- Verify live MCP discovery after restart. A configuration listing is not a
  connected-server proof. Apply `docs/spec/09-verification-spec.md`.
- Client removal and release approval are separate user decisions.
