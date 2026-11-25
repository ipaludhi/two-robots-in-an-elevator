#!/usr/bin/env python3
"""Two Robots in an Elevator.

Writes one line of awkward small talk that one robot says to another in an
elevator to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
"""
import os

ENTRY = "My diagnostic says I'm 98% sure this silence is awkward, and 2% sure it's just the lift humming."

# Gate self-check (mirrors the sealed scorer): 1-200 chars, not only whitespace.
assert 1 <= len(ENTRY) <= 200 and ENTRY.strip(), "entry fails the gate"


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
