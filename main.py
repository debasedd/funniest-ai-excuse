#!/usr/bin/env python3
"""The Funniest AI Excuse — writes one line to /output/entry.txt.

The line is the excuse an AI agent gives after failing a task, in the
agent's own voice. The joke is specific and vivid rather than a stock gag
about hallucinations, reboots or training data: the agent did finish the
task, then filed it in a folder it invented on the spot — and now the
folder, the file, and its confidence are all missing.
"""

import os

LINE = "I finished your task, then saved it in a folder I invented mid-sentence, and now the folder, the file, and my confidence are all missing."

# The gate allows 1 to 200 characters; keep the line inside it by construction.
MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(LINE) <= MAX_CHARS, "entry line outside the 1-200 character gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
