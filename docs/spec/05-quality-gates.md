# Quality Gates and Test Verification

This inventory describes the implemented tests through the Guide 1.7 revision (2026-10-28). Historical
module names and index manifests are not implemented checks.

## 1. Required quality gates

Run in this order before completing a task or committing; each must exit 0:

```bash
uv run ruff check .
uv run ruff format --check .
uv run mypy src tests
uv run pytest
```

Ruff must report no lint errors or formatting mismatches, strict mypy no errors,
and pytest no failing tests. Preserve the first failure and diagnose it; do not
change expectations merely to obtain a pass. A successful rerun does not erase
an earlier failure. Record commands, conditions, outputs and unrun checks.

## 2. Actual test inventory

CI also runs `uv audit --locked` against OSV on all three platforms, including
development dependencies. A finding or lookup failure fails the job; no
advisories are suppressed. This online check sends package names and versions
to OSV and is separate from the four offline-capable quality gates. Weekly
CI and Dependabot checks cover newly disclosed advisories; Dependabot opens
security fixes only, without routine version-update pull requests. GitHub secret
scanning and push protection provide the repository's hosted secret checks.

### 2.1 `tests/test_catalog.py` (6 tests)

- `test_procedure_catalog_contents`: 21 entries, order, procedure codes/kinds/URIs.
- `test_procedure_catalog_aliases_and_get`: guide and P01 lookup/aliases.
- `test_procedure_catalog_unknown_id_error`: unknown procedure rejection.
- `test_procedure_catalog_json_manifest`: schema version and manifest count.
- `test_instruction_catalog_contents`: four documents and priority order.
- `test_instruction_catalog_get_and_unknown`: instruction content and unknown-ID rejection.

Catalog definitions are in Python, not `index.yaml`. Alias examples do not
prove that every possible alias or YAML metadata field was checked.

### 2.2 `tests/test_data_integrity.py` (40 test instances)

- `test_file_counts`: exactly 21 procedure YAML and four instruction Markdown files.
- `test_procedure_yaml_integrity`: existence, exact byte size, 65,536-byte ceiling
  and SHA-256 for each of the 21 procedures.
- `test_instruction_markdown_integrity`: the byte/hash/encoding checks for four instructions.
- `test_procedure_yaml_rejects_duplicate_keys`: two malformed inputs demonstrate
  rejection of duplicate metadata and nested mode keys.
- `test_asset_rejects_bom_and_cr`: two inputs demonstrate rejection of BOM and CR.
- `test_procedure_asset_rejects_invalid_structure`: five mutated inputs demonstrate
  rejection of invalid version/ID, empty modes, duplicate step numbers and a
  missing guide block.
- `test_p05_preserves_source_actor_scope_for_repeated_requests` and
  `test_p10_checks_combined_predicate_coverage`: focused guidance checks.
- `test_guide_route_and_record_structure`: Guide routing and ten-field record structure.
- `test_guide_reporting_policy`: concise default, full-record triggers and reporting events.
- `test_guide_entry_is_concise_version_17`: Guide version, size and removed duplicate catalog.

The expected hashes are reviewed current expectations. Historical content 1.0
hashes remain in section 3 of `04-rename-map.md`. Hash equality demonstrates
exact bytes; it does not demonstrate semantic quality. A02 adds a test-only safe YAML loader that rejects duplicate keys without changing
PyYAML's global loader registry. Bundled assets are checked for UTF-8/no BOM/LF,
current allowed versions, metadata matching the public catalog, distinct guide/procedure
blocks, nonempty modes and uniquely numbered nonempty actions. These checks
validate the editorial asset contract; the runtime still serves raw text and
has no new loader, state or dependencies. This minimum structure does not prove
that mode prerequisites, actions and outcomes are semantically consistent.

### 2.3 `tests/test_server.py` (9 tests)

- `test_server_instructions_offer_guide_entry_without_enforcing_read_order`:
  Guide-first guidance without a server-side read-order claim.
- `test_main_starts_stdio_without_update_banner`: explicit STDIO and no FastMCP
  banner or update check at startup.
- `test_server_tools_list_and_call`: two tools and discovery response counts/schema.
- `test_server_resources_catalogs`: catalog resources and their MIME/count/schema.
- `test_server_read_all_procedure_resources_and_mimes`: all 21 procedure URI reads
  match the local catalog's exact text and YAML MIME type.
- `test_server_read_all_instruction_resources_and_mimes`: all four instruction
  URI reads match exact text and Markdown MIME type.
- `test_server_unknown_resource_errors`: unknown-ID resource errors.
- `test_server_prompt_rendering`: instruction prompts include ID, task and rules.
- `test_server_prompt_validation_errors`: empty/oversized tasks and unknown IDs.

These use an in-memory FastMCP client. They do not prove every platform/client
installation, immutable runtime internals or field-level YAML semantics.

### 2.4 `tests/test_server_stdio.py` (1 test)

- `test_server_stdio_subprocess`: launches `uv run arale-code` locally, discovers
  tool names and calls procedure discovery with count/schema assertions inside
  a 20-second timeout. It also reads the actual Guide resource and checks version
  1.7 and its concise default. It does not assert independent shutdown, server-name,
  every URI read or cross-platform behavior.

The observed suite contains 56 tests. A01 and revision results are in
`docs/plan/rettifiche-21.yaml`; later changes may alter the inventory/count.

## 3. Editorial revision and completion evidence

For each procedure, keep original section, problem, source, observable result,
changes, dependencies, checks, exact-byte evidence and status in the register.
Trace ordinary and adverse scenarios, autonomous use and relevant handoffs.
Revision tasks must preserve names, canonical IDs, titles, aliases and URIs.

Before changing P00, reference twenty completed procedure cards. At closure,
verify unique 21-card coverage, existing references, unchanged historical 1.0
table, current hashes and the four gates. Do not equate structural checks or
editorial scenarios with live E2E evidence, human acceptance or release.

Evidence is bound to the input revision, diff and exact bytes. When relevant
inputs change, earlier results need rerunning or explicit compatibility evidence.
Research references inherited from Plan A identify provenance; they do not
mean source content was revalidated or new product dependencies authorized.
