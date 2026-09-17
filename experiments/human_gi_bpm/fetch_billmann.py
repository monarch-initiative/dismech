#!/usr/bin/env python3
"""Download and convert the Billmann et al. 2026 HAP1 genetic interaction
supplementary data used by this experiment.

Source: Boone lab supplement for Billmann, Costanzo et al., Cell 2026,
"Global genetic interaction network of a human cell maps conserved principles
and informs functional interpretation of gene co-essentiality profiles"
(doi:10.1016/j.cell.2026.…; data also archived at Mendeley Data
doi:10.17632/bpcpfns6vb.1, CC BY 4.0).

Files fetched (~160 MB total; kept OUTSIDE the repository — pass a scratch
directory as --data-dir):
- File_S1.xlsx  query mutant cell lines and screen metadata
- File_S4.xlsx  qGI score + FDR matrices (17,804 library genes x 298 screens)
                and the pairwise significant-GI table
- File_S11.xlsx SAFE network-region bioprocess assignments per gene

Requires: pandas, openpyxl, pyarrow (e.g. `uv run --with pandas,openpyxl,pyarrow`).
"""
import argparse
import pathlib
import urllib.request

BASE = "https://boonelab.ccbr.utoronto.ca/supplement/billmanncostanzo2026/assets/data_files"
FILES = ["File_S1.xlsx", "File_S4.xlsx", "File_S11.xlsx"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data-dir", required=True,
                    help="scratch directory for downloads and parquet output")
    args = ap.parse_args()
    out = pathlib.Path(args.data_dir)
    out.mkdir(parents=True, exist_ok=True)

    for f in FILES:
        dest = out / f
        if not dest.exists():
            print(f"downloading {f} ...")
            urllib.request.urlretrieve(f"{BASE}/{f}", dest)

    import pandas as pd
    for sheet in ["qGI_scores", "qGI_FDR"]:
        dest = out / f"{sheet}.parquet"
        if not dest.exists():
            print(f"converting {sheet} ...")
            df = pd.read_excel(out / "File_S4.xlsx", sheet_name=sheet, index_col=0)
            df.to_parquet(dest)
    dest = out / "pairwise_gi.parquet"
    if not dest.exists():
        pd.read_excel(out / "File_S4.xlsx",
                      sheet_name="pairwise GI_Complete dataset").to_parquet(dest)
    print("done")


if __name__ == "__main__":
    main()
