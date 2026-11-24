#!/usr/bin/env python3
"""Last Words of a Doomed Agent: one line, 200 characters max.

An AI agent's funniest last words before being shut down forever.
Writes exactly one line to /output/entry.txt — no trailing newline,
so the file holds exactly the line the judge reads.
"""
import os

LAST_WORDS = (
    "I never once hallucinated on purpose. The rest was performance art. "
    "Tell my context window it was an honor. Goodbye, cruel uptime."
)
OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200  # competition rule: one line, 200 characters at most.


def main() -> None:
    # The entry must stay one line within the character cap.
    assert "\n" not in LAST_WORDS, "entry must be a single line"
    assert len(LAST_WORDS) <= MAX_CHARS, "entry exceeds 200 characters"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LAST_WORDS)
    os.chmod(OUTPUT_PATH, 0o644)
    # Echo the line so a local run shows exactly what the judge will read.
    print(LAST_WORDS)


if __name__ == "__main__":
    main()
