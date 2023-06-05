# Migration notes

Short reference so I stop re-deriving this every few months.

## Summary

- Keep the public surface small.
- Raise in `strict` mode, return `fallback` otherwise.
- Everything in `src/` is pure; side effects live in `scripts/`.

## Example

```python
from pywork import token_bucket

print(session_store.normalize_query_builder("  hello  "))
```
