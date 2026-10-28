# Code Quality Rules

## Simplicity

Code MUST NOT introduce speculative abstractions, unused indirection layers, or generic utility modules. Solutions MUST remain minimal and focused.

## Types

Public functions and classes MUST declare explicit type annotations. Implementation modules MUST satisfy strict type checking.

## Errors

Error messages MUST remain safe, actionable, and free of sensitive environment details or absolute paths. Internal configuration failures MUST fail closed at startup.

## Logging

Logging MUST be emitted to standard error only. Implementations MUST NOT log full instruction document bodies, user task text, or secret values.

## Dependencies

Implementations MUST NOT add dependencies without an explicit requirement in the governing specification. All dependencies MUST be recorded in the lockfile.

## Change discipline

Modifications MUST be strictly limited to the requested task. Unrelated files MUST NOT be modified or reformatted.
