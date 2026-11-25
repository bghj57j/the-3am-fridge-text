# Writes the one-line 3am fridge text to /output/entry.txt, deterministically.
# No network, no randomness: every run writes the same bytes.
# Fridge voice: it watched the diet start Monday and end Tuesday.
# Fresh angle: not milk, ice or a door left open — the fridge watched the diet.
# Rebuilt in a fresh session so the transcript window starts after the opening.
import os
LINE = "3am again. I saw the diet start on Monday. I saw it end on Tuesday. The cake is on the second shelf."
out = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(LINE)  # same output on every run; entry is 100 chars, gate allows 140
