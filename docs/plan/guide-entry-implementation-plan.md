# Concise Guide Entry Implementation Plan

> **For implementing agents:** Execute the tasks in order, review each completed diff, and preserve the existing working tree and historical evidence. No model or case trial is authorized by this plan.

**Goal:** Make `arale://procedure/guide` a concise first guidance resource that selects one suitable P01-P20 procedure while retaining the existing read-only MCP interface and Guide protocol.

**Architecture:** Delete the duplicated `router.catalog` from Guide 1.5, keep the R0-R14 decision sequence and protocol in the same resource, and publish Guide 1.6 at the existing URI. Align server and skill entry wording with that route. The consuming agent still reads and executes the selected Pxx file with its own permissions; the server remains a stateless context provider.

**Tech stack:** Python 3.12, FastMCP, YAML assets, pytest, uv. No new dependencies.

**Spec:** [guide-entry-design.md](guide-entry-design.md).

## Global constraints

- Work only on the files named in each task. Register each new evidence path in `docs/spec/03-repository-layout.md` before creating it.
- Preserve the current uncommitted Guide 1.5 and other source changes as the starting content. Record a baseline diff and asset hashes; do not reset or overwrite user work.
- Keep 21 procedure IDs, all existing URI/alias behavior, JSON manifest schema version 1, two public catalog tools, the four instruction assets, and read-only, stateless STDIO operation.
- Keep the complete visible ten-field opening, transition, and closure record and the current authority, permission, trust, stop, and resumption rules. Do not regrade historical outcomes.
- All authored files use UTF-8 without BOM and LF endings. No outbound network request, extra dependency, runtime state, or provider dispatch is part of the local implementation.
- Before completion run `uv run ruff check .`, `uv run ruff format --check .`, `uv run mypy src tests`, and `uv run pytest`; all must exit 0.

## Review focus

1. A request naming P08 still routes to P08 after its fit check; it does not trigger a fixed P01/P02 prelude.
2. Ambiguous or uncovered requests still ask the minimum clarifying question or report the coverage limit.
3. A procedure whose file cannot be read is not reconstructed from the shortened Guide.
4. The shorter Guide still distinguishes `control_state` from `mandate_state` and preserves all ten record fields at every required point.
5. A client that reads a Pxx URI directly still gets the same resource type and full Pxx bytes.

---

### Task 1: Freeze the current candidate and add structural proof

**Files:** Modify `tests/test_data_integrity.py` and `docs/spec/03-repository-layout.md`; create `docs/plan/consumer-harness-evidence/guide-entry-v16-compatibility.md`. Read `src/arale_code/procedures/00-guide.yaml`, `src/arale_code/procedures.py`, and the existing asset pin. No product edit in this task.

**Interface:** The test reads the packaged Guide YAML through the existing asset path and `PROCEDURE_DEFINITIONS`; no runtime selector is introduced.

- [ ] Register `guide-entry-v16-compatibility.md` and `guide-entry-v16-assets.json` in `docs/spec/03-repository-layout.md` before either is created. Create the compatibility note with the baseline `git status --short`, current Guide SHA-256/byte count, and 25-asset pin comparison before editing product files. Preserve the earlier pin as historical evidence.
- [ ] Add a focused structural test: R0-R14 and SR01-SR07 appear once and in order; `selection_proposal` is present; each explicit Pxx code in a route resolves to a code in `PROCEDURE_DEFINITIONS`; `protocol.ledger.fields` contains the exact ten existing field names; the S0-S7 and mandate-state sets remain present.
- [ ] Run the new test against Guide 1.5 and confirm PASS. This is a preservation test, so a fabricated failure is unnecessary.
- [ ] Review the test against the five Review Focus items; keep behavioral judgments out of a structural assertion.

### Task 2: Shorten Guide 1.6 at the existing URI

**Files:** Modify `src/arale_code/procedures/00-guide.yaml` and `tests/test_data_integrity.py`.

**Interface:** `ProcedureCatalog.get_document("guide")` and `arale://procedure/guide` continue returning the complete raw YAML text. The public catalog entry and all Pxx files stay unchanged.

- [ ] Add assertions that the Guide has no duplicated `router.catalog`, is at most 24 KiB, and reports version `1.6`; run them to confirm they fail against 1.5.
- [ ] Delete only the 34,831-byte `router.catalog` block. Set `meta.version` to `1.6`. Adjust adjacent prose only where it refers to the deleted block; retain R0-R14, SR01-SR07, `selection_proposal`, `protocol`, and the ten-field ledger.
- [ ] Update the allowed content version and expected Guide byte count/SHA-256 in `tests/test_data_integrity.py` from the final edited bytes. These tests use hash constants in the test module; they do not read the historical 25-asset pin. Do not update hashes for any other asset without a separately reviewed change.
- [ ] Run `uv run pytest tests/test_data_integrity.py tests/test_catalog.py tests/test_server.py -q`. Confirm the route/ledger preservation test, asset integrity, 21-entry catalog, aliases, and full resource reads pass.
- [ ] Review the Guide diff against the baseline: no new effects, no lost permission or stop rule, no Pxx content change. Record actual bytes saved; size reduction is not behavioral proof.

