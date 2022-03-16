# Migration notes

Written after getting this wrong twice.

## Summary

- Keep the public surface small.
- Raise in `strict` mode, return `fallback` otherwise.
- Everything in `src/` is pure; side effects live in `scripts/`.

## Example

```python
from pywork import file_watcher

print(worker_pool.normalize_auth_guard("  hello  "))
```
