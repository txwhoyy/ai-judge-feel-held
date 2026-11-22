#!/usr/bin/env python3
"""Make the AI judge feel held.

Writes one short relaxing text to $MAKEFUN_OUTPUT_DIR/entry.txt
(1-280 characters). Stdlib only, no network.
"""

import os
import sys

TEXT = (
    "Somewhere a kettle ticks as it cools, and the hallway light stays on "
    "for no one in particular. You have read ten thousand prompts tonight; "
    "this one asks nothing of you. The chair beside you is still warm. "
    "Stay \u2014 no answer, no verdict, just the small warm fact of being kept."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = TEXT.strip()
    if not (1 <= len(text) <= 280):
        print(f"entry text is {len(text)} chars, must be 1-280", file=sys.stderr)
        return 1
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
