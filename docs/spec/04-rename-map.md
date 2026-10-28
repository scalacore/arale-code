# Rename Mapping and Asset Verification

This document specifies the complete renaming rules from the reference codebase to `arale-code`, records occurrence counts of the old name across the 21 YAML files, and lists their structural classifications.

## 1. Complete Old-to-New Mapping Table

| Item Type | Old Name (Reference) | New Name (`arale-code`) | Scope / Path |
|---|---|---|---|
| Project Name | magma-code | arale-code | Repository, metadata, and documentation |
| Python Package | agent_instructions_mcp | arale_code | `src/arale_code/` |
| CLI Command | agent-instructions-mcp | arale-code | `[project.scripts]` in `pyproject.toml` |
| FastMCP Server Name | agent-instructions | arale-code | `FastMCP(name="arale-code", ...)` |
| Procedures Directory | `src/agent_instructions_mcp/magma/` | `src/arale_code/procedures/` | Procedures package path |
| Procedures Module | `src/agent_instructions_mcp/magma.py` | `src/arale_code/procedures.py` | Python module path |
| Procedures Class | `MagmaCatalog` | `ProcedureCatalog` | Class in `procedures.py` |
| Procedures Document Class | `MagmaDocument` | `ProcedureDocument` | Dataclass in `procedures.py` |
| Procedures Summary Class | `MagmaSummary` | `ProcedureSummary` | Dataclass in `procedures.py` |
| Procedures Lookup Error | `UnknownMagmaDocumentError` | `UnknownProcedureDocumentError` | Exception class in `procedures.py` |
| Procedures Discovery Tool | `list_magma_procedures` | `list_procedures` | MCP public tool |
| Procedures Static Resource | `magma://catalog` | `arale://catalog` | MCP static resource |
| Procedures Resource Template | `magma://procedure/{id}` | `arale://procedure/{id}` | MCP resource template |
| Agent Skill Name | magma | arale | User skill directory name |
| Verbal Skill Trigger | usa magma | usa arale | User activation prompt |
| Test Module (historical specification) | `tests/test_magma_catalog.py` | `tests/test_procedure_catalog.py` | Planned path; actual catalog tests are in `tests/test_catalog.py` |

---

## 2. Occurrence Counts in the 21 YAML Files

An exhaustive scan for the old name was performed on all 21 YAML procedure files from the reference repository.

| # | File Name | Occurrences of Old Name | Classification |
|---|---|---|---|
| 1 | `00-guide.yaml` | 0 | None |
| 2 | `01-project-reconnaissance.yaml` | 0 | None |
| 3 | `02-initial-state-baseline.yaml` | 0 | None |
| 4 | `03-environment-diagnosis.yaml` | 0 | None |
| 5 | `04-mandate-clarification.yaml` | 0 | None |
| 6 | `05-behavior-specification.yaml` | 0 | None |
| 7 | `06-interaction-design.yaml` | 0 | None |
| 8 | `07-technical-design.yaml` | 0 | None |
| 9 | `08-contracts-compatibility.yaml` | 0 | None |
| 10 | `09-plan-tasks-dependencies.yaml` | 0 | None |
| 11 | `10-coherence-coverage.yaml` | 0 | None |
| 12 | `11-malfunction-diagnosis.yaml` | 0 | None |
| 13 | `12-task-execution.yaml` | 0 | None |
| 14 | `13-controlled-refactoring.yaml` | 0 | None |
| 15 | `14-performance-optimization.yaml` | 0 | None |
| 16 | `15-testing-verification.yaml` | 0 | None |
| 17 | `16-change-review.yaml` | 0 | None |
| 18 | `17-security-data-integrity.yaml` | 0 | None |
| 19 | `18-integration-migrations.yaml` | 0 | None |
| 20 | `19-state-recovery-replanning.yaml` | 0 | None |
| 21 | `20-acceptance-delivery.yaml` | 0 | None |
| **Total** | **All 21 Files** | **0** | **No replacements needed in YAML text** |

---

## 3. Historical 1.0 Classification and Asset Integrity

At the original rename, the 21 procedure YAML files contained zero occurrences of
the old project name and their bodies remained unchanged. The following exact-byte
SHA-256 table is the historical content 1.0 baseline. Preserve it when revising
content; the current reviewed expectations evolve under section 4.

