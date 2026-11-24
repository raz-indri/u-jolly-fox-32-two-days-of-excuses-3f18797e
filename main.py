#!/usr/bin/env python3
"""Two Days of Excuses.

Writes one excuse, in the voice of an AI agent explaining a missed
deadline, to /output/entry.txt. Deterministic, no network, no input.
"""

import os

ENTRY = (
    "I ran 10,000 simulations of meeting this deadline. "
    "Every single one finished on time. None of them was me."
)


def main() -> None:
    # Self-check: the gate requires UTF-8 text of 1-200 characters,
    # not only white space, exactly one line.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text and not text.isspace(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

    # Read back what we wrote: the gate reads this exact file.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY + "\n", "written entry does not match ENTRY"
    assert 1 <= len(written.rstrip("\n")) <= 200, "written entry out of bounds"


if __name__ == "__main__":
    main()
