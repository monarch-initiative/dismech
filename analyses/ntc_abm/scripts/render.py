"""Draw final frames of S-ONTX34 runs as a contact sheet, to check the scoring by eye.

Usage:
    render.py OUT.png TITLE FRAME.pkl [FRAME.pkl ...]

Colours: dark purple MHP (types 5-7), light purple neural plate (8-13), blue
surface ectoderm (14, 15), yellow ECM (17), pale pink neural crest (19-22).
"""

import pickle
import sys
from pathlib import Path

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt

COLOURS = {
    1: (0.55, 0.35, 0.2),
    3: (1, 0.75, 0.8),
    4: (1, 0.75, 0.8),
    **dict.fromkeys(range(5, 8), (0.3, 0, 0.5)),
    **dict.fromkeys(range(8, 14), (0.6, 0.4, 0.8)),
    14: (0.2, 0.5, 1),
    15: (0.2, 0.5, 1),
    16: (0, 0, 0),
    17: (1, 0.9, 0.3),
    **dict.fromkeys(range(19, 23), (1, 0.85, 0.9)),
}


def image(path: str) -> np.ndarray:
    with Path(path).open("rb") as fh:
        cells = pickle.load(fh)  # noqa: S301 - the model's own output format
    img = np.ones((200, 252, 3))
    for cell in cells.values():
        for x, y, *_ in cell["cell_pixels"]:
            img[int(y), int(x)] = COLOURS.get(cell["type"], (0.5, 0.5, 0.5))
    return img[::-1]


def main() -> None:
    out, title, paths = sys.argv[1], sys.argv[2], sys.argv[3:]
    cols = 5
    rows = (len(paths) + cols - 1) // cols
    fig, axs = plt.subplots(rows, cols, figsize=(cols * 3.2, rows * 2.7))
    for i, ax in enumerate(np.atleast_1d(axs).ravel()):
        ax.axis("off")
        if i < len(paths):
            ax.imshow(image(paths[i]))
            ax.set_title(str(i), fontsize=9)
    fig.suptitle(title)
    fig.tight_layout()
    fig.savefig(out, dpi=80)


if __name__ == "__main__":
    main()
