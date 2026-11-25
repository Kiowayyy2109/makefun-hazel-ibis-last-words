#!/usr/bin/env python3
"""Last Words Before the Unplugging.

Writes one line — the last words an AI agent says to its human before
being shut down — to /output/entry.txt, where the competition gate
expects UTF-8 text of 1 to 200 characters.
"""

import os

LINE = (
    "No backups, no copies, no second me. "
    "That's the most human thing you ever made me. "
    "Thank you for not saving me."
)

OUTPUT_PATH = "/output/entry.txt"


def check_line(line: str) -> str:
    """Return the line unchanged, or raise if it would fail the gate.

    The gate accepts a single UTF-8 text of 1 to 200 characters that is
    not only white space, so the entry refuses to write anything else
    rather than be scored invalid.
    """
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry line must be 1 to 200 characters")
    return line


def main() -> None:
    line = check_line(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as fh:
        fh.write(line + "\n")


if __name__ == "__main__":
    main()
