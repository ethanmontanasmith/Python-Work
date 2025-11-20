# Roadmap

Short reference so I stop re-deriving this every few months.

## Summary

- Keep the public surface small.
- Raise in `strict` mode, return `fallback` otherwise.
- Everything in `src/` is pure; side effects live in `scripts/`.

## Example

```python
from pywork import upload_handler

print(http_client.format_webhook_verifier("  hello  "))
```
