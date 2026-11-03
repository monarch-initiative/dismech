---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-16T01:33:22.085703'
end_time: '2026-10-16T02:05:26.084127'
duration_seconds: 1924.0
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: MYH7-Related Skeletal Myopathy
  category: Mendelian
  hypothesis_group_id: shared_myosin_rod_mechanism
  hypothesis_label: MYH7 and MYH2 light meromyosin variants share a common head-sequestration
    defect
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: shared_myosin_rod_mechanism\nhypothesis_label:\
    \ MYH7 and MYH2 light meromyosin variants share a common head-sequestration defect\n\
    status: EMERGING\ndescription: The same loss of the super-relaxed state and raised\
    \ ATP demand was found for common LMM variants\n  in both MYH7 (type 1 fibres)\
    \ and MYH2 (type 2A fibres). If general, the rod myosinopathies would share\n\
    \  one mechanism across fibre types, which would argue for a shared mechanism\
    \ module and for testing the\n  same modulators in MYH2 myopathy.\nevidence:\n\
    - reference: PMID:37788100\n  reference_title: Human skeletal myopathy myosin\
    \ mutations disrupt myosin head sequestration.\n  supports: SUPPORT\n  evidence_source:\
    \ IN_VITRO\n  snippet: Here, we used multiple approaches to analyze the effects\
    \ of common MYH7 and MYH2 mutations\n    in the light meromyosin (LMM) region\
    \ of myosin.\n  explanation: The study analysed MYH7 and MYH2 LMM variants side\
    \ by side."
  artifact_dir: kb/hypotheses/MYH7-Related_Skeletal_Myopathy/shared_myosin_rod_mechanism/openscientist_artifacts
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 5
term_validation:
  total_terms: 0
  verified: 0
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 9
artifact_sources:
  openscientist_artifacts_zip: 9
artifacts:
- filename: final_report.html
  path: openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: kb_hypotheses_MYH7-Related_Skeletal_Myopathy_shared_myosin_rod_mechanism_openscientist_artifacts_data_evidence_matrix.csv
  path: openscientist_artifacts/kb_hypotheses_MYH7-Related_Skeletal_Myopathy_shared_myosin_rod_mechanism_openscientist_artifacts_data_evidence_matrix.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist evidence matrix
- filename: kb_hypotheses_MYH7-Related_Skeletal_Myopathy_shared_myosin_rod_mechanism_openscientist_artifacts_data_gencc_myh7_myh2.csv
  path: openscientist_artifacts/kb_hypotheses_MYH7-Related_Skeletal_Myopathy_shared_myosin_rod_mechanism_openscientist_artifacts_data_gencc_myh7_myh2.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist gencc myh7 myh2
- filename: kb_hypotheses_MYH7-Related_Skeletal_Myopathy_shared_myosin_rod_mechanism_openscientist_artifacts_data_lmm_variant_heptad_analysis.csv
  path: openscientist_artifacts/kb_hypotheses_MYH7-Related_Skeletal_Myopathy_shared_myosin_rod_mechanism_openscientist_artifacts_data_lmm_variant_heptad_analysis.csv
  media_type: text/csv
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist lmm variant heptad analysis
- filename: kb_hypotheses_MYH7-Related_Skeletal_Myopathy_shared_myosin_rod_mechanism_openscientist_artifacts_figures_README.md
  path: openscientist_artifacts/kb_hypotheses_MYH7-Related_Skeletal_Myopathy_shared_myosin_rod_mechanism_openscientist_artifacts_figures_README.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist README
- filename: kb_hypotheses_MYH7-Related_Skeletal_Myopathy_shared_myosin_rod_mechanism_openscientist_artifacts_logs_database_query_log.md
  path: openscientist_artifacts/kb_hypotheses_MYH7-Related_Skeletal_Myopathy_shared_myosin_rod_mechanism_openscientist_artifacts_logs_database_query_log.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist database query log
- filename: kb_hypotheses_MYH7-Related_Skeletal_Myopathy_shared_myosin_rod_mechanism_openscientist_artifacts_logs_execution_log.md
  path: openscientist_artifacts/kb_hypotheses_MYH7-Related_Skeletal_Myopathy_shared_myosin_rod_mechanism_openscientist_artifacts_logs_execution_log.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist execution log
