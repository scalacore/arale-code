# C01-C50 reconciliation and package review

Date: 2026-10-27. Baseline: working tree against `7807c5b`. This review does not approve a release or change historical trial outcomes.

Publication privacy update (2026-10-28): personal absolute paths in this review,
the Guide compatibility note and the selected P2 JSON record are replaced with
`<USER_HOME>` and `<DEVELOPMENT_REPO>` labels. These are edited publication
copies; original evidence remains in the private development archive. Recorded
source hashes and trial outcomes are unchanged; the publication files themselves
have different bytes and must not be treated as the original raw records.

## Guide 1.6 reconciliation for the final copy

This review originally selected Guide 1.5. The subsequent Guide 1.6 edit removed its
duplicated routing catalog and produced a new 25-asset pin in
[`guide-entry-v16-assets.json`](guide-entry-v16-assets.json). Use that pin, together
with [`guide-entry-v16-compatibility.md`](guide-entry-v16-compatibility.md), for
the final product copy. Keep `C01-C50-20261027-final-assets.json` and the
assessments below as historical Guide 1.5 evidence. The Guide 1.6 installed
STDIO host proof in the compatibility note matched all 25 new pins. The wheel
hash there predates the later README correction; the final copy must use a fresh
wheel built from its own complete source tree.
No historical case result is promoted to Guide 1.6 acceptance by this update.

The final 64-file repository selection also fixes startup to request STDIO
explicitly and suppress the FastMCP banner, whose default update notice can
query PyPI. Its 55 product tests and four quality gates pass. An offline wheel
built from that clean copy has SHA-256
`bafcba80cc8bfbe7b6c233aca6af4efb3d417bd6e52cc941eaf3fe1b36a967ab`;
an isolated installation served all 25 Guide 1.6 pinned resources over STDIO
with two catalog tools and no startup banner. This verifies a local install,
not a deployed client host or release acceptance.

## Reconciliation

The [effective disposition manifest](C01-C50-20261027-effective-dispositions.json) links 50 distinct cases to 50 terminal runs and independent PASS assessments: 35 accepted originals and 15 accepted derived trials. All 100 linked run and assessment SHA-256 values were checked against current files. There are zero open **case task** dispositions. Earlier FAIL and NON_VALUTABILE records remain historical evidence.

These passes span six Arale asset snapshots (38, 4, 3, 3, 1 and 1 accepted runs). Forty-seven accepted runs differ from the current source in at least one recorded Guide or procedure hash. The rollup is valid as historical case-level acceptance; it is not a fresh 50-case regression on one current build. Task PASS also does not establish universal Arale protocol compliance, causal benefit or release approval.

## Review findings

1. **Release claims need precise scope.** The [Guide 1.5 content pin](C01-C50-20261027-final-assets.json) fixes the 25 assets selected at the original review. An offline wheel and isolated FastMCP host served those pinned resource bytes, and one fresh C03 run has an author PASS assessment against that earlier candidate. The [compatibility assessment](C01-C50-20261027-compatibility-assessment.md) records why the historical 50/50 PASS is versioned and does not prove universal Guide 1.5 compliance or a same-build suite PASS. The user has clarified that repeating the remaining 46 cases is outside the harness-learning objective. Select final evidence and disclose this limit; do not turn it into another mandatory full run. A deployed host and user release approval remain unverified.
2. **Medium: raw evidence needs an explicit retention decision before transfer.** At the original review, `docs/plan/consumer-harness-evidence/` was about 246 MB with about 2,509 untracked files. Forty-four of the 50 accepted `run.json` files retain full `requests[].payload.messages`; across the 299 runs then present, 277 retain messages, including 16 with provider dispatches. Newer C45-C50 runs avoid that retention. The current workspace keeps the historical evidence; do not copy all raw journals into the clean final repository by default. Select reviewable, authorized evidence and preserve hashes and provenance to the retained archive.
3. **Medium: diagnostic harness has machine local prerequisites.** `docs/plan/openrouter_completion.mjs` imports a credential helper from `<USER_HOME>/.local/bin/`, and the provider smoke, transport probe and Luna runner refer to paths under `<USER_HOME>/.codex/`. The harness is locally verified, but another checkout cannot reproduce its provider diagnostics without equivalent setup. Document these prerequisites or make them configurable before calling the harness portable.
4. **Low: continuity files are outside the product package.** The untracked `.codex/FLOW.md`, `.codex/FLOW.archive.md` and `.codex/flow_legacy_1.md` are session records. Exclude them from the final repository unless the repository layout is explicitly extended for them.

