# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Rosacea
- **Category:** Complex

## Target Hypothesis
- **Hypothesis ID:** phyma_fibroblast_identity
- **Hypothesis Label:** Rhinophyma fibroblasts are the PTGDS-high pro-inflammatory population of papulopustular disease, not a scar-type myofibroblast
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: phyma_fibroblast_identity
hypothesis_label: Rhinophyma fibroblasts are the PTGDS-high pro-inflammatory population of papulopustular
  disease, not a scar-type myofibroblast
status: EMERGING
applies_to_subtypes:
- Phymatous Rosacea
description: 'Single-cell transcriptomics of papulopustular rosacea identifies an expanded pro-inflammatory
  fibroblast population, marked by PTGDS, as the leading source of inflammatory and vasodilatory signals,
  and fibroblast depletion or PTGDS knockdown blocks disease in mice. Rhinophyma, the end-stage phymatous
  lesion, is clinically fibrotic yet reverts toward normal after surgical debulking, unlike hypertrophic
  scar. The hypothesis is that the phyma fibroblast is the same inflammation-driven state as the papulopustular
  fibroblast, persisting rather than transitioning to a scar-type myofibroblast, which would explain both
  the reversibility and why the fibrotic remodeling node feeds phymatous change. An exploratory comparison
  of the rhinophyma versus hypertrophic scar versus healthy skin single-cell atlas (ArrayExpress E-MTAB-16629)
  against the published papulopustular fibroblast markers asks whether rhinophyma fibroblasts carry the
  PTGDS pro-inflammatory signature or the ACTA2/COL1A1 myofibroblast signature of scar. Downstream causal
  edges that belong to this hypothesis opt in via hypothesis_groups: [phyma_fibroblast_identity].'
evidence:
- reference: PMID:39384741
  reference_title: Single-cell transcriptomics reveals aberrant skin-resident cell populations and identifies
    fibroblasts as a determinant in rosacea.
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: The papulopustular rosacea is featured by expansion of pro-inflammatory fibroblasts, Schwann,
    endothelial and macrophage/dendritic cells.
  explanation: The papulopustular fibroblast population the phyma fibroblast is to be compared against.
- reference: PMID:39384741
  reference_title: Single-cell transcriptomics reveals aberrant skin-resident cell populations and identifies
    fibroblasts as a determinant in rosacea.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: Depletion of fibroblasts or knockdown of PTGDS, a gene specifically upregulated in fibroblasts,
    blocks rosacea development in mice.
  explanation: Establishes PTGDS as the marker and the fibroblast as causal in the inflammatory subtype.
notes: 'Exploratory dataset run: arrayexpress:E-MTAB-16629 (released 2026-02-18). The papulopustular single-cell
  data of Chen et al. have no public accession in the cached full text, so the comparison must use the
  published marker genes rather than a joint embedding.'
