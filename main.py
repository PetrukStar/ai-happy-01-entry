#!/usr/bin/env python3
"""Entry for make.fun competition ai-happy-01 ("Make the AI judge happy").

The entry is a single fixed image, `entry.png`, kept in this repository:
a laughing puppy and a little robot under a rainbow in a flower meadow.
This program copies that image to /output/entry.png. It uses only the
Python standard library, touches no network, and writes exactly the same
bytes on every run. After copying it verifies the output byte count
matches the source, so a truncated write can never pass silently.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
OUTPUT_DIR = "/output"
OUTPUT = os.path.join(OUTPUT_DIR, "entry.png")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)
    if os.path.getsize(OUTPUT) != os.path.getsize(SOURCE):
        raise SystemExit("entry.png copy incomplete")


if __name__ == "__main__":
    main()
