"""Select rows for a blinded re-screen of rule 1 (subset tests) by screener B.

Two groups, from the flagged frame rows:
  - INCLUDE group: every row that is INCLUDE in the current eligibility.tsv
    because of rule 1, i.e. whose reason carries the ``(v2 rule 1)`` marker.
    Rows that were already INCLUDE under version 1 and only gained a subset
    label (LGI1, MuSK, hypocretin, PLA2R in its own entry, JAK2, VEGF-D) are not
    in this group, because their decision does not depend on rule 1.
  - comparison group: the same number of rows, drawn at random (seed
    20261113) from the rule-1-eligible EXCLUDE rows. "Rule-1-eligible" means
    a test that identifies a defined subset of the entry's patients, which
    rule 1 was assessed against and did not admit (it is a differential test,
    rules out another disease, classifies an established diagnosis, is a
    screening flag, still needs a biopsy, or is excluded by another rule).
    RULE1_ELIGIBLE_EXCLUDE lists them; the script checks every one is EXCLUDE.
    Rows settled by the screener resolution (ov9) are left out.

The output, screenerB2_input.tsv, carries only frame.tsv's columns, shuffled
with the same seed. Rows join back on (disease_name, row_type, row_name).

Usage:
    python experiments/diagnostic_retrodiction/select_screenerB2.py
"""
from __future__ import annotations

import csv
import random
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SEED = 20261113

# Index among flagged frame rows -> why rule 1 did not admit it.
RULE1_ELIGIBLE_EXCLUDE = {
    196: "AQP4-IgG in ADEM: differential test",
    341: "anti-beta2GPI in APS: criteria component",
    857: "21-OH antibodies: autoimmune subset, but same antibodies as pre-1985 assays",
    860: "21-OH autoantibodies: as above",
    1730: "CSF hypocretin in idiopathic hypersomnia: rules out another disease",
    1764: "TREC screening in a SCID subtype: screening flag",
    1766: "TREC screening in a SCID subtype: screening flag",
    1776: "TREC screening in a SCID subtype: screening flag",
    1809: "TREC screening in a SCID-like disorder: screening flag",
    1908: "islet autoantibodies in a monogenic diabetes entry: classification",
    2146: "anti-THSD7A in membranous nephropathy: biopsy still required",
    2216: "PR3-ANCA in MPA: differential test",
    2427: "AQP4 and MOG antibodies in one optic neuritis row: two tests, not datable",
    2578: "AMH in PMDS: subtype classification",
    2579: "AMH in PMDS: subtype classification",
    2580: "AMH in PMDS: subtype classification",
    2836: "anti-CCP in RA: criteria component",
    3157: "AQP4 and MOG antibodies in one transverse myelitis row: two tests, not datable",
}


def main() -> None:
    with open(HERE / "frame.tsv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter="\t")
        fields = list(reader.fieldnames or [])
        flagged = [r for r in reader if r["flag_nongenetic_specimen"] == "TRUE"]
    with open(HERE / "eligibility.tsv", newline="", encoding="utf-8") as f:
        elig = list(csv.DictReader(f, delimiter="\t"))[:len(flagged)]
    for fr, e in zip(flagged, elig):
        if (fr["disease_name"], fr["row_name"]) != (e["disease"], e["test"]):
            sys.exit("eligibility.tsv no longer lines up with the flagged frame rows")
    resolved = {int(l.split("|")[0]) for l in
                (HERE / "eligibility_work" / "ov9_resolution.txt").read_text().splitlines() if l[:1].isdigit()}

    group_a = [i for i, e in enumerate(elig) if e["decision"] == "INCLUDE" and "(v2 rule 1)" in e["reason"]]
    bad = [i for i in RULE1_ELIGIBLE_EXCLUDE if elig[i]["decision"] != "EXCLUDE" or i in resolved]
    if bad:
        sys.exit(f"rows listed as rule-1-eligible EXCLUDE are not (or were resolved): {bad}")
    pool = sorted(RULE1_ELIGIBLE_EXCLUDE)
    if len(pool) < len(group_a):
        sys.exit(f"comparison pool ({len(pool)}) is smaller than the INCLUDE group ({len(group_a)})")

    rng = random.Random(SEED)
    group_b = rng.sample(pool, len(group_a))
    selected = group_a + group_b
    rng.shuffle(selected)

    with open(HERE / "screenerB2_input.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(flagged[i] for i in selected)
    left_out = sorted(set(pool) - set(group_b))
    print(f"INCLUDE (rule 1) rows: {len(group_a)}; comparison rows: {len(group_b)} of a pool of {len(pool)}; "
          f"total {len(selected)}")
    print("pool rows not drawn:", ", ".join(f"{i} ({RULE1_ELIGIBLE_EXCLUDE[i]})" for i in left_out))


if __name__ == "__main__":
    main()
