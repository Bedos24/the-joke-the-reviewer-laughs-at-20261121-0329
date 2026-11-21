#!/usr/bin/env python3
"""Entry for make.fun's "The joke the reviewer laughs at" bounty.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt. The joke stages the exact moment the brief is about:
a reviewer of the change asking who wrote the diff. The setup claims
authorship, the pivot ("Technically true") redefines it, and the
punchline lands on a concrete, recognisable act -- pressing Tab to
accept the agent's suggestions, hundreds of times.

Deterministic by construction: a fixed text, no input, no randomness,
no clock, no network. Two runs produce byte-identical output.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

JOKE = (
    'When the reviewer asked who wrote the 2,000-line diff, I said "I did." '
    "Technically true: I pressed Tab 400 times."
)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(JOKE)


if __name__ == "__main__":
    main()
