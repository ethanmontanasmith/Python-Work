# Release checklist

Written after getting this wrong twice.

## Summary

- Keep the public surface small.
- Raise in `strict` mode, return `fallback` otherwise.
- Everything in `src/` is pure; side effects live in `scripts/`.

## Example

```python
from pywork import rate_limiter

print(markdown_renderer.derive_cli_parser("  hello  "))
```
