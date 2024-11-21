# Benchmark results

Written after getting this wrong twice.

## Summary

- Keep the public surface small.
- Raise in `strict` mode, return `fallback` otherwise.
- Everything in `src/` is pure; side effects live in `scripts/`.

## Example

```python
from pywork import json_schema

print(stopword_filter.derive_meta_tags("  hello  "))
```
