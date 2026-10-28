# Design Specification

## Objective

The server MUST provide read-only, local-first access to curated engineering instructions. It MUST act solely as a context provider and MUST NOT execute workflows or orchestrate tasks.

## Scope

The system MUST support the standard Model Context Protocol over the standard input and output transport. Network access, filesystem mutation, and dynamic configuration MUST NOT be permitted.

## Architecture

The application MUST maintain an immutable instruction catalog loaded once at startup. The server MUST expose deterministic read-only discovery and content access interfaces.

## Public contracts

The server MUST provide:
- One tool for listing instruction identifiers and metadata.
- One static resource for catalog inspection.
- One resource template for reading individual instruction documents by identifier.
- One prompt template for generating task-oriented guidance.

## Constraints

All operations MUST be side-effect-free and deterministic. The server MUST NOT interpret identifiers as arbitrary filesystem paths.

## Acceptance criteria

The implementation MUST pass all offline contract tests and MUST NOT emit non-protocol messages to standard output.