## Checks and transfer boundary

`uv run ruff check .`, `uv run ruff format --check .`, `uv run mypy src tests`, `uv run pytest` (51 passed), `uv run pytest docs/plan/test_consumer_luna_runner.py -q` (875 passed) and `git diff --check` passed. A scan of 2,628 tracked and untracked files found no UTF-8 BOM, invalid UTF-8 text or CRLF in text files; a signature scan found no high-confidence API key or private-key token. The large evidence archive was sampled for content rather than audited line by line.

For the proposed final repository in another workspace, use the Guide 1.6 asset pin to copy only reviewed product files, required tests, maintained documentation and selected evidence. Keep the raw trial archive in this working workspace. Create the new Git history only after selection and verification; no `git init` or transfer has been performed here.

## Final repository selection

The selected product tree consists of `.gitattributes`, `.gitignore`, `.python-version`, `AGENTS.md`, `README.md`, `INSTALL.md`, `pyproject.toml`, `uv.lock`, `skills/arale/SKILL.md`, all files under `src/arale_code/`, the four `tests/test_*.py` modules, and the maintained `docs/spec/` files. The 25 content assets within `src/arale_code/` must match `guide-entry-v16-assets.json` byte for byte. Include the changed `tests/test_data_integrity.py` expectations with those assets. This is a file selection, not a claim that a final checkout or deployment exists.

The clean deployable repository contains that product tree, the Guide 1.6 design
and implementation notes, and the compact records selected below. It excludes
the consumer harness, its fixtures, raw run journals, historical planning
materials and continuity files. The harness is not self-contained without raw
case evidence and its machine-local prerequisites: a reduced staging copy
passed the 54 product tests but its harness suite failed on missing archived
`run.json` inputs. Keep the complete conductor-only harness in this original
workspace. A later diagnostic transfer needs a separate complete inventory,
prerequisite setup and evidence review; never expose facilitator/evaluator
fixtures to a consuming agent.

Select these compact review records from `docs/plan/consumer-harness-evidence/`: `guide-entry-v16-assets.json`, `guide-entry-v16-compatibility.md`, `C01-C50-20261027-final-assets.json`, `C01-C50-20261027-effective-dispositions.json`, `C01-C50-20261027-compatibility-assessment.md`, this package review, `C03-20261027-current-content-assessment.json`, and `p2-effect-schema-streaming-20261025/final-p2-acceptance.json`. The first two identify the final product bytes; the others retain versioned case outcomes, five-profile boundary, earlier C03 author review, and limits. The disposition and P2 records contain hashes and paths into the retained raw archive; without that archive in the final repository, their underlying runs cannot be independently rechecked from the final checkout alone. Keep the original archive here unchanged, preserve its path and hashes as provenance, and provide access only after a separate review of its retained messages and authorization for transfer. Do not describe the compact records as a self-contained evidence archive.

## Local prerequisites for diagnostics

The product uses the locked Python dependencies in `uv.lock`. The diagnostic harness additionally expects a local Codex app-server/client installation, a macOS sandbox for the native boundary probes, Node.js for `openrouter_completion.mjs`, and a separately configured OpenRouter Luna credential. The transport imports a key helper from `<USER_HOME>/.local/bin/claude-openrouter.mjs`; the provider smoke expects `<USER_HOME>/.codex/hooks/anti-loop.py`; the transport probe and Luna runner read Codex config/cache under `<USER_HOME>/.codex/`. `consumer_harness.py` uses `/private/tmp/arale-code-consumer-harness` as scratch space. These paths are machine local, are not supplied by the repository, and must be replaced or supplied equivalently before provider diagnostics on another checkout. Do not copy keys, Codex home, or anti-loop state into the final repository. Offline unit tests and product installation do not establish that another machine's provider diagnostics are ready.

## Scoped release decision

The reviewable handoff is ready for selection, but the Guide 1.6 release remains **hold**. The local wheel/host served all 25 Guide 1.6 pinned bytes; no deployed host is identified. The historical 50/50 PASS spans earlier asset snapshots, and the fresh Guide 1.5 C03 result has author review only. P2 acceptance covers five named profiles and their fixed permission contracts, not arbitrary syscalls. A final release needs the user's decision on the selected package and target host, followed by verification that the chosen host serves the Guide 1.6 pin. This decision does not require replaying the remaining 46 cases for the clarified harness-learning objective.
