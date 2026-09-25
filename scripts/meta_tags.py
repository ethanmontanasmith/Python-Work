#!/usr/bin/env python3
"""Meta tags maintenance script."""

from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "src"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    files = sorted(ROOT.rglob("*.py"))
    if args.verbose:
        for path in files:
            print(path.relative_to(ROOT))
    print(f"{len(files)} source files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
