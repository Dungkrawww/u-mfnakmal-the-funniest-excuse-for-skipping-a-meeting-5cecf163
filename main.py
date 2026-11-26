#!/usr/bin/env python3
"""Funniest Excuse for Skipping a Meeting — make.fun one-liner entry.

Writes a single funny excuse line to /output/entry.txt (the file the
gate scorer checks) and prints the same line to stdout.
"""

import os

EXCUSE = (
    "I have to skip this one \u2014 I've already attended it three times "
    "in my head, and in every version we still end with "
    "'let's circle back.'"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)
    print(EXCUSE)


if __name__ == "__main__":
    main()
