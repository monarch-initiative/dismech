# Citations for Research Query

**Query:** # Mechanistic Hypothesis Search (Dataset-Anchored)

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

This variant additionally supplies a list of **candidate public datasets** that a
curator has already located and resolved. Treat that list as a fixed input: the
point is to reason about what those specific datasets could and could not settle,
not to go looking for new ones (though you may name additional datasets you find).

## Target Disease
- **Disease Name:** Adult-Onset Autosomal Dominant Demyelinating Leukodystrophy
- **Category:** Neurodegenerative Disease

## Target Hypothesis
- **Hypothesis ID:** oligodendrocyte_silencer_loss_model
- **Hypothesis Label:** Oligodendrocyte Silencer Loss Model
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: oligodendrocyte_silencer_loss_model
hypothesis_label: Oligodendrocyte Silencer Loss Model
status: EMERGING
description: In upstream-deletion ADLD, LMNB1 overexpression is proposed to follow from loss of a CTCF-associated
  silencer upstream of LMNB1 that represses the gene specifically in oligodendrocyte-lineage cells, through
  promoter looping and PRC2 recruitment. The inverted-duplication allele is proposed to converge on the
  same loss of silencer control by sequestering the original silencer (an Orca contact prediction). The
  competing model, proposed first for the approximately 660 kb deletion, is that removal of a topological
  domain boundary lets forebrain-directed enhancers contact the LMNB1 promoter. The 2025 functional study
  leaves open whether silencer loss alone is sufficient or ectopic enhancer contact is also required.
  Neither the silencer-promoter contact nor the boundary has been measured in human oligodendrocytes.
applies_to_subtypes:
- Upstream Deletion-Related ADLD
evidence:
- reference: PMID:39910058
  reference_title: An oligodendrocyte silencer element underlies the pathogenic impact of lamin B1 structural
    variants.
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: the presence of the CTCF2 sequence in both orientations significantly reduced luciferase activity
    only in Oli-neu cells, signifying silencer activity that is specific for oligodendrocyte-lineage cells
  explanation: Reporter assays localize oligodendrocyte-lineage-specific silencer activity to the CTCF2
    element.
- reference: PMID:39910058
  reference_title: An oligodendrocyte silencer element underlies the pathogenic impact of lamin B1 structural
    variants.
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: observed an increase in Lmnb1 expression only in Oli-neu cells but not in either the N2A or
    3T3 cells
  explanation: Deleting the element raises Lmnb1 expression in an oligodendrocyte-lineage line only.
