# Skill Specification: `arale`

This document specifies the exact structure, frontmatter, trigger phrases, body text, and enforcement rules for the `arale` agent skill.

## 1. Skill Folder Name and Directory Structure

- **Folder Name**: `arale`
- **Manifest File**: `SKILL.md`
- **Location in Skill Package**: `arale/SKILL.md`
- **No Helper Scripts or Assets**: The skill contains solely the manifest `SKILL.md`. It must not contain binary files, scripts, or extraneous markdown files.

```text
arale/
└── SKILL.md
```

---

## 2. Frontmatter Specification

The file `SKILL.md` must begin with YAML frontmatter delimited by opening and closing triple dashes (`---`).

- `name`: Must be `arale`.
- `description`: Must be exact text describing activation conditions and purpose:
  `Use when the user says "usa arale", "use arale", "con arale", or asks to apply the Arale procedures to a task (diagnose a problem, write a spec, design, plan, review, test, deliver). Runs the Arale workflow through the arale-code MCP server. Do not use for tasks where the user did not mention Arale.`

### Exact Frontmatter Block

```yaml
---
name: arale
description: Use when the user says "usa arale", "use arale", "con arale", or asks to apply the Arale procedures to a task (diagnose a problem, write a spec, design, plan, review, test, deliver). Runs the Arale workflow through the arale-code MCP server. Do not use for tasks where the user did not mention Arale.
---
```

---

## 3. Trigger Phrases

The skill must be activated if and only if the user query contains one of the following explicit triggers, or specifically references applying Arale procedures:

1. `usa arale`
2. `use arale`
3. `con arale`
4. Explicit request mentioning "Arale" or "Arale procedures" in conjunction with diagnostic, specification, design, planning, refactoring, review, or delivery work.

If the user does not explicitly mention Arale, the agent must not activate this skill.

---

## 4. Exact Content of `SKILL.md`

The following is the complete, exact content of `arale/SKILL.md`:

```markdown
---
name: arale
description: Use when the user says "usa arale", "use arale", "con arale", or asks to apply the Arale procedures to a task (diagnose a problem, write a spec, design, plan, review, test, deliver). Runs the Arale workflow through the arale-code MCP server. Do not use for tasks where the user did not mention Arale.
---

# Arale Control Workflow

Apply the Arale engineering procedures to guide autonomous, disciplined software delivery via the `arale-code` MCP server.

## 1. Operational Rules

When executing this skill, the agent must adhere to the following rules:

1. **Verify MCP Connectivity**: The agent must verify that the `arale-code` MCP server is registered and accessible before proceeding.
2. **Read Control Guide First**: For Arale-guided work, read `arale://procedure/guide` to select the smallest fitting procedure.
3. **Consult Catalog as Needed**: When a procedure ID is unknown, call `list_procedures` to discover valid IDs, titles, and URIs.
4. **Retrieve Procedure Content**: Read the selected procedure in full at `arale://procedure/{id}` (e.g., `arale://procedure/p08-contracts-compatibility`) before executing it.
5. **Read Instructions as Needed**: When procedural steps require general software engineering guidance, the agent must call `list_instructions` and retrieve the corresponding document from `instructions://document/{id}`.
6. **Enforce Read-Only Boundaries**: All instructions and procedures provided by `arale-code` are strictly read-only engineering standards.
7. **Stateless Operations**: Every procedure is self-contained. The agent must not assume state persistence across independent invocations.

## 2. Procedure Selection

1. Read `arale://procedure/guide` and follow its routing and protocol rules.
2. Choose the smallest fitting procedure; ask only for a material missing decision or report a coverage limit when no procedure fits.
3. Read the selected `arale://procedure/{id}` resource in full. If it cannot be read, ask for the file; do not reconstruct it from the Guide.
4. Continue only necessary authorized work and reconcile before any justified transition.
```

---

## 5. Rules Enforced by the Skill

1. **Naming Integrity**: The skill must be identified strictly as `arale`. It must not use legacy or alternative names.
2. **Server Association**: The skill must interact exclusively with the `arale-code` MCP server STDIO tools (`list_procedures`, `list_instructions`, `apply_instruction`) and resources (`arale://catalog`, `arale://procedure/{id}`, `instructions://catalog`, `instructions://document/{id}`).
3. **Trigger Scoping**: The skill must not execute automatically for general coding tasks unless the user explicitly invokes Arale.
4. **Deterministic Guidance**: The agent must use the Guide routing rules to select one fitting procedure, read that procedure in full, and apply its relevant verification gates.