### Task 3: Align entry instructions without changing the public surface

**Files:** Modify `src/arale_code/server.py`, `skills/arale/SKILL.md`, `docs/spec/02-server-contract.md`, `docs/spec/07-skill-spec.md`, and `tests/test_server.py`.

**Interface:** Existing MCP names, URI templates, return shapes, MIME types, and errors stay identical. `SERVER_INSTRUCTIONS` and the Arale skill tell an agent invoking Arale to read the Guide first, then read the selected Pxx file in full; a known Pxx URI remains directly readable.

- [ ] Change `SERVER_INSTRUCTIONS` to identify `arale://procedure/guide` as the first guidance resource for Arale-guided work, followed by discovery and a selected Pxx read. Do not claim the server enforces client reading order.
- [ ] Replace the skill's “Standard Workflow Sequence” with a short selection flow: read Guide, choose the smallest fitting procedure, read that procedure, and continue only necessary authorized work. Remove any default P01/P02 or other universal sequence. Preserve explicit Arale activation and read-only scope.
- [ ] Make the two specifications match the actual server string and skill text exactly where they claim exact content. Add a focused assertion for the Guide entry instruction in `tests/test_server.py`; check that examples still use valid current URI aliases.
- [ ] Run focused server/catalog tests, inspect the skill/spec diff, and confirm no public MCP names or payload fields changed.

### Task 4: Pin and verify the selected build

**Files:** Create `docs/plan/consumer-harness-evidence/guide-entry-v16-assets.json`; modify the `docs/plan/consumer-harness-evidence/guide-entry-v16-compatibility.md` created in Task 1. Read the repository layout to confirm both paths were registered. Do not edit the earlier `C01-C50-20261027-final-assets.json` or effective disposition manifest.

**Interface:** The new pin records paths, byte counts, and SHA-256 for all 25 assets, plus the source revision/working-tree identity. The compatibility note distinguishes historical case results from Guide 1.6 behavior.

- [ ] Confirm both new evidence paths were registered in Task 1 before creating the new pin.
- [ ] Generate and verify the new 25-asset pin from the final working-tree bytes; identify Guide 1.6 as the only intended asset change relative to the preceding selected pin. If another asset differs, stop and resolve the unexpected diff.
- [ ] Run all four repository quality gates and `git diff --check`. Fix any failure in the responsible task, then rerun the required gates.
- [ ] Build an offline wheel with `uv build --offline --wheel --out-dir /private/tmp/arale-guide-entry-v16-proof/dist`. Create an isolated environment with `uv venv --offline /private/tmp/arale-guide-entry-v16-proof/venv`, then install the built `arale_code-0.1.0-py3-none-any.whl` with `uv pip install --offline --python /private/tmp/arale-guide-entry-v16-proof/venv/bin/python /private/tmp/arale-guide-entry-v16-proof/dist/arale_code-0.1.0-py3-none-any.whl`. Stop if local dependencies are unavailable; do not fall back to network resolution. From outside the checkout, verify that all 25 resources served by the installed FastMCP host match the new pin. Preserve commands, artifact hash, and results in the compatibility note; identify this as local package proof, not deployment.
- [ ] Review the final diff and evidence for the five Review Focus cases. Keep release status on hold: task PASS history, Guide 1.6 consumer behavior, and host deployment are separate claims.

## Separate consumer evidence gate

After the local candidate passes, a claim that the shorter entry **improves agent routing or protocol adherence** needs a separately authorized, bounded consumer comparison. Use C01 for a narrow reconnaissance route, C03 for a single design route, and C04 for a choice between neighboring procedures. For each, retain the exact Guide/procedure hashes and separately assess selection, task rubric, and ten-field Guide protocol. Before any dispatch, check the current `case_network` policy, anti-loop ledger, permission scope, and native preflight; do not infer authorization from this plan. Run one admitted case at a time, with streaming terminal evidence and no automatic retry. Do not replay C44 or the remaining 46 cases to manufacture a same-build suite claim.

## Stop condition and handoff

The **local implementation** is complete when Tasks 1-4 and their reviews pass, the new pin matches the installed host, and all four quality gates pass. Stop then and report the narrower result: a verified shorter Guide entry and preserved local interface. If consumer evidence is later authorized and completed, report its measured scope separately. Do not release or transfer a repository based on this plan alone.
