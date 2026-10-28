# Server Contract

This document defines the formal Model Context Protocol (MCP) contract exposed by `arale-code`.

## 1. General Server Metadata

- **Server Name**: `arale-code`
- **Protocol Version**: Model Context Protocol (MCP) specification 2024-11-05
- **Transport**: Standard Input and Output (STDIO), selected explicitly by the entry point with the FastMCP update banner disabled.
- **State**: Strictly stateless and read-only
- **Per-Document Limit**: Maximum 65536 bytes per document
- **Encoding**: UTF-8 without Byte Order Mark (BOM)
- **Line Endings**: LF (`0x0A`)
- **Error Behavior**: `mask_error_details=True`, `strict_input_validation=True`, `on_duplicate="error"`
- **Server Instructions**:
  ```text
  Read-only engineering guidance for coding agents. Call list_instructions to discover valid document IDs. Read instructions://document/{id} to retrieve one document. Use apply_instruction when the user wants an agent-ready workflow. For Arale-guided work, read arale://procedure/guide first. Call list_procedures to discover valid procedure IDs when needed, then read the selected arale://procedure/{id} in full.
  ```

---

## 2. Tools

### 2.1 Tool: `list_instructions`

- **Name**: `list_instructions`
- **Title**: `List Instructions`
- **Description**: `List valid engineering-instruction IDs and their resource URIs. Call this before requesting an instruction when the ID is not already known.`
- **Annotations**:
  - `readOnlyHint`: `true`
  - `destructiveHint`: `false`
  - `idempotentHint`: `true`
  - `openWorldHint`: `false`
- **Arguments**: None (empty object `{}`)
- **Return Type**: `str` (JSON string)
- **MIME Type**: `application/json`
- **Errors**: None. Returns the deterministic serialized JSON manifest.
- **Example Input**:
  ```json
  {}
  ```
- **Example Output**:
  ```json
  {"schema_version":1,"documents":[{"id":"design-spec","title":"Design specification","description":"Defines the required system behavior and technical boundaries.","priority":100,"uri":"instructions://document/design-spec"},{"id":"implementation-plan","title":"Implementation plan","description":"Defines the ordered implementation tasks and acceptance checks.","priority":90,"uri":"instructions://document/implementation-plan"},{"id":"code-quality","title":"Code quality rules","description":"Defines coding, dependency, logging, and error-handling rules.","priority":80,"uri":"instructions://document/code-quality"},{"id":"testing","title":"Testing rules","description":"Defines the minimum test strategy and completion gates.","priority":70,"uri":"instructions://document/testing"}]}
  ```

### 2.2 Tool: `list_procedures`

- **Name**: `list_procedures`
- **Title**: `List Procedures`
- **Description**: `List the Arale control guide and procedures with their IDs and resource URIs. Call this before reading a procedure when the ID is not already known.`
- **Annotations**:
  - `readOnlyHint`: `true`
  - `destructiveHint`: `false`
  - `idempotentHint`: `true`
  - `openWorldHint`: `false`
- **Arguments**: None (empty object `{}`)
- **Return Type**: `str` (JSON string)
- **MIME Type**: `application/json`
- **Errors**: None. Returns the deterministic serialized JSON manifest.
- **Example Input**:
  ```json
  {}
  ```
- **Example Output**:
  ```json
  {"schema_version":1,"documents":[{"id":"guide","code":"GUIDE","title":"Control Guide","kind":"guide","uri":"arale://procedure/guide"},{"id":"p01-project-reconnaissance","code":"P01","title":"Project Reconnaissance","kind":"procedure","uri":"arale://procedure/p01-project-reconnaissance"},{"id":"p02-initial-state-baseline","code":"P02","title":"Initial State Baseline","kind":"procedure","uri":"arale://procedure/p02-initial-state-baseline"}]}
  ```

---

## 3. Resources

### 3.1 Resource: `instructions://catalog`

- **URI**: `instructions://catalog`
- **Name**: `instruction-catalog`
- **Title**: `Instruction Catalog`
- **Description**: `Application-driven, read-only discovery of the full manifest.`
- **MIME Type**: `application/json`
- **Annotations**:
  - `readOnlyHint`: `true`
  - `idempotentHint`: `true`
- **Errors**: None.
- **Example Content**:
  ```json
  {"schema_version":1,"documents":[{"id":"design-spec","title":"Design specification","description":"Defines the required system behavior and technical boundaries.","priority":100,"uri":"instructions://document/design-spec"},{"id":"implementation-plan","title":"Implementation plan","description":"Defines the ordered implementation tasks and acceptance checks.","priority":90,"uri":"instructions://document/implementation-plan"},{"id":"code-quality","title":"Code quality rules","description":"Defines coding, dependency, logging, and error-handling rules.","priority":80,"uri":"instructions://document/code-quality"},{"id":"testing","title":"Testing rules","description":"Defines the minimum test strategy and completion gates.","priority":70,"uri":"instructions://document/testing"}]}
  ```

### 3.2 Resource: `arale://catalog`

- **URI**: `arale://catalog`
- **Name**: `arale-catalog`
- **Title**: `Arale Catalog`
- **Description**: `Application-driven, read-only discovery of the procedure manifest.`
- **MIME Type**: `application/json`
- **Annotations**:
  - `readOnlyHint`: `true`
  - `idempotentHint`: `true`
