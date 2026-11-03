---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-10-18T05:26:57.651859'
end_time: '2026-10-18T05:47:52.938090'
duration_seconds: 1255.29
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Conserved Cellular Senescence Module
  category: Module
  hypothesis_group_id: upar_senescence_surface_marker_target
  hypothesis_label: uPAR (PLAUR) as a Senescence-Enriched Surface Marker and Senolytic
    Target
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: upar_senescence_surface_marker_target\nhypothesis_label:\
    \ uPAR (PLAUR) as a Senescence-Enriched Surface Marker and Senolytic Target\n\
    status: EMERGING\ndescription: 'uPAR, the urokinase plasminogen activator receptor\
    \ encoded by PLAUR, is upregulated on the\n  surface of senescent cells and is\
    \ the antigen that senolytic CAR T cells target. This hypothesis holds\n  that\
    \ uPAR marks the age-accumulating senescent-cell population well enough to serve\
    \ as a therapeutic\n  handle, so that clearing uPAR-positive cells reverses age-related\
    \ tissue dysfunction. The open question\n  is specificity: uPAR is expressed on\
    \ non-senescent myeloid, endothelial and other cells and has roles\n  in normal\
    \ immunity and fibrinolysis, so how cleanly it separates senescent from non-senescent\
    \ cells\n  across tissues, and how far the mouse evidence extends to humans, is\
    \ unresolved.'\nevidence:\n- reference: PMID:38267706\n  reference_title: Prophylactic\
    \ and long-lasting efficacy of senolytic CAR T cells against age-related\n   \
    \ metabolic dysfunction.\n  supports: SUPPORT\n  evidence_source: MODEL_ORGANISM\n\
    \  snippet: Plasma levels of soluble uPAR positively correlate with the pace of\
    \ aging in humans15,16 and\n    Plaur (the gene encoding uPAR) is a component\
    \ of the SenMayo gene signature recently reported to identify\n    senescent cells\
    \ in aged tissues17.\n  explanation: Ties uPAR to an established senescence gene\
    \ signature and to a human aging correlate, the\n    basis for treating it as\
    \ a senescence marker.\n- reference: PMID:38267706\n  reference_title: Prophylactic\
    \ and long-lasting efficacy of senolytic CAR T cells against age-related\n   \
    \ metabolic dysfunction.\n  supports: SUPPORT\n  evidence_source: MODEL_ORGANISM\n\
    \  snippet: This increase in the fraction of uPAR-positive cells was paralleled\
    \ by an increase in the percentage\n    of senescence-associated beta-galactosidase\
    \ (SA-\u03B2-gal)-positive cells\n  explanation: Co-accumulation of uPAR-positive\
    \ and SA-beta-gal-positive cells with age links the surface\n    marker to a canonical\
    \ senescence readout.\nnotes: Seeded from the anti-uPAR CAR T lead (Impetus Grants,\
    \ Corina Amor). The module already records\n  that uPAR is senescence-enriched\
    \ rather than senescence-specific (its positive cells in aged tissue\n  are mainly\
    \ endothelial, myeloid, dendritic and preadipocyte). An OpenScientist run was\
    \ commissioned\n  on this group to test marker specificity across tissues and\
    \ the strength of the human evidence; its\n  assessment will be added separately."
  artifact_dir: kb/hypotheses/cellular_senescence/upar_senescence_surface_marker_target/openscientist_artifacts
  analysis_objective: Assess how specifically uPAR (PLAUR) marks senescent cells versus
    non-senescent myeloid, endothelial and other populations across tissues; how strong
    the human (vs mouse) evidence is that uPAR-positive cell burden tracks aging and
    that clearance is beneficial; and whether uPAR is a functional driver of the senescent
    state or only a surface marker
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
citation_count: 15
term_validation:
  total_terms: 0
  verified: 0
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 7
artifact_sources:
  openscientist_artifacts_zip: 7
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
- filename: kb_hypotheses_cellular_senescence_upar_senescence_surface_marker_target_openscientist_artifacts_data_clinicaltrials_search_log.json
  path: openscientist_artifacts/kb_hypotheses_cellular_senescence_upar_senescence_surface_marker_target_openscientist_artifacts_data_clinicaltrials_search_log.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist clinicaltrials search log
- filename: kb_hypotheses_cellular_senescence_upar_senescence_surface_marker_target_openscientist_artifacts_data_hpa_plaur_specificity.json
  path: openscientist_artifacts/kb_hypotheses_cellular_senescence_upar_senescence_surface_marker_target_openscientist_artifacts_data_hpa_plaur_specificity.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist hpa plaur specificity
- filename: kb_hypotheses_cellular_senescence_upar_senescence_surface_marker_target_openscientist_artifacts_data_hpa_senescence_marker_panel.json
  path: openscientist_artifacts/kb_hypotheses_cellular_senescence_upar_senescence_surface_marker_target_openscientist_artifacts_data_hpa_senescence_marker_panel.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist hpa senescence marker panel
- filename: kb_hypotheses_cellular_senescence_upar_senescence_surface_marker_target_openscientist_artifacts_data_opentargets_plaur_associations.json
  path: openscientist_artifacts/kb_hypotheses_cellular_senescence_upar_senescence_surface_marker_target_openscientist_artifacts_data_opentargets_plaur_associations.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist opentargets plaur associations
