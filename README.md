# Python-Work

A long-running personal Python repo: small utilities, dated working
notes, and whatever I happened to be learning that week. Standard
library only - no runtime dependencies.

## Layout

```
src/pywork/   small, dependency-free helpers
tests/        pytest suites
notes/        dated working notes
docs/         longer write-ups
scripts/      one-off maintenance scripts
```

## Getting started

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pip install -e .
pytest
```

## License

MIT
