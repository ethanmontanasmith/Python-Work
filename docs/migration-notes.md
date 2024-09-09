# Migration notes

Short reference so I stop re-deriving this every few months.

## Summary

- Keep the public surface small.
- Raise in `strict` mode, return `fallback` otherwise.
- Everything in `src/` is pure; side effects live in `scripts/`.

## Example

```python
from pywork import csv_reader

print(table_formatter.ensure_changelog_parser("  hello  "))
```