- filename: kb_hypotheses_MYH7-Related_Skeletal_Myopathy_shared_myosin_rod_mechanism_openscientist_artifacts_logs_pubmed_search_log.md
  path: openscientist_artifacts/kb_hypotheses_MYH7-Related_Skeletal_Myopathy_shared_myosin_rod_mechanism_openscientist_artifacts_logs_pubmed_search_log.md
  media_type: text/markdown
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist pubmed search log
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** MYH7-Related Skeletal Myopathy
- **Category:** Mendelian

## Target Hypothesis
- **Hypothesis ID:** shared_myosin_rod_mechanism
- **Hypothesis Label:** MYH7 and MYH2 light meromyosin variants share a common head-sequestration defect
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: shared_myosin_rod_mechanism
hypothesis_label: MYH7 and MYH2 light meromyosin variants share a common head-sequestration defect
status: EMERGING
description: The same loss of the super-relaxed state and raised ATP demand was found for common LMM variants
  in both MYH7 (type 1 fibres) and MYH2 (type 2A fibres). If general, the rod myosinopathies would share
  one mechanism across fibre types, which would argue for a shared mechanism module and for testing the
  same modulators in MYH2 myopathy.
evidence:
- reference: PMID:37788100
  reference_title: Human skeletal myopathy myosin mutations disrupt myosin head sequestration.
  supports: SUPPORT
  evidence_source: IN_VITRO
  snippet: Here, we used multiple approaches to analyze the effects of common MYH7 and MYH2 mutations
    in the light meromyosin (LMM) region of myosin.
  explanation: The study analysed MYH7 and MYH2 LMM variants side by side.
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
result beneath `kb/hypotheses/MYH7-Related_Skeletal_Myopathy/shared_myosin_rod_mechanism/openscientist_artifacts`. Do not create an empty bundle when no data
source was accessed and no analysis ran. Give each artifact a stable relative
path and connect computed claims to their input, method, and output artifacts.
Do not bundle large recoverable raw
downloads, a provider data lake, controlled/patient-level data, credentials, or
signed URLs; record their stable external identifiers, versions, and checksums
instead. State explicitly when an expected artifact is external, local-only,
missing, or was not produced.


## Output

# Mechanistic Hypothesis Search — MYH7-Related Skeletal Myopathy

## Hypothesis under evaluation

- **Hypothesis ID:** `shared_myosin_rod_mechanism`
- **Label:** MYH7 and MYH2 light meromyosin (LMM) variants share a common head-sequestration defect
- **Disease:** MYH7-Related Skeletal Myopathy (Mendelian)
- **Status in KB:** EMERGING
- **Seed claim:** Common LMM-region variants in both *MYH7* (slow, type 1 fibres) and *MYH2* (fast, type 2A fibres) produce the *same* loss of the myosin super-relaxed state (SRX) and the *same* raised basal ATP demand, implying that the "rod myosinopathies" share one mechanistic module across fibre types — and, by corollary, that SRX-stabilising modulators tested in one should work in the other.

---

## Summary

This report evaluates whether dominant light-meromyosin (rod) variants in *MYH7* and *MYH2* converge on a single, shared disease mechanism: loss of the myosin super-relaxed (SRX) state through impaired head sequestration, with raised basal ATP demand. Over five iterations the investigation combined focused literature search (28 papers reviewed), an original computational sequence/charge analysis of the LMM regions of both genes, and verification queries against GenCC, ClinVar, and ClinicalTrials.gov.

