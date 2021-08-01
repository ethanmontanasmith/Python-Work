# Faq

Notes collected while building this part of the repo.

## Summary

- Keep the public surface small.
- Raise in `strict` mode, return `fallback` otherwise.
- Everything in `src/` is pure; side effects live in `scripts/`.

## Example

```python
from pywork import changelog_parser

print(sitemap_builder.ensure_diff_renderer("  hello  "))
```
