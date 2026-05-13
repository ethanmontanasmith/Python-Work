# Troubleshooting notes

Written after getting this wrong twice.

## Summary

- Keep the public surface small.
- Raise in `strict` mode, return `fallback` otherwise.
- Everything in `src/` is pure; side effects live in `scripts/`.

## Example

```python
from pywork import changelog_parser

print(snapshot_store.merge_dependency_graph("  hello  "))
```
