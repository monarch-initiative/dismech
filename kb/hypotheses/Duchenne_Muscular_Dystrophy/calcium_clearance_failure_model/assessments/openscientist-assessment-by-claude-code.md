# OpenScientist dataset-analysis run, calcium clearance model

Assessment of `../openscientist.md` by `claude-code`, 2026-11-25. The YAML
sidecar beside this file is authoritative; this is the human-readable version.

**Verdict: UNRESOLVED.** The run could not test the hypothesis it was given,
and it does not pass the repository's execution gate.

## Why the run does not pass the gate

`just validate-hypothesis-analysis-run` reports 27 problems. They fall into two
groups that need to be read differently.

Two are the provider's. The response body opens with a Markdown heading instead
of the required first line `ANALYSIS_STATUS: SUCCEEDED`. The template states
that contract exactly, so this is not ambiguity. Because the marker is absent
the runner refused to stamp `artifact_manifest_sha256` into the report
frontmatter, which means the report is not cryptographically bound to the
manifest bytes.

The other 25 are ours. The gate requires the manifest keys `provider`, and per
input `identifier`, `canonical_url` or `uri`, and `retrieved_at` or
`retrieval_time_utc`. `templates/hypothesis_dataset_analysis.md` describes the
manifest only in prose — "accession and retrieval URL/date/checksum/byte
count" — and never names any of those keys; `provider` appears nowhere in the
template at all. The run wrote `accession`, `retrieval_url` and
`retrieval_date_utc`, with every value correct and present. A provider that
follows the template cannot pass this gate, so re-running against the unchanged
template fails the same 25 checks. Fixing the template is the prerequisite for
any rerun.

Neither the report nor the manifest has been corrected to make the gate pass.
The stale binding is left stale, and the locked analysis is recorded as
`PARTIAL` rather than `SUCCEEDED`.

## What was verified independently

The manifest claims a byte-identical clean replay. That claim was checked rather
than relayed:

- All ten primary and replay output pairs match by `sha256sum`.
- The manifest hashes for `analysis.py`, `gene_results.csv` and
  `normalized_counts.csv` match the committed files.
- The FBN1, FBN2, DMD and ATP2A2 figures quoted in the report match
  `target_gene_results.csv` exactly, so the report's locked numbers are bound to
  the committed tables by content even though the hash binding is missing.
- `just verify-datasets --accession geo:GSE299627` resolves and returns the
  title of PMID:40979067, so the series is the one behind the paper's human arm.
- Both PMIDs the report cites are real and are the bioRxiv preprint and the
  microPublication Biology version of the same paper. The sentence the report
  quotes from the preprint is an exact match to that abstract. The run was
  launched with `--no-validate-references`, so this check was the assessor's.

So the computation happened and is reproducible. What is missing is the
certification, not the work.

## What the run found

The hypothesis concerns a rate of calcium transport and the dataset contains
transcript counts, so the exploration leaves the hypothesis where it found it.
The report says this plainly in its body and in its manifest, which is the
single most important thing it does.

What the dataset can speak to is one upstream node, fibrillin downregulation,
and it splits that claim:

- **FBN1 reproduces** to three significant figures: -1.2004 against the
  published -1.2, BH q = 3.4e-12. It holds between -1.200 and -1.204 across five
  filtering variants and near -1.2 in every between-line contrast.
- **FBN2 does not.** -0.358 against the published -0.9, BH q = 0.111, and
  significant in no between-line contrast.

Three further results decide how much weight any of this can carry. One
dystrophic replicate differs from its own two siblings by +0.788 log2 for FBN2,
the size of the published disease effect, so that effect is not distinguishable
from within-line replicate noise. The dystrophic line is independently less
proliferative and less myoblast-like, with the first principal component
separating the two lines completely, which supplies a differentiation-state
explanation for the one block-level result the report treats as its strongest
support. And the dystrophin positive control is weak at -0.431, BH q = 0.056, so
gene-level counts alone do not confirm the group labels.

## Post-lock work is where the audit trail thins

Findings F003 to F009 were computed after `MANIFEST.yaml` was closed, in memory,
writing no file under the artifact directory. The report is explicit about this,
and re-verified the 35 manifest entries afterwards.

The consequence for the reader is uneven. F003, F004, F005, F007 and F009 have
their code committed inside the `provenance_plot_*.json` payloads along with a
figure, so they are inspectable and re-runnable but their result tables are not
committed and the verified replay does not cover them. F006 and F008 have no
committed artifact at all and rest only on the report's prose.

That is unfortunate in proportion to how useful they are: the two findings that
most change the reading of this dataset, the within-line fibrillin swing and the
line-divergence analysis, are the two least auditable. Both are marked
`NEEDS_VERIFICATION` and should be re-derived from the committed locked count
matrix before being cited anywhere.

## What this means for the disease entry

The entry's `Fibrillin-Related ECM Protein Downregulation` node is supported by
a snippet asserting significant downregulation of both FBN1 and FBN2. The
snippet is an exact and correctly attributed quotation, so the evidence item is
not defective. But the FBN2 half is not supported by the dataset behind the
paper, and the node's claim therefore reads stronger than the data warrants.

Nothing in this exploration is promotable as it stands. Promotion would require
normal reference-cache and evidence validation against the publication, not
against this report.
