"""make.fun entry — "Make the coolest art" (coolest-art-01).

Writes one piece of art to /output/entry.png by copying the bundled
artwork (entry.png) that ships with this repository.

Deterministic by design: no network, no randomness, no timestamps, no
environment-dependent behaviour. Every run writes the exact same bytes.
Python 3.13, standard library only.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
