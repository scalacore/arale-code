# Agent Rules for arale-code

Operational and engineering rules for AI coding agents modifying this repository.

## Operational Constraints

- Work only in the phase and files named by the active user instruction.
- In this clean distribution, create files only in paths listed in `docs/spec/03-repository-layout.md`. Routine edits to existing documentation and packaging files are allowed when the active task names them; this rule does not authorize client configuration, deployment, or release.
- All source files, documentation, and data assets must use UTF-8 encoding without BOM.
- All files must enforce LF line endings (`\n`, `0x0A`). Do not commit CRLF line endings.
- Do not add runtime or transport state; `arale-code` must remain strictly read-only and stateless.
- Do not add dependencies beyond `fastmcp`, `PyYAML`, and defined dev tooling.
- The MCP server must make no outbound network requests and must not read arbitrary environment variables. Installer dependency downloads require separate, explicit user authorization; use an offline installation path when the local cache is sufficient.

## Quality Gates

Before completing any task or committing changes, all quality gates must pass:

1. `uv run ruff check .` (Exit 0, zero lint errors)
2. `uv run ruff format --check .` (Exit 0, zero formatting mismatches)
3. `uv run mypy src tests` (Exit 0, strict mode without errors)
4. `uv run pytest` (Exit 0, all unit, contract, and integration tests passing)

## Resolution Protocol

If an instruction is ambiguous or conflicts with these rules, stop and ask the user.
