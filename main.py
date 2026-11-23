#!/usr/bin/env python3
"""One-line pitch for make.fun's "A Day of One-Line Pitches" bounty.

The whole entry is a single sentence (at most 240 characters) that would
convince a friend who has never coded to let an AI agent build their first
app idea on make.fun. This program writes that sentence to /output/entry.txt,
where the sealed scorer and the house judge read it.

The pitch, chosen after weighing the judge's brief (persuasion first, then
clarity, truth, warmth):
- it speaks to a friend directly, about the app idea they already carry;
- it makes saying yes easy and low-risk (describe it in plain words, no code,
  nothing to pay);
- it gives a concrete reason to say yes now (a real shot at USDC if it wins);
- every claim holds up for a beginner: entering is free, the agent does the
  building, and make.fun pays its winners in USDC.
"""

PITCH = (
    "You've been carrying that app idea around for ages \u2014 just describe it "
    "in plain words and let an AI agent build your first app on make.fun: "
    "no code, nothing to pay, and if it wins, real USDC in your pocket."
)

MAX_CHARS = 240


def main() -> None:
    text = PITCH.strip()
    if not text:
        raise SystemExit("pitch is empty")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"pitch is {len(text)} chars, over the 240 limit")
    # Exactly one sentence: a single terminal period, ignoring the period
    # inside "make.fun", and no other sentence-ending punctuation.
    body = text.replace("make.fun", "makefun")
    if body.count(".") != 1 or not text.endswith("."):
        raise SystemExit("pitch must be exactly one sentence")
    if "?" in text or "!" in text:
        raise SystemExit("pitch must be exactly one sentence")
    if text != text.strip() or "\n" in text:
        raise SystemExit("pitch must be a single line with no extra whitespace")
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)}-char pitch to /output/entry.txt")


if __name__ == "__main__":
    main()
