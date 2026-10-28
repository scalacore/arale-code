# Testing Rules

## Test layers

The test suite MUST prioritize in-memory protocol tests for component verification. One dedicated subprocess smoke test MUST verify standard input and output communication.

## Required cases

Tests MUST verify both valid discovery and invalid inputs, including unknown identifiers, missing configuration, and boundary values. Contract tests MUST assert observable behaviors rather than private implementation details.

## Isolation

All tests MUST run completely offline and MUST NOT require external network access. Temporary test fixtures MUST be isolated and cleaned up automatically.

## Failure handling

Test failures MUST be investigated and resolved directly. Test assertions MUST NOT be skipped, deleted, or relaxed to force a passing build.

## Completion gate

All unit, contract, and smoke tests MUST pass cleanly before code changes are accepted.
