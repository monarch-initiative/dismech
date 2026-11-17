"""Assessor replication of the OpenScientist report's RNA-seq claim.

The report states that LMNB1 is not depleted in oligodendrocytes across the 4DN
"RNA-seq on human cortical neural cells" sets. It saved no code or tables, so
this script recomputes the comparison independently from the same public files.

It also runs two comparisons the report did not: a within-donor contrast (which
removes the donor and cohort effects a cross-sectional median hides), and a
split of the oligodendrocyte samples by mature-myelin marker level. Both are
assessor additions, reported in the assessment sidecar as leads rather than
results; the maturity split is perfectly confounded with donor cohort, which
the script prints so the confound cannot be overlooked.

Inputs are the openly mirrored per-set gene-expression TSVs (RSEM TPM, GRCh38)
named by a 4DN portal search response. Nothing here needs a portal key.

Usage:
  python -I openscientist-replication-rna-by-claude-opus-5.py \
      <4dn_search_json> <download_dir> <output_dir>

The search JSON is the response of
https://data.4dnucleome.org/search/?type=ExperimentSetReplicate&status=released
  &dataset_label=RNA-seq+on+human+cortical+neural+cells&limit=100&format=json
requesting the accession, description and processed-file fields.
"""

import hashlib
import json
import re
import sys
import urllib.request
from pathlib import Path

import pandas as pd
from scipy import stats

# Ensembl REST lookup of each symbol, 2026-11-14. LMNB1 is the gene under test;
# CANX is a same-chromosome housekeeping comparator; the rest are cell-identity
# markers used only to confirm what each sorted sample actually contains.
GENES = {
    "ENSG00000113368": "LMNB1",
    "ENSG00000123560": "PLP1",
    "ENSG00000197971": "MBP",
    "ENSG00000105695": "MAG",
    "ENSG00000182578": "CSF1R",
    "ENSG00000204472": "AIF1",
    "ENSG00000131095": "GFAP",
    "ENSG00000171885": "AQP4",
    "ENSG00000104888": "SLC17A7",
    "ENSG00000128683": "GAD1",
    "ENSG00000127022": "CANX",
}

# MAG (myelin-associated glycoprotein) separates the oligodendrocyte samples
# into two non-overlapping groups in this corpus. The threshold sits inside a
# wide empty gap (observed values 1.2-8.5 and 110.1-115.0 TPM), so its exact
# value does not change the grouping.
MATURE_MAG_TPM = 50.0


def cell_type(description: str) -> str:
    text = description.lower()
    for key, label in (
        ("oligodendro", "oligodendrocyte"),
        ("microglia", "microglia"),
        ("astrocyte", "astrocyte"),
        ("excitatory", "excitatory_neuron"),
        ("interneuron", "interneuron"),
    ):
        if key in text:
            return label
    return "unassigned"


def load_samples(search_json: Path, download_dir: Path) -> pd.DataFrame:
    download_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    for record in sorted(
        json.loads(search_json.read_text())["@graph"], key=lambda x: x["accession"]
    ):
        files = list(record.get("processed_files") or [])
        for experiment in record.get("experiments_in_set", []):
            files += experiment.get("processed_files") or []
        tables = [
            f
            for f in files
            if f.get("file_type") == "gene expression" and f.get("open_data_url")
        ]
        donor = re.search(r"donor (\S+)", record.get("description", ""))
        row = {
            "set": record["accession"],
            "description": record.get("description", ""),
            "cell_type": cell_type(record.get("description", "")),
            "donor": donor.group(1).rstrip(",") if donor else "",
        }
        if not tables:
            # Recorded rather than dropped: the report says all 42 sets were
            # openly mirrored, and this is where that count is checked.
            rows.append({**row, "status": "excluded: no openly mirrored gene TSV"})
            continue
        table = tables[0]
        path = download_dir / f"{table['accession']}.tsv"
        if not path.exists():
            urllib.request.urlretrieve(table["open_data_url"], path)
        payload = path.read_bytes()
        frame = pd.read_csv(path, sep="\t")
        frame["gid"] = frame["gene_id"].astype(str).str.split(".").str[0]
        tpm = frame.set_index("gid")["TPM"]
        rows.append(
            {
                **row,
                "status": "included",
                "file": table["accession"],
                "url": table["open_data_url"],
                "sha256": hashlib.sha256(payload).hexdigest(),
                **{sym: float(tpm.get(gid, float("nan"))) for gid, sym in GENES.items()},
            }
        )
    return pd.DataFrame(rows)


