# Product Scope

## 1. Purpose

`arale-code` is a read-only Model Context Protocol (MCP) server and procedure library. It delivers curated software engineering procedures and instructions directly to AI coding agents over standard input and output (STDIO).

## 2. Target Users and Clients

### 2.1 Users
- Software developers and engineers pairing with AI coding agents.
- Autonomous coding agents operating in terminal, IDE, or background agent environments.

### 2.2 Target Clients
- Codex CLI
- Claude Code
- Cursor
- OpenCode
- Antigravity CLI

### 2.3 Target Operating Systems
- macOS
- Linux
- Windows

## 3. In Scope

- Server execution strictly over local STDIO transport.
- Provision of four engineering instruction documents (`design-spec`, `implementation-plan`, `code-quality`, `testing`) formatted in Markdown (`text/markdown`).
- Provision of twenty-one structured engineering procedure files (`guide` and `p01` through `p20`) formatted in YAML (`application/yaml`).
- Deterministic catalog serialization in JSON (`application/json`).
- Public tools `list_instructions` and `list_procedures`.
- Public static resources `instructions://catalog` and `arale://catalog`.
- Public resource templates `instructions://document/{id}` and `arale://procedure/{id}`.
- Public prompt template `apply_instruction`.
- Strict input validation, error masking, and offline operation.
- Re-computed SHA-256 integrity validation of all bundled assets.

## 4. Out of Scope

- Remote network protocols including HTTP, Server-Sent Events (SSE), and WebSockets.
- Database systems, persistent key-value storage, caching systems, or mutable state stores.
- Direct execution of shell commands, workflow orchestration, or filesystem mutation by the server.
- Installation, management, or execution of external client binaries.
- Authentication handshakes, dynamic client registration, or credential providers.

## 5. Non-Goals

- `arale-code` must not act as a task runner, scheduler, or execution sandbox.
- `arale-code` must not modify files within user repositories.
- `arale-code` must not establish outbound network connections.
- `arale-code` must not maintain state across or within client sessions.
