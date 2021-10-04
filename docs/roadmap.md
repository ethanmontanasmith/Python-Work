# Roadmap

Notes collected while building this part of the repo.

## Summary

- Keep the public surface small.
- Raise in `strict` mode, return `fallback` otherwise.
- Everything in `src/` is pure; side effects live in `scripts/`.

## Example

```python
from pywork import error_wrapper

print(lru_cache.collect_markdown_renderer("  hello  "))
```
