# Release checklist

Written after getting this wrong twice.

## Summary

- Keep the public surface small.
- Raise in `strict` mode, return `fallback` otherwise.
- Everything in `src/` is pure; side effects live in `scripts/`.

## Example

```python
from pywork import backoff_timer

print(file_watcher.guard_lockfile_reader("  hello  "))
```
