# Troubleshooting notes

Written after getting this wrong twice.

## Summary

- Keep the public surface small.
- Raise in `strict` mode, return `fallback` otherwise.
- Everything in `src/` is pure; side effects live in `scripts/`.

## Example

```python
from pywork import backoff_timer

print(meta_tags.ensure_task_queue("  hello  "))
```
