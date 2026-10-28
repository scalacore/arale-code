# Verification Specification: Client and MCP Acceptance

`INSTALL.md` defines preparation and client registration. This specification
defines the observed acceptance contract. Local repository checks do not
establish a live client connection or a release approval.

## Before restart: configuration only

Confirm the selected client lists `arale-code` as configured. If a configuration
file was edited, parse it as JSON or TOML and confirm all unrelated entries
remain. This phase does not prove that the client can start or discover the
server. Preserve the pre-edit backup until the live checks pass.

## After restart: live client session

Use the selected client's MCP interface or protocol client connected to its
registered `arale-code` server. Record actual responses, not a configuration
listing or direct `uv run` output.

1. **Tools:** Discover exactly the two catalog tools `list_instructions` and
   `list_procedures`. Call both with `{}`. Each returns a JSON string with
   `schema_version: 1` and a `documents` array. The instruction array has
   four entries; the procedure array has 21.
2. **Procedure manifest:** Each `documents` entry has `id`, `code`, `title`,
   `kind` and `uri`. The first is `guide`, code `GUIDE`, kind `guide`, URI
   `arale://procedure/guide`. The remaining entries are the canonical
   `p01-project-reconnaissance` through `p20-acceptance-delivery` IDs in
   manifest order, each with kind `procedure` and its own
   `arale://procedure/<id>` URI. The short `p01` through `p20` forms are
   lookup aliases, not the manifest IDs.
3. **Catalog resources:** Read `instructions://catalog` and `arale://catalog`.
   Each has MIME `application/json` and the same version and document count
   as its corresponding tool.
4. **Guide resource:** Read `arale://procedure/guide`; MIME is
   `application/yaml`. Parse its YAML and confirm `meta.id: GUIDE`,
   `meta.version: '1.6'`, `meta.kind: control_guide`, and top-level `boot`,
   `router` and `protocol`. This is the Guide 1.6 resource shape; it does not
   have the old top-level `id`, `phases` and `routing_table` fields.
5. **Prompt:** Render `apply_instruction` with
   `{"id":"testing","task":"Review the current test plan"}`. Expect one
   user message containing `Instruction ID: testing`, the supplied task and
   the bundled testing instruction. A missing or blank `task` is invalid.
6. **Repository:** Run `git status --short` at `<REPO_ROOT>` and confirm the
   installation or live check made no unexpected changes.

Any failed item leaves the selected client unverified. Report its observed
state and fix or diagnose it before claiming a connected installation.

## Repository quality and package checks

Before a documentation-alignment commit, run `git diff --check` and the four
quality gates in `AGENTS.md`. In the clean distribution, build a fresh offline
wheel and compare its 21 procedure YAML and four instruction Markdown bytes
against `docs/plan/consumer-harness-evidence/guide-entry-v16-assets.json`.
These local checks prove package integrity; they do not replace the post-restart
client checks. Review the commit and confirm its Git tree is clean.