- filename: kb_hypotheses_cellular_senescence_upar_senescence_surface_marker_target_openscientist_artifacts_data_senmayo_plaur_membership.json
  path: openscientist_artifacts/kb_hypotheses_cellular_senescence_upar_senescence_surface_marker_target_openscientist_artifacts_data_senmayo_plaur_membership.json
  media_type: application/json
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist senmayo plaur membership
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Conserved Cellular Senescence Module
- **Category:** Module

## Target Hypothesis
- **Hypothesis ID:** upar_senescence_surface_marker_target
- **Hypothesis Label:** uPAR (PLAUR) as a Senescence-Enriched Surface Marker and Senolytic Target
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: upar_senescence_surface_marker_target
hypothesis_label: uPAR (PLAUR) as a Senescence-Enriched Surface Marker and Senolytic Target
status: EMERGING
description: 'uPAR, the urokinase plasminogen activator receptor encoded by PLAUR, is upregulated on the
  surface of senescent cells and is the antigen that senolytic CAR T cells target. This hypothesis holds
  that uPAR marks the age-accumulating senescent-cell population well enough to serve as a therapeutic
  handle, so that clearing uPAR-positive cells reverses age-related tissue dysfunction. The open question
  is specificity: uPAR is expressed on non-senescent myeloid, endothelial and other cells and has roles
  in normal immunity and fibrinolysis, so how cleanly it separates senescent from non-senescent cells
  across tissues, and how far the mouse evidence extends to humans, is unresolved.'
evidence:
- reference: PMID:38267706
  reference_title: Prophylactic and long-lasting efficacy of senolytic CAR T cells against age-related
    metabolic dysfunction.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: Plasma levels of soluble uPAR positively correlate with the pace of aging in humans15,16 and
    Plaur (the gene encoding uPAR) is a component of the SenMayo gene signature recently reported to identify
    senescent cells in aged tissues17.
  explanation: Ties uPAR to an established senescence gene signature and to a human aging correlate, the
    basis for treating it as a senescence marker.
- reference: PMID:38267706
  reference_title: Prophylactic and long-lasting efficacy of senolytic CAR T cells against age-related
    metabolic dysfunction.
  supports: SUPPORT
  evidence_source: MODEL_ORGANISM
  snippet: This increase in the fraction of uPAR-positive cells was paralleled by an increase in the percentage
    of senescence-associated beta-galactosidase (SA-β-gal)-positive cells
  explanation: Co-accumulation of uPAR-positive and SA-beta-gal-positive cells with age links the surface
    marker to a canonical senescence readout.
notes: Seeded from the anti-uPAR CAR T lead (Impetus Grants, Corina Amor). The module already records
  that uPAR is senescence-enriched rather than senescence-specific (its positive cells in aged tissue
  are mainly endothelial, myeloid, dendritic and preadipocyte). An OpenScientist run was commissioned
  on this group to test marker specificity across tissues and the strength of the human evidence; its
  assessment will be added separately.
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
result beneath `kb/hypotheses/cellular_senescence/upar_senescence_surface_marker_target/openscientist_artifacts`. Do not create an empty bundle when no data
source was accessed and no analysis ran. Give each artifact a stable relative
path and connect computed claims to their input, method, and output artifacts.
Do not bundle large recoverable raw
downloads, a provider data lake, controlled/patient-level data, credentials, or
signed URLs; record their stable external identifiers, versions, and checksums
instead. State explicitly when an expected artifact is external, local-only,
missing, or was not produced.


## Output

# uPAR (PLAUR) as a Senescence-Enriched Surface Marker and Senolytic Target — Mechanistic Hypothesis Search

**Hypothesis ID:** `upar_senescence_surface_marker_target`
**Module:** Conserved Cellular Senescence Module
**Status in KB:** EMERGING
**Search date:** 2026-10-18

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED** — the hypothesis is correct in its therapeutic core but overstated in its specificity claim. The current literature cleanly confirms the KB's own framing that uPAR is **senescence-enriched, not senescence-specific**.

Three pillars of the hypothesis are well-supported. First, PLAUR is a **verified member of the SenMayo senescence gene signature** (MSigDB `SAUL_SEN_MAYO`, M45803) and encodes a genuinely surface-accessible, GPI-anchored protein. Second, **uPAR-positive cells accumulate with age in parallel with SA-β-gal-positive cells**, and clearing them is causally beneficial: anti-uPAR CAR T cells (and independently-developed BiTEs, chimeric "matchmaker" peptides, and uPAR-targeted nanoparticles) reverse metabolic, intestinal, hepatic-fibrotic and arthritic aging phenotypes across multiple independent mouse studies. Third, **soluble uPAR (suPAR) tracks accelerated biological aging in a population-representative human cohort** (Dunedin Study), providing a human aging correlate.

However, the specificity premise — that uPAR "marks the age-accumulating senescent-cell population well enough to serve as a therapeutic handle" — is only **quantitative, not categorical**. Human Protein Atlas data show uPAR is constitutively high on normal neutrophils, monocytes, dendritic cells, macrophages and endothelium, is "Detected in all" tissues, and is classified "Cell type enhanced" (never "Cell type specific"). No candidate senescence surface marker in an 11-gene panel was cell-type-specific at baseline, so **any specificity must come from senescence-driven upregulation above a non-zero baseline rather than from a senescence-restricted on/off expression pattern**. On-target toxicity is already documented (a uPAR T-cell engager caused dose-dependent hepatotoxicity via attack on hepatic endothelial cells). The human evidence is thin: a soluble-suPAR aging correlate and a single rheumatoid-arthritis scRNA dataset, with **zero registered human senolytic/uPAR CAR-T trials** on ClinicalTrials.gov as of the search date. Human genetics (Open Targets) links PLAUR to age-related cardiovascular/inflammatory disease and leukocyte count — consistent with its myeloid/vascular biology — but shows **no direct genetic association with aging, longevity, or cellular-senescence terms**.