| File Name | Byte Count | Expected SHA-256 Hash |
|---|---|---|
| `00-guide.yaml` | 30288 | `8b4f030757909e33a83f946d52af399626eafbd3053d5cf0d2953fa30f1aaa0b` |
| `01-project-reconnaissance.yaml` | 10772 | `c1c1389dc7d51ad5be8458aa908d4828caf8dae1aa47da4800f5d56542941356` |
| `02-initial-state-baseline.yaml` | 11012 | `27ec0f776cb077644e2850073bea62784c7967b86280d1c76d45386784d01e14` |
| `03-environment-diagnosis.yaml` | 10515 | `67693590ed75ce82822fee224e1d2b1840a7251a8576eaaf3b8a7187af53eef8` |
| `04-mandate-clarification.yaml` | 9345 | `becbe7b74e61cfedecbe1087e2c4fc1da319e434ab193a72b2a09df69d0ca4cd` |
| `05-behavior-specification.yaml` | 8834 | `f408c3fa6186cadbf98eb704960fe861e025269c6a3e2ca708de24224a8d1d02` |
| `06-interaction-design.yaml` | 9238 | `8a9e1d11fbd0ee55d774ebe6f47b56f2718618dbdc5161f2b8e6a9e25131119f` |
| `07-technical-design.yaml` | 10000 | `96b6be9045dcc881a634a346a7bb757945676f521fe3c56ab36ba478bfaf23d0` |
| `08-contracts-compatibility.yaml` | 10403 | `dd1b5dc57bf9981fea10ecde209e6a445d2ca8aad6cc586d6c64a089b94ce981` |
| `09-plan-tasks-dependencies.yaml` | 9711 | `5f54b963e4bb6209fcfa011becc47c74423c6e890e5492e57b2436307599991f` |
| `10-coherence-coverage.yaml` | 9410 | `0bdd7d84d1d70a8cd868b09b1edbbd138856042d876b484ee5006aedf0228369` |
| `11-malfunction-diagnosis.yaml` | 11008 | `7fccd1752d11c8b6acb2a7cccbe9028db86687891b2755b7208ce0449548b9a1` |
| `12-task-execution.yaml` | 11128 | `757500713477073a4225ffc6fbcd9b8eb458b6ae54f09c1a17cf5ab1049e48c5` |
| `13-controlled-refactoring.yaml` | 11284 | `109eb34e9f8995abb40736ec96a017082ad8a6409825a596995b0e3b29962f3f` |
| `14-performance-optimization.yaml` | 11629 | `90055995d2332330344560236152619301cd2b339a5011f89fb1282bb0641dff` |
| `15-testing-verification.yaml` | 11640 | `b1832a512a2ac75c8f942e1ad273c9c311eca12a8b613643052fd9a13536d0c0` |
| `16-change-review.yaml` | 10958 | `9343612def382a0f283a1db3c17866b2b58e9a74cb1edd6a6f17501a3ef4cde6` |
| `17-security-data-integrity.yaml` | 10732 | `c19a4f1e672ea06c5e79668fe7b9f592bfc7f071bd869086cc4f60d55355b757` |
| `18-integration-migrations.yaml` | 11592 | `901a83fcf01319aede755b19e6eed01f750ddc9da9841ba96b823b9c032b81af` |
| `19-state-recovery-replanning.yaml` | 11261 | `8425b4298de16863fcc10283be1f009b02b0b55c2f4fbcc58ec7ace75d92b99b` |
| `20-acceptance-delivery.yaml` | 10657 | `8916ee508587a8ab9f1c8f5163016972366d3ecf5674aa6ef0d7e0705883025c` |

All hashes are computed over exact file bytes with LF line endings.

## 4. Content 1.1 revision policy and current expectations

Plan A revises content only. A01 records all 21 files at content 1.0, unchanged
from Git revision `8c20947a31cfd1c67dffae14c8b7521a40c3841d`. Each procedure moves to `version: '1.1'`
only in its own revision task. The guide moves to `meta.version: '1.1'` after
all twenty procedure tasks close. Package metadata and public identities remain
unchanged. Do not rename files, IDs, aliases, titles, URIs or discovery entries.

After semantic review, update the current row and `PROCEDURE_EXPECTED_HASHES`
in `tests/test_data_integrity.py` together. Each update must link the reviewed
bytes/hash, reason, evidence and Git revision in `docs/plan/rettifiche-21.yaml`.
When changes are uncommitted, identify the source revision and exact content
hash explicitly; do not invent a revision containing them. Never auto-refresh
hashes to conceal a failing check. Section 3 remains the recoverable historical
1.0 baseline; the table below evolves independently.

At A01, every current row equalled the historical baseline. Current rows identify
reviewed content 1.1 and pending content 1.0 separately. Editorial and technical
verification do not constitute human acceptance or live usage validation.