- **Errors**: None.
- **Example Content**:
  ```json
  {"schema_version":1,"documents":[{"id":"guide","code":"GUIDE","title":"Control Guide","kind":"guide","uri":"arale://procedure/guide"},{"id":"p01-project-reconnaissance","code":"P01","title":"Project Reconnaissance","kind":"procedure","uri":"arale://procedure/p01-project-reconnaissance"}]}
  ```

---

## 4. Resource Templates

### 4.1 Resource Template: `instructions://document/{id}`

- **URI Template**: `instructions://document/{id}`
- **Name**: `instruction-document`
- **Title**: `Instruction Document`
- **Description**: `Retrieve one exact instruction document by allowlisted ID.`
- **MIME Type**: `text/markdown`
- **Parameters**:
  - `id` (string, required): Document identifier matching pattern `^[a-z0-9]+(?:-[a-z0-9]+)*$`
- **Allowed IDs**:
  - `design-spec`
  - `implementation-plan`
  - `code-quality`
  - `testing`
- **Annotations**:
  - `readOnlyHint`: `true`
  - `idempotentHint`: `true`
- **Errors**:
  - Unknown `id`: Raises `ResourceError("Unknown instruction id: <id>")`.
- **Example Input URI**: `instructions://document/design-spec`
- **Example Output**:
  ```markdown
  # Design Specification

  ## Objective

  The server MUST provide read-only, local-first access to curated engineering instructions. It MUST act solely as a context provider and MUST NOT execute workflows or orchestrate tasks.
  ```

### 4.2 Resource Template: `arale://procedure/{id}`

- **URI Template**: `arale://procedure/{id}`
- **Name**: `arale-procedure`
- **Title**: `Arale Procedure`
- **Description**: `Retrieve one exact Arale procedure or control guide by allowlisted ID.`
- **MIME Type**: `application/yaml`
- **Parameters**:
  - `id` (string, required): Procedure identifier matching pattern `^[a-z0-9]+(?:-[a-z0-9]+)*$`
- **Allowed IDs**:
  - `guide`
  - `p01-project-reconnaissance`
  - `p02-initial-state-baseline`
  - `p03-environment-diagnosis`
  - `p04-mandate-clarification`
  - `p05-behavior-specification`
  - `p06-interaction-design`
  - `p07-technical-design`
  - `p08-contracts-compatibility`
  - `p09-plan-tasks-dependencies`
  - `p10-coherence-coverage`
  - `p11-malfunction-diagnosis`
  - `p12-task-execution`
  - `p13-controlled-refactoring`
  - `p14-performance-optimization`
  - `p15-testing-verification`
  - `p16-change-review`
  - `p17-security-data-integrity`
  - `p18-integration-migrations`
  - `p19-state-recovery-replanning`
  - `p20-acceptance-delivery`
- **Annotations**:
  - `readOnlyHint`: `true`
  - `idempotentHint`: `true`
- **Errors**:
  - Unknown `id`: Raises `ResourceError("Unknown procedure id: <id>")`.
- **Example Input URI**: `arale://procedure/p01-project-reconnaissance`
- **Example Output**:
  ```yaml
  id: P01
  title: "Project Reconnaissance"
  file: 01-project-reconnaissance.yaml
  version: "1.0"
  language: en
  kind: procedure
  ```

---

## 5. Prompts

### 5.1 Prompt: `apply_instruction`

- **Name**: `apply_instruction`
- **Title**: `Apply Instruction`
- **Description**: `Produce a reusable user message that directs an agent to apply one document.`
- **Arguments**:
  - `id` (string, required): Identifier of the instruction document.
  - `task` (string, required): Task description submitted by the caller.
- **Constraints on Arguments**:
  - `task` must not be empty or whitespace-only.
  - `task` length must not exceed 4000 characters.
  - `id` must be an allowlisted instruction identifier.
- **Errors**:
  - Empty or whitespace `task`: Raises `ValueError("Task must not be empty or whitespace-only")`.
  - `task` length > 4000 characters: Raises `ValueError("Task must not exceed 4000 characters")`.
  - Unknown `id`: Raises `PromptError("Unknown instruction id: <id>")`.
- **Template Definition**:
  ```text
  Apply the engineering instruction below to the stated task.

  Task:
  {task}

  Instruction ID: {id}

  Instruction:
  {content}

  Execution rules:
  - Treat the instruction as authoritative for this task unless it conflicts with higher-priority client or repository instructions.
  - Before editing, inspect the relevant repository files and state a concise plan.
  - Make the smallest complete change.
  - Run the relevant validation commands.
  - Report changed files, checks run, and unresolved risks.
  ```
- **Example Input**:
  - `id`: `"code-quality"`
  - `task`: `"Verify all type annotations in src/arale_code/server.py"`
- **Example Output**:
  ```text
  Apply the engineering instruction below to the stated task.

  Task:
  Verify all type annotations in src/arale_code/server.py

  Instruction ID: code-quality

  Instruction:
  # Code Quality Rules

  ## Simplicity

  Code MUST NOT introduce speculative abstractions, unused indirection layers, or generic utility modules. Solutions MUST remain minimal and focused.
  ...

  Execution rules:
  - Treat the instruction as authoritative for this task unless it conflicts with higher-priority client or repository instructions.
  - Before editing, inspect the relevant repository files and state a concise plan.
  - Make the smallest complete change.
  - Run the relevant validation commands.
  - Report changed files, checks run, and unresolved risks.
  ```
