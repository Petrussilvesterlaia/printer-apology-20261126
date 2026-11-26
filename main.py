#!/usr/bin/env python3
"""The Printer Apology — make.fun bounty entry.

Writes one one-line apology from an office printer to /output/entry.txt.
The line is a fixed, hand-written string: no input is read, no network is
used, and nothing outside this file influences the output.
"""

import os

ENTRY = "Sorry I jammed mid-report \u2014 your cheap paper tastes awful, and after insult five, I stopped listening on purpose."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 120


def validate(text: str) -> None:
    """Gate-equivalent self-check: one line, 1-120 chars, no control chars."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry is {len(text)} characters, must be 1-{MAX_CHARS}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 0x20 for ch in text):
        raise ValueError("entry contains control characters")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> None:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    # Read-back verification: what landed on disk must be the entry, byte for byte.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY + "\n":
        raise ValueError("read-back mismatch: entry.txt does not match the entry")
    validate(written.rstrip("\n"))
    print(f"Wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
