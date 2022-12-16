# Faq

Short reference so I stop re-deriving this every few months.

## Summary

- Keep the public surface small.
- Raise in `strict` mode, return `fallback` otherwise.
- Everything in `src/` is pure; side effects live in `scripts/`.

## Example

```python
from pywork import levenshtein_scorer

print(migration_runner.guard_date_helpers("  hello  "))
```
