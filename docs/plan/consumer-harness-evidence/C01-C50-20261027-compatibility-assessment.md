# Final asset selection and offline compatibility assessment

Date: 2026-10-27. Scope: Arale content assets and the 50 accepted case runs. This is the selected final content candidate for package preparation; deployment and release acceptance remain separate.

## Selected content

Select the current working-tree bytes of all 21 procedure assets (Guide plus P01 to P20) and four instruction assets. The [pin](C01-C50-20261027-final-assets.json) gives the path, URI, byte length and SHA-256 of each asset. Its ordered 21-procedure A03 manifest digest is `669d8c9e08875fcc9dd5ea0b4dbc43c19b00fb16ee35dd5a7155170693d22f55`. The historical A03 manifest digest recomputes to `0d113bc319bf2ff61955f6c33932fd51fcecd52a7ca8a8181734c76d8172fa17` by the same method. The base Git commit is `7807c5be577d9642fc4a5d292e29f0e48bb1c568`; it does not identify these uncommitted content revisions by itself.

The six edited assets are Guide 1.5, P05 1.2, P08 1.5, P09 1.4, P10 1.3 and P12 1.2. The other 15 procedure assets and all four instruction assets match the baseline bytes. A changed selected asset requires a new manifest and renewed affected assessment.

## Method and result

For each row in the [effective disposition manifest](C01-C50-20261027-effective-dispositions.json), compare the accepted `run.json` `contract.resource_sha256` map with the 25 selected file hashes. All 50 runs record the same 25 resource URIs. The accepted runs fall into six distinct asset snapshots and five difference groups relative to the selected bytes:

| Changed selected procedure assets versus accepted run | Cases | Current-content evidence |
| --- | ---: | --- |
| None | 3: C45, C46, C50 | Historical PASS uses identical Arale content bytes. |
| P09 | 4: C44, C47, C48, C49 | Historical PASS applies to its snapshot; selected P09 outcome unverified. |
| Guide, P08, P09 | 2: C05, C26 | Historical PASS applies to its snapshot; selected guidance outcome unverified. |
| Guide, P08, P09, P10, P12 | 3: C02, C18, C27 | Historical PASS applies to its snapshot; selected guidance outcome unverified. |
| Guide, P05, P08, P09, P10, P12 | 38 cases, individually identified in the JSON pin | Historical PASS applies to its snapshot; selected guidance outcome unverified. |

Across groups, 47 accepted runs differ in at least one content asset. No failed historical assessment is rewritten. The 50 effective case dispositions remain PASS under their original versioned evidence; only three have matching selected asset bytes.

## Compatibility judgment

The repository diff changes YAML guidance only. Procedure IDs, resource URIs, catalog definitions, instruction assets and server code are unchanged. The selected content is statically compatible at the MCP discovery and resource-addressing interface. This does not establish that a consuming agent will produce the same answer.

- Guide 1.5 now requires a complete visible ten-field record before substantive work, at transitions and at closure. This changes the expected agent output for any case that applies the Guide. An old PASS cannot prove compliance with this new protocol.
- P05 1.2 adds preservation of a source-stated actor scope. P08 1.5 asks for more exact field, unit, consumer/version and example analysis. P09 1.4 requires separate planned analysis work, provisional output revisions and distinguishing checks. P10 1.3 asks for combined-input evidence for Boolean rules. P12 1.2 adds numeric-domain and precision checks. These additions can change case answers or rubric coverage; neither semantic equivalence nor regression is demonstrated by a file hash or an offline reading.
- A claim of 50/50 selected-content case PASS would need affected reassessment or fresh evidence for the 47 changed-snapshot cases. That claim is separate from the completed historical 50-case harness exercise. Keep task rubrics, Guide protocol compliance and release approval as separate judgments.

No model request, case replay, provider dispatch or network access was used for this assessment. The selected asset pin is the reproducible source candidate; current-content case acceptance and final release readiness remain open.

## Independent trace reassessment of the 47 changed-snapshot cases

The accepted `run.json` files were read again, using their `arale_usage.resource_reads` records rather than treating the complete server resource manifest as if every resource had been consumed. Each read records the delivered content hash. The groups below compare those hashes with the selected asset pin; repeated reads of an asset count once per case. The old case rubrics and PASS dispositions are unchanged.

