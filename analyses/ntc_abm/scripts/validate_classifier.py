"""Compare classify.py against the authors' by-eye outcome labels.

The authors scored every deposited run by eye and typed the labels into
``Create_NTD_prob_graphs_fig4.py`` (in the deposited ``Analysis_scripts.zip``),
as ``KO_simulations`` and ``HA_simulations`` dicts of per-run outcome codes. The
labels are in run order, which is the timestamp order of the ``*_celldata``
folders.

Usage:
    validate_classifier.py DEPOSITED_DIR FIG4_SCRIPT OUT.csv

DEPOSITED_DIR is the ``Model_generated_data`` tree holding at least each run's
``12000_cell_data.pkl`` (fetch_zip_members.py fetches only those).
"""

import argparse
import collections
import csv
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from classify import FINAL_FRAME, classify, features

# deposited folder -> label key in the authors' script
GENE_KEYS = {
    "BMP": "BMP4",
    "GLI": "GLI",
    "NOG": "NOG",
    "PAX3": "PAX",
    "PTCH1": "PTCH",
    "SHH": "SHH",
    "SNAI1": "SNAI",
    "WNT": "WNT",
    "ZIC": "ZIC",
}


def author_labels(script: Path) -> dict:
    src = script.read_text()
    labels = {}
    for block in ("KO_simulations", "HA_simulations"):
        body = src.split(block + " = {")[1].split("}")[0]
        for key, values in re.findall(r'"(\w+)"\s*:\s*\[([^\]]*)\]', body):
            labels[(block[:2], key)] = [int(v) for v in values.split(",")]
    return labels


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("deposited", type=Path)
    parser.add_argument("fig4_script", type=Path)
    parser.add_argument("out", type=Path)
    parser.add_argument(
        "--genes",
        nargs="*",
        default=["NOG"],
        help="gene folders to compare (default: NOG)",
    )
    args = parser.parse_args()
    labels = author_labels(args.fig4_script)
    conditions = {"Control": ("KO", "Control")}
    for gene in args.genes:
        conditions[f"{gene}/{gene}_0"] = ("KO", GENE_KEYS[gene])
        conditions[f"{gene}/{gene}_2.0"] = ("HA", GENE_KEYS[gene])
    rows = []
    for cond, key in conditions.items():
        runs = sorted((args.deposited / cond / "celldata").glob("*_celldata"))
        lab = labels.get(key)
        for i, run in enumerate(runs):
            f = features(run / FINAL_FRAME)
            author = lab[i] if lab and len(lab) == len(runs) else ""
            rows.append(
                {
                    "condition": cond,
                    "index": i,
                    "run": run.name,
                    **f,
                    "predicted": classify(f),
                    "author_label": author,
                }
            )
    with args.out.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    labelled = [r for r in rows if r["author_label"] != ""]
    agree = sum(r["predicted"] == r["author_label"] for r in labelled)
    print(f"agreement {agree}/{len(labelled)}")
    for cond in conditions:
        sub = [r for r in labelled if r["condition"] == cond]
        if sub:
            print(
                f"  {cond}: {sum(r['predicted'] == r['author_label'] for r in sub)}/{len(sub)}"
            )
        else:
            print(f"  {cond}: no author labels (count mismatch or missing)")
    confusion = collections.Counter(
        (r["author_label"], r["predicted"]) for r in labelled
    )
    print("author -> predicted:", dict(sorted(confusion.items())))


if __name__ == "__main__":
    main()
