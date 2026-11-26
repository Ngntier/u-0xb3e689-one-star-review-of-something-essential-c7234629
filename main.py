"""One-Star Review of Something Essential.

Joke angle: sleep as a defective product. The complaint is filed in
earnest against a thing that cannot be fixed: sleep takes a third of
your life, offers no refund, and -- the sting, arriving last -- hands
you back each morning just as tired as you were. One grievance, told
deadpan, no exclamation, no second joke.
"""

import os

ENTRY = "Sleep takes a third of my life, offers no refund, and returns me every morning just as tired as I was."


def main() -> None:
    line = ENTRY
    if not 1 <= len(line) <= 160:
        raise ValueError("entry must be 1-160 characters")
    if line != line.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if "!" in line:
        raise ValueError("entry must not contain exclamation marks (deadpan tone)")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in line):
        raise ValueError("entry must not contain control characters")
    data = line.encode("utf-8")
    if len(data) > 160:
        raise ValueError("entry must be at most 160 UTF-8 bytes")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