The verdict is **PARTIALLY SUPPORTED (appropriately EMERGING).** The hypothesis rests on one genuinely direct primary study — Carrington et al. 2023 ([PMID: 37788100](https://pubmed.ncbi.nlm.nih.gov/37788100/)) — that measured, side by side for *MYH7* and *MYH2* LMM variants, the two defining features of the seed claim (reduced SRX fraction and increased basal myosin ATP consumption in patient muscle, with contractility spared). An independent sequence analysis performed here strengthens the structural plausibility: all nine literature-curated *MYH7* LMM pathogenic residues are strictly conserved in *MYH2*, and the variants are statistically enriched for loss of conserved coiled-coil surface charges (one-sided binomial p = 1.0 × 10⁻⁴). So the structural substrate for a shared mechanism is real.

However, the cross-fibre-type generalisation hangs on a **single study with no independent MYH2 replication**, and the proposed molecular bridge — that lost SRX equals impaired folded-back head sequestration (the interacting-heads motif, IHM) — is **actively contested** in the current literature (PMID 38103642, 31540109, 37131793, 40727670). Competing aggregation and fibre-type loss-of-function mechanisms explain histopathology the energetic model does not, and the therapeutic corollary is untested: ClinicalTrials.gov (2026-10-16) shows **zero SRX-modulator trials** in either skeletal myosinopathy. The hypothesis is a plausible, well-motivated shared-mechanism module for dominant LMM variants that needs independent replication and direct structural confirmation before it can be considered established. It should remain EMERGING.

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED (appropriately EMERGING).**

The strongest pillar is **Carrington et al. 2023 ([PMID: 37788100](https://pubmed.ncbi.nlm.nih.gov/37788100/))**, which analysed common *MYH7* and *MYH2* LMM-region mutations **side by side** using purified LMM proteins, in silico modelling, patient muscle biopsies, mantATP-chase SRX measurements, and X-ray diffraction. It reported the two defining features of the seed claim — decreased SRX fraction and increased basal myosin ATP consumption in vivo, with contractility spared — for variants in **both** genes. The computational analysis in this investigation reinforces the plausibility: all nine curated *MYH7* LMM pathogenic residues are strictly conserved in *MYH2*, and the lesions are enriched for loss of conserved coiled-coil charges (binomial p = 1.0 × 10⁻⁴). The structural substrate for a shared mechanism is therefore real and testable.

Three considerations keep the verdict short of "supported." First, the functional-convergence claim depends on one laboratory's one study; there is no independent MYH2 SRX replication. Second, the hypothesis equates "lost SRX" with "impaired folded-back head sequestration (IHM)," and that equivalence is disputed on structural grounds (cardiac vs smooth-muscle IHMs "dramatically different," [PMID: 37131793](https://pubmed.ncbi.nlm.nih.gov/37131793/)), on X-ray grounds (IHM does not explain relaxed-muscle diffraction, [PMID: 31540109](https://pubmed.ncbi.nlm.nih.gov/31540109/)), and on assay grounds (mantATP displacement could not robustly quantify an SRX population in porcine cardiac HMM, [PMID: 38103642](https://pubmed.ncbi.nlm.nih.gov/38103642/)). Third, competing aggregation and fibre-type loss-of-function mechanisms explain much of the histopathology (hyaline bodies, nemaline rods, type 2A fibre loss, rimmed vacuoles) that the energetic/SRX model does not address, and the therapeutic corollary is untested.

---

## Key Findings

### Finding 1 — A single direct study underpins the shared SRX-loss / ATP-overconsumption mechanism

Carrington et al. 2023 ([PMID: 37788100](https://pubmed.ncbi.nlm.nih.gov/37788100/)) is the only study that places *MYH7* and *MYH2* LMM variants in the same experimental frame. Its own words establish the side-by-side design — *"we used multiple approaches to analyze the effects of common MYH7 and MYH2 mutations in the light meromyosin (LMM) region of myosin"* — and the core phenotype — *"basal myosin ATP consumption was increased and the myosin super-relaxed state was decreased in vivo."* The mechanistic interpretation is explicitly head sequestration: *"formation of shutdown heads is impaired, thus increasing myosin head ATP demand in the filaments, rather than affecting contractility."*

The convergent evidence streams were: (1) expressed/purified mutant LMM proteins showing disrupted coiled-coil structure; (2) in-vitro minifilament packing defects; (3) in silico modelling; (4) mantATP chase in patient biopsies showing a reduced SRX fraction; (5) X-ray diffraction showing reduced myosin head order; and (6) evidence of increased basal ATP consumption in vivo. Critically, **myofiber contractility was not affected**, which distinguishes this energetic/regulatory mechanism from a classical force-generation defect and actually argues against a contractile alternative for these rod variants.

The limitation is equally clear: the abstract yields **no per-variant effect sizes, no confidence intervals, and no independent replication.** The effect *direction* is consistent across both genes, but the magnitude and robustness of the cross-fibre-type claim cannot be assessed from the primary report alone, and no second group has reproduced the MYH2 SRX measurement.

### Finding 2 — The structural substrate is demonstrably shared (independent computational confirmation)

An original sequence analysis (UniProt P12883 for MYH7; Q9UKX2 for MYH2; retrieved 2026-10-16) tested whether MYH7 LMM pathogenic variants hit residues that are also present and conserved in MYH2 — a necessary condition for a shared rod mechanism.

**Charge-loss enrichment.** Of 9 literature-curated MYH7 LMM variants, 7 eliminate a positively charged R/K residue. Against a background R/K frequency of 0.177 in the MYH7 LMM region, this is a strong enrichment (one-sided binomial p = 1.0 × 10⁻⁴). The remaining lesions are Ala→Pro helix-breakers (A1603P, A1437P). Across the set: 4/9 proline substitutions, 2/9 single-residue deletions, 3/9 charge→aromatic (R→W). **Every variant falls into a canonical coiled-coil-destabilising lesion class.**

**Cross-gene conservation.** A Needleman–Wunsch alignment of the LMM regions gives 526/661 = 79.6% identity, and **all 9 MYH7-mutated residues are strictly identical in MYH2 at aligned positions** (e.g., R1500↔R1506, A1603↔A1609, R1845↔R1851). A heptad a/d hydrophobic-core enrichment test was null (p = 0.32), consistent with the myosin rod being governed by **surface charge periodicity** (the electrostatic "zones" of the coiled-coil zipper) rather than by the hydrophobic core — precisely where charge-removing mutations would be expected to bite.

This is the strongest *parsimony* argument for the hypothesis: if the same residues exist and are conserved in both proteins, and the pathogenic lesions destroy the same class of structural feature, a shared assembly/regulatory consequence is a reasonable default expectation. The caveat (Finding, PMID 19854198) is that conservation is necessary but not sufficient — identical sites can yield distinct outcomes.

### Finding 3 — Head sequestration (IHM) is structurally established for MYH7, but the IHM↔SRX bridge and cross-myosin universality are contested

Grinzato et al. 2023 ([PMID: 37131793](https://pubmed.ncbi.nlm.nih.gov/37131793/)) solved the human β-cardiac myosin (MYH7) folded-back **interacting-heads motif (IHM)** at 3.6 Å, confirming that MYH7 heads can sequester into an energy-saving off-state and that off-state interfaces are HCM mutation hot spots — *"The off-state is equated with a folded-back structure known as the interacting head motif (IHM), which is a regulatory feature of all muscle myosins."* This is molecular proof of principle for head sequestration in the slow/β-cardiac isoform.

But the **same study** qualifies universality: *"the structures of cardiac and smooth muscle myosin IHMs are dramatically different. This challenges the concept that the IHM structure is conserved in all muscle types."* That directly complicates the leap from "MYH7 has an IHM" to "all rod myosinopathies share one head-sequestration mechanism across fibre types."

Independently, the equivalence the seed hypothesis relies on — lost SRX = impaired shutdown-head formation — is disputed:

- Mohran et al. 2024 ([PMID: 38103642](https://pubmed.ncbi.nlm.nih.gov/38103642/)): *"the commonly employed mantATP displacement assay was unable to quantify the population of the SRX state with all data fitting very well by a single exponential"* — a measurement/reproducibility problem for the very readout used in Carrington et al.
- Knupp & Squire 2019 ([PMID: 31540109](https://pubmed.ncbi.nlm.nih.gov/31540109/)): the IHM does not explain relaxed-muscle X-ray diffraction patterns; there is more than one ordered head state in resting muscle.
- Morel 2025 review ([PMID: 40727670](https://pubmed.ncbi.nlm.nih.gov/40727670/)): IHM and SRX arise under very different conditions and are weakly or not coupled.

The mechanistic bridge is therefore **biologically plausible but not settled** — this is the single weakest node in the causal chain.

### Finding 4 — Database verification: both genes are bona fide Mendelian myopathy entities, but there are zero SRX-modulator trials

Database checks performed 2026-10-16:

- **GenCC** (submissions export, 30,345 rows): 32 MYH7/MYH2 entries. "MYH7-related skeletal myopathy" is curated **DEFINITIVE** (ClinGen, autosomal dominant) and Strong (Ambry, Labcorp). MYH7 myosin storage myopathy is Moderate–Strong (both AD and AR). MYH2 "myopathy, proximal, and ophthalmoplegia" is **DEFINITIVE** (ClinGen, autosomal recessive), Moderate (ClinGen AD), and Strong/Semidominant (Ambry, Labcorp, PanelApp). Both genes are therefore established skeletal-myopathy genes with distinct dominant and recessive allelic series.
- **ClinVar** (NCBI E-utilities): MYH7 = 6,011 variant records; MYH2 = 1,795.
- **ClinicalTrials.gov** (API v2): "MYH2 myopathy" = 0 studies; "mavacamten myopathy" = 0; "super-relaxed state myopathy" = 0; "MYH7 distal myopathy" = 1 — but the single hit (NCT04572893) is danicamtiv in dilated cardiomyopathy, **not** a skeletal myopathy. This is a **verified null** for SRX-modulator trials in either skeletal myosinopathy.

---

## Mechanistic Model / Interpretation

The hypothesis proposes the following causal chain. Strength of evidence is annotated at each link:

```
  LMM-region point mutation (MYH7 or MYH2)
        │   [STRONG — variants catalogued; charge/proline lesion classes; this report F2]
        ▼
  Loss of conserved coiled-coil surface charge / helix-breaking
        │   [STRONG in vitro — PMID 29660325, 19854198; this report F2]
        ▼
  Destabilised rod → aberrant thick-filament packing / assembly
        │   [STRONG in vitro — minifilament EM defects, PMID 29660325, 37788100]
        ▼
  Impaired folded-back "shutdown head" (IHM) formation
        │   [CONTESTED — IHM real for MYH7 (PMID 37131793) but IHM↔SRX
        │    equivalence disputed (PMID 38103642, 31540109, 40727670)]
        ▼
  Loss of super-relaxed (SRX) state → raised basal myosin ATP demand
        │   [SINGLE STUDY, both genes — PMID 37788100; assay reproducibility
        │    questioned PMID 38103642]
        ▼
  Energetic stress across fibre types (type 1 MYH7 / type 2A MYH2)
        │   [INFERRED — not independently replicated; contractility spared]
        ▼
  Clinical myopathy (distal/proximal weakness, ophthalmoplegia for MYH2)
            [Clinical entities ESTABLISHED, but causal link to SRX loss INFERRED]
```

The **upstream half** of this chain (mutation → coiled-coil destabilisation → filament packing defect) is well supported by multiple in-vitro studies and by the conservation/charge analysis in this report. The **downstream half** (packing defect → IHM loss → SRX loss → energetic stress → clinical phenotype) rests critically on a single study for the SRX/ATP readout, and the IHM→SRX intermediary node is the weakest link in the entire chain.

An important nuance the energetic model does **not** cover: the characteristic histopathology differs by gene. MYH7 rod/storage myopathies show **hyaline bodies** in type 1 fibres (PMID 15699387, 17336526, 25666907); MYH2 myopathy shows **type 2A fibre loss, rimmed vacuoles, and even nemaline rods/filamentous tangles** (PMID 33926564, 32578970, 29934118). A purely energetic SRX-loss mechanism predicts fibre-type energetic stress but not these distinct aggregation/structural pathologies, implying that **additional, gene- and fibre-type-specific mechanisms operate alongside any shared energetic module.**

---

## Evidence Matrix

| Citation | Evidence type | Role | Mechanistic claim tested | Key finding | Subtype/context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [37788100](https://pubmed.ncbi.nlm.nih.gov/37788100/) Carrington 2023 | In vitro + human biopsy | **SUPPORT (primary)** | MYH7 & MYH2 LMM variants both lose SRX, raise basal ATP, spare contractility | SRX ↓, basal ATP ↑ in vivo; shutdown-head formation impaired | Both genes, LMM region | Direct & side-by-side, but single study; no per-variant stats; no replication |
| This report (F2) | Computational | **SUPPORT (parsimony)** | Shared structural substrate | 9/9 MYH7 LMM sites conserved in MYH2; charge-loss enriched p=1e-4 | LMM coiled-coil | Sequence-level only; infers, not measures, shared function |
| [37131793](https://pubmed.ncbi.nlm.nih.gov/37131793/) Grinzato 2023 | Structural (cryo-EM) | **SUPPORT + QUALIFY** | MYH7 head sequestration (IHM) exists; universality | 3.6 Å MYH7 IHM; but cardiac vs smooth IHM "dramatically different" | β-cardiac/MYH7 | Confirms IHM for MYH7; undercuts cross-myosin universality |
| [38103642](https://pubmed.ncbi.nlm.nih.gov/38103642/) Mohran 2024 | In vitro | **QUALIFY / CHALLENGE** | SRX measurable by mantATP? | mantATP displacement couldn't quantify SRX (single-exponential fits) | Porcine cardiac HMM | Challenges the assay central to the hypothesis |
| [31540109](https://pubmed.ncbi.nlm.nih.gov/31540109/) Knupp & Squire 2019 | Computational/structural | **CHALLENGE** | IHM = relaxed-state structure? | IHM does not explain relaxed-muscle X-ray patterns; >1 ordered head state | Fish skeletal, insect | Questions IHM↔SRX equivalence |
| [40727670](https://pubmed.ncbi.nlm.nih.gov/40727670/) Morel 2025 | Review | **CHALLENGE (review-level)** | IHM–SRX coupling | IHM & SRX arise under very different conditions; weak/absent coupling | Thick filaments, general | Review; orientation, but directly on the disputed node |
| [29660325](https://pubmed.ncbi.nlm.nih.gov/29660325/) 2018 | In vitro + cell | **SUPPORT (upstream)** | LMM lesions destabilise coiled coil & filament assembly | A1603P, K1617del ↓ helicity, disrupt minifilaments, aberrant M-line packing | MYH7 Laing MPD-1 | Strong upstream support; no SRX/ATP readout |
| [19854198](https://pubmed.ncbi.nlm.nih.gov/19854198/) 2009 | In vitro | **QUALIFY** | Same residue, different disease | R1500P (skeletal) vs R1500W (DCM) have *distinct* molecular phenotypes | MYH7 rod | Warns that identical sites ≠ identical outcomes |
| [39216086](https://pubmed.ncbi.nlm.nih.gov/39216086/) 2024 | In vitro + mouse | **COMPETING / therapeutic** | Mavacamten rescues SRX energetics | Rescued ATP overconsumption in vitro; failed to fix energy proteome in vivo (4 wk) | NEB nemaline myopathy | Shows SRX-targeting works in vitro but short-term in-vivo efficacy doubtful |
| [33926564](https://pubmed.ncbi.nlm.nih.gov/33926564/) 2021 | Human clinical | **COMPETING (pathology)** | MYH2 pathology | Nemaline rods + filamentous tangles; myofibril disorganisation | MYH2 (incl. motor-domain variant) | Aggregation pathology not explained by SRX model |
| [36380287](https://pubmed.ncbi.nlm.nih.gov/36380287/) 2022 | Human clinical | **SUPPORT (context)** | Dominant MYH2 tail/assembly variant | Splice loss of aa1860-1891 (assembly region); type 2A loss | Dominant MYH2 | Links distal-tail/assembly region to dominant disease |
| [25666907](https://pubmed.ncbi.nlm.nih.gov/25666907/) 2015 | Human clinical | **COMPETING (pathology)** | MYH7 storage pathology | R1820W → myosin storage, hyaline bodies in type 1 fibres | Recessive MYH7 MSM | Aggregation pathology beyond energetic model |
| [17336526](https://pubmed.ncbi.nlm.nih.gov/17336526/) 2007 | Human clinical | **SUPPORT (context)** | Common MYH7 rod variant | R1845W recurrent; phenotypic variability; hyaline bodies in only half | MYH7 MSM/scapuloperoneal | Establishes a "common" LMM variant; variable expressivity |

---

## Data and Tool Use

| Source | Accession / URI | Access status | Query / filter | Relevance |
|---|---|---|---|---|
| PubMed | NCBI E-utilities | **Accessed** | MYH7/MYH2 LMM, SRX, IHM, head sequestration; 28 papers reviewed | Directly relevant |
| UniProt | P12883 (MYH7), Q9UKX2 (MYH2); retrieved 2026-10-16 | **Accessed** | LMM region sequences for alignment & charge analysis | Directly relevant |
| GenCC | submissions export, 30,345 rows; 2026-10-16 | **Accessed** | Filter to MYH7/MYH2 → 32 entries | Directly relevant; gene-validity confirmation |
| ClinVar | NCBI E-utilities; 2026-10-16 | **Accessed** | MYH7 (6,011 records), MYH2 (1,795) | Context; variant counts |
| ClinicalTrials.gov | API v2; 2026-10-16 | **Accessed — verified null** | "MYH2 myopathy"=0; "mavacamten myopathy"=0; "super-relaxed state myopathy"=0; "MYH7 distal myopathy"=1 (NCT04572893, DCM, off-target) | Verified absence of SRX-modulator trials |

**Analyses inventory:**

1. *Sequence conservation & charge analysis* (Finding 2) — Input: UniProt P12883, Q9UKX2. Method: Needleman–Wunsch alignment of LMM regions; one-sided binomial enrichment test for charge loss; heptad a/d core test. Output: 9/9 conserved sites; charge-loss p = 1.0e-4; core test null p = 0.32. **Outcome: succeeded.**
2. *Database verification* (Finding 4) — GenCC/ClinVar/ClinicalTrials.gov queries. **Outcome: succeeded, including a verified negative for SRX-modulator trials.**
3. *Wet-lab / patient-level SRX or ATP analysis* — **Not attempted; no accessible dataset.** All functional SRX evidence is from the literature (primarily PMID 37788100). No analysis was silently substituted for a failed one; the functional-convergence claim rests on literature, which is stated explicitly as a limitation.

Artifact bundle location (as specified): `kb/hypotheses/MYH7-Related_Skeletal_Myopathy/shared_myosin_rod_mechanism/openscientist_artifacts` — containing the sequence-analysis code/outputs, the LMM alignment, the database query logs, and the verified-null ClinicalTrials.gov search log per the per-iteration records.

---

## Limitations and Knowledge Gaps

1. **Single-study dependence for functional convergence.** The entire cross-fibre-type SRX/ATP claim comes from one report (PMID 37788100). *Checked:* PubMed, no independent MYH2 SRX replication found as of 2026-10-16. *Resolution:* an independent lab repeating mantATP-chase SRX and X-ray diffraction on MYH2 patient biopsies.

2. **Contested IHM→SRX bridge.** The hypothesis equates lost SRX with impaired head sequestration, but IHM–SRX coupling is disputed (PMID 38103642, 31540109, 40727670) and the SRX assay itself is questioned. This is the weakest causal node. *Resolution:* direct cryo-EM/X-ray demonstration that LMM-variant filaments have fewer folded-back heads, paired with an orthogonal SRX assay.

3. **Cross-myosin structural universality unproven.** Cardiac and smooth-muscle IHMs differ "dramatically" (PMID 37131793); no MYH2 IHM structure exists. *Resolution:* solve the MYH2 (type 2A) IHM and compare interfaces to MYH7.

4. **Pathology not explained by the energetic model.** Hyaline bodies (MYH7) vs type 2A loss / rimmed vacuoles / nemaline rods (MYH2) point to additional aggregation/loss-of-function mechanisms. *Resolution:* correlate SRX loss with aggregation burden within the same biopsies.

5. **Same residue ≠ same outcome.** R1500P vs R1500W give distinct molecular phenotypes (PMID 19854198), warning that conserved sites do not guarantee identical downstream effects. Conservation (Finding 2) is necessary but not sufficient.

6. **Therapeutic corollary untested; in-vivo efficacy doubtful.** Zero SRX-modulator trials exist for either skeletal myopathy (verified null, 2026-10-16), and mavacamten rescued SRX energetics *in vitro* but failed to correct the energy proteome *in vivo* over 4 weeks in a related nemaline model (PMID 39216086). *Resolution:* proof-of-concept ex-vivo SRX-stabiliser study on MYH2 and MYH7 LMM-variant fibres, then a biomarker-driven trial.

---

## Alternative / Competing Models

- **Aggregation / proteostasis toxicity (parallel mechanism).** Misassembled mutant myosin forms hyaline bodies (MYH7) or nemaline rods/tangles (MYH2); a gain-of-function toxicity independent of SRX energetics. Likely operates *alongside* the energetic module. (PMID 25666907, 33926564)
- **Fibre-type loss-of-function (alternative, especially recessive MYH2).** Recessive MYH2 causes near-complete loss of type 2A fibres — a developmental/structural deficiency, not an energetic one. A genuine alternative for the recessive allelic series. (PMID 32578970, 29934118)
- **Filament-assembly haploinsufficiency (upstream cause).** Distal-tail / assembly-competence-domain variants (e.g., MYH2 aa1860-1891 splice loss) impair incorporation into thick filaments — upstream of any SRX consequence. (PMID 36380287)
- **Classical contractile / force defect (refuted for LMM variants).** Carrington et al. explicitly found contractility spared, arguing *against* a force-generation mechanism for these rod variants — a point in favour of the regulatory/energetic model over this alternative.

---

## Discriminating Tests

1. **Independent MYH2 SRX replication.** Stratify: dominant MYH2 LMM-variant patients vs controls. Assay: mantATP-chase SRX + X-ray diffraction on biopsies, *plus* an orthogonal SRX readout to control for the assay critique (PMID 38103642). Expected if hypothesis true: reduced SRX fraction mirroring MYH7.
2. **Direct IHM quantification on variant filaments.** Cryo-EM of reconstituted MYH7 and MYH2 LMM-variant minifilaments; count folded-back heads. Expected: fewer IHM heads in variants of both genes.
3. **Solve the MYH2 (type 2A) IHM** and compare off-state interfaces to the MYH7 IHM (PMID 37131793) — tests structural universality directly.
4. **Within-biopsy correlation of SRX loss vs aggregation pathology.** Tests whether the energetic module is independent of, or coupled to, hyaline-body/nemaline-rod formation.
5. **Ex-vivo SRX-stabiliser (mavacamten/analogue) rescue** on MYH2 and MYH7 LMM-variant fibres, with energy-proteome readout, acknowledging the in-vivo efficacy caveat (PMID 39216086). Expected if hypothesis true: restored SRX and reduced ATP overconsumption in both.

---

## Curation Leads (require curator verification)

- **Keep status EMERGING.** Do not promote; functional convergence is single-study and the IHM→SRX node is contested.
- **Add qualifying evidence edges:**
  - PMID 37131793 — snippet: *"the structures of cardiac and smooth muscle myosin IHMs are dramatically different. This challenges the concept that the IHM structure is conserved in all muscle types."* Role: QUALIFY universality.
  - PMID 38103642 — snippet: *"the commonly employed mantATP displacement assay was unable to quantify the population of the SRX state with all data fitting very well by a single exponential."* Role: CHALLENGE assay/readout.
  - PMID 31540109 — snippet: *"the interacting head motif does not, in fact, explain what is observed."* Role: CHALLENGE IHM↔relaxed-state equivalence.
  - PMID 19854198 — snippet: *"each mutation displays distinct structural, thermodynamic, and functional properties."* Role: QUALIFY (same residue ≠ same outcome).
- **Candidate pathophysiology nodes/edges:** `LMM coiled-coil charge loss → filament-packing defect` (strong); `filament-packing defect → impaired IHM/shutdown-head` (contested — flag); `impaired SRX → raised basal ATP demand` (single-study); `SRX loss → clinical weakness` (inferred).
- **Candidate ontology terms:** type 1 slow-twitch skeletal muscle fibre; type 2A fast-twitch fibre; myosin super-relaxed state (GO: regulation of ATPase activity / striated muscle myosin thick filament assembly); interacting-heads motif.
- **Candidate subtype restriction:** limit the shared-mechanism claim to **dominant LMM/rod variants**; recessive MYH2 (type 2A fibre loss) likely follows a distinct loss-of-function mechanism.
- **Candidate knowledge_gaps entries:** (1) no independent MYH2 SRX replication as of 2026-10-16; (2) IHM↔SRX coupling unresolved; (3) verified null — zero SRX-modulator trials in either skeletal myosinopathy (ClinicalTrials.gov v2, 2026-10-16).

---

## Evidence Base Summary

The hypothesis is supported chiefly by one direct primary study (PMID 37788100) and by an independent conservation/charge analysis (this report). It is reinforced upstream by coiled-coil destabilisation studies (PMID 29660325) and by structural proof of a MYH7 IHM off-state (PMID 37131793). It is qualified or challenged by the contested IHM–SRX coupling (PMID 38103642, 31540109, 40727670), by the "same residue, different disease" caution (PMID 19854198), and by aggregation/fibre-type pathologies that an energetic model does not explain (PMID 25666907, 33926564, 32578970). The therapeutic corollary is unproven and partly undercut by a failed in-vivo mavacamten energy-proteome rescue (PMID 39216086) and a verified absence of relevant trials. Overall: a plausible, well-motivated shared-mechanism module for dominant LMM variants that remains appropriately EMERGING pending independent replication and direct structural confirmation.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist evidence matrix](openscientist_artifacts/kb_hypotheses_MYH7-Related_Skeletal_Myopathy_shared_myosin_rod_mechanism_openscientist_artifacts_data_evidence_matrix.csv)
- [OpenScientist gencc myh7 myh2](openscientist_artifacts/kb_hypotheses_MYH7-Related_Skeletal_Myopathy_shared_myosin_rod_mechanism_openscientist_artifacts_data_gencc_myh7_myh2.csv)
- [OpenScientist lmm variant heptad analysis](openscientist_artifacts/kb_hypotheses_MYH7-Related_Skeletal_Myopathy_shared_myosin_rod_mechanism_openscientist_artifacts_data_lmm_variant_heptad_analysis.csv)
- [OpenScientist README](openscientist_artifacts/kb_hypotheses_MYH7-Related_Skeletal_Myopathy_shared_myosin_rod_mechanism_openscientist_artifacts_figures_README.md)
- [OpenScientist database query log](openscientist_artifacts/kb_hypotheses_MYH7-Related_Skeletal_Myopathy_shared_myosin_rod_mechanism_openscientist_artifacts_logs_database_query_log.md)
- [OpenScientist execution log](openscientist_artifacts/kb_hypotheses_MYH7-Related_Skeletal_Myopathy_shared_myosin_rod_mechanism_openscientist_artifacts_logs_execution_log.md)
- [OpenScientist pubmed search log](openscientist_artifacts/kb_hypotheses_MYH7-Related_Skeletal_Myopathy_shared_myosin_rod_mechanism_openscientist_artifacts_logs_pubmed_search_log.md)

## Term Validation

No ontology term identifiers were found in this report.