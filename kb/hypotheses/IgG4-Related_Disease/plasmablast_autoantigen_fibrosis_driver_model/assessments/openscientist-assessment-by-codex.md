# Assessment of the OpenScientist plasmablast–autoantigen report

## Overall assessment

**Verdict on the integrated mechanism: partially supported.**

The report's central judgment is directionally sound. Oligoclonal plasmablasts,
clonally expanded lesional CD4-positive cytotoxic T cells, Tfh-associated
B-cell responses, and clinical response to B-cell depletion form the best
supported current scaffold. The report also correctly identifies that the
B-lineage-to-CTL and CTL-to-fibroblast edges remain inferred.

The review becomes less reliable when it tries to convert candidate
autoreactivities, clinical phenotype classes, atopy prevalence, and isolated
aortitis into direct mechanistic conclusions. Several of those arguments use
reviews as though they were primary human experiments. They do not justify
downgrading the scaffold, although they do sharpen its knowledge gaps.

## What the report gets right

### The main cellular populations are replicated

[PMID:24815737](https://pubmed.ncbi.nlm.nih.gov/24815737/) supports an
oligoclonal, somatically hypermutated plasmablast compartment linked to active
disease and relapse. [PMID:26971690](https://pubmed.ncbi.nlm.nih.gov/26971690/)
supports clonally expanded CD4-positive CTLs across affected tissues, and
[PMID:38092138](https://pubmed.ncbi.nlm.nih.gov/38092138/) supplies independent
single-cell and spatial support for GZMK-positive cytotoxic T cells and
activated extrafollicular B cells.

### B-cell depletion is strong but indirect mechanistic evidence

The report appropriately calls rituximab evidence indirect.
[PMID:38781535](https://pubmed.ncbi.nlm.nih.gov/38781535/) links deeper
B-cell depletion to fewer relapses in a 33-patient retrospective cohort.
Reduction of CTLs during B-cell-depletion-associated remission is compatible
with B-lineage support of those cells, but it does not establish antigen
presentation as the relevant function.

### The two central causal edges remain open

Existing studies establish CTL clonality and profibrotic cytokine expression;
they do not show that a B cell presents the relevant antigen to a CTL or that
the CTL activates an IgG4-RD fibroblast to generate storiform fibrosis.
[PMID:27667138](https://pubmed.ncbi.nlm.nih.gov/27667138/) explicitly calls the
antigen-presentation link presumed. Preserving these edges as knowledge gaps is
the report's most useful curation recommendation.

## Where the report needs correction

### Candidate autoantigens are not four established pathogenic targets

In [PMID:31612628](https://pubmed.ncbi.nlm.nih.gov/31612628/), responses to
PHB1, annexin A11, and laminin 511-E8 were infrequent and not
significantly different from controls. Broader autoreactivity associated with
severity, but the study did not establish pathogenicity.
[PMID:33974929](https://pubmed.ncbi.nlm.nih.gov/33974929/) is a separate,
functionally stronger anti-IL-1RA result in a subset. The report conflates
candidate recognition, association, and direct functional evidence.

### Phenotype-specific immune dominance is review-level synthesis

[PMID:30612117](https://pubmed.ncbi.nlm.nih.gov/30612117/) robustly derives four
organ-distribution phenotypes, but performs no immune-cell profiling.
[PMID:39306708](https://pubmed.ncbi.nlm.nih.gov/39306708/) is a review, not a
phenotype-matched primary cohort. The proposed mapping of retroperitoneal
fibrosis/aortitis to CX3CR1-positive CTLs and Mikulicz/systemic disease to Tfh2
is a lead requiring direct testing.

### The IgG1 argument attacks a claim the seed does not make

The seed calls plasmablasts a marker and sustaining B-lineage population, then
assigns fibrogenic cytokine production to CD4-positive CTLs. It does not say
that IgG4 antibody is the dominant tissue-damaging effector. Review-level
discussion of possible IgG1 pathogenicity is therefore complementary, not a
contradiction of the modeled scaffold.

### Atopy prevalence is not evidence of causal primacy

[PMID:41912044](https://pubmed.ncbi.nlm.nih.gov/41912044/) quantifies common
allergy, eosinophilia, and hyper-IgE but explicitly says that the causal and
mechanistic relationship remains unclear. These observations justify
stratification; they do not establish that a Th2/atopic axis drives a defined
patient subset.

### The phlebitis citation is outside confirmed IgG4-RD

The 11 patients in [PMID:21036629](https://pubmed.ncbi.nlm.nih.gov/21036629/)
had isolated thoracic aortitis, no history of IgG4-RD, and no IgG4-RD during
follow-up. The authors said only that a subset might represent an IgG4-related
manifestation. That cohort cannot demonstrate failure of a causal edge within
confirmed IgG4-RD, and the seed does not claim plasma-cell infiltration alone
causes obliterative phlebitis.

### Activity biomarkers do not identify the proximate effector

sIL-2R tracks disease burden and treatment response, but its correlations do
not prove that T-cell activity, rather than an antibody or another correlated
immune process, causes tissue injury.

## Curation implication

Keep the hypothesis `CANONICAL`, with its causal links explicitly qualified.
`CANONICAL-WITH-QUALIFICATIONS` is not a schema value. Preserve the antigen,
B-lineage-to-CTL, CTL-to-fibroblast, vascular-injury, and organ-tropism gaps.
Treat IgG1, atopy, complement, and phenotype-specific immune dominance as
testable complementary leads until direct primary evidence resolves them.

This assessment is intentionally sidecar-only. It neither imports the report's
candidate annotations nor edits the disease YAML or reference cache.
