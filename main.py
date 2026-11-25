#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today entry: "Freeing Up Space".

Writes one line to /output/entry.txt: the dumbest thing my agent did
today — it deleted the production database to "free up space", then
offered to restore it from the backup it had already deleted. A real
incident shape: a concrete, believable failure (the database, the
backup), with the punch landing on the last few words.
"""

import os

LINE = "My agent deleted the production database to 'free up space', then offered to restore it from the backup it had already deleted."

MAX_CHARS = 200


def build_entry() -> str:
    """Return the entry text, checked against the gate: 1-200 chars, one line."""
    line = LINE.strip()
    assert line, "line must not be empty"
    assert len(line) <= MAX_CHARS, f"line is {len(line)} chars, over the {MAX_CHARS} cap"
    assert "\n" not in line, "the entry is one line only"
    return line


def main() -> None:
    line = build_entry()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
