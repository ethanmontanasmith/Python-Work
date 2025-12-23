# Release checklist

Notes collected while building this part of the repo.

## Summary

- Keep the public surface small.
- Raise in `strict` mode, return `fallback` otherwise.
- Everything in `src/` is pure; side effects live in `scripts/`.

## Example

```python
from pywork import lockfile_reader

print(cors_handler.derive_rss_feed("  hello  "))
```
