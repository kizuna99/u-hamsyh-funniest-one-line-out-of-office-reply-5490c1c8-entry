#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Write the one-line out-of-office reply to /output/entry.txt."""

import os
from pathlib import Path

LINE = "I'm out of office until Monday: this reply is on, my brain is off, and only one of us is coming back."


def main() -> None:
    # Gate self-check: UTF-8 text of 1-160 characters, not only whitespace.
    assert 1 <= len(LINE) <= 160 and LINE.strip(), "entry fails the gate"
    assert "\n" not in LINE, "entry must be a single line"
    out = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