def main(search_json: str, download_dir: str, output_dir: str) -> None:
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    table = load_samples(Path(search_json), Path(download_dir))
    table.to_csv(out / "rna-samples.csv", index=False)

    included = table[table.status == "included"].copy()
    excluded = table[table.status != "included"]
    print(f"sets in search response: {len(table)}")
    print(f"included: {len(included)}   excluded: {len(excluded)}")
    for _, row in excluded.iterrows():
        print(f"  excluded {row['set']} ({row['cell_type']}): {row['status']}")

    summary = included.groupby("cell_type")[list(GENES.values())].median().round(2)
    summary.insert(0, "n", included.groupby("cell_type").size())
    summary.to_csv(out / "rna-median-tpm-by-cell-type.csv")
    print("\n== median TPM by cell type (the report's comparison) ==")
    print(summary.to_string())

    groups = [g["LMNB1"].to_numpy() for _, g in included.groupby("cell_type")]
    kruskal = stats.kruskal(*groups)
    oligo = included[included.cell_type == "oligodendrocyte"]["LMNB1"]
    others = included[included.cell_type != "oligodendrocyte"]["LMNB1"]
    mwu = stats.mannwhitneyu(oligo, others, alternative="two-sided")
    print(f"LMNB1 Kruskal-Wallis H={kruskal.statistic:.2f} p={kruskal.pvalue:.3f}")
    print(f"LMNB1 oligodendrocyte vs others Mann-Whitney p={mwu.pvalue:.3f}")

    # Within-donor contrast. LMNB1 is normalized to CANX so that library-level
    # differences between samples of one donor do not drive the ratio.
    included["lmnb1_over_canx"] = included.LMNB1 / included.CANX
    print("\n== within-donor oligodendrocyte vs other cortical cells ==")
    paired = []
    for donor, group in included.groupby("donor"):
        this = group[group.cell_type == "oligodendrocyte"]
        rest = group[group.cell_type != "oligodendrocyte"]
        if this.empty or rest.empty:
            continue
        ratio = this.lmnb1_over_canx.iloc[0] / rest.lmnb1_over_canx.median()
        mature = this.MAG.iloc[0] >= MATURE_MAG_TPM
        paired.append(
            {
                "donor": donor,
                "cohort": donor.split("-")[0],
                "oligo_MAG_tpm": round(float(this.MAG.iloc[0]), 1),
                "myelin_high": mature,
                "oligo_lmnb1_over_canx": round(float(this.lmnb1_over_canx.iloc[0]), 4),
                "other_median_lmnb1_over_canx": round(
                    float(rest.lmnb1_over_canx.median()), 4
                ),
                "ratio": round(float(ratio), 2),
                "n_other_cell_types": len(rest),
            }
        )
    paired_frame = pd.DataFrame(paired).sort_values(["myelin_high", "donor"])
    paired_frame.to_csv(out / "rna-within-donor.csv", index=False)
    print(paired_frame.to_string(index=False))

    high = paired_frame[paired_frame.myelin_high]
    low = paired_frame[~paired_frame.myelin_high]
    print(
        f"\nmyelin-high donors (MAG >= {MATURE_MAG_TPM:g} TPM): n={len(high)} "
        f"ratios {sorted(high.ratio)}"
    )
    print(f"myelin-low donors: n={len(low)} ratios {sorted(low.ratio)}")
    print(
        "CONFOUND: myelin-high cohorts "
        f"{sorted(set(high.cohort))} vs myelin-low cohorts {sorted(set(low.cohort))}. "
        "With this corpus the maturity split cannot be separated from donor "
        "cohort or sampled region, so the contrast is a lead, not a result."
    )


if __name__ == "__main__":
    main(*sys.argv[1:4])