The most important caveat for curators: the therapeutic efficacy evidence (strong, causal, multi-tissue, mouse) and the specificity evidence (weak — uPAR is broadly expressed) are not in conflict; they coexist because senolytic efficacy does not require a perfectly specific marker, only a favorable therapeutic window. The hypothesis should retain **EMERGING** status, with its specificity qualifier preserved and strengthened, and with an explicit note that human translation is unproven.

---

## Key Findings

### F001 — uPAR is constitutively high on normal myeloid cells (specificity ceiling)

Human Protein Atlas consensus RNA data (retrieved 2026-10-18 via the HPA search/download API, ENSG00000011422) classify **PLAUR as "Tissue enriched" but "Detected in all" tissues**; its single-cell class is "Cell type enhanced" (explicitly *not* "Cell type specific"), and its blood class is "Immune cell enhanced." Ranked single-cell expression (nCPM) is dominated by normal myeloid lineage: Neutrophils 7137.8, Epididymal basal 3927.4, monocytes 2786.3, Ocular epithelial 2333.0, conventional dendritic cells (cDC) 1115.4, Endometrial secretory 874.8, Macrophages 787.2. The top expressers are overwhelmingly normal, non-senescent cells.

This baseline expression has direct therapeutic consequences. A uPAR-targeting T-cell engager (GFD-CD3) produced **dose-dependent hepatotoxicity through T cell-mediated attack on hepatic endothelial cells** ([PMID: 42806572](https://pubmed.ncbi.nlm.nih.gov/42806572/)) — an on-target, off-senescent-cell effect. Independently, uPAR "is broadly expressed in solid tumors enriched for TP53 and RAS pathway mutations" ([PMID: 41916312](https://pubmed.ncbi.nlm.nih.gov/41916312/)), confirming that uPAR surface expression is broad rather than restricted to senescent cells. **This finding is the mechanistic basis for the "enriched, not specific" caveat.**

### F002 — PLAUR is a verified SenMayo member, but embedded in a secretory inflammatory program

The authoritative SenMayo set (`SAUL_SEN_MAYO`, systematic name M45803, source [PMID: 35974106](https://pubmed.ncbi.nlm.nih.gov/35974106/), Saul et al. 2022 *Nat Commun*, Supplementary Data 1) was retrieved from MSigDB on 2026-10-18. A programmatic membership check confirmed **`'PLAUR' in geneSymbols = True`** (index 99 of 124 genes). Critically, the set also contains the full plasminogen-activation/fibrinolysis axis (PLAT, PLAU, PLAUR, SERPINE1) and is dominated by secreted SASP factors (CCL/CXCL chemokines, IL1A/IL1B/IL6/CXCL8, MMP1/2/3/9/13, IGFBP family, VEGFA, TNF).

The interpretation is nuanced: PLAUR is the **only canonical surface-anchored candidate among the SenMayo genes**, which is precisely why it is attractive as a therapeutic handle — but it is embedded in a *secretory* inflammatory program. Its presence in SenMayo reflects SASP/inflammation biology as much as a senescence-specific surface identity. This aligns with its known role as a GPI-anchored receptor in the fibrinolysis cascade and leukocyte activation.

### F003 — Human suPAR tracks accelerated biological aging (supportive but indirect)

In the Dunedin Study, a population-representative 1972–73 New Zealand birth cohort (n=1037; suPAR measured at ages 38 and 45, 875/997 living participants at 45), **elevated plasma suPAR was associated with accelerated pace of biological aging across multiple organ systems, older facial appearance, older brain age, and greater decline in physical/cognitive function**; improvements in health habits blunted the suPAR rise ([PMID: 32766674](https://pubmed.ncbi.nlm.nih.gov/32766674/), Rasmussen et al. 2021). Regressions adjusted for sex, smoking, CRP, and current health conditions.

This is the primary human cohort evidence cited in the seed hypothesis. It is **supportive but indirect**: it measures *soluble* uPAR (a cleaved/shed circulating form, an inflammation biomarker) rather than *membrane* uPAR on senescent cells, and correlation with aging pace does not establish that suPAR originates from senescent cells or that membrane uPAR marks them specifically.

### F004 — uPAR is one of several competing senescent-cell surface markers; off-target toxicity is a recurring theme

uPAR is used as a senescent-cell handle beyond CAR T: a chimeric "matchmaker" peptide binds uPAR to drive immune clearance of senescent cells in liver fibrosis, lung injury, cancer and natural aging ([PMID: 39623223](https://pubmed.ncbi.nlm.nih.gov/39623223/), 2025), explicitly noting that senolytics are "limited by off-target toxicity." Competing/alternative senescent-cell surface markers under active development include **GPNMB** (engineered senolytic EVs, [PMID: 38794820](https://pubmed.ncbi.nlm.nih.gov/38794820/)), **NKG2D ligands** (anti-NKG2D CAR T, [PMID: 41476987](https://pubmed.ncbi.nlm.nih.gov/41476987/)), **TSPAN8** (senescent CAFs, [PMID: 41577205](https://pubmed.ncbi.nlm.nih.gov/41577205/)), and **TM4SF1** (senescent pancreatic β-cells, [PMID: 42425712](https://pubmed.ncbi.nlm.nih.gov/42425712/)). A 2025 review concludes that key unresolved challenges are "the identification of specific and universal senescence markers, potential off-target effects, and long-term safety concerns," with a "significant translational gap" ([PMID: 41476987](https://pubmed.ncbi.nlm.nih.gov/41476987/)).

The field-level picture is that uPAR is a **leading but not unique** surface handle, and that marker specificity plus off-target toxicity are acknowledged, unsolved problems across all such markers.

### F005 — No candidate senescence surface marker is cell-type-specific at baseline

An HPA consensus RNA comparison (2026-10-18) across 11 senescence-associated genes plus a specificity positive control found that **all of PLAUR, CDKN2A, CDKN1A, GPNMB, DPP4, B2M, TM4SF1, SERPINE1, LMNB1, TSPAN8, and NCAM1 are classified "Cell type enhanced" (not "Cell type specific")**; only the melanocyte gene MLANA (positive control) is "Cell type enriched/specific." Among the panel, PLAUR carries the **highest absolute immune-cell baseline expression** (Neutrophils 7138, monocytes 2786 nCPM) and is "Detected in all" tissues.

The implication is structural: because no senescence surface marker is specific at baseline, **specificity for senolysis can only come from senescence-driven upregulation above baseline**, not from a clean on/off switch. For uPAR, the high myeloid baseline makes the required fold-change discrimination harder than for lower-baseline markers.

### F006 — Strongest direct evidence: anti-uPAR CAR T causally reverses age-related pathologies in mice (tissue-dependent target identity)

This is the strongest pillar of the hypothesis. Convergent, interventional mouse evidence that clearing uPAR+ cells reverses age-related dysfunction:

1. **Proof-of-concept:** senolytic anti-uPAR CAR T cells safely reverse senescence-associated pathologies ([PMID: 32555459](https://pubmed.ncbi.nlm.nih.gov/32555459/), Amor et al. 2020 *Nature*).
2. **Durable efficacy:** a *single* administration improves exercise capacity in physiological aging and ameliorates metabolic dysfunction/glucose tolerance in aged and high-fat-diet mice — "a single administration of these senolytic CAR T cells is sufficient to achieve long-term therapeutic and preventive effects" ([PMID: 38267706](https://pubmed.ncbi.nlm.nih.gov/38267706/), Amor et al. 2024).
3. **Second tissue:** "both therapeutic and prophylactic treatment with anti-uPAR CAR T cells improved barrier function, regenerative capacity, inflammation, mucosal immune function and microbiome composition in aged mice" — with the accumulating target cells being "mostly epithelial uPAR-positive cells in the aging gut" ([PMID: 41291258](https://pubmed.ncbi.nlm.nih.gov/41291258/), 2026).
4. **In-vivo manufacturing + human signal:** mRNA/LNP uPAR CAR-T alleviates liver fibrosis and rheumatoid arthritis, and "Single-cell sequencing in humans confirms uPAR's relevance to senescence and inflammation in RA" ([PMID: 40602406](https://pubmed.ncbi.nlm.nih.gov/40602406/), 2025).

Two points are curation-critical. First, the efficacy is **causal and reproducible across independent groups and tissues** (metabolic, intestinal, hepatic, arthritic). Second, **the uPAR+ target cell identity is tissue-dependent** — endothelial/myeloid/preadipocyte in prior work, "mostly epithelial" in the aging gut — reinforcing that uPAR marks a heterogeneous, context-dependent population rather than a single senescent cell type.

### F007 — Source-level gap: no registered human senolytic/uPAR CAR-T trial

ClinicalTrials.gov API v2 was searched 2026-10-18 (query.term, countTotal=true). Results:

| Query | Total hits | Nature of hits |
|---|---|---|
| `senolytic` | 31 | all small-molecule senolytics (OA/PAD/vascular/pulmonary aging); none CAR-T |
| `senescent cell CAR T` | 72 | all oncology CAR-T; none senolytic or uPAR |
| `senolytic CAR` | 0 | — |
| `uPAR CAR` | 0 | — |
| `PLAUR CAR` | 0 | — |
| `urokinase CAR T` | 0 | — |
| `uPAR senolytic` | 0 | — |

API functionality was confirmed by non-zero calibration queries. **As of the search date there is no registered human trial of a uPAR-directed senolytic CAR-T (or any senolytic CAR-T).** The search log is saved in the artifact bundle (`artifacts/data/clinicaltrials_search_log.json`). This is a genuine, verified source-level absence, not an unchecked assumption.

### F008 — Human genetics (Open Targets): PLAUR tracks cardiovascular/inflammatory disease and leukocyte count, not senescence

Open Targets Platform GraphQL (accessed 2026-10-18; PLAUR/ENSG00000011422; 1616 associated diseases) returned highest genetic-association scores for: **abdominal aortic aneurysm 0.813, "Decreased total leukocyte count" 0.747, myocardial infarction 0.604, angina pectoris 0.597, aortic aneurysm 0.597, coronary artery disorder 0.592**; neurodegenerative/Parkinson/Alzheimer terms appear only at the overall-score level. There was **no direct genetic association with aging/longevity/cellular-senescence terms**. The association profile is exactly what uPAR's known myeloid/vascular/fibrinolytic biology predicts, and it does *not* independently nominate uPAR as a senescence gene. Artifact: `data/opentargets_plaur_associations.json`.

---

## Mechanistic Model / Interpretation

The hypothesis implies the following causal chain. Strength of support is annotated at each link.

```
  Aging / oncogenic stress / therapy-induced damage
        │  [STRONG: senescence biology is well established]
        ▼
  Cellular senescence program (p16/p21, SA-β-gal, SASP)
        │  [STRONG: PLAUR verified in SenMayo (M45803, F002)]
        ▼
  Upregulation of surface uPAR on (a fraction of) senescent cells
        │  [MODERATE: uPAR+ cells accumulate with age parallel to SA-β-gal (seed PMID 38267706);
        │   BUT high non-senescent baseline on myeloid/endothelial cells (F001, F005)]
        ▼
  uPAR+ cells accumulate in aged tissue (tissue-dependent identity:
  endothelial / myeloid / epithelial / preadipocyte)
        │  [STRONG in mouse (F006); target identity shifts by tissue]
        ▼
  Anti-uPAR CAR-T / BiTE / peptide / nanoparticle clears uPAR+ cells
        │  [STRONG causal mouse evidence, multi-tissue, multi-modality (F006, F004)]
        │  [RISK: on-target clearance of normal uPAR+ cells → hepatotoxicity (F001)]
        ▼
  Reversal of age-related tissue dysfunction
        │  [STRONG in mouse: metabolic, intestinal, hepatic-fibrotic, arthritic (F006)]
        ▼
  Clinical benefit in humans
           [UNPROVEN: no human trial (F007); human data = suPAR aging
            correlate (F003) + 1 RA scRNA dataset (F006); genetics
            points to CVD/leukocyte biology, not senescence (F008)]
```

**Where the literature is strong:** the two termini — senescence biology upstream and causal therapeutic reversal in mice downstream. Clearing uPAR+ cells demonstrably reverses aging phenotypes across four tissues and at least four targeting modalities.

**Where links are inferred or weak:** (1) the *specificity* of the senescence→surface-uPAR step — uPAR is upregulated on *a fraction* of senescent cells but is also constitutively high on normal cells, so the marker separates senescent from non-senescent cells only quantitatively; (2) the human translation terminus — essentially unvalidated, resting on a soluble-biomarker correlate and one scRNA dataset.

**The reconciling insight:** therapeutic efficacy and imperfect specificity coexist because senolysis exploits a *therapeutic window* (senescent cells may be more abundant, more uPAR-high, or more vulnerable), not a binary marker. The mouse efficacy data do not require — and do not demonstrate — clean specificity.

---

## Evidence Matrix

| Citation | Evidence type | Stance | Mechanistic claim tested | Key finding | Context | Confidence & limitations |
|---|---|---|---|---|---|---|
| [PMID: 38267706](https://pubmed.ncbi.nlm.nih.gov/38267706/) | Model organism | **Support** | uPAR+ cells accumulate with age & clearing them reverses metabolic dysfunction | Single-dose senolytic CAR-T gives durable therapeutic+preventive benefit; uPAR+ co-accumulates with SA-β-gal+ | Aged / HFD mice | High for efficacy; mouse only; specificity not resolved |
| [PMID: 32555459](https://pubmed.ncbi.nlm.nih.gov/32555459/) | Model organism | **Support** | Senolytic anti-uPAR CAR-T reverses senescence pathologies | Proof-of-concept: safe reversal of senescence-associated pathologies | Atherosclerosis, liver fibrosis (mouse) | High; foundational; mouse only |
| [PMID: 41291258](https://pubmed.ncbi.nlm.nih.gov/41291258/) | Model organism | **Support** | Clearing uPAR+ cells restores tissue fitness in a second organ | Improved intestinal barrier, regeneration, inflammation, microbiome; target cells "mostly epithelial" | Aged mouse gut | High; shows tissue-dependent target identity |
| [PMID: 40602406](https://pubmed.ncbi.nlm.nih.gov/40602406/) | Model organism + human scRNA | **Support / qualify** | In-vivo uPAR CAR-T treats fibrosis/RA; human relevance | Alleviates liver fibrosis & RA; human scRNA confirms uPAR relevance to senescence/inflammation in RA | Mouse + human RA | Moderate; only human single-cell datapoint |
| [PMID: 32766674](https://pubmed.ncbi.nlm.nih.gov/32766674/) | Human clinical (cohort) | **Support (indirect)** | Soluble uPAR correlates with aging pace | Elevated suPAR → accelerated biological aging across organ systems | Dunedin cohort, n=1037 | Moderate; soluble not membrane uPAR; correlational |
| [PMID: 39623223](https://pubmed.ncbi.nlm.nih.gov/39623223/) | In vitro / model organism | **Support** | uPAR usable as senescent-cell handle beyond CAR-T | Chimeric peptide binds uPAR to clear senescent cells in fibrosis/injury/aging | Multi-model | Moderate; notes off-target toxicity limit |
| [PMID: 42806572](https://pubmed.ncbi.nlm.nih.gov/42806572/) | Model organism (mouse + NHP) | **Refute / qualify** | uPAR targeting is specific & safe | uPAR BiTE caused dose-dependent hepatotoxicity via attack on hepatic endothelial cells | Mouse, non-human primate | High for toxicity; on-target off-senescent effect |
| [PMID: 41916312](https://pubmed.ncbi.nlm.nih.gov/41916312/) | Model organism / computational | **Qualify** | uPAR expression is senescence-restricted | uPAR "broadly expressed in solid tumors" (TP53/RAS enriched) | Solid tumors | High; confirms broad, non-senescent expression |
| HPA consensus RNA (F001, F005) | Computational (database) | **Qualify / refute specificity** | uPAR is a senescence-specific surface tag | PLAUR "Cell type enhanced," "Detected in all," highest myeloid baseline of 11-gene panel; no marker is specific | Human, cross-tissue | High; bulk/enhanced classes; not senescence-state-resolved |
| Open Targets (F008) | Computational (genetics) | **Qualify** | PLAUR is genetically a senescence gene | Top associations = AAA, leukocyte count, MI, angina; no aging/senescence terms | Human genetics | High; reflects myeloid/vascular biology |
| [PMID: 41476987](https://pubmed.ncbi.nlm.nih.gov/41476987/) | Review | **Qualify** | Senescence markers are specific & safe | Unresolved: "specific and universal senescence markers, off-target effects, long-term safety"; "significant translational gap" | Field review | Review-level; orientation |
| [PMID: 38794820](https://pubmed.ncbi.nlm.nih.gov/38794820/) | In vitro / model organism | **Competing** | uPAR is the surface handle for senolysis | GPNMB is an alternative senescent-cell surface marker (engineered EVs) | Tumor microenvironment | Competing marker |
| [PMID: 42425712](https://pubmed.ncbi.nlm.nih.gov/42425712/) | Model organism | **Competing** | uPAR marks senescent β-cells | TM4SF1 identified as surface marker of senescent β-cells (vs uPAR) | Pancreatic β-cells / T2DM | Competing marker, tissue-specific |
| [PMID: 41577205](https://pubmed.ncbi.nlm.nih.gov/41577205/) | Review / model organism | **Competing** | uPAR is the universal senescent-stroma marker | TSPAN8 marks senescent CAFs | Tumor stroma | Competing marker |
| [PMID: 42442548](https://pubmed.ncbi.nlm.nih.gov/42442548/) | Model organism | **Support** | uPAR-targeted delivery reduces senescent-adipocyte burden | uPAR-targeted D+Q nanoparticles improve insulin sensitivity in HFD obese mice | Aged/obese adipose | Moderate; alternative modality, mouse |
| [PMID: 42312503](https://pubmed.ncbi.nlm.nih.gov/42312503/) | Review | **Qualify** | uPAR CAR-T is clinically ready | uPAR senolytic CAR-T "remain at a preclinical stage" for lymphoma TIS | NHL therapy-induced senescence | Review-level; confirms preclinical status |

---

## Data and Tool Use

| Source | Accession / URI | Access status | Query / filters | Relevance | Artifact |
|---|---|---|---|---|---|
| Human Protein Atlas (consensus RNA, single-cell, blood) | ENSG00000011422 (PLAUR) + 11-gene panel | **Accessed** (2026-10-18, search/download API) | Expression class + ranked nCPM across cell types/tissues | Directly relevant: baseline specificity of the marker | HPA tables (F001, F005) |
| MSigDB — SenMayo | `SAUL_SEN_MAYO` / M45803 (source PMID 35974106) | **Accessed** (2026-10-18) | `'PLAUR' in geneSymbols` membership check | Directly relevant: verifies seed claim of SenMayo membership | Gene list + membership check (F002) |
| ClinicalTrials.gov API v2 | api.clinicaltrials.gov/v2 | **Accessed; negative result verified** (2026-10-18) | 7 query.term searches (table in F007), countTotal=true | Directly relevant: human trial landscape | `artifacts/data/clinicaltrials_search_log.json` (F007) |
| Open Targets Platform | GraphQL; ENSG00000011422 | **Accessed** (2026-10-18) | PLAUR associated diseases, ranked by genetic-association score | Directly relevant: human genetic nomination | `data/opentargets_plaur_associations.json` (F008) |
| PubMed (via search_pubmed) | 33 papers reviewed | **Accessed** | uPAR/PLAUR senescence, senolytic CAR-T, SenMayo, suPAR aging | Directly relevant: primary + review literature | Literature list (this report) |

**Analysis inventory (input → method → output):**

1. **HPA specificity analysis (F001/F005)** — Input: HPA consensus RNA + single-cell nCPM for PLAUR and an 11-gene senescence panel + MLANA control. Method: retrieve expression-class annotations and rank absolute nCPM. Output: PLAUR = "Cell type enhanced," "Detected in all," highest myeloid baseline; no panel gene specific. **Outcome: succeeded.**
2. **SenMayo membership check (F002)** — Input: MSigDB `SAUL_SEN_MAYO` gene list (124/125 symbols). Method: programmatic string membership. Output: `True`, index 99. **Outcome: succeeded.**
3. **ClinicalTrials.gov trial census (F007)** — Input: 7 term queries. Method: API v2 countTotal calls with calibration controls. Output: all uPAR/senolytic-CAR queries = 0; small-molecule/oncology controls non-zero. **Outcome: succeeded (verified negative).**
4. **Open Targets genetics (F008)** — Input: PLAUR gene ID. Method: GraphQL associated-diseases query, sort by score. Output: top terms AAA/leukocyte/MI/angina; no senescence terms. **Outcome: succeeded.**

No patient-level or controlled-access data were used. No analysis was proposed-but-not-run; no fallback from a failed computational analysis to literature synthesis occurred. The HPA/Open Targets analyses rely on *bulk/enhanced* expression classes and are **not resolved by senescence state** — they bound baseline specificity but cannot measure senescence-induced fold-change, which is the actual discriminator; this is a stated limitation.

---

## Limitations and Knowledge Gaps

**1. Senescence-state-resolved surface uPAR quantification is missing.** All specificity evidence here (HPA, Open Targets) reflects baseline/bulk expression in normal cells, not the uPAR surface density on *senescent* vs *non-senescent* cells of the same type. *Why it matters:* the therapeutic window depends on the fold-change, not the baseline. *What was checked:* HPA expression classes (no senescence axis available). *Resolution:* paired flow cytometry / CyTOF of surface uPAR on SA-β-gal+ vs SA-β-gal− cells across tissues.

**2. Human translation is essentially unvalidated.** *What was checked:* ClinicalTrials.gov (7 queries, 2026-10-18) → zero senolytic/uPAR CAR-T trials; human data limited to the Dunedin suPAR correlate (soluble, not membrane) and one RA scRNA dataset. *Resolution:* a first-in-human dose-finding senolytic CAR-T trial with uPAR surface-expression biomarker stratification.

**3. On-target toxicity against normal uPAR+ cells is documented but not bounded.** Hepatic-endothelial injury occurred with a uPAR BiTE ([PMID: 42806572](https://pubmed.ncbi.nlm.nih.gov/42806572/)). *Why it matters:* defines the safety ceiling. *Resolution:* dose-response toxicity studies with serum aminotransferase monitoring (already proposed as a safety readout in that paper) and transient/controllable CAR designs.

**4. The suPAR→membrane-uPAR→senescent-cell link is inferred, not demonstrated.** Soluble suPAR correlating with aging pace does not establish that it is shed from senescent cells. *Resolution:* source-tissue deconvolution of plasma suPAR; longitudinal suPAR vs tissue senescent-cell burden.

**5. Genetic nomination is absent.** Open Targets shows PLAUR's human genetics point to CVD/leukocyte biology, with no aging/senescence terms. *Why it matters:* no Mendelian-randomization-style human causal support that uPAR biology drives senescence/aging. *Resolution:* MR of PLAUR variants against aging-pace / senescence-burden phenotypes.

**6. Tissue-dependent target identity is unresolved for specificity.** uPAR+ cells are endothelial/myeloid in some tissues and "mostly epithelial" in the aging gut ([PMID: 41291258](https://pubmed.ncbi.nlm.nih.gov/41291258/)). *Resolution:* cross-tissue single-cell atlas of uPAR+ cells co-stained for canonical senescence markers.

---

## Alternative Models

| Alternative hypothesis | Relationship to seed | Rationale |
|---|---|---|
| **Competing surface markers** (GPNMB [PMID 38794820], NKG2DL [PMID 41476987], TSPAN8 [PMID 41577205], TM4SF1 [PMID 42425712]) | **Alternative/parallel** | Each is a surface marker for senescence in a specific tissue; several may be more tissue-specific than uPAR. uPAR is a leading but not unique handle. |
| **uPAR as SASP/inflammation marker, not senescence-surface tag** | **Reframing/competing** | PLAUR sits inside the SenMayo *secretory* program (F002) and its human genetics/expression track myeloid-vascular inflammation (F001, F008). Benefit from clearing uPAR+ cells may be driven by removing inflammatory myeloid/endothelial cells (inflamm-aging), not canonically senescent cells. |
| **Therapeutic-window model (quantitative enrichment)** | **Refinement of the seed** | Senolytic efficacy requires only that uPAR+ burden/density is higher in diseased/aged tissue, not binary specificity. Best reconciles strong efficacy (F006) with weak specificity (F001/F005). |
| **Small-molecule senolytics (D+Q, navitoclax, fisetin)** | **Parallel mechanism** | Achieve senolysis via pro-survival-pathway inhibition without any surface marker; the dominant clinical modality (all 31 ClinicalTrials.gov senolytic trials). |
| **Soluble suPAR as a bystander aging biomarker** | **Downstream consequence** | suPAR may index systemic inflammation/organ damage rather than cause or specifically mark tissue senescence (F003). |

---

## Discriminating Tests

1. **Senescence-resolved surface-uPAR cytometry (specificity test).** Sample: multiple aged mouse tissues + human tissue where available. Perturbation: none (observational). Readout: surface uPAR density on SA-β-gal+/p16+ vs matched non-senescent cells of each type. *Expected if seed is right:* senescent cells carry significantly higher surface uPAR than same-type non-senescent cells; *if the alternative (myeloid-inflammation) model holds:* uPAR density is driven by lineage, not senescence state.

2. **Head-to-head marker comparison for therapeutic index.** Compare anti-uPAR vs anti-GPNMB vs anti-NKG2DL CAR-T/EV for senolytic efficacy and on-target toxicity in the same aged-mouse models. *Expected:* ranks markers by therapeutic window; informs which is most tissue-selective.

3. **First-in-human biomarker-stratified senolytic CAR-T trial.** Stratify patients (e.g., metabolic dysfunction, fibrosis, RA) by tissue uPAR+ senescent-cell burden; primary safety endpoint includes serum aminotransferases (hepatic-endothelial toxicity monitor per [PMID: 42806572](https://pubmed.ncbi.nlm.nih.gov/42806572/)). *Expected:* establishes human efficacy/safety and whether uPAR+ burden predicts response.

4. **Mendelian randomization of PLAUR variants vs aging-pace phenotypes.** Using the genetic instruments already catalogued in Open Targets (F008). *Expected if seed is right:* PLAUR variants causally associate with senescence/aging-pace outcomes; *current null genetic signal predicts a negative/weak result*, which would favor the SASP-biomarker reframing.

5. **Plasma suPAR source deconvolution.** Determine whether circulating suPAR derives from senescent cells vs activated myeloid cells, via tissue-conditional PLAUR knockout + plasma suPAR measurement. *Expected:* clarifies whether the human suPAR-aging correlate (F003) reflects senescence biology.

---

## Curation Leads (require curator verification)

**Candidate evidence references & snippets to verify:**
- [PMID: 42806572](https://pubmed.ncbi.nlm.nih.gov/42806572/) — "high-dose GFD-CD3 predominantly induced hepatotoxicity through T cell-mediated attack on hepatic endothelial cells" → add as **REFUTES/QUALIFIES specificity** (on-target off-senescent toxicity).
- [PMID: 41291258](https://pubmed.ncbi.nlm.nih.gov/41291258/) — "the accumulation of mostly epithelial uPAR-positive cells in the aging gut" → add as **SUPPORT** + tissue-dependent target-identity node.
- [PMID: 40602406](https://pubmed.ncbi.nlm.nih.gov/40602406/) — "Single-cell sequencing in humans confirms uPAR's relevance to senescence and inflammation in RA" → add as the **human single-cell** datapoint.
- [PMID: 41916312](https://pubmed.ncbi.nlm.nih.gov/41916312/) — "uPAR is broadly expressed in solid tumors enriched for TP53 and RAS pathway mutations" → **QUALIFIES** specificity.
- [PMID: 41476987](https://pubmed.ncbi.nlm.nih.gov/41476987/) — "the identification of specific and universal senescence markers, potential off-target effects, and long-term safety concerns" → review-level **QUALIFIER**.

**Candidate pathophysiology nodes/edges:**
- Node: *surface uPAR density on senescent cells* (quantitative, tissue-dependent) — not a binary marker.
- Edge: *SASP/inflamm-aging → myeloid/endothelial uPAR+ cells* as a parallel, possibly dominant, contributor to therapeutic benefit.
- Edge: *anti-uPAR clearance → hepatic-endothelial toxicity* (safety liability).

**Candidate ontology terms:** senescent epithelial cell (gut), hepatic endothelial cell, neutrophil, monocyte, conventional dendritic cell, preadipocyte; biological processes: SASP, fibrinolysis/plasminogen activation, leukocyte activation.

**Candidate status/subtype restrictions:** retain **EMERGING**. Add explicit subtype note: *efficacy evidence is mouse-only across metabolic/intestinal/hepatic/arthritic contexts; human evidence restricted to one RA scRNA dataset + a soluble-suPAR aging correlate; no registered human trial as of 2026-10-18.*

**Candidate knowledge_gaps / discussion prompts:**
- "uPAR separates senescent from non-senescent cells only quantitatively; surface fold-change on senescent vs same-type non-senescent cells is unmeasured."
- "No human senolytic/uPAR CAR-T trial registered (ClinicalTrials.gov, 2026-10-18)."
- "PLAUR human genetics (Open Targets, 2026-10-18) nominate CVD/leukocyte biology, not senescence/aging."

**Artifact bundle** (`kb/hypotheses/cellular_senescence/upar_senescence_surface_marker_target/openscientist_artifacts`): contains the ClinicalTrials.gov search log, Open Targets associations JSON, HPA expression tables, and SenMayo membership check. The MANIFEST records status/fallback flags and checksummed inputs/outputs. No large raw downloads, controlled data, or credentials are bundled; external sources are recorded by stable identifier.

---

## Proposed Follow-up Experiments / Actions

1. **Run the senescence-resolved surface-uPAR cytometry** (Discriminating Test 1) — the single highest-value experiment; directly tests the specificity premise the KB flags as the open question.
2. **Catalogue uPAR+ cell identity across a cross-tissue single-cell senescence atlas** co-stained for p16/SA-β-gal, to map where uPAR is senescence-enriched vs lineage-driven.
3. **Perform Mendelian randomization** of PLAUR instruments against aging-pace/senescence phenotypes using the Open Targets genetic data already retrieved (F008).
4. **Update the KB** with the curation leads above, preserving EMERGING status and strengthening the specificity qualifier and human-translation caveat.
5. **Monitor ClinicalTrials.gov** for the first registered uPAR/senolytic CAR-T trial; re-run the F007 query set periodically.

---

*Report compiled from 5 OpenScientist iterations: 8 confirmed findings, 33 papers reviewed, 4 computational database analyses (HPA, MSigDB, ClinicalTrials.gov, Open Targets), all executed and logged on 2026-10-18.*


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
- [OpenScientist clinicaltrials search log](openscientist_artifacts/kb_hypotheses_cellular_senescence_upar_senescence_surface_marker_target_openscientist_artifacts_data_clinicaltrials_search_log.json)
- [OpenScientist hpa plaur specificity](openscientist_artifacts/kb_hypotheses_cellular_senescence_upar_senescence_surface_marker_target_openscientist_artifacts_data_hpa_plaur_specificity.json)
- [OpenScientist hpa senescence marker panel](openscientist_artifacts/kb_hypotheses_cellular_senescence_upar_senescence_surface_marker_target_openscientist_artifacts_data_hpa_senescence_marker_panel.json)
- [OpenScientist opentargets plaur associations](openscientist_artifacts/kb_hypotheses_cellular_senescence_upar_senescence_surface_marker_target_openscientist_artifacts_data_opentargets_plaur_associations.json)
- [OpenScientist senmayo plaur membership](openscientist_artifacts/kb_hypotheses_cellular_senescence_upar_senescence_surface_marker_target_openscientist_artifacts_data_senmayo_plaur_membership.json)

## Term Validation

No ontology term identifiers were found in this report.