"""Score the final (MCS 12000) frame of S-ONTX34 runs on the Noggin (NOG) axis.

Outcome codes follow the authors' scheme: 0 normal, 1 midline fusion defect,
2 open NTD (aperta), 3 closed NTD (occulta). Rules, in order:

  2 open   : the surface ectoderm (cell types 14, 15) is not one continuous sheet
  0 normal : the neural tissue (types 5-13) encloses a lumen of area >= LUMEN_MIN
  3 closed : no lumen, and the neural mask has a wide dorsal gap (convex-hull
             deficiency >= SLIT_MIN): the folds are apposed under intact
             ectoderm but never fused
  1 fusion : no lumen and no wide gap: the folds fused into a solid rod

Scope: calibrated and checked against the authors' by-eye labels on the NOG axis
only (control, NOG knockout; see validate_classifier.py). For other genes the
authors' "midline fusion" calls include runs with an open lumen that these rules
score as normal, so do not use it there without re-validating.

Usage:
    classify.py ROOT OUT.csv

ROOT is a simulate.py work directory or the deposited Model_generated_data tree;
every ``*_celldata/12000_cell_data.pkl`` below it is scored. The condition name
is the path above the ``repNN`` or ``celldata`` folder.
"""

import argparse
import collections
import csv
import pickle
from pathlib import Path

import numpy as np
from matplotlib.path import Path as MPath
from scipy import ndimage
from scipy.spatial import ConvexHull

W, H = 252, 200
NEURAL = list(range(5, 14))
ECTO = [14, 15]
LUMEN_MIN = 200
SLIT_MIN = 600
CROSS = ndimage.generate_binary_structure(2, 1)
FINAL_FRAME = "12000_cell_data.pkl"
OUTCOMES = {0: "normal", 1: "midline_fusion", 2: "open_ntd", 3: "closed_ntd"}


def features(path: Path) -> dict:
    with Path(path).open("rb") as fh:
        cells = pickle.load(fh)  # noqa: S301 - the model's own output format
    lab = np.zeros((W, H), dtype=np.int16)
    for cell in cells.values():
        for x, y, *_ in cell["cell_pixels"]:
            lab[int(x), int(y)] = cell["type"]
    neural = np.isin(lab, NEURAL)
    ecto = np.isin(lab, ECTO)
    ecomp, n_e = ndimage.label(ecto, structure=np.ones((3, 3)))
    left = set(np.unique(ecomp[lab == 14])) - {0}
    right = set(np.unique(ecomp[lab == 15])) - {0}
    sizes = ndimage.sum(ecto, ecomp, range(1, n_e + 1))
    main = int(np.argmax(sizes)) + 1 if n_e else 0
    holes = ndimage.binary_fill_holes(neural) & ~neural
    pts = np.argwhere(neural)
    hull = ConvexHull(pts)
    xs, ys = np.mgrid[0:W, 0:H]
    inside = (
        MPath(pts[hull.vertices])
        .contains_points(np.c_[xs.ravel(), ys.ravel()])
        .reshape(W, H)
    )
    return {
        "neural_area": int(neural.sum()),
        "lumen_area": int(holes.sum()),
        "slit_area": int((inside & ~neural & ~holes).sum()),
        "ecto_continuous": bool(main in left and main in right),
        "neural_ecto_contact": int(
            (neural & ndimage.binary_dilation(ecto, structure=CROSS)).sum()
        ),
    }


def classify(f: dict) -> int:
    if not f["ecto_continuous"]:
        return 2
    if f["lumen_area"] >= LUMEN_MIN:
        return 0
    if f["slit_area"] >= SLIT_MIN:
        return 3
    return 1


def condition_of(root: Path, frame: Path) -> str:
    parts = frame.relative_to(root).parts
    for i, part in enumerate(parts):
        if part == "celldata" or (part.startswith("rep") and part[3:].isdigit()):
            return "/".join(parts[:i]) or "."
    return "/".join(parts[:-2])


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("root", type=Path)
    parser.add_argument("out", type=Path)
    args = parser.parse_args()
    rows = []
    for frame in sorted(args.root.rglob(f"*_celldata/{FINAL_FRAME}")):
        f = features(frame)
        code = classify(f)
        rows.append(
            {
                "condition": condition_of(args.root, frame),
                "frame": str(frame.relative_to(args.root)),
                **f,
                "outcome_code": code,
                "outcome": OUTCOMES[code],
            }
        )
    if not rows:
        raise SystemExit(f"no */{FINAL_FRAME} under {args.root}")
    with args.out.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    counts = collections.defaultdict(collections.Counter)
    for row in rows:
        counts[row["condition"]][row["outcome"]] += 1
    print("condition\tn\t" + "\t".join(OUTCOMES.values()))
    for cond in sorted(counts):
        c = counts[cond]
        print(
            f"{cond}\t{sum(c.values())}\t"
            + "\t".join(str(c[o]) for o in OUTCOMES.values())
        )


if __name__ == "__main__":
    main()
