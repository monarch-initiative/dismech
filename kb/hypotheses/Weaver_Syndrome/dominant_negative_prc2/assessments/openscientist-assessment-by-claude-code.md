# OpenScientist report on `dominant_negative_prc2` — assessment narrative

Companion to `openscientist-assessment-by-claude-code.yaml`, which is authoritative.

## Why this run was commissioned

The Weaver entry records `functional_impact_category: UNKNOWN` on its variant node
because the literature splits two ways. In vitro reconstitution of tested EZH2 alleles
reads them as hypomorphic loss of function (PMID:26694085); a 2025 isogenic study reasons
from the absence of early truncating alleles and from disproportionate H3K27me2/3 loss at
low mutant expression to a dominant-negative mechanism (PMID:40846643). The entry carries
both as competing `mechanistic_hypotheses` and a `CONTROVERSY` discussion naming the
experiment that would separate them: an isogenic comparison of a heterozygous missense
knock-in against a heterozygous null in one background.

The question this run was meant to answer is narrow. Can a provider search settle that?

## What the run concluded, and what it actually showed

Its verdict is "partially-to-well supported", but its own caveats undercut reading that as
a resolution. It states plainly that dominant-negative interference and haploinsufficiency
both lower net PRC2 output, converge on the same reduced-H3K27me3 endpoint, and are best
viewed as compatible mechanisms at different molecular scales rather than exclusive
alternatives. That is the same conclusion the entry already encodes by leaving the
category `UNKNOWN`. The three evidence lines it calls convergent — the isogenic study, the
R684C mouse, and its own variant-spectrum computation — are each compatible with reduced
net PRC2 output from any cause, which is what the competing hypothesis also predicts. None
is a test that separates them.

## The two contributions worth keeping

**PMID:28696078.** A de novo 1.2-Mb deletion at 7q36.1 removing the whole *EZH2* gene, in a
child with tall stature and intellectual disability, whose authors conclude that
haploinsufficiency may replicate the Weaver phenotype. This was not in the entry. It is the
nearest human approximation to the null arm of the discriminating experiment, and it argues
that a poison protein is not required to produce the phenotype. It is a single case, and
the authors describe the presentation as Weaver-like rather than classic Weaver syndrome,
so it constrains the dominant-negative reading without excluding it. Promoted to the
`loss_of_function_prc2` hypothesis and named in the controversy rationale.

**The reciprocal arm is single-source.** The seed hypothesis asserted a reciprocal contrast
in which germline gain-of-function *EZH2* variants cause growth restriction. A targeted
PubMed search, with the queries committed in the run's search log, returned no independent
primary germline report; the only such comparison lives inside PMID:40846643 itself. The
report correctly separates this from somatic oncogenic Y641 alleles, which raise H3K27me3
but cause lymphoma rather than a growth syndrome. The hypothesis description was amended to
mark the arm single-source. This is a correction to curation I wrote, found by the run.

## Bundle quality

The variant-spectrum computation is real and its committed CSV reproduces every count in
the report exactly: 27 ClinVar Weaver-annotated pathogenic and likely-pathogenic alleles,
21 missense spanning codons 132 to 746, three truncating at codons 730, 733 and 738. The
gnomAD JSON records both query and response. The search log lists each query with the PMIDs
it returned, which is how PMID:28696078 traces to a search rather than to recall.

Against that: no `MANIFEST.yaml`, so the analysis-run gate cannot be applied; no environment
specification; and the analysis code exists only as an embedded string inside
`provenance_ezh2_weaver_lollipop.json`, while the report and the bundle's own figures README
point at `code/clinvar_gnomad_analysis.py`, which was never delivered. A curator replaying
this has to know to look in the provenance JSON. The figures README additionally claims the
lollipop PNG could not be copied out of the sandbox, which the delivered bundle contradicts
— the PNG is there. The analyses are therefore recorded as `PARTIAL` and
`PARTIALLY_AUDITABLE`.

## Disposition

The category stays `UNKNOWN`. Two curation changes were promoted, both verified against
fetched records. Nothing from the run's computational analyses was promoted, since a
partially auditable analysis cannot carry a retained claim.
