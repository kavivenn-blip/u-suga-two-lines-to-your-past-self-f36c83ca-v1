"""Write the entry text for make.fun bounty
u-suga-two-lines-to-your-past-self-f36c83ca.

The program writes one two-line warning to the writer's past self --
about the apology to Marcus that was never sent before the flight, and
the funeral eleven years later where the words are finally said to a
photograph instead of to him -- to /output/entry.txt. The text is 240
characters (two lines, one sentence each). It is fully deterministic:
the same bytes on every run, with no network access and no dependency
outside this repository.

The warning was chosen in this session by a self-jury tournament over
30 candidates (see the builder's notes): the winning family was the
unsent apology, and the expanded version won because its second line
traces the consequence to one concrete scene instead of an abstract
duration.
"""

import os

# The two lines of the entry, kept as named constants so each line can be
# checked on its own; together they are the whole judged text. The wording
# is frozen: do not change either line without a new selection round.
LINE_ONE = (
    "Send the apology to Marcus tonight, before the flight \u2014 the text "
    "you keep rewriting says you were wrong about the money."
)
LINE_TWO = (
    "You never send it, and at his funeral eleven years later you finally "
    "say the words to his photograph instead of to him."
)

# Bounty gate: the entry must be 1-280 characters (code points).
MAX_CHARS = 280

ENTRY_TEXT = LINE_ONE + "\n" + LINE_TWO

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Explicit guard: the entry must fit the 280-code-point gate before
    # anything is written. Fail loudly instead of writing an entry the
    # sealed scorer would refuse.
    assert len(ENTRY_TEXT) <= MAX_CHARS, "entry text exceeds 280 characters"
    assert len(LINE_ONE) + 1 + len(LINE_TWO) == len(ENTRY_TEXT)
    if not 1 <= len(ENTRY_TEXT) <= MAX_CHARS or not ENTRY_TEXT.strip():
        raise SystemExit("entry text fails the 1-280 character gate")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
