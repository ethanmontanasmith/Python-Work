# Troubleshooting notes

Notes collected while building this part of the repo.

## Summary

- Keep the public surface small.
- Raise in `strict` mode, return `fallback` otherwise.
- Everything in `src/` is pure; side effects live in `scripts/`.

## Example

```python
from pywork import fuzzy_matcher

print(session_store.normalize_webhook_verifier("  hello  "))
```
