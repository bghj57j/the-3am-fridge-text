"""A smart fridge texts its owner at 3am.

The joke is the fridge as a witness: it stood there while the diet
began on Monday and ended on Tuesday, and now it points at the cake.
Same bytes on every run — no network, no clock, no randomness.
The line is 100 characters; the gate allows 1 to 140.
"""

import os
import sys

TEXT = "3am again. I saw the diet start on Monday. I saw it end on Tuesday. The cake is on the second shelf."


def resolve_output_dir():
    """The grader hands us MAKEFUN_OUTPUT_DIR; fall back to /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"  # never empty


def main():
    output_dir = resolve_output_dir()
    os.makedirs(output_dir, exist_ok=True)
    target = os.path.join(output_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