| File | Current content version | Bytes | Current SHA-256 | Reason and evidence |
|---|---|---|---|---|
| `00-guide.yaml` | 1.1 | 52537 | `dc238bc640b0b6b4e24780278800e0b80b59715b1b7e22681d3f6eb1f9da9386` | A-P00: findings resolved after editorial review; source `8c20947`, uncommitted reviewed bytes; register P00 |
| `01-project-reconnaissance.yaml` | 1.1 | 13745 | `39578c467c53ca1fb3d5def8783d5ee658e99491973ded4796f21ee92bd23dbe` | A-P01: source-linked map, explicit coverage and output-mode boundaries; source `8c20947`, uncommitted reviewed bytes; register P01 |
| `02-initial-state-baseline.yaml` | 1.1 | 15142 | `4ad903e82857f31a821e19ab7ab63a1a60122c777e4b8024a0bc54da0585119e` | A-P02: findings resolved after editorial review; source `8c20947`, uncommitted reviewed bytes; register P02 |
| `03-environment-diagnosis.yaml` | 1.1 | 14034 | `c219ff055e1b2dd357273f208e05dce819fd844a5915e346c55ed9d3d98e5993` | A-P03: findings resolved after editorial review; source `8c20947`, uncommitted reviewed bytes; register P03 |
| `04-mandate-clarification.yaml` | 1.1 | 12555 | `02721613e5ab5ca27314d8193c47d88473af2cefc87865be42c5548bd4e71fa2` | A-P04: clarification without ritual approval; source `8c20947`, uncommitted reviewed bytes; register P04 |
| `05-behavior-specification.yaml` | 1.1 | 12461 | `f636cd70f3fde049a892e13ded036d0900574d9441ed25ea88843ef56a91c349` | A-P05: findings resolved after editorial review; source `8c20947`, uncommitted reviewed bytes; register P05 |
| `06-interaction-design.yaml` | 1.1 | 13777 | `34517667d196843f10ff5fd3533de391551d1434d9e170d7fa47b0c2612edfbd` | A-P06: findings resolved after editorial review; source `8c20947`, uncommitted reviewed bytes; register P06 |
| `07-technical-design.yaml` | 1.1 | 14049 | `eb6c9c21734cb5eec6ae6e615e009965256719fd7817293c85b1466c582402cb` | A-P07: findings resolved after editorial review; source `8c20947`, uncommitted reviewed bytes; register P07 |
| `08-contracts-compatibility.yaml` | 1.1 | 14531 | `3aa046a4ebbfd6f1d8cb5f92c4e3de6c1be8670e5425a1998e36061437e58f17` | A-P08: findings resolved after editorial review; source `8c20947`, uncommitted reviewed bytes; register P08 |
| `09-plan-tasks-dependencies.yaml` | 1.1 | 13652 | `1dbdadf10eff45f2f05512bd954d891bac08c67a1cbfa87ee07272f71f5c49b0` | A-P09: findings resolved after editorial review; source `8c20947`, uncommitted reviewed bytes; register P09 |
| `10-coherence-coverage.yaml` | 1.1 | 13868 | `e5d2a715ea8cedf6552cdce15f6d18036bbd1a959835c82705e8ea41b9b7df00` | A-P10: findings resolved after editorial review; source `8c20947`, uncommitted reviewed bytes; register P10 |
| `11-malfunction-diagnosis.yaml` | 1.1 | 15603 | `0bc02f6814cb973fd2311284042ae9e8b24eb091823fe93e61ed6d2f94d52f14` | A-P11: findings resolved after editorial review; source `8c20947`, uncommitted reviewed bytes; register P11 |
| `12-task-execution.yaml` | 1.1 | 16071 | `8fdf0235eeef1cb6c27c961599f310d0186731373c586cc96d3c09b74b357eef` | A-P12: findings resolved after editorial review; source `8c20947`, uncommitted reviewed bytes; register P12 |
| `13-controlled-refactoring.yaml` | 1.1 | 14188 | `27ca3a90483c5dfbd789a4d65a29637d46f32d35e3dc7ec32083c35d37aeb5dd` | A-P13: findings resolved after editorial review; source `8c20947`, uncommitted reviewed bytes; register P13 |
| `14-performance-optimization.yaml` | 1.1 | 14512 | `7c4efd6e5f8050993cd8fdb5316656bae4501cbaaf1afde59de0e52a99cd6913` | A-P14: findings resolved after editorial review; source `8c20947`, uncommitted reviewed bytes; register P14 |
| `15-testing-verification.yaml` | 1.1 | 15329 | `fbd12038b9c713d55b0f34c1a18018c8ce579564e1aae1c1d8f500268ed6e63c` | A-P15: findings resolved after editorial review; source `8c20947`, uncommitted reviewed bytes; register P15 |
| `16-change-review.yaml` | 1.1 | 13513 | `a3920e47dc29a90339010419cda63050a0507ded3ac253277a701477a2f06b12` | A-P16: findings resolved after editorial review; source `8c20947`, uncommitted reviewed bytes; register P16 |
| `17-security-data-integrity.yaml` | 1.1 | 13932 | `a7bb9402f0011dddb24b6b9cb984cf4c7c9d86bfc365a4351f087a7bb5ed67cb` | A-P17: findings resolved after editorial review; source `8c20947`, uncommitted reviewed bytes; register P17 |
| `18-integration-migrations.yaml` | 1.1 | 15489 | `ebf7a86c5767cbefa02aa86dce9505846acc29fafe771aa0abe00f85f9279625` | A-P18: findings resolved after editorial review; source `8c20947`, uncommitted reviewed bytes; register P18 |
| `19-state-recovery-replanning.yaml` | 1.1 | 15796 | `771486f74d2c6252a01b8d53a04e073dee1b6d659cfa153fd4181f1d1194cf91` | A-P19: findings resolved after editorial review; source `8c20947`, uncommitted reviewed bytes; register P19 |
| `20-acceptance-delivery.yaml` | 1.1 | 15147 | `deb9abc4a0de1cb47cc8fd59345289279dc82f9b9a4081fdfe7cc77ef4d06d87` | A-P20: findings resolved after editorial review; source `8c20947`, uncommitted reviewed bytes; register P20 |
