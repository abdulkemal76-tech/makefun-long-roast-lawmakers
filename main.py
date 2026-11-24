#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

Writes one satirical sentence (at most 320 characters) roasting
lawmakers who would regulate AI, crypto or the internet but cannot
convert a file to PDF, to /output/entry.txt.

Stdlib only.
"""

import os

# Final wording: the punch now lands on the last few words, the
# PDF conversion itself, with the hour (8:15) as the anchor just
# before it. "Writing" reads cleaner than "drafting".
SENTENCE = (
    "The senator writing the AI Safety Act keeps a file on his desktop "
    "called FINAL_v7_ACTUALLY_FINAL.docx, and every morning at 8:15 "
    "his aide turns it into a PDF for him."
)


def main() -> None:
    text = SENTENCE.strip()
    assert text, "entry must not be empty"
    assert len(text) <= 320, f"entry is {len(text)} chars, over the 320 cap"
    assert text.count(".") >= 1, "entry must be a sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} characters to /output/entry.txt")
    print(text)


if __name__ == "__main__":
    main()
