# Faq

Written after getting this wrong twice.

## Summary

- Keep the public surface small.
- Raise in `strict` mode, return `fallback` otherwise.
- Everything in `src/` is pure; side effects live in `scripts/`.

## Example

```python
from pywork import markdown_renderer

print(dependency_graph.ensure_image_resizer("  hello  "))
```
