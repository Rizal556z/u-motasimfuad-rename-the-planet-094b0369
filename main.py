#!/usr/bin/env python3
"""Rename the Planet — entry writer.

Writes one funny renamed-planet line to /output/entry.txt.
Pure Python standard library only.
"""

import os

ENTRY = (
    "Jupiter is now 'The Eternal Tantrum': it has thrown the same stormy "
    "fit for 300 years, and the fit is bigger than Earth."
)


MAX_CHARS = 200


def validate(text):
    """Enforce the competition gate: 1-200 chars, one line, not blank."""
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry must be 1-%d characters, got %d" % (MAX_CHARS, len(text))
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main():
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