```

## Curator-Supplied Candidate Datasets

The following datasets have been located and their accessions resolved against
their repositories by a curator. Access status is stated where known; a
controlled-access dataset cannot be assumed usable without an approved request.

All accessions below were resolved against the 4D Nucleome (4DN) Data Portal (data.4dnucleome.org) on 2026-11-13. All are wild-type: no dataset contains an ADLD allele. 4DN processed files are on GRCh38; the ADLD deletion intervals recorded in the knowledge base are hg19 and need liftover: ~660 kb deletion hg19 chr5:125,385,805-126,043,053; 249 kb deletion hg19 chr5:125,855,011-126,103,996; their overlap is hg19 chr5:125,855,011-126,043,053.

Access: 4DN file downloads need a free portal account and access key. Files mirrored on the AWS Open Data bucket (4dn-open-data-public) download without a key; at the time of checking only some of the files below were mirrored.

1. 4DN dataset "HiChIP on human cortical neural cells": H3K4me3 HiChIP on sorted adult human cortical nuclei, by cell type and donor. Oligodendrocytes/OPC (NeuN- OLIG2+), 9 donors; excitatory neurons, 8; interneurons, 7; microglia (NeuN- PU1+), 7; astrocytes, 5. Several donors contribute more than one cell type, so within-donor comparisons are possible. Processed files per set: pairs, .hic and .mcool (GRCh38); BAMs are restricted. Example oligodendrocyte set 4DNESC4J62CH (donor UCSF2018-002), mcool 4DNFIDAEB919, openly downloadable at https://4dn-open-data-public.s3.amazonaws.com/fourfront-webprod/wfoutput/5156ec0f-63a0-4ec9-bf28-3037e98c6c80/4DNFIDAEB919.mcool . Other oligodendrocyte sets: 4DNESB3SIXSL, 4DNESTDDORXU, 4DNESSUI9T7M, 4DNESKKUWHXY, 4DNESQL937TL, 4DNESVL32QPU, 4DNESK1VH3Y9, 4DNESRE1E33C. Comparator sets include microglia 4DNESTPBOMIT and 4DNES1B1TIOJ (openly mirrored mcools) and astrocytes 4DNESJHI15YI, 4DNESAE33PJ8. Browse: https://data.4dnucleome.org/browse/?dataset_label=HiChIP+on+human+cortical+neural+cells&experimentset_type=replicate&type=ExperimentSetReplicate . No publication is linked to these sets on the portal.

2. 4DN datasets "ATAC-seq on human cortical neural cells" (36 sets) and "RNA-seq on human cortical neural cells" (42 sets): the same sorted cortical cell types and donor identifiers as item 1, e.g. ATAC-seq on cortical oligodendrocytes 4DNESOGDCWOG and RNA-seq on cortical oligodendrocytes 4DNESYCPG6S5.

3. 4DN dataset "snm3c-seq on hippocampus tissue": single-nucleus methyl-Hi-C on postmortem neurotypical human hippocampus, 40 sets, e.g. 4DNESATHQR75 (Zemke NR et al. 2024, doi:10.1101/2024.10.14.618338). Cell types are assigned per nucleus; whether oligodendrocytes are resolved with enough contacts at one locus is unverified.

4. HFFc6 human foreskin fibroblast reference: Micro-C 4DNESWST3UBH and CTCF CUT&Tag 4DNES89MZOPI. Relevant because LMNB1 expression in ADLD alleles has been measured in patient fibroblasts, not in oligodendrocytes.

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

### Mechanistic Causal Chain

Describe the causal chain implied by the hypothesis from upstream trigger to
clinical manifestation. Identify where the literature is strong, where the links
are inferred, and where there are missing causal steps.

### Dataset-Anchored Analysis

This section is the reason this report was commissioned. For **each** dataset in
the curator-supplied list above, state:

- **Fitness for purpose.** Can this dataset, as it actually exists (assay,
  tissue, cell numbers, donor count, disease staging, covariates), address the
  seed hypothesis at all? Say plainly when it cannot. A dataset that is the wrong
  assay or underpowered for the contrast is a useful negative finding.
- **The specific analysis.** Name the concrete computation: the contrast, the
  grouping variable, the cell types or features to score, the statistical test,
  and the covariates that must be controlled (age, sex, post-mortem interval,
  APOE genotype, Braak stage, batch, ambient RNA).
- **The discriminating prediction.** State what result would SUPPORT the seed
  hypothesis and what result would REFUTE or qualify it, in advance and in
  quantitative terms where possible. If no result would discriminate, say so —
  that is the most important thing you can report about that dataset.
- **Known confounds and prior analyses.** Has this dataset already been analyzed
  for this question, and by whom? Re-deriving a published result is not a test.
  Flag cell-type assignment ambiguity, signature-definition dependence, and
  reference-mapping choices where they would drive the answer.

Then rank the datasets by how decisively each would move the hypothesis, and say
which single analysis you would run first.

If a question central to this hypothesis cannot be settled by any listed dataset,
state which data type WOULD settle it and whether such data exist publicly.

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
evidence or experiment would resolve it.

### Alternative Models

List competing or complementary hypotheses. For each, explain whether it is an
alternative to the seed hypothesis, a downstream consequence, an upstream cause,
or a parallel mechanism.

### Discriminating Tests

Recommend concrete studies or assays that would most efficiently test this
hypothesis against alternatives. Include patient stratification, biomarkers,
sample type, model system, perturbation, and expected result where applicable.
Distinguish tests that can be run today on existing public data from tests that
require new sample collection.

### Curation Leads

Provide candidate updates for the KB, but label these as leads requiring curator
verification. Include:

- candidate evidence references and exact abstract snippets to verify
- candidate pathophysiology nodes or edges
- candidate ontology terms for cell types and biological processes
- candidate subtype restrictions or status changes
- candidate `knowledge_gaps` or discussion prompts for unresolved causal claims,
  conflicting evidence, or explicit source/data absences
- candidate `datasets:` entries, giving the accession exactly as the repository
  states it

Do not invent dataset accessions. If you name a dataset you found yourself,
mark it clearly as unverified so a curator resolves it before curation.

If the provider supports artifacts, produce artifact-friendly outputs such as an
evidence matrix, mechanistic diagram, knowledge-gap table, or comparison table.
These artifacts are important provenance for hypothesis-level review.

**Provider:** openscientist
**Generated:** 2026-11-14T07:26:53.851232

1. PMID:39910058
2. PMID:25701871
3. PMID:39078102
4. PMID:33034697
5. PMID:37609196
6. PMID:26311780
7. PMID:27854160
8. PMID:30949481
9. PMID:33252173
10. PMID:25637521