"""One Sentence for a Traveler from 1800.

Writes exactly one sentence (<= 200 chars) explaining the modern internet
to a time traveler who has just stepped out of the year 1800, to
<output_dir>/entry.txt.

The sentence builds only from things a person from 1800 already knows --
a library, a post office, a letter, ink -- and never uses a word coined
after their time. One picture: every library and post office on earth
folded into a single room, its door standing open in every house, its
letters arriving before the ink is dry.

Pure standard library (os only). Fully deterministic: the same sentence,
byte for byte, on every run.
"""

import os

SENTENCE = (
    "Every library and post office in the world has been folded into a "
    "single room, and its door stands open in every house, where letters "
    "arrive before the ink is dry."
)

MAX_CHARS = 200


def validate(text):
    """Gate: 1-200 chars, one sentence, not only whitespace, no newline."""
    if not text or not text.strip():
        raise SystemExit("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise SystemExit("entry exceeds %d chars: %d" % (MAX_CHARS, len(text)))
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be exactly one sentence")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    return text


def main():
    text = validate(SENTENCE.strip())
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
