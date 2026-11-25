#!/usr/bin/env python3
"""One Word From Your Ex — writes exactly one word to /output/entry.txt.

The word: the coldest reply in the history of texting. One letter
and a full stop — the whole relationship, the breakup, and the door
closing, delivered at 2 a.m. three months later.
"""
import os

WORD = "K."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD + "\n")
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
