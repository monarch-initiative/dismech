# human_gi_bpm — compensatory-pathway (BPM) mining on human genetic interaction data

**Question.** The GIDEON paper (Garcia et al., Bioinformatics 2026, btag385;
assessed in
[`docs/reports/gideon-bpm-compensatory-pathways-assessment-2026-09-02.md`](../../docs/reports/gideon-bpm-compensatory-pathways-assessment-2026-09-02.md))
mines yeast genetic interaction data for Between-Pathway Models (BPMs) — paired
gene modules that compensate for each other. Does the same motif search work on
the first genome-scale *human* genetic interaction map, and do the resulting
module pairs land on dismech-curated disease genes?

**Data.** Billmann, Costanzo et al., Cell 2026 — CRISPR qGI screens in HAP1
cells: 222 query genes × 17,804 library genes (298 screens across two media),
~131k significant interactions. Supplement files (CC BY 4.0) from the Boone lab
site; see `fetch_billmann.py`. The bulk data stays outside the repository;
only scripts and small derived tables are committed.

**Method.** `bpm_search.py` adapts the GIDEON BPM objective to the *bipartite*
query × library matrix (yeast data is all-by-all; the human map is not):
cross-module and within-query-module terms use measured qGI, and library-side
within-module cohesion — unmeasurable here — is enforced by qGI-profile
correlation, in the spirit of Kelley & Ideker 2005 using PPI for within-pathway
support. Greedy seed-centered growth (the analog of GIDEON's gene-centering
ILP constraint: a BPM must retain its stringent-negative seed pair), iterative
trimming, min 3 / max 25 genes per module, Jaccard pruning at 0.66 — the field's
conventions where transferable. No ILP solver is used; this is a heuristic
pilot, not a GIDEON reimplementation.

`annotate_bpms.py` scores each module's functional coherence against the
paper's own SAFE network-region bioprocess assignments (File_S11) and overlaps
module genes with dismech-curated disease genes
(`extract_dismech_genes.py`).

**Reproduce.**

```bash
uv run --with pandas,openpyxl,pyarrow python experiments/human_gi_bpm/fetch_billmann.py --data-dir /tmp/billmann
uv run python experiments/human_gi_bpm/extract_dismech_genes.py > /tmp/billmann/dismech_genes.tsv
uv run --with pandas,pyarrow python experiments/human_gi_bpm/bpm_search.py --data-dir /tmp/billmann --out /tmp/billmann/bpms.tsv
uv run --with pandas,openpyxl python experiments/human_gi_bpm/annotate_bpms.py \
  --bpms /tmp/billmann/bpms.tsv --safe /tmp/billmann/File_S11.xlsx \
  --dismech-genes /tmp/billmann/dismech_genes.tsv \
  --out bpms_annotated.tsv --overlap-out dismech_overlap.tsv
```

| Run | Data snapshot | Findings |
|---|---|---|
| [`billmann_hap1/`](billmann_hap1/) | Boone lab supplement, fetched 2026-09-16 | [`FINDINGS.md`](billmann_hap1/FINDINGS.md) |
