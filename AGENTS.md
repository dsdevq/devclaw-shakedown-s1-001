# AGENTS.md

## Repository

`devclaw-shakedown-s1-001` — devclaw shakedown scenario S1 run 001.

## Stack

- **Language**: Python 3.13 (stdlib only for this project)
- **Test runner**: pytest (`python -m pytest`)
- **Speckit**: `.specify/` scaffold; feature artifacts in `specs/NNN-*/`

## Verify command

```bash
python -m pytest
```

All tests must pass before a change is considered done.

## Layout

```
word_count.py          # word_count(text) utility
tests/
└── test_word_count.py # pytest suite for word_count
specs/001-wordcount/   # speckit artifacts for this feature
.specify/              # speckit scripts and templates
```

## Gotchas

- `pytest` is NOT on PATH by default in this environment; invoke via `python -m pytest`.
- `pip install pytest` installs to `~/.local/bin` which may not be on PATH — use the module form above.
- No `pyproject.toml` or `requirements.txt` currently exists; pytest is the only non-stdlib dep.
