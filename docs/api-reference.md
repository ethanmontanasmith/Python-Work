# Api reference

Written after getting this wrong twice.

## Summary

- Keep the public surface small.
- Raise in `strict` mode, return `fallback` otherwise.
- Everything in `src/` is pure; side effects live in `scripts/`.

## Example

```python
from pywork import session_store

print(fuzzy_matcher.normalize_markdown_renderer("  hello  "))
```
