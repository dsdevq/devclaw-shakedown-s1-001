# Feature Specification: word_count Utility

**Feature Branch**: `001-wordcount`

**Created**: 2026-08-17

**Status**: Approved

## User Scenarios & Testing

### User Story 1 - word_count Python utility (Priority: P1)

A developer calls `word_count(text)` and receives the count of whitespace-separated words in `text`. Empty or whitespace-only input returns 0.

**Why this priority**: Core deliverable — the entire feature is this one function.

**Independent Test**: Import `word_count` from the module and assert return values against known inputs.

**Acceptance Scenarios**:

1. **Given** `text = "hello world"`, **When** `word_count(text)` is called, **Then** returns `2`.
2. **Given** `text = ""`, **When** `word_count(text)` is called, **Then** returns `0`.
3. **Given** `text = "  "`, **When** `word_count(text)` is called, **Then** returns `0`.
4. **Given** `text = "one  two\tthree\nfour"`, **When** `word_count(text)` is called, **Then** returns `4`.

---

### Edge Cases

- Empty string → 0
- String containing only spaces, tabs, newlines → 0
- Multiple consecutive whitespace characters between words
- Tabs and newlines as delimiters

## Requirements

### Functional Requirements

- **FR-001**: `word_count(text: str) -> int` MUST exist in a `word_count` module importable from the repo root.
- **FR-002**: Function MUST split on any whitespace (spaces, tabs, newlines) using Python's default `str.split()` semantics.
- **FR-003**: Empty string and whitespace-only string MUST return `0`.
- **FR-004**: A pytest suite MUST cover: normal sentence, multiple spaces, tabs/newlines, empty string.

## Success Criteria

- **SC-001**: `python -m pytest` exits 0 with all word_count tests passing.
- **SC-002**: `word_count("")` returns `0`.
- **SC-003**: `word_count("  \t\n  ")` returns `0`.
- **SC-004**: `word_count("hello world")` returns `2`.

## Assumptions

- Python 3.x stdlib only; no external dependencies needed.
- Tests live in `tests/test_word_count.py`.
- The module file is `word_count.py` at the repository root.
