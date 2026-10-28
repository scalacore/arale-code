# Concise Guide entry: design contract

Date: 2026-10-27. Status: selected design direction for planning; no product files have been changed by this document.

## Intent and evidence

`arale-code` serves read-only, stateless guidance. Its current `arale://procedure/guide` is the intended first file for an Arale-guided task, but the client chooses which resource to read. The Guide is 54,040 bytes; its embedded `router.catalog` occupies 34,831 bytes. The same procedure purposes, fit checks, modes, and limits are available in the individual P01-P20 files. The server catalog lists IDs and URIs but does not execute a route.

The historical 50 case task PASS outcomes span six asset snapshots. They do not prove universal Guide protocol compliance or a same-build regression. C44 evidence shows complete Guide delivery with a missing visible lifecycle record; one newer C03 author review finds a complete opening and closure record. File size is a plausible design cost, not a proven cause of C44. The redesign must be measured against routing, task quality, and Guide protocol separately.

## Chosen interface

Keep `arale://procedure/guide` as the first guidance resource for an Arale-guided task. Keep the 21 existing procedure IDs and resource URIs, the catalog JSON schema version, the two public tools, and the existing read-only server role. The Guide supplies a short orientation, R0-R14 route decisions, selection and fit rules, and the current cross-cutting protocol. It sends the agent to one complete Pxx file for the bounded activity; it does not execute that activity.

Remove the verbose `router.catalog` duplication from the Guide. The existing R0-R14 decisions and each Pxx file supply the route and fit information. Do not add a router tool, mutable state, inference, remote transport, dependency, or universal procedure sequence. The initial Guide target is at most 24 KiB; the 34,831-byte deletion alone projects 19,209 bytes before small wording changes. Size is a constraint on duplication, not a license to drop necessary authority or safety rules.

For this revision, preserve the visible ten-field opening, transition, and closure record, including separate `control_state` and `mandate_state`. Whether a smaller user-facing record is sufficient remains a separate product decision. Do not reinterpret historical protocol FAILs after this edit.

## Alternatives considered

1. Change only server and skill wording. This leaves the 54 KB first read and duplicated catalog.
2. Shorten the existing Guide resource while retaining its URI and the P01-P20 resources. **Selected** because it improves the first-read interface without moving orchestration into the server.
3. Add a `choose_procedure` runtime tool. This changes the public MCP contract and server responsibility without evidence that a deterministic runtime selector is needed.

## Observable acceptance

- The Guide remains valid YAML with `meta`, `boot`, `router`, and `protocol`; its version advances to `1.6` and its bytes are at most 24 KiB.
- Every R0-R14 decision remains present, in order; all referenced procedure codes resolve to existing P01-P20 resources. The agent is still told to read a candidate procedure in full and check fit before using it.
- The ten ledger fields and opening, transition, closure obligations remain present. Existing permission, authority, untrusted-content, stop, and no-state rules remain effective.
- The Arale skill and server instructions describe Guide-first discovery without imposing P01/P02 or any other universal sequence. Existing direct resource reads and aliases remain valid.
- All four repository quality gates pass. A new offline wheel and isolated host serve every selected asset byte; the new content pin is distinct from, and does not overwrite, historical pins.
- Any claim that agents route or comply better requires a separate bounded consumer comparison. Local tests and smaller bytes alone support only the content and interface claims above.

## Release and evidence limit

This design does not authorize a case trial, provider dispatch, network change, final repository transfer, or release. Historical cases and raw evidence remain unchanged. A later selected-build release decision must identify the deployed host and use evidence whose scope matches the claim.
