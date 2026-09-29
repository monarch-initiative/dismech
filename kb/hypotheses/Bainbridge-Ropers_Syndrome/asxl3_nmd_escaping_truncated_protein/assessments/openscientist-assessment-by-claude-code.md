# OpenScientist report on `asxl3_nmd_escaping_truncated_protein` — assessment narrative

Companion to `openscientist-assessment-by-claude-code.yaml`, which is authoritative.

## Why this run was commissioned

The Bainbridge-Ropers entry records `functional_impact_category: UNKNOWN` on its variant
node because truncating *ASXL3* alleles split into two classes with different expected
fates. Alleles that trigger nonsense-mediated decay reduce ASXL3 message and protein, which
is the dosage model the pathophysiology chain is built on. Alleles that escape decay should
yield a truncated protein whose activity has never been assayed, and carriers of the two
classes differ phenotypically. The entry carries both readings as competing
`mechanistic_hypotheses` with a `CONTROVERSY` discussion, whose discriminating experiment
begins with a step nobody has published: does a truncated ASXL3 protein exist in patient
cells at all?

## What the run found, and why it matters more than the parallel Weaver run

Its verdict — that the decay-escaping mechanism is at most a phenotypic modifier and not
the primary mechanism, with its central molecular claim untested in ASXL3 material — is
well argued and does not by itself move the category. The valuable part is narrower and
sharper.

The entry cited PMID:42494517, the largest ASXL3 cohort, for a phenotype difference
tracking the decay-escaping class: autistic features are enriched there. That reads as
support for the truncated-protein hypothesis, and it is how I curated it. The run read the
same paper further. The *core* severity measures run the other way: intellectual disability
and global developmental delay are more severe in the decay-subject null group. The
inference is clean. If a decay-escaping truncated protein were simply more toxic than a
null, the no-decay class should carry the greater core burden. It does not.

That is a correction to curation I wrote, from a paper I had already cited, found by
reading it more completely than I did. The alternative hypothesis is now qualified as a
candidate modifier rather than a symmetric competitor, and the counter-sentence is curated
as a `REFUTE` item against it. The inference is not airtight — severity could track variant
position or residual function rather than protein activity, and the report says so — but it
changes the balance of the argument.

The run adds a second directional argument I did not have. The one functional readout from
ASXL3 patient material shows *increased* H2AK119 ubiquitination, which is the
loss-of-function direction and the opposite of the ASXL1 gain-of-function paradigm this
hypothesis reasons from, where truncated ASXL1 hyperactivates BAP1 and decreases the mark.
The report caveats this correctly: the assayed allele underwent decay, so it does not
represent the class in question. Recorded in the controversy rationale with that caveat
intact.

## What was not promoted

The ASXL1 "loss-is-gain" literature (PMID:35122023, PMID:34186160, PMID:34536441) is the
strongest available support for the alternative hypothesis and is entirely cross-gene. The
report says so itself, calling it plausibility rather than proof for ASXL3. It stays in the
assessment as a lead — it is also relevant to the Bohring-Opitz entry, where the same
question arises for ASXL1 itself — and does not enter the disease YAML, because a mechanism
demonstrated in a paralogue is not evidence about this gene's alleles.

The exon, decay-boundary and domain mapping is a prediction about a protein whose existence
in patient cells is exactly what the run's own literature search failed to find evidence
for. It is reported honestly as a predictive match rather than a demonstration, and it is
not promoted.

## Bundle quality

The data outputs are present and internally consistent: a twelve-exon coding map with
per-exon decay classification, a domain table, a summary JSON whose transcript, protein
length, junction and boundary values agree with the report's prose, and a positional
analysis JSON recording sources, retrieval date and gnomAD constraint. The access log
records each endpoint call.

The report states that checksums and replay instructions live in
`openscientist_artifacts/MANIFEST.yaml` and names two analysis scripts under a code
directory. None of the three files is in the bundle. Unlike the parallel Weaver run there
is no provenance record carrying the code as an embedded string, so neither computation is
replayable from what was committed, and the analysis-run gate cannot be applied. The
outputs remain inspectable, which is why the analyses are `PARTIAL` rather than
`REPORTED_ONLY`.

## Disposition

The category stays `UNKNOWN`. One hypothesis was qualified and one `REFUTE` evidence item
promoted, both verified against the cached record. Nothing from the computational analyses
was promoted.
