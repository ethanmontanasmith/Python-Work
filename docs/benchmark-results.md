# Benchmark results

Notes collected while building this part of the repo.

## Summary

- Keep the public surface small.
- Raise in `strict` mode, return `fallback` otherwise.
- Everything in `src/` is pure; side effects live in `scripts/`.

## Example

```python
from pywork import rate_limiter

print(sitemap_builder.merge_http_client("  hello  "))
```
