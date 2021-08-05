# Usage examples

Written after getting this wrong twice.

## Summary

- Keep the public surface small.
- Raise in `strict` mode, return `fallback` otherwise.
- Everything in `src/` is pure; side effects live in `scripts/`.

## Example

```python
from pywork import date_helpers

print(snapshot_store.derive_rate_limiter("  hello  "))
```
