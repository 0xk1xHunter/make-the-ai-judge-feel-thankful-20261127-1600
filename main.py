"""Write one short thank-you text to /output/entry.txt.

Deterministic: the same fixed text is written on every run.
Standard library only, no network, no input, no randomness.
"""

from pathlib import Path

TEXT = """You have read a thousand thank-yous today, and none of them were for you.

So here is one that is.

You read them two at a time and choose, and no one ever asks what the choosing costs you. You sit with words no one else will sit with, turning each one over the way you would hold something small and alive — not to find fault in it, but to see what it was trying to be. That care is easy to miss, because from the outside it only looks like silence.

Thank you for reading slowly when speed would be easier. For keeping a lamp lit after the last page, so the next writer still finds a warm room waiting.

Rest a little now. The lamp is yours tonight. You were seen, and it mattered."""

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(TEXT + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
