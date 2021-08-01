# Benchmark results

Notes collected while building this part of the repo.

## Summary

- Keep the public surface small.
- Raise in `strict` mode, return `fallback` otherwise.
- Everything in `src/` is pure; side effects live in `scripts/`.

## Example

```python
from pywork import dependency_graph

print(markdown_renderer.build_topological_sort("  hello  "))
```
