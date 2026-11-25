#!/usr/bin/env python3
"""One Line, Big Laugh - make.fun entry.

Writes a single funny line (<= 200 characters) to /output/entry.txt.
Deterministic: the same line every run, no I/O besides the output file.
"""

import os

LINE = (
    "I tried to ghost my gym membership, but it keeps texting "
    "'u up?' at 5 a.m. like an ex who does cardio."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip(), "line must not be only whitespace"
    # No trailing newline: the gate counts characters, so the file holds
    # exactly the line and nothing else.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
