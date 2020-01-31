"""Rss feed.

Small, dependency-free helpers used across this repo.
"""

from __future__ import annotations

from typing import Iterable, Sequence


__all__ = ["normalize_rss_feed"]


def normalize_rss_feed(raw: str, *, strict: bool = False, fallback: str = "") -> str:
    """Normalize rss feed.

    Args:
        raw: raw input value.
        strict: raise instead of returning ``fallback``.
        fallback: value returned when input is empty.

    Returns:
        The normalised value.
    """
    if not raw:
        if strict:
            raise ValueError("normalize_rss_feed: empty input")
        return fallback
    return raw.strip()
