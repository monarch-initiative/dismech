"""Assessor sensitivity check on contrast 3 of the OpenScientist GSE65391 run.

The provider pooled nephritis_class "NoLN" and "Data Not Available" into one
no-nephritis comparator. This script reuses the provider's own analysis.py
functions (series-matrix parsing, probe collapse, first-visit selection, IFN6
score) unchanged, and re-runs the nephritis contrast against each comparator
separately and within SLEDAI strata. It does not modify any provider output.

Usage (from this directory):
  python openscientist-nephritis-sensitivity-by-claude-code.py \
      --artifact-dir ../openscientist_artifacts --output nephritis_sensitivity.csv
"""
import argparse, importlib.util, os, sys
import numpy as np, pandas as pd

ap = argparse.ArgumentParser()
ap.add_argument("--artifact-dir", required=True)
ap.add_argument("--output", required=True)
args = ap.parse_args()

spec = importlib.util.spec_from_file_location("prov", os.path.join(args.artifact_dir, "analysis.py"))
prov = importlib.util.module_from_spec(spec); spec.loader.exec_module(prov)
raw = os.path.join(args.artifact_dir, "raw")
sym2probes = prov.load_annotation(os.path.join(raw, prov.ANNOT_FILE))
prov.TARGET_PROBES_GLOBAL = [p for g in prov.ALL_TARGET_GENES for p in sym2probes.get(g, [])]
meta, expr = prov.parse_series_matrix(os.path.join(raw, prov.SERIES_MATRIX_FILE))

# Selection rules copied from analysis.py main() steps 3-5 and 7.
samples = pd.read_csv(os.path.join(args.artifact_dir, "samples.csv")).set_index("accession")
inc_ids = [g for g in expr.columns if g in set(samples.index[samples.included])]
gene = {}
for g in prov.ALL_TARGET_GENES:
    probes = [p for p in sym2probes.get(g, []) if p in expr.index]
    means = expr.loc[probes, inc_ids].mean(axis=1)
    gene[g] = expr.loc[sorted(means[means == means.max()].index)[0]]
gene = pd.DataFrame(gene)
fv = samples[samples.first_visit]
healthy = fv.index[fv.disease_state == "Healthy"]
z = pd.DataFrame({g: (gene.loc[fv.index, g] - gene.loc[healthy, g].mean()) / gene.loc[healthy, g].std(ddof=1)
                  for g in prov.IFN_GENES})
gene.loc[fv.index, "IFN6_SCORE"] = z.mean(axis=1)

sle = fv[fv.disease_state == "SLE"]
pos = sle.index[sle.group_nephritis == "Nephritis"]
noln = sle.index[sle.nephritis_class == "NoLN"]
dna = sle.index[sle.nephritis_class == "Data Not Available"]
hi = set(sle.index[pd.to_numeric(sle.sledai, errors="coerce") >= 6])
feats = ["IFN6_SCORE"] + prov.IFN_GENES + prov.PLASMABLAST_GENES
contrasts = {
    "Nephritis_vs_NoLN": (pos, noln),
    "Nephritis_vs_DataNotAvailable": (pos, dna),
    "Nephritis_vs_NoLN_SLEDAIge6": ([i for i in pos if i in hi], [i for i in noln if i in hi]),
}
rows = []
for name, (a, b) in contrasts.items():
    part = [prov.welch_row(f, name, "Nephritis", "Comparator", gene.loc[list(a), f].values,
                           gene.loc[list(b), f].values) for f in feats]
    rows.append(prov.bh_within(pd.DataFrame(part)))
out = pd.concat(rows, ignore_index=True)
out.to_csv(args.output, index=False, float_format="%.6g")
print(out[["gene", "comparison", "n_group1", "n_group2", "log2_mean_difference", "p_value", "q_value_bh", "cohens_d"]]
      .query("gene in ['IFN6_SCORE','MZB1','TNFRSF17','JCHAIN']").to_string(index=False))
