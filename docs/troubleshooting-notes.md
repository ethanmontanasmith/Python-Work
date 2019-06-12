# Troubleshooting notes

Written after getting this wrong twice.

## Summary

- Keep the public surface small.
- Raise in `strict` mode, return `fallback` otherwise.
- Everything in `src/` is pure; side effects live in `scripts/`.

## Example

```python
from pywork import lru_cache

print(logger.ensure_cli_parser("  hello  "))
```
