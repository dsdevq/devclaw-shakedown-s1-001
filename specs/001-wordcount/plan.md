# Implementation Plan: word_count Utility

**Branch**: `001-wordcount` | **Date**: 2026-08-17 | **Spec**: [spec.md](spec.md)

## Summary

Implement `word_count(text: str) -> int` in `word_count.py` at the repo root. Use `str.split()` (no argument) which splits on any whitespace and collapses runs, making the empty/whitespace-only → 0 case trivially correct. Pair with a pytest suite in `tests/test_word_count.py`.

## Technical Context

**Language/Version**: Python 3.x  
**Primary Dependencies**: stdlib only (no external packages)  
**Storage**: N/A  
**Testing**: pytest (`python -m pytest`)  
**Target Platform**: Linux  
**Project Type**: library utility  
**Performance Goals**: N/A  
**Constraints**: No external deps  
**Scale/Scope**: Single function + test file

## Project Structure

```text
word_count.py          # module with word_count()
tests/
└── test_word_count.py # pytest suite
specs/001-wordcount/
├── spec.md
├── plan.md
└── tasks.md
```

**Structure Decision**: Flat layout — no src/ wrapper needed for a single-function utility. pytest discovers `tests/` by default.

## Judgment Calls

- `str.split()` without args handles multiple spaces, tabs, newlines, and leading/trailing whitespace in one step — no regex, no edge-case juggling.
- Module placed at repo root (not under `src/`) to keep imports simple: `from word_count import word_count`.
