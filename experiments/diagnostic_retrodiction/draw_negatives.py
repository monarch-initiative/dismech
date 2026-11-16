"""Draw the expanded negative controls from coverage.tsv.

Pool: coverage.tsv rows with frame_flagged_rows 0 (no frame row flagged as an
accessible, non-germline test) and n_measurable >= 1 (at least one pathograph
node passing the coverage audit's measurable-node rule), leaving out the six
original negatives, sorted by kb_file. Draw: random.Random(SEED).sample(pool,
N_DRAW). The pool does not read coverage.tsv's ``source`` column, so rerunning
coverage_audit/audit.py with the drawn diseases in negatives.tsv (which
relabels them NEGATIVE) does not change the draw.

Prints the drawn rows; negatives.tsv records them, with the usability
judgment for each, and the original six negatives.

Usage:
    python experiments/diagnostic_retrodiction/draw_negatives.py
"""
import csv
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
SEED = 20261114
N_DRAW = 12
ORIGINAL_NEGATIVES = (
    "kb/disorders/Hypermobile_Ehlers-Danlos_Syndrome.yaml", "kb/disorders/Kawasaki_Disease.yaml",
    "kb/disorders/Sarcoidosis.yaml", "kb/disorders/Behcets_Disease.yaml",
    "kb/disorders/Complex_Regional_Pain_Syndrome_Type_1.yaml", "kb/disorders/Takayasu_Arteritis.yaml",
)


def draw() -> list[dict]:
    with open(HERE / "coverage.tsv", newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f, delimiter="\t"))
    original = set(ORIGINAL_NEGATIVES)
    pool = sorted((r for r in rows if r["frame_flagged_rows"] == "0" and r["n_measurable"]
                   and int(r["n_measurable"]) >= 1 and r["kb_file"] not in original),
                  key=lambda r: r["kb_file"])
    return random.Random(SEED).sample(pool, N_DRAW), len(pool)


if __name__ == "__main__":
    drawn, n = draw()
    print(f"pool {n}; drew {len(drawn)} with seed {SEED}")
    for r in drawn:
        print("\t".join([r["disease"], r["kb_file"], r["mondo_id"], r["status"], r["n_measurable"],
                         r["measurable_nodes"][:200]]))
