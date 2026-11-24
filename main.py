"""One-Liner Marathon — one comedy joke up to 280 characters.

The program writes a single line of text (1-280 chars, UTF-8) to
/output/entry.txt, exactly as the competition gate requires.

The joke: a wedding-vow request detours into a proposal to the household
Wi-Fi router. The punchline turns on "dropped" — a connection that drops
versus a partner who drops you — so the router wins the only relationship
in the house that has never once failed. Two short sentences keep the
setup tight and let the turn land on the first read.
"""

import os

LINE = (
    "I asked an AI to write my wedding vows. It proposed to the Wi-Fi "
    "router instead — the only thing in this house that has never once "
    "dropped me."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 280, f"line is {len(text)} chars, must be 1-280"
    assert text and not text.isspace()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
