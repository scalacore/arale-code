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
