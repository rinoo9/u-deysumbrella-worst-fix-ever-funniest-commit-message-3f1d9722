#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message.

Writes one commit message (at most 100 characters) for a bug fix that
made everything worse, to /output/entry.txt.
"""

from pathlib import Path

COMMIT_MESSAGE = "fix: login crash by removing the login button; zero logins, zero crashes"


def main() -> None:
    text = COMMIT_MESSAGE.strip()
    if not 1 <= len(text) <= 100:
        raise ValueError(f"entry must be 1-100 chars, got {len(text)}")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
