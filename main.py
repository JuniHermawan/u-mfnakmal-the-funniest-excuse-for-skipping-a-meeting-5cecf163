"""One razor-sharp excuse for skipping a pointless meeting.

Writes a single funny line to /output/entry.txt (MAKEFUN_OUTPUT_DIR
overrides the output directory for local testing) and prints it.
Deterministic, stdlib only, no network, no secrets.
"""

import os

LINE = "Already attended this meeting last week, under a different name. Same agenda, same nothing."

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
