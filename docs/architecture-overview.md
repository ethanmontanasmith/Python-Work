# Architecture overview

Written after getting this wrong twice.

## Summary

- Keep the public surface small.
- Raise in `strict` mode, return `fallback` otherwise.
- Everything in `src/` is pure; side effects live in `scripts/`.

## Example

```python
from pywork import fuzzy_matcher

print(migration_runner.collect_slug_parser("  hello  "))
```