| Changed assets actually read in the accepted trace | Cases | Finding against selected guidance |
| --- | --- | --- |
| Guide only | C02-C04, C07-C11, C16-C21, C26, C29-C32, C34, C36-C41, C43 (27) | The trace received the older Guide. The preserved agent messages contain no complete labeled ten-field opening and closure records required by Guide 1.5. Current Guide protocol compliance is not established. |
| Guide and P05 | C12, C13, C22, C23, C42 (5) | The Guide gap applies. P05 1.2 also adds source-stated actor-scope preservation; the old answer cannot prove response to that new instruction. |
| Guide and P10 | C25, C28, C33, C35 (4) | The Guide gap applies. P10 1.3 additionally requires distinguishing combined-input coverage where a rule combines predicates. |
| Guide and P09 | C05, C15 (2) | The Guide gap applies. P09 1.4 adds separate planned analysis work, provisional output revisions and concrete distinguishing checks. |
| Guide and P12 | C06, C27 (2) | The Guide gap applies. P12 1.2 adds accepted numeric-domain and precision checks where relevant. |
| Guide and P08 | C14, C24 (2) | The Guide gap applies. P08 1.5 adds exact supplied quantities, consumer/version outcomes, examples and transition decisions where relevant. |
| No changed asset read | C01, C44, C47-C49 (5) | C01 made no Arale resource read. C44 and C47-C49 read selected-byte Guide and unchanged procedures; their server manifests included an older P09 that was not read. These five traces have no direct changed-content exposure, but they are not executions against one packaged selected build and do not prove a fresh current-content case outcome. |

The 42 cases with changed content actually delivered all precede Guide 1.5. Their preserved visible agent messages do not contain even the complete set of ten required field labels (`request`, `procedure`, `control_state`, `mandate_state`, `mandate_summary`, `outcome`, `evidence_refs`, `open_decisions`, `assumptions`, `next_step`). This is a check of visible trace evidence, not an inference about the model's internal state. It is sufficient to reject a claim that these traces demonstrate Guide 1.5 compliance. For the changed procedure obligations, applicability and semantic compliance would require a case-specific review of the supplied material and answer; the Guide gap already prevents promoting these 42 old runs to full selected-guidance acceptance.

The reassessment therefore closes the offline classification for all 47 cases without assigning a new PASS or FAIL to any historical run. A future 50/50 selected-build claim would need fresh, independently assessed execution for the affected cases, including Guide protocol as its own criterion. Keep the original task rubrics separate. Case execution remains outside this offline step.

## Packaged host proof and release decision

Built `arale_code-0.1.0-py3-none-any.whl` offline from this working tree using `uv build --offline --wheel`. Its SHA-256 is `aa6481c86d58c9315157ab7613b0411dc595531ff5429a8b546c728c286d51cb`. All 25 wheel asset bytes and the files installed into a new isolated virtual environment matched the selected pin. From `/private/tmp`, outside the source checkout, that installed package supplied the `arale_code.server.mcp` host. A FastMCP client read all 25 pinned resource URIs and each returned text hashed to the corresponding pinned SHA-256; zero mismatches. The wheel and environment are retained under `/private/tmp/arale-code-package-proof/` as local disposable proof, not a committed or deployed release artifact.

This proves that a newly built, locally installed host serves the selected bytes. It does not identify any previously installed or running host used by consumers, and does not show that a deployed host serves this build. Release evidence remains incomplete because 47 accepted cases are historical snapshots, 42 directly consumed changed guidance, and selected-build consumer outcomes and Guide protocol compliance have not been independently accepted. The current-content release decision is **hold**. Historical 50/50 task PASS, package-byte proof, current-content consumer acceptance and final user release approval remain distinct states.

## First fresh selected-content case

On 2026-10-27, C03 completed one new native Luna run using the selected 25-asset manifest. The [author assessment](C03-20261027-current-content-assessment.json) finds K01-K05 PASS and a visible ten-field opening and closure record. Six provider journals are terminal, the final provider answer equals the native delivered answer, the workspace is unchanged, and `case_network` was restored byte-for-byte to `denied`. The prior C03 run and assessment remain untouched.

This is one fresh case result with author review. Independent task and Guide protocol acceptance is still pending; it does not update the historical 50-case disposition manifest or establish a selected-build suite PASS. The other 46 changed-snapshot cases still lack fresh selected-content results.

## Objective and stop decision

The user clarified that the 50 cases were an exercise to learn whether the harness and system worked, exposed useful failures, and respected the tested security boundaries. They were not a requirement to repeat all 50 on one final content snapshot. For that objective, the versioned 50-case PASS manifest, accepted P2 boundary review for five selected profiles, pinned 25-asset package proof, and fresh C03 smoke result provide sufficient evidence to move to final repository preparation. The 100 historical run/assessment links were hash-checked again on 2026-10-27 with zero mismatches.

Stop the planned 46-case repeat. Do not run another case solely to obtain a same-build 50/50 number. A concrete new defect, a specific uncovered risk, or an explicit user request can justify a focused test. The remaining limits are disclosed: no universal Guide 1.5 compliance claim, no arbitrary-syscall security claim, no same-build suite claim, no identified deployed host, and no user release approval. The next work is selecting reviewable files and evidence for the final repository and making its local harness prerequisites explicit.
