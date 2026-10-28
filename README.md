# arale-code

**Local engineering guidance for coding agents, served through MCP.** `arale-code` gives an agent four reusable instructions, a control Guide and 20 software engineering procedures. The server provides documents; the agent decides what to do with them under its own tools and permissions.

![An original guide character holding a book and pointing to three procedure cards](docs/assets/guide-to-procedures.webp)

*Read the Guide, choose one procedure, then read its full document.*

## Find the right procedure

1. Connect an MCP client to the local STDIO server.
2. Read `arale://procedure/guide` for the selection rules, or call `list_procedures` to discover IDs and resource URIs.
3. Read the selected procedure in full, then apply it to the user’s task within the agent’s existing permissions.

For example, call the `list_procedures` MCP tool with an empty argument object:

```json
{}
```

It returns a JSON string whose first entry is the Guide (excerpt; the full `documents` array has 21 entries):

```json
{"schema_version":1,"documents":[{"id":"guide","code":"GUIDE","title":"Control Guide","kind":"guide","uri":"arale://procedure/guide"}]}
```

Read that URI as an MCP resource to get the YAML Guide. Its `meta.id` is `GUIDE` and its `meta.version` is `'1.6'`. The example shows catalog discovery; it does not cause the server to edit a project.

## Get started

You need Python 3.12 and `uv`, with the locked dependencies available locally. From the repository root, prepare the environment without a network request:

```bash
uv sync --locked --offline --no-python-downloads
```

Then follow [INSTALL.md](INSTALL.md) to register **one** client and check its live MCP connection. It documents Codex CLI, Claude Code, Cursor, OpenCode and Antigravity CLI, including the local launch command. An offline sync can fail if Python or a locked dependency is missing from the local cache; the installation guide explains what to check before downloading anything.

## What is included

| Interface | Contents |
| --- | --- |
| Tools | `list_instructions`, `list_procedures` |
| Catalog resources | `instructions://catalog`, `arale://catalog` |
| Resource templates | `instructions://document/{id}`, `arale://procedure/{id}` |
| Prompt | `apply_instruction` with an instruction `id` and a nonempty `task` |

The bundled documents are four Markdown instructions, one YAML Guide and 20 YAML procedures. See the [MCP contract](docs/spec/02-server-contract.md) for exact IDs, response shapes and errors.

## Boundaries and verification

The server is read-only and stateless. It serves bundled guidance over local STDIO; it does not execute procedures, grant permissions or make outbound network requests. The consuming agent remains responsible for any project changes.

Repository tests and an isolated local STDIO package check have verified the bundled interface and Guide 1.6 assets. The five client paths in [INSTALL.md](INSTALL.md) are documented installation paths; live discovery in each client has not been verified here. See the [verification contract](docs/spec/09-verification-spec.md) for the checks required after client registration.

## Develop and contribute

Prepare the locked environment as above, then run the repository’s quality gates:

```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy src tests
uv run pytest
```

For changes to the MCP interface or bundled documents, read the [server contract](docs/spec/02-server-contract.md) and [quality gates](docs/spec/05-quality-gates.md), and include the relevant verification with your proposed change. For installation questions, start with [INSTALL.md](INSTALL.md).

## License and maintainer

Maintained by Scala Core. Licensed under [Apache 2.0](LICENSE); see [NOTICE](NOTICE) for attribution.