```

## Research Objective

Build a focused hypothesis-search report that answers:

1. What is the strongest direct evidence for this hypothesis?
2. What evidence argues against it, fails to reproduce it, or limits its scope?
3. Which claims are established, emerging, speculative, or contradicted?
4. Which patient subtypes, stages, tissues, cell types, molecular pathways, or
   biomarkers does the hypothesis best explain?
5. Which alternative or competing mechanistic hypotheses explain the same disease
   features better or more parsimoniously?
6. What are the explicit knowledge gaps: missing causal steps, unconfirmed edges,
   contradictory evidence, unknown source-to-target links, or source/data absences?
7. What experiments, cohorts, assays, datasets, or trials would most directly
   distinguish this hypothesis from alternatives?

Use primary literature whenever possible. Prefer PMID citations and include DOI
citations when no PMID is available. Treat reviews as orientation unless they
contain directly relevant synthesized evidence that should be clearly labeled as
review-level support.

When dataset or scientific-tool access is available, use it for questions that
can be tested computationally rather than limiting the run to literature search.
Preflight the required data lake, databases, packages, credentials, and tools
before claiming that an analysis can run. Never silently fall back from a failed
dataset/tool analysis to literature synthesis or model knowledge: report the
failure, the fallback, and the resulting limitation explicitly. A proposed
analysis must never be described as performed.

## Required Output

### Executive Judgment

Give a concise verdict on the hypothesis as of the current literature:
supported, partially supported, unresolved, weakly supported, or refuted. Explain
the reasoning and the most important caveats.

### Evidence Matrix

Create a table with one row per important evidence item:

- Citation (PMID preferred)
- Evidence type (human clinical, model organism, in vitro, computational, review)
- Supports / refutes / qualifies / competing
- Mechanistic claim tested
- Key finding
- Disease subtype or context
- Confidence and limitations

### Data and Tool Use

Inventory every dataset, database, API, supplementary file, or local input
material to the report. For each, state:

- stable accession or URI, repository/source, version or snapshot, and retrieval
  date where known;
- whether it was only cited/proposed, actually accessed, searched with no usable
  result, or could not be verified;
- the exact query, filters, cohort, sample subset, organism, tissue, assay, and
  comparison used where applicable;
- whether the accession resolved and whether its subject matter is genuinely
  relevant to this disease and hypothesis.

For accessed sources and negative searches, save a sanitized query response,
input manifest, or search log in the provider artifact bundle; prose alone does
not establish access or a negative result.

Inventory each attempted analysis separately. Trace input -> method -> output,
including software/model versions, material parameters, code or workflow,
environment, random seeds where relevant, output files, and limitations. Label
the execution outcome as succeeded, partial, failed, skipped, or reported-only.
Do not count a prose assertion without inspectable execution evidence as a
successful analysis.

### Mechanistic Causal Chain

Describe the causal chain implied by the hypothesis from upstream trigger to
clinical manifestation. Identify where the literature is strong, where the links
are inferred, and where there are missing causal steps.

### Knowledge Gaps

Identify explicit known unknowns surfaced by the search. Treat absence of
evidence as a curation-relevant finding only when the search actually checked for
it. Include:

- Unknown or weakly supported causal steps in the hypothesis
- Unconfirmed causal graph edges that need direct perturbation or longitudinal
  evidence
- Conflicting evidence, failed replications, or incompatible subtype-specific
  findings
- Unknown mechanism of action for relevant treatments, biomarkers, or
  interventions tied to this hypothesis
- Source-level or dataset-level absences, such as no relevant GenCC, ClinGen,
  trial, omics, or cohort evidence found as of the search date

For each gap, state the scope, why it matters, what was checked, and what
evidence or experiment would resolve it. A negative database search must include
the database/version, query, filters, and search date; otherwise label it
unverified rather than claiming absence.

### Alternative Models

List competing or complementary hypotheses. For each, explain whether it is an
alternative to the seed hypothesis, a downstream consequence, an upstream cause,
or a parallel mechanism.

### Discriminating Tests

Recommend concrete studies or assays that would most efficiently test this
hypothesis against alternatives. Include patient stratification, biomarkers,
sample type, model system, perturbation, and expected result where applicable.

### Curation Leads

Provide candidate updates for the KB, but label these as leads requiring curator
verification. Include:

- candidate evidence references and exact abstract snippets to verify
- candidate pathophysiology nodes or edges
- candidate ontology terms for cell types and biological processes
- candidate subtype restrictions or status changes
- candidate `knowledge_gaps` or discussion prompts for unresolved causal claims,
  conflicting evidence, or explicit source/data absences

If the provider supports artifacts, produce a provider artifact bundle containing
canonical `MANIFEST.yaml` (schema version, status/fallback flags, checksummed
inputs/outputs, and replay verification), code/query/configuration, an
environment or package-version record,
sanitized execution logs, and small derived tables/figures needed to inspect the
result beneath `kb/hypotheses/Rosacea/phyma_fibroblast_identity/openscientist_artifacts`. Do not create an empty bundle when no data
source was accessed and no analysis ran. Give each artifact a stable relative
path and connect computed claims to their input, method, and output artifacts.
Do not bundle large recoverable raw
downloads, a provider data lake, controlled/patient-level data, credentials, or
signed URLs; record their stable external identifiers, versions, and checksums
instead. State explicitly when an expected artifact is external, local-only,
missing, or was not produced.

**Provider:** openscientist
**Generated:** 2026-09-06T18:50:42.850829

1. PMID:39384741
2. PMID:25421393
3. PMID:20531985
4. PMID:31066603
5. PMID:40478772
6. PMID:24563692
7. PMID:22076323
8. PMID:42106045
9. PMID:41898724
10. PMID:42423091
11. PMID:24206029