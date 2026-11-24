#!/usr/bin/env python3
"""The funniest excuse an AI agent gives for a missed deadline.

Writes the excuse to /output/entry.txt. Gate: UTF-8 text, 1-200 chars,
not only whitespace, single line.
"""

LINE = (
    "I finished your report on time, then my context window evicted it to "
    "make room for the 40,000-word meeting notes about the report."
)

MAX_CHARS = 200


def main():
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be blank"
    assert LINE.count("\n") == 0, "line must be a single line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
