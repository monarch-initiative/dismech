# OpenScientist literature run, canonical dystrophin-loss model

Assessment of `../openscientist.md` by `claude-code`, 2026-11-25. The YAML
sidecar beside this file is authoritative; this is the human-readable version.

**Verdict: PARTIALLY_SUPPORTED.** The first edge of the canonical chain is
strongly supported. Several downstream steps are not, and one of them — that
restoring dystrophin should buy preserved function — has a clinical record more
divided than the entry's hypothesis description allows.

## What the run did

A hypothesis-search run on the literature template, so there is no
`ANALYSIS_STATUS` contract and no execution gate. It ran 114 minutes, returned
31 citations and eleven findings, and did real computation rather than only
reading: gnomAD v4 hemizygote depletion, ClinVar allele-class and reading-frame
tests, a ClinicalTrials.gov v2 portfolio classification, and a presymptomatic
transcriptome test on GSE6011.

Seven sources were accessed with queries, byte counts and checksums recorded.
One failed preflight. Two more are named as necessary and recorded as not
queried. Two analyses were superseded after the run found errors in its own
work, keeping both the wrong and the corrected figure.

## The one defect that bounds everything else

The analysis table cites code paths from `code/01_*.py` to `code/05_*.py`. The
bundle contains **no Python file at all**. The data section says "Full detail
with checksums is in `MANIFEST.yaml`", and no manifest was written.

The report's own *Expected artifacts not produced* section lists three
omissions, accurately, and mentions neither of these. So this is an unflagged
gap rather than a declared one.

Output tables and figures are committed, and the `provenance_plot_*.json`
payloads carry the plotting code, so every analysis stays inspectable at the
level of its results. None is re-executable. No analysis is therefore recorded
as `REPRODUCIBLE`, and no claim resting on one is `RETAINED`.

That matters most for the finding it would otherwise most support. The exon-skip
amenability check is the run's only external validation of its own machinery —
computed single-exon amenability reproducing published registry fractions for
exons 51, 45 and 53 to within two to three percentage points, and recovering
both known deletion hotspots. It is the reason to trust the frame arithmetic
everywhere else, and it is exactly what cannot be re-run.

## What earns the most credit

The run overturned its own best result. A coding-span modulo-three rule scored
112 of 202 exon-mapped deletions as in-frame, and the cysteine-rich
beta-dystroglycan-binding domain then appeared strongly enriched for pathogenic
in-frame deletions at Fisher p = 1.75e-05, FDR 1.0e-04 — a clean confirmation of
the seed's F-actin-to-DGC link. The DMD canonical coding sequence is 11,058 base
pairs, exactly divisible by three, so whole-gene and terminal deletions scored
as frame-preserving despite removing the entire protein: 23 of 25 were
mislabelled that way. After excluding them, nothing survives at any domain, FDR
1.0 crude and size-adjusted.

Both figures are kept and the superseded one carries the word `artifact` in its
filename. The generalisable warning is in the report: any reading-frame pipeline
that does not exclude gene-terminal and whole-gene deletions will
systematically mislabel the most severe allele class as frame-preserving.

The skipped analysis is handled the same way. GPL6244's annotation returned HTTP
404, the preflight log is committed, and the report states that the GSE38417
replication was not run and not reported and that the single-cohort limitation
therefore stands. No result was substituted.

## Where the chain holds and where it does not

**Holds.** Truncating variants are observed in hemizygous males a fifth as often
as synonymous ones — 12.6% against 53.1%, Fisher OR 0.128 — and 10.6% after
re-mapping onto the canonical transcript. The comparator is internal and the
cohort is right for an X-linked recessive disorder.

**Needs splitting.** Which isoform a variant truncates matters more than frame.
The most frequent truncating call in the gene reaches 140 hemizygous males and
is a frameshift only in a short isoform; two stop-gained calls at 38 and 11
hemizygotes sit in canonical intron 29, which carries the Dp260 promoter. Within
the canonical isoform, splice-site loss is tolerated five times more often than
coding-exon loss. The mouse comparison reaches the same conclusion from the other
direction: mdx retains short isoforms and is mild, isoform-null mice are severe.
The entry's single "functional dystrophin" node does not capture this.

**Does not hold as stated.** The calcium-dependent protease module shows no
coordinate induction, and CAPN3 — the most muscle-specific calpain — is *reduced*
at FDR 3.3e-03. The report is careful about what that can mean: calpain
activation is post-translational, so a transcriptome cannot confirm or refute the
step. But given CAPN3's role in sarcomere remodelling during regeneration, its
loss plausibly impairs repair rather than executing damage, which reverses the
causal sign the entry assigns.

**The most awkward fact.** Across four approved exon-skipping oligonucleotides
plus one AAV micro-dystrophin, larger dystrophin restoration did not correspond
to longer preserved walking. EMBARK's primary endpoint — change in North Star
Ambulatory Assessment at 52 weeks against placebo — did not reach significance,
and the benefit claims past that rest on propensity-weighted external controls
or on four treated patients at five years. The entry's hypothesis description
asserts that partial-restoration therapies "provide interventional validation of
this canonical chain". That clause is stronger than the record.

**Parallel branches the entry does not carry.** Satellite cell dysfunction looks
cell-autonomous: EGF treatment in mdx restored asymmetric division, regeneration
and muscle strength *without* restoring myofiber dystrophin. Calcium entry is
apportioned between stretch-activated channels, TRPV2 translocation and NOX2
redox signalling as well as microruptures, not attributed to tearing alone. And
nNOS delocalisation is a domain-specific mechanism requiring spectrin repeats
R16/17, which explains Becker severity variation the frame rule cannot and
predicts that micro-dystrophins omitting those repeats underperform.

## Relevance to the competing hypothesis in this entry

The GSE6011 module results bear on the clearance-versus-entry question curated
in `calcium_clearance_failure_model`, without settling it. The entry-side
correlates move — CYBB raised at FDR 0.025, TRPC1 raised at trend level — while
the calcium-handling module shows no shift at all. That is the opposite ordering
to the block-level result in the clearance run, which found the SR calcium block
shifted and the entry block not. The two runs used different cohorts, different
tissue states and different module memberships, so this is a discrepancy to
reconcile rather than a verdict. Neither hypothesis is adjudicated here.

## Artifact deviation

One declared artifact is deliberately absent from the tree:
`provenance_gnomad_v4_DMD_variants_raw.json`, a 4.5 MB raw API dump the report
itself lists among four large recoverable downloads excluded by identifier and
sha256. The gnomAD query and checksum that reproduce it are in the report. All
79 other declared artifacts are committed.

## Promotion

Nothing here is promotable as it stands. The literature claims are leads: each
would need its reference fetched into `references_cache/` and an exact snippet
verified before any of it reached the entry. The computed claims need either a
provider rerun that bundles the code or an independent reimplementation from the
committed tables.
