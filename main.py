#!/usr/bin/env python3
"""The Best Advice I Ever Got — make.fun entry.

Writes one sentence (<= 200 characters) about the best advice the
writer ever received to /output/entry.txt.
"""

import os

SENTENCE = (
    "My grandmother, stirring soup with the same wooden spoon for forty "
    "years, told me to marry the one who stays kind when the food burns."
)


def main() -> None:
    sentence = SENTENCE.strip()
    assert sentence, "sentence must not be empty"
    assert len(sentence) <= 200, f"sentence is {len(sentence)} chars, over 200"
    assert sentence.count(".") == 1, "entry must be exactly one sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(sentence + "\n")


if __name__ == "__main__":
    main()
