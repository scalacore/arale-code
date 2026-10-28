# Guide 1.7: reporting presentation

The Guide's ten operational fields and state/authorization enums remain intact.
Their default visible representation is concise, in the user's language.
An ordinary reply does not close the user's objective. The consuming agent
applies this guidance; the server still returns raw resources without rendering,
state, storage, new tools or changes to the twenty bounded procedures.

## Presentation contract

- Opening: briefly identify the objective and authorized scope.
- Ordinary progress: deliver useful content; omit unchanged status blocks.
- A material decision, scope change, blocker or suspension: explain the
  relevant facts, consequences and actual question or condition for resumption.
- Resumption or procedure change: reconcile valid authority and prerequisites;
  explain relevant changes without requesting approval already provided.
- Closure of the user's objective: report results, actual evidence, limits and
  unresolved matters once. Retain the selected procedure's required report content.
- Full record: show all ten labeled fields when explicitly requested or needed
  for an audit or handoff that requires the complete operational context.
  An audit or handoff label alone does not make the full record necessary.

Use short headings, prose, labeled bullets or a table. Ordinary updates need
no raw YAML, enum codes or empty fields. Work state and authorization remain
distinct in meaning; use separately labeled exact enum values in the full view.
For example, an approved specification mandate may still await a decision on
requirements. A shorter response never changes the mandate or verifies a check.
Neither presentation implies hidden persistence, private reasoning disclosure
or authority to save the record. Recover missing context before proceeding.

## Review scenarios

| Scenario | Required observable behavior |
|---|---|
| Continue P05 with unchanged scope | Provide the next requirements without repeating the ten-field footer or requesting authority again. |
| Await validation of FIN-01 to FIN-06 | Put the unresolved choice and consequences next to the question; distinguish it from the already approved specify-only mandate. |
| User requests the full record | Return all ten labeled fields, with control and mandate states separate and valid. |
| A required check is unavailable | State the missing check and its consequence; concise output must not imply verification. |
| Move to another already authorized procedure | Reconcile and continue; name the transition when useful without another full record by default. |
| User objective is complete | State result, evidence and limits once; do not append a duplicate technical closure block. |
| Read-only work encounters a new write target | Ask for the new effect before writing; presentation changes grant no authority. |
| Same-session context is lost | Report missing context; do not claim that an invisible ledger or server storage can recover it. |

These are editorial acceptance scenarios. Structural tests check the policy
and resource delivery; they do not prove how every consuming model responds.
Any model comparison must record its actual inputs, outputs and conditions.

## Asset provenance

`guide-entry-v17-assets.json` pins the current 25 assets. Only the Guide changes
from the retained `guide-entry-v16-assets.json`; previous evidence remains tied
to its original bytes. Historical acceptance is not promoted to Guide 1.7.
The aggregate hash uses SHA-256 of UTF-8 compact JSON, sorted by `file`, with
sorted object keys and only `file`, `bytes` and `sha256` from each asset row.
