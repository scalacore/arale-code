# Guide 1.6 local compatibility evidence

## Before product edits

Base commit: `7807c5be577d9642fc4a5d292e29f0e48bb1c568` on `main`. The working tree was already dirty. `git status --short` showed modified `docs/plan/piano-b-progress.yaml`, `docs/spec/03-repository-layout.md`, Guide, P05, P08, P09, P10, P12, and `tests/test_data_integrity.py`; it also showed untracked `.codex/`, consumer harness files and evidence, usage materials, design, and implementation plan. None was reset.

Guide 1.5 baseline: 54,040 bytes; SHA-256 `dabf9b0bd75774c4c8ac4cd7401362c9df37a49bde27b0f2e4305d9139c24e9c`.

The 25 assets (21 procedures and four instructions) matched every byte count and SHA-256 in `C01-C50-20261027-final-assets.json` before product edits: zero mismatches. That earlier pin remains historical evidence.

## Guide 1.6 result

Guide 1.6 is 19,209 bytes, SHA-256 `69825372a8f32dbe9c92c9a155aabc2a3934c43e263cc869916bd68087ccae2e`. Removing the 34,831-byte duplicated `router.catalog` block accounts for the byte reduction; the version changed from 1.5 to 1.6. The new `guide-entry-v16-assets.json` pins all 25 source assets. Its asset-set SHA-256 is `dc83a4db9695d794f42f0bf23ec6ec008e45fcd0faacf71c6c322cd40abceed4`. Fresh file reads matched every pin; only Guide differs from the preceding selected pin. The earlier pin and case dispositions were not edited.

Structural proof preserves R0-R14, SR01-SR07, `selection_proposal`, S0-S7, mandate states, and the ten separate ledger fields. R0 still routes a named P08 through SR02's fit check; no universal P01/P02 sequence remains in the skill. R2 and R14 still cover ambiguity and lack of coverage. SR07 still requires the full Pxx file and forbids reconstruction if unreadable. These are source and structural checks, not evidence of consuming-agent behavior.

The server instructions and skill now direct a Guide-first selection followed by a full selected Pxx read. No MCP name, URI template, MIME type, payload field, or direct Pxx read behavior changed. In-memory resource tests and the installed-host proof below checked the full resource bytes.

## Local verification

- `uv run pytest tests/test_data_integrity.py::test_guide_route_and_record_structure -q`: PASS on Guide 1.5 before the edit.
- `uv run pytest tests/test_data_integrity.py::test_guide_entry_is_concise_version_16 -q`: expected FAIL on Guide 1.5 before the edit.
- `uv run pytest tests/test_data_integrity.py tests/test_catalog.py tests/test_server.py -q`: 52 PASS after the Guide edit.
- `uv run pytest tests/test_server.py tests/test_catalog.py -q`: 14 PASS after entry-instruction alignment.
- `uv run ruff check .`: PASS. `uv run ruff format --check .`: PASS, 29 files. `uv run mypy src tests`: PASS, 9 source files. `uv run pytest`: PASS, 54 tests.
- `git diff --check`: PASS.

Offline package commands from the repository root:

```text
uv build --offline --wheel --out-dir /private/tmp/arale-guide-entry-v16-proof/dist
uv venv --offline /private/tmp/arale-guide-entry-v16-proof/venv
uv pip install --offline --python /private/tmp/arale-guide-entry-v16-proof/venv/bin/python /private/tmp/arale-guide-entry-v16-proof/dist/arale_code-0.1.0-py3-none-any.whl
```

All three exited 0 without network resolution. Wheel SHA-256: `bd465f2bfc92a051d48ad2fbb51f2ba4ab72a60c3ce107f3ae0a34aeccf73743`.

From `/private/tmp`, an isolated Python 3.12 client launched the installed `/private/tmp/arale-guide-entry-v16-proof/venv/bin/arale-code` over STDIO. It confirmed the two catalog tools, schema version 1 with 21 documents, and exact MIME, byte count, and SHA-256 matches for all 21 procedure and four instruction resources against the new pin. The first local proof invocation failed before connecting because `StdioTransport` requires an explicit `args` argument; the corrected invocation used `args=[]` and passed all checks. This is local installed-package proof, not deployment.

The corrected host check was run from `/private/tmp` with the isolated Python executable and the following `-c` program:

```python
import asyncio
import hashlib
import json
from pathlib import Path
from fastmcp.client import Client
from fastmcp.client.transports import StdioTransport

pin = json.loads(Path("<DEVELOPMENT_REPO>/docs/plan/consumer-harness-evidence/guide-entry-v16-assets.json").read_text())

async def verify():
    transport = StdioTransport(command="/private/tmp/arale-guide-entry-v16-proof/venv/bin/arale-code", args=[])
    async with Client(transport=transport) as client:
        tools = await client.list_tools()
        assert {tool.name for tool in tools} == {"list_instructions", "list_procedures"}
        manifest = json.loads((await client.call_tool("list_procedures", {})).data)
        assert manifest["schema_version"] == 1 and len(manifest["documents"]) == 21
        for row in pin["procedure_assets"] + pin["instruction_assets"]:
            resource = await client.read_resource(row["uri"])
            assert len(resource) == 1
            expected_mime = "application/yaml" if row in pin["procedure_assets"] else "text/markdown"
            assert resource[0].mime_type == expected_mime
            raw = resource[0].text.encode("utf-8")
            assert len(raw) == row["bytes"]
            assert hashlib.sha256(raw).hexdigest() == row["sha256"]

asyncio.run(verify())
```

Historical case results remain tied to their recorded asset hashes. Guide 1.6 routing or protocol improvement in a consuming agent is unverified and needs a separately authorized bounded comparison. Release and transfer remain on hold.
