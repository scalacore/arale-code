# Installing `arale-code` in one MCP client

This guide prepares the read-only, stateless STDIO server and registers it in
one client selected by the user. Registration, live connection, and release
approval are separate results. Client configuration requires a separate task.

## 1. Inspect before installation

Run these checks from the intended repository, before any `uv run` or `uv sync`:

1. Compare `git rev-parse --show-toplevel` with `pwd` (PowerShell:
   `(Get-Location).Path`). Resolve the intended absolute root as `<REPO_ROOT>`.
   Check `git status --short` and resolve unexpected changes before using it.
2. Confirm `pyproject.toml` and `uv.lock` exist at the root, and that the
   project requires Python 3.12.
3. Run `uv --version` and resolve the absolute executable as `<UV_PATH>`
   (`command -v uv` or `(Get-Command uv).Source`). If absent, stop and ask
   before fetching or installing `uv`.
4. Find a local Python without downloading one:

   ```bash
   uv python find --offline --no-python-downloads 3.12
   ```

   Check the returned interpreter's version. A cached uv-managed interpreter
   is acceptable. If absent, stop and ask before fetching Python 3.12.

Use absolute paths in client configurations. Escape Windows backslashes in
JSON, or use forward slashes. Confirm `skills/arale/SKILL.md` exists before
copying the skill.

## 2. Prepare the locked environment offline

From `<REPO_ROOT>`, run:

```bash
uv sync --locked --offline --no-python-downloads
```

This preserves `uv.lock`, forbids network access and prevents Python downloads.
If the cache lacks a required package or build dependency, stop. Report its
name/version, the proposed source and exactly what would be fetched; request
separate, explicit authorization before an online retry. Apply the same rule
if `uv` or Python is missing. Never replace a lock mismatch with an unlocked
sync. A failed offline preparation means no client registration yet.

After successful sync, use this client command:

```text
<UV_PATH> --directory <REPO_ROOT> run --locked --offline --no-python-downloads --no-sync arale-code
```

`--no-sync` uses the prepared environment; the other flags prevent a client
launch from fetching dependencies or Python. After a repository update, repeat
the offline sync before restarting a client.

## 3. Select and register one client

Ask which one to configure: Codex CLI, Claude Code, Cursor, OpenCode, or
Antigravity CLI. Antigravity IDE uses distinct paths below. Preserve other
configuration entries. Before manual edits, read the entire file and copy an
existing file byte for byte to `<file>.bak`; record if it does not yet exist.
After editing, parse JSON or TOML and restore the backup (or remove only the
new file) on failure. Copy `skills/arale/`, never link it, and repeat after
repository updates. Create only the selected client's directories.

### Codex CLI

```bash
codex mcp add arale-code -- "<UV_PATH>" --directory "<REPO_ROOT>" run --locked --offline --no-python-downloads --no-sync arale-code
codex mcp list
```

Use the native STDIO command first. If it fails, inspect `~/.codex/config.toml`
and add an equivalent `[mcp_servers.arale-code]` with absolute `command` and
`args`. Copy the skill to `~/.agents/skills/arale/`. Restart Codex; check
`/mcp` in the new session. `codex mcp list` proves configuration only.

### Claude Code

```bash
claude mcp add --transport stdio --scope user arale-code -- "<UV_PATH>" --directory "<REPO_ROOT>" run --locked --offline --no-python-downloads --no-sync arale-code
claude mcp list
```

Use the native STDIO command first. If it fails, inspect `~/.claude.json` and
add an equivalent user-scope `mcpServers.arale-code` STDIO object. Copy the
skill to `~/.claude/skills/arale/`. Restart Claude Code; check `/mcp` in the
new session. `claude mcp list` alone does not prove live discovery.

### Cursor

Edit `~/.cursor/mcp.json` for global registration, or the intended project's
`.cursor/mcp.json`. Merge this entry into the existing `mcpServers` object:

```json
"arale-code": {
  "command": "<UV_PATH>",
  "args": ["--directory", "<REPO_ROOT>", "run", "--locked", "--offline", "--no-python-downloads", "--no-sync", "arale-code"]
}
```

Copy the skill to `~/.cursor/skills/arale/` or the project's
`.cursor/skills/arale/`. Restart Cursor or reload its window. Inspect MCP
status in Cursor, then run the live checks below. No CLI enable command is
assumed.

### OpenCode

Inspect the installed version and `opencode mcp add --help`. Use the documented
interactive `opencode mcp add` flow when available and enter the STDIO command
from section 2. Alternatively, inspect the version-matched MCP docs before
editing its configuration, commonly `~/.config/opencode/opencode.json`.
Stable releases document `mcp.arale-code` with `type: "local"`, a command
array and `enabled: true`; V2 documents `mcp.servers.arale-code` and
`disabled: false`. Do not guess across schemas. Copy the skill to the
version-documented skill path, commonly `~/.config/opencode/skills/arale/`.
Restart and run `opencode mcp list`, then perform the live checks below.

### Antigravity CLI and IDE

Identify the installed surface. Official CLI guidance documents global MCP
configuration at `~/.gemini/antigravity-cli/mcp_config.json`, while other
Google guidance names `~/.gemini/config/mcp_config.json` for IDE and CLI.
Verify which configuration the installed client actually reads before editing.
The CLI global skill path is `~/.gemini/antigravity-cli/skills/arale/`; the IDE
global skill path is `~/.gemini/config/skills/arale/`. The project skill path
for either is `<PROJECT_ROOT>/.agents/skills/arale/`. Do not create paths for
the other surface.

In the verified MCP JSON, merge `mcpServers.arale-code` with `command` and
`args` as in the Cursor example. Restart the selected surface; inspect its
MCP connection view and skill list, then run the live checks. If a config or
skill path cannot be verified, report that uncertainty and skip that edit.

## 4. Verify the installed client

Configuration listing and valid JSON/TOML prove only registration. After the
client restarts, use that client's live MCP connection to:

1. Discover `list_instructions` and `list_procedures`.
2. Call `list_procedures`; parse its JSON string and confirm
   `schema_version: 1` and exactly 21 entries under `documents`.
3. Read `arale://procedure/guide`; confirm MIME `application/yaml`, parse its
   YAML, and check `meta.id: GUIDE` and `meta.version: '1.6'`.
4. Render `apply_instruction` with `id: testing` and a nonempty `task`, such
   as `Review the current test plan`; confirm it includes the testing text.
5. Check `git status --short` in `<REPO_ROOT>` for unexpected changes.

Any failed live check leaves installation unverified. The exact acceptance
contract is in `docs/spec/09-verification-spec.md`.

## 5. Removal

Only on a separate user request, remove the selected client's `arale-code`
MCP entry and copied skill, preserving all others. Codex and Claude document
`codex mcp remove arale-code` and `claude mcp remove arale-code`. For other
clients, follow the installed version's removal method or remove only the
verified configuration entry after backup and re-parse. Restart and verify
that the server and copied skill are absent.

## Official references

- [uv CLI](https://docs.astral.sh/uv/reference/cli/)
- [Codex MCP](https://learn.chatgpt.com/docs/extend/mcp?surface=cli) and [skills](https://learn.chatgpt.com/docs/build-skills)
- [Claude Code MCP](https://code.claude.com/docs/en/mcp) and [skills](https://code.claude.com/docs/en/skills)
- [Cursor MCP](https://docs.cursor.com/context/model-context-protocol) and [skills](https://cursor.com/help/customization/skills)
- [OpenCode MCP](https://opencode.ai/docs/mcp-servers/), [CLI](https://dev.opencode.ai/docs/cli/) and [V2 MCP](https://dev.opencode.ai/v2/docs/mcp-servers/)
- [Antigravity CLI MCP](https://codelabs.developers.google.com/genai-for-dev-antigravity-cli) and [skills](https://www.antigravity.google/docs/skills?tab=ide)
