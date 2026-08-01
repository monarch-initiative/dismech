---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-07-26T04:12:42.309038'
end_time: '2026-07-26T04:50:40.525995'
duration_seconds: 2278.22
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Hepatocellular Carcinoma
  category: ''
  hypothesis_group_id: rpp40_rnase_p_pretrna_mtor_myc_bridge
  hypothesis_label: RNase P Pre-tRNA Processing as the RPP40-mTOR/MYC Bridge
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: rpp40_rnase_p_pretrna_mtor_myc_bridge\nhypothesis_label:\
    \ RNase P Pre-tRNA Processing as the RPP40-mTOR/MYC Bridge\nstatus: EMERGING\n\
    description: Elevated RPP40 may sustain mTOR/MYC output in established hepatocellular\
    \ carcinoma specifically\n  because its contribution to RNase P preserves 5-prime\
    \ pre-tRNA maturation and translational capacity.\n  This narrow model predicts\
    \ that an RNase P/pre-tRNA defect after acute RPP40 loss precedes signaling\n\
    \  decline and is phenocopied by an RNase-P-specific perturbation. RPP40 is also\
    \ shared with RNase MRP,\n  however, and independent HCC evidence linking RPP40\
    \ to ribosomal-RNA and ribosomal-gene expression makes\n  an RNase MRP/pre-rRNA\
    \ or broader ribosome-biogenesis route a direct competitor. Neither published\
    \ HCC\n  study establishes the proposed RNase P ordering.\nevidence:\n- reference:\
    \ PMID:42424930\n  reference_title: RPP40, a subunit of Ribonuclease P, facilitates\
    \ hepatocellular carcinoma proliferation\n    by activating the mTOR/MYC signaling.\n\
    \  supports: PARTIAL\n  evidence_source: COMPUTATIONAL\n  snippet: Analysis showed\
    \ that RPP40 expression was markedly upregulated in HCC tissues compared to adjacent\n\
    \    normal tissues. High RPP40 expression correlated with poorer clinical outcomes,\
    \ even among patients\n    with matched histological grade or pathological stage.\n\
    \  explanation: Multi-dataset human-tumor associations support expression and\
    \ prognostic correlation, but\n    they do not establish whether RPP40 is a driver,\
    \ dependency, or consequence of proliferative state.\n- reference: PMID:42424930\n\
    \  reference_title: RPP40, a subunit of Ribonuclease P, facilitates hepatocellular\
    \ carcinoma proliferation\n    by activating the mTOR/MYC signaling.\n  supports:\
    \ PARTIAL\n  evidence_source: IN_VITRO\n  snippet: RPP40 suppression attenuated\
    \ cellular migration and proliferation, whereas its overexpression\n    enhanced\
    \ these malignant phenotypes both in vitro and in vivo.\n  explanation: This item\
    \ classifies the cell-culture component of the mixed result. The Huh-7 and HepG2\n\
    \    perturbations support an RPP40-dependent malignant phenotype in vitro, but\
    \ did not test pre-tRNA maturation\n    or RNase-P specificity.\n- reference:\
    \ PMID:42424930\n  reference_title: RPP40, a subunit of Ribonuclease P, facilitates\
    \ hepatocellular carcinoma proliferation\n    by activating the mTOR/MYC signaling.\n\
    \  supports: PARTIAL\n  evidence_source: MODEL_ORGANISM\n  snippet: RPP40 suppression\
    \ attenuated cellular migration and proliferation, whereas its overexpression\n\
    \    enhanced these malignant phenotypes both in vitro and in vivo.\n  explanation:\
    \ This separately classifies the subcutaneous mouse-xenograft component of the\
    \ mixed result.\n    It supports an in-vivo model phenotype but neither human-tumor\
    \ causality nor an RNase-P/pre-tRNA mechanism.\n- reference: PMID:42424930\n \
    \ reference_title: RPP40, a subunit of Ribonuclease P, facilitates hepatocellular\
    \ carcinoma proliferation\n    by activating the mTOR/MYC signaling.\n  supports:\
    \ PARTIAL\n  evidence_source: COMPUTATIONAL\n  snippet: The mTOR/MYC signaling\
    \ pathway was pinpointed as the key pathway regulated by RPP40 in HCC.\n  explanation:\
    \ The integrated pathway analysis nominates mTOR/MYC downstream of RPP40, but\
    \ the abstract\n    does not establish the intervening RNA-processing branch.\n\
    notes: This hypothesis is intentionally not wired as a causal pathograph edge.\
    \ Evidence supports the flanking\n  RPP40 and mTOR/MYC observations, not the proposed\
    \ RNase-P/pre-tRNA bridge."
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: true
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 7200
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 27
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
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
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Hepatocellular Carcinoma
- **Category:**

## Target Hypothesis
- **Hypothesis ID:** rpp40_rnase_p_pretrna_mtor_myc_bridge
- **Hypothesis Label:** RNase P Pre-tRNA Processing as the RPP40-mTOR/MYC Bridge
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: rpp40_rnase_p_pretrna_mtor_myc_bridge
hypothesis_label: RNase P Pre-tRNA Processing as the RPP40-mTOR/MYC Bridge
status: EMERGING
description: Elevated RPP40 may sustain mTOR/MYC output in established hepatocellular carcinoma specifically
  because its contribution to RNase P preserves 5-prime pre-tRNA maturation and translational capacity.
  This narrow model predicts that an RNase P/pre-tRNA defect after acute RPP40 loss precedes signaling
  decline and is phenocopied by an RNase-P-specific perturbation. RPP40 is also shared with RNase MRP,
  however, and independent HCC evidence linking RPP40 to ribosomal-RNA and ribosomal-gene expression makes
  an RNase MRP/pre-rRNA or broader ribosome-biogenesis route a direct competitor. Neither published HCC
  study establishes the proposed RNase P ordering.
evidence:
- reference: PMID:42424930
  reference_title: RPP40, a subunit of Ribonuclease P, facilitates hepatocellular carcinoma proliferation
    by activating the mTOR/MYC signaling.
  supports: PARTIAL
  evidence_source: COMPUTATIONAL
  snippet: Analysis showed that RPP40 expression was markedly upregulated in HCC tissues compared to adjacent
    normal tissues. High RPP40 expression correlated with poorer clinical outcomes, even among patients
    with matched histological grade or pathological stage.
  explanation: Multi-dataset human-tumor associations support expression and prognostic correlation, but
    they do not establish whether RPP40 is a driver, dependency, or consequence of proliferative state.
- reference: PMID:42424930
  reference_title: RPP40, a subunit of Ribonuclease P, facilitates hepatocellular carcinoma proliferation
    by activating the mTOR/MYC signaling.
  supports: PARTIAL
  evidence_source: IN_VITRO
  snippet: RPP40 suppression attenuated cellular migration and proliferation, whereas its overexpression
    enhanced these malignant phenotypes both in vitro and in vivo.
  explanation: This item classifies the cell-culture component of the mixed result. The Huh-7 and HepG2
    perturbations support an RPP40-dependent malignant phenotype in vitro, but did not test pre-tRNA maturation
    or RNase-P specificity.
- reference: PMID:42424930
  reference_title: RPP40, a subunit of Ribonuclease P, facilitates hepatocellular carcinoma proliferation
    by activating the mTOR/MYC signaling.
  supports: PARTIAL
  evidence_source: MODEL_ORGANISM
  snippet: RPP40 suppression attenuated cellular migration and proliferation, whereas its overexpression
    enhanced these malignant phenotypes both in vitro and in vivo.
  explanation: This separately classifies the subcutaneous mouse-xenograft component of the mixed result.
    It supports an in-vivo model phenotype but neither human-tumor causality nor an RNase-P/pre-tRNA mechanism.
- reference: PMID:42424930
  reference_title: RPP40, a subunit of Ribonuclease P, facilitates hepatocellular carcinoma proliferation
    by activating the mTOR/MYC signaling.
  supports: PARTIAL
  evidence_source: COMPUTATIONAL
  snippet: The mTOR/MYC signaling pathway was pinpointed as the key pathway regulated by RPP40 in HCC.
  explanation: The integrated pathway analysis nominates mTOR/MYC downstream of RPP40, but the abstract
    does not establish the intervening RNA-processing branch.
notes: This hypothesis is intentionally not wired as a causal pathograph edge. Evidence supports the flanking
  RPP40 and mTOR/MYC observations, not the proposed RNase-P/pre-tRNA bridge.
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

### Curation Leads

Provide candidate updates for the KB, but label these as leads requiring curator
verification. Include:

- candidate evidence references and exact abstract snippets to verify
- candidate pathophysiology nodes or edges
- candidate ontology terms for cell types and biological processes
- candidate subtype restrictions or status changes
- candidate `knowledge_gaps` or discussion prompts for unresolved causal claims,
  conflicting evidence, or explicit source/data absences

If the provider supports artifacts, produce artifact-friendly outputs such as an
evidence matrix, mechanistic diagram, knowledge-gap table, or comparison table.
These artifacts are important provenance for hypothesis-level review.


## Output

# Hypothesis-Search Report

## Hypothesis: RNase P Pre-tRNA Processing as the RPP40–mTOR/MYC Bridge (`rpp40_rnase_p_pretrna_mtor_myc_bridge`)
**Disease:** Hepatocellular Carcinoma (HCC) · **KB status:** EMERGING · **Search date:** 2026-07-26

---

## Executive Judgment

**Verdict: WEAKLY SUPPORTED / UNRESOLVED.**

The *flanking* claims of the hypothesis are supported by a single primary study: RPP40 is upregulated in HCC, carries independent prognostic value, and its perturbation changes proliferation/migration with mTOR/MYC nominated as the downstream pathway (PMID:42424930). The *central* claim — that RPP40 sustains mTOR/MYC **specifically through RNase P–mediated 5′ pre-tRNA maturation**, that an RNase P/pre-tRNA defect **precedes** signaling decline after acute RPP40 loss, and that the phenotype is **phenocopied by an RNase-P-specific perturbation** — has **no direct experimental support in any published HCC study.**

Two independent lines of evidence actively weaken the RNase-P-specific framing:

1. **Shared-subunit problem.** RPP40 is a constituent of **both** RNase P and RNase MRP, and biochemically partitions with essentially all RNase MRP complexes (PMID:16723659). An RPP40 gain/loss experiment therefore perturbs pre-tRNA maturation (RNase P) **and** pre-rRNA/ribosome biogenesis (RNase MRP) at once. The seed paper's RPP40 manipulations cannot, in principle, isolate the RNase-P branch.
2. **Directionality problem.** The canonical axis runs **mTOR/MYC → tRNA + rRNA synthesis** (PMID:25148809, 22260684, 18980784), i.e., signaling upstream of RNA processing/production. The seed hypothesis inverts this (RNA processing upstream, sustaining mTOR/MYC). The inverted ordering is a legitimate but non-default model that would require explicit time-resolved perturbation to establish.

A third, still more parsimonious competitor emerged on further search: pan-cancer profiling (PMID:41933259) shows RPP40 is a **broadly essential, cell-cycle-coupled gene**, upregulated and independently prognostic across most tumor types, and prognostic likewise in endometrial carcinoma, AML, and TNBC (PMID:36091104, 35334008). The identical "RPP40↑ → worse prognosis → proliferation" pattern across many cancers indicates the HCC observation is a **generic correlate of the proliferative state**, not an HCC-specific RNase-P/pre-tRNA mechanism. "Broadly essential" (pan-essential in CRISPR screens) further argues RPP40 is a housekeeping dependency rather than a *selective* HCC driver.

Because both the RNase MRP / pre-rRNA / ribosome-biogenesis route and the generic proliferation-correlate account explain the same HCC phenotype at least as parsimoniously, and neither the seed route nor its alternatives has been directly tested, the hypothesis should remain **EMERGING with an explicit knowledge-gap flag** on the RNase-P/pre-tRNA bridge and directionality edges.

**Most important caveat:** The entire primary-evidence base is one 2026 paper (PMID:42424930) whose abstract confirms neither pre-tRNA assays, RNase-P activity assays, nor temporal ordering. All mechanistic specificity in the seed hypothesis is currently *inferred*, not *demonstrated*.

**Two further points sharpen the verdict (Iteration 4):** (i) The competing ribosome-biogenesis route now has **direct HCC-specific support** — mTORC1→HEATR1 and MYC/E2F→fibrillarin/PELP1 drive HCC through rRNA/ribosome biogenesis (PMID:37247644, 36004921, 39258975, 36207533) — so the competitor is no longer merely extrapolated from non-HCC systems. (ii) The seed's named step is problematic at the molecular level: pre-tRNA 5'-leader processing is **co-transcriptional within Pol III initiation complexes** (downstream of mTOR/MYC) and its 5'-leader-degradation catalysis is attributed to **Rpp14, not RPP40** (PMID:37831743), so an RPP40 perturbation cannot cleanly isolate "RNase-P 5' pre-tRNA maturation" even in principle.

---

## Evidence Matrix

| # | Citation (PMID) | Evidence type | Stance | Mechanistic claim tested | Key finding | Subtype / context | Confidence & limitations |
|---|---|---|---|---|---|---|---|
| 1 | 42424930 (2026) | Human clinical + in vitro + model organism + computational | **Qualifies (partial support)** | RPP40 drives HCC proliferation via mTOR/MYC | RPP40 ↑ in HCC vs adjacent normal; worse outcomes at matched grade/stage; knockdown ↓ and overexpression ↑ migration/proliferation in Huh-7/HepG2 and xenografts; mTOR/MYC nominated as key pathway | HCC (bulk + scRNA-seq; Huh-7, HepG2, mouse xenograft) | Moderate for association/phenotype; **does not test pre-tRNA maturation, RNase-P activity, ordering, or RNase-P specificity**. Single study. |
| 2 | 16723659 (2006) | In vitro (biochemistry) | **Competing / limits scope** | Is RPP40 RNase-P-specific? | Rpp40 sediments with both 12S RNase P and 60–80S RNase MRP; "probably associated with all RNase MRP complexes" | Human HeLa complexes | High. Directly undermines RNase-P specificity of an RPP40 perturbation. |
| 3 | 39896489 / 40413743 / 40867056 (2025) | In vitro (genetic screen) | **Enables discrimination** | Do MRP-specific subunits exist? | RPP24/RMP24 & RPP64/RMP64 are RNase-MRP-specific; required for pre-rRNA ITS processing; NOT required for RNase P; do not bind H1 RNA | Human cells | High. Provides tools (MRP-specific vs P-specific knockdowns) to separate the branches. |
| 4 | 35115551 (2022) | Model organism + human primary cells | **Competing (supports MRP route)** | Does RNase MRP loss impair growth via pre-rRNA? | RMRP disruption → pre-rRNA accumulation, impaired ribosome synthesis, growth arrest; CHH mutations delay pre-rRNA processing | Human/mouse; CHH | High for MRP→rRNA→growth link; not HCC-specific. |
| 5 | 42277007 (2026) | In vitro (genome-wide screen) | **Qualifies (shared control)** | Are pre-tRNA & pre-rRNA processing co-regulated? | RMPPc pathway co-controls pre-rRNA ITS and pre-tRNA 5′-leader processing through a single RPP14 exon-inclusion control point; "prerequisite for translation" | Human cells | Moderate–high. Shows the two branches are mechanistically entangled, not cleanly separable. |
| 6 | 29186115 (2017, *Nature*) | In vitro + patient-derived model organism | **Competing / entangling** | Does tRNA biology act via ribosome biogenesis in HCC? | LeuCAG3′tsRNA inhibition → apoptosis in patient-derived orthotopic HCC; tsRNA enhances RPS28/RPS15 translation; RPS28 loss blocks pre-18S rRNA processing | HCC (orthotopic PDX) | High. In HCC, tRNA-derived RNA converges on rRNA processing/ribosome biogenesis — blurs P vs MRP dichotomy. |
| 7 | 25148809 (2014) | Review/mechanistic | **Competing (directionality)** | Is mTOR upstream or downstream of ribosome biogenesis? | mTORC1 positively regulates rRNA transcription, ribosomal-protein synthesis, assembly, and pre-rRNA processing | General mammalian | High as orientation. Inverts seed ordering. |
| 8 | 22260684 (2012) | Mechanistic | **Competing (directionality)** | mTOR control of rRNA processing | mTORC1 promotes rRNA synthesis and regulates pre-rRNA precursor processing; TOP-mRNA (ribosomal-protein) translation | Human cells | High. |
| 9 | 18980784 (2008) | Review | **Competing (directionality)** | MYC control of Pol I/III | c-Myc stimulates Pol I & Pol III output → ↑ rRNA and tRNA; pre-rRNA has prognostic value | Cancer (general) | Review-level support; MYC upstream of tRNA/rRNA. |
| 10 | 41777667 (2026) | Review | **Competing (MYC–nucleolus)** | MYC–ribosome-biogenesis coupling | MYC central to rDNA transcription, rRNA processing, ribosome assembly; nucleolar size ↑ with proliferation | Tumor cells | Review-level orientation for the MRP/rRNA route. |
| 11 | 42323524 / 41281472 / 35879647 (2022–2026) | Human clinical + in vitro | **Parallel (tRNA biology in HCC)** | Do tRNA-derived species drive HCC? | Multiple tsRNAs/tRFs are oncogenic prognostic markers in HCC (e.g., 5′tRF-Gly→CEACAM1) | HCC | Moderate. Supports tRNA relevance in HCC but via *fragments*, not RNase-P 5′-leader maturation. |
| 12 | 25497380 (2015) | Review | **Parallel (tRNA–growth)** | Oncogenic pathways → tRNA synthesis | PI3K/TORC1, Ras/ERK, Myc regulate Pol III/tRNA; tRNA changes sufficient to drive translation/growth | Cancer (general) | Review-level; reinforces mTOR/MYC-upstream directionality. |
| 13 | 41933259 (2026) | Human clinical + computational (CRISPR, scRNA-seq, IHC, proteomics) | **Competing (parsimony)** | Is RPP40 an HCC-specific driver or a pan-cancer proliferation-coupled essential? | RPP40 upregulated in most cancers; "a broadly essential gene for cancer cell survival"; independent risk factor for OS/PFS across cohorts; promotes proliferation "by activating cell cycle pathways" with strong cell-cycle dependence | Pan-cancer (multi-omics) | High. Reframes RPP40 as a housekeeping/proliferation-coupled essential, not an HCC-specific RNase-P driver. |
| 14 | 36091104 (2022) / 35334008 (2022) | Human clinical + in vitro | **Competing (parsimony)** | Is the RPP40↑/poor-prognosis pattern HCC-specific? | RPP40 independently prognostic in UCEC; a promoter of AML chemoresistance and early-TNBC recurrence; member of a validated 7-mRNA early-TNBC prognostic signature | UCEC, AML, TNBC | Moderate–high. Same pattern recurs across tumor types → generic proliferation correlate. |
| 15 | 37831743 (2023) | In vitro (biochemistry) | **Qualifies / limits specificity** | Is RNase-P 5'-leader maturation an isolable RPP40 step? | RNase P is embedded in Pol III initiation complexes and processes pre-tRNA co-transcriptionally; 5'-leader degradation is a 3'-5' exo activity of **Rpp14, not RPP40** | Human cells | High. The named step is Pol III-coupled and not RPP40-catalyzed → hard to isolate as an RPP40-specific bridge. |
| 16 | 28697848 (2017) / 36549864 (2023) | Review/mechanistic | **Qualifies (moonlighting)** | Does RNase P have non-pre-tRNA functions? | Nuclear RNase P acts in chromatin remodeling, Pol III initiation, DSB repair, replication-stress response, innate immunity | Human cells | Moderate–high. Multiple non-pre-tRNA routes could produce an RPP40 proliferation phenotype. |
| 17 | 37247644 (2023) | Human clinical + in vitro + model organism | **Competing (HCC-specific rRNA route)** | Does mTOR-driven ribosome biogenesis drive HCC? | mTORC1-upregulated HEATR1 promotes HCC by "dominating ribosome biogenesis"; ribosome-biogenesis hyperactivation drives hepatocyte transformation | HCC (TCGA/GEO, xenograft/orthotopic) | High. Direct HCC evidence for the mTOR→ribosome-biogenesis competitor. |
| 18 | 36207533 (2022) / 36004921 (2022) / 39258975 (2024) | Model organism + human clinical | **Competing (MYC→rRNA in HCC)** | Is MYC's HCC program ribosome biogenesis? | Ribosome biogenesis is MYC's most specific program in human cancers incl. HCC; fibrillarin (rRNA) and PELP1 (Rix complex) drive HCC via MYC/E2F | HCC + MYC-driven cancers | High. MYC upstream of rRNA/ribosome biogenesis in HCC → favors rRNA competitor and directionality reversal. |

---

## Mechanistic Causal Chain (as implied by the hypothesis)

```
RPP40 overexpression (HCC)
   │  [STRONG: PMID 42424930 — expression/prognosis]
   ▼
↑ RNase P holoenzyme function ──► 5′ pre-tRNA leader maturation
   │  [MISSING in HCC: no pre-tRNA / RNase-P activity assay]
   │  [CONFOUND: RPP40 also ↑ RNase MRP → pre-rRNA (PMID 16723659)]
   ▼
↑ mature tRNA pool ──► ↑ translational capacity
   │  [INFERRED: not measured in HCC; entangled with rRNA (PMID 29186115, 42277007)]
   ▼
Sustained mTOR/MYC output
   │  [INVERTED vs canon: mTOR/MYC normally UPSTREAM of tRNA/rRNA (PMID 25148809, 18980784)]
   ▼
Proliferation / migration / worse prognosis
      [STRONG phenotype: PMID 42424930 — but attributes to mTOR/MYC generically]
```

- **Strong links:** RPP40 expression ↔ HCC prognosis; RPP40 perturbation ↔ malignant phenotype; mTOR/MYC ↔ proliferation.
- **Inferred links:** RPP40 → RNase-P-specific pre-tRNA maturation → translational capacity (never assayed in HCC).
- **Missing / inverted causal steps:** (a) directionality (RNA processing → mTOR/MYC vs mTOR/MYC → RNA processing); (b) temporal ordering after acute RPP40 loss; (c) RNase-P specificity (shared subunit); (d) phenocopy by an RNase-P-specific perturbation.

---

## Knowledge Gaps

| Gap | Scope | Why it matters | What was checked | Resolving evidence/experiment |
|---|---|---|---|---|
| **G1 – RNase-P/pre-tRNA bridge never assayed in HCC** | Core causal edge | The entire specificity of the hypothesis rests here | PubMed: RPP40+HCC+mTOR/MYC returns only PMID:42424930, whose abstract has no pre-tRNA/RNase-P assay | Northern/qPCR of 5′-leader-containing pre-tRNAs and RNase-P cleavage assays after acute RPP40 depletion in HCC cells |
| **G2 – Shared-subunit confounding** | Perturbation validity | RPP40 loss hits RNase P **and** RNase MRP (PMID:16723659); phenotype cannot be branch-assigned | Confirmed via subunit-composition literature | Parallel knockdown of P-specific (POP4/RPP21; H1 RNA) vs MRP-specific (RPP24/RPP64; MRP RNA) with matched readouts |
| **G3 – Directionality unproven/inverted** | Causal-graph edge | Canon has mTOR/MYC upstream (PMID:25148809, 18980784); seed reverses it | Checked mTOR/MYC–ribosome-biogenesis literature | Time-resolved multi-omics after acute RPP40 loss: does pre-tRNA defect precede mTOR/MYC decline? |
| **G4 – No RNase-P-specific phenocopy** | Prediction test | Hypothesis predicts an RNase-P-only perturbation reproduces the mTOR/MYC phenotype | Searched; none reported in HCC | POP4/RPP21 knockdown in Huh-7/HepG2 with mTOR/MYC and proliferation readouts |
| **G5 – tRNA/rRNA entanglement in HCC** | Mechanistic separability | In HCC, tRNA-derived RNA acts through pre-18S rRNA processing (PMID:29186115); RMPPc co-controls both (PMID:42277007) | Confirmed in literature | Isotope/metabolic-labeling flux to separate pre-tRNA vs pre-rRNA maturation contributions to translation |
| **G6 – Source/data absences** | Curation | No GenCC/ClinGen gene–disease record and no clinical trial ties RPP40 to RNase-P activity in HCC | PubMed searched; pan-cancer CRISPR essentiality now available (PMID:41933259) but ClinGen/GenCC/trials not directly queried | Query ClinGen/GenCC/ClinicalTrials.gov/TCGA-LIHC for RPP40 gene–disease/trial records |
| **G8 – Catalytic locus of the named step** | Core mechanism | The seed attributes the pre-tRNA 5'-leader step to RPP40, but the 5'-leader-degradation catalysis is reported for **Rpp14** (PMID:37831743); RPP40's precise catalytic/structural contribution to pre-tRNA cleavage is unspecified | Checked RNase P subunit-function literature | Structure-function / separation-of-function assays defining RPP40's specific role in pre-tRNA cleavage vs holoenzyme integrity vs MRP function |
| **G7 – Selective vs pan-essential dependency** *(largely resolved)* | Interpretation / driver claim | RPP40 is "broadly essential" pan-cancer (PMID:41933259); a pan-essential gene is a weak candidate for a *selective* HCC driver mechanism | Pan-cancer CRISPR result checked; **direct DepMap portal API access attempted this session but blocked (HTTP 403)** | Published CRISPR screen already classifies RPP40 as pan-essential → its HCC requirement is not lineage-selective. Confirmatory raw-DepMap comparison (RPP40 Chronos in liver lines vs common-essential median) remains a clean but likely-confirmatory follow-up |

---

## Alternative Models

1. **RNase MRP / pre-rRNA / ribosome-biogenesis route (primary competitor — now with direct HCC support).** RPP40 sustains proliferation through RNase MRP–dependent pre-rRNA maturation and ribosome biogenesis rather than RNase P. Supported by RPP40's near-universal association with RNase MRP (PMID:16723659), MRP loss→pre-rRNA accumulation→growth arrest (PMID:35115551), MYC/mTOR–ribosome-biogenesis coupling (PMID:41777667, 25148809), and now **direct HCC evidence** that mTORC1-driven ribosome biogenesis (HEATR1) and MYC/E2F-linked rRNA factors (fibrillarin, PELP1) promote HCC (PMID:37247644, 36004921, 39258975, 36207533). **Status: parallel/alternative to seed, arguably more parsimonious and now HCC-substantiated.**
2. **mTOR/MYC-upstream model (directionality reversal).** mTOR/MYC hyperactivation is the driver and elevated RPP40 (and tRNA/rRNA output) is a *downstream consequence* or permissive amplifier (PMID:18980784, 25497380). **Status: upstream-cause alternative; makes RPP40 a consequence/dependency rather than initiator.**
3. **Integrated RMPPc co-processing model.** Pre-tRNA and pre-rRNA maturation are jointly controlled and jointly required for translation (PMID:42277007); RPP40's effect is on *combined* processing capacity, not one branch. **Status: complementary — dissolves the P-vs-MRP dichotomy.**
4. **tRNA-fragment / translational-fine-tuning route.** Oncogenic tsRNAs/tRFs in HCC act through ribosomal-protein translation and rRNA processing (PMID:29186115, 35879647, 42323524). **Status: parallel mechanism linking tRNA biology to HCC without invoking RNase-P 5′-leader maturation.**
5. **Generic proliferation-correlate / pan-essential housekeeping model (most parsimonious competitor).** RPP40 is a broadly essential, cell-cycle-coupled core RNase P/MRP subunit whose upregulation and prognostic value recur across most cancers (PMID:41933259, 36091104, 35334008). Under this model the HCC association is a passenger/correlate of high proliferative-biosynthetic demand, and RPP40 is a housekeeping dependency rather than a *selective* HCC driver acting through a specific RNA-processing branch. **Status: alternative to the seed that requires no tissue- or branch-specific mechanism; the seed must show HCC-selective dependency and branch specificity to survive this competitor.**
6. **Transcription-coupled / moonlighting RNase P model.** Rather than a stand-alone 5'-leader maturation step, RPP40/RNase P supports tRNA output via co-transcriptional processing within Pol III initiation complexes (PMID:37831743, 33929081) and/or via non-canonical chromatin-remodeling, DSB-repair, and innate-immunity functions (PMID:28697848, 36549864). Notably the 5'-leader-degradation catalysis is attributed to **Rpp14, not RPP40** (PMID:37831743). **Status: refines and simultaneously undermines the seed — the named step is Pol III-coupled (downstream of mTOR/MYC) and not RPP40-catalyzed, so it cannot be isolated by an RPP40 perturbation.**

---

## Discriminating Tests

| Test | Design | Expected result if SEED (RNase P) true | Expected if COMPETITOR (RNase MRP) true |
|---|---|---|---|
| **T1 – Branch-specific knockdown** | In Huh-7/HepG2: knock down P-specific POP4/RPP21 vs MRP-specific RPP24/RPP64; measure proliferation, mTOR/MYC signaling | POP4/RPP21 knockdown phenocopies RPP40 loss; RPP24/RPP64 does not | RPP24/RPP64 knockdown phenocopies; POP4/RPP21 does not |
| **T2 – Direct processing assays** | After acute RPP40 depletion, quantify 5′-leader pre-tRNA intermediates (RNase P) vs ITS1-site-2 pre-rRNA intermediates (RNase MRP) by Northern/qPCR/RNA-seq | Pre-tRNA leaders accumulate first/dominantly | Pre-rRNA intermediates accumulate first/dominantly |
| **T3 – Temporal ordering** | Time-course (0–72 h) of acute RPP40 degron depletion; joint measurement of pre-tRNA maturation, polysome/translation, and mTOR/MYC activity | pre-tRNA defect precedes translational and mTOR/MYC decline | mTOR/MYC decline precedes or coincides with rRNA/ribosome defect |
| **T4 – Rescue specificity** | Rescue RPP40-null cells with separation-of-function RPP40 alleles competent for P but not MRP (or vice versa) | P-competent allele restores mTOR/MYC + proliferation | MRP-competent allele restores phenotype |
| **T5 – Patient stratification** | TCGA-LIHC / cohorts: correlate RPP40 with pre-tRNA-processing signatures vs rRNA/ribosome-biogenesis signatures and with mTOR/MYC activity, stratified by stage/grade | RPP40–mTOR/MYC coupling tracks pre-tRNA signature | Coupling tracks rRNA/ribosome-biogenesis signature |
| **T6 – Dependency mapping** | DepMap: is RPP40 a selective dependency in liver lines, and does it cluster with RNase P vs RNase MRP / ribosome-biogenesis co-dependencies? | Co-dependency with RNase-P-specific genes | Co-dependency with MRP / ribosome-biogenesis genes |

---

## Curation Leads (require curator verification)

**Candidate evidence references / snippets to verify:**
- PMID:16723659 — verify snippet: *"hPop1, Rpp40, Rpp38, and Rpp30 (and possibly also hPop5), which are probably associated with all RNase MRP complexes"* → supports `evidence_source: IN_VITRO`, stance **COMPETING/QUALIFIES** (shared-subunit limit on RNase-P specificity).
- PMID:39896489 — verify: *"Unlike all other human RNase MRP protein components, RPP24 and RPP64 are not required for RNase P activity and do not associate with RNase P-specific RNA H1"* → supports discriminating-tool availability.
- PMID:35115551 — verify: *"CRISPR-mediated disruption of RMRP in human cells lines caused growth arrest, with pre-rRNA accumulation"* → supports competing MRP route.
- PMID:25148809 — verify: *"mTORC1 positively regulates several steps in ribosome biogenesis, including ribosomal RNA transcription…"* → directionality caveat.
- PMID:29186115 — verify: HCC tsRNA → *"blocks pre-18S ribosomal RNA processing"* → tRNA/rRNA entanglement in HCC.
- PMID:42277007 — verify: RMPPc *"integrated control over the processing of… internal transcribed spacers in pre-rRNA, and 5′-leader sequences in pre-tRNA"* → co-processing model.
- PMID:41933259 — verify: *"it was identified as a broadly essential gene for cancer cell survival"* and *"RPP40 likely promotes tumor proliferation by activating cell cycle pathways"* → supports generic proliferation-correlate competitor; stance **COMPETING (parsimony)**, evidence_source COMPUTATIONAL/HUMAN.
- PMID:36091104 — verify: *"one of the promoting factors for the chemoresistance of acute myeloid leukemia and a recurrence predictor of early-stage triple-negative breast cancer"* → pan-cancer prognostic pattern.
- PMID:37831743 — verify: *"transcription complexes of RNA polymerase III assembled on tRNA genes comprise RNase P that cleaves precursor tRNA and subsequently degrades the excised 5' leader"* and *"a 3'-5' exoribonucleolytic activity carried out by the protein subunit Rpp14"* → transcription-coupled processing + Rpp14 (not RPP40) catalysis; stance **QUALIFIES/limits specificity**.
- PMID:37247644 — verify: *"Hyperactivation of ribosome biogenesis leads to hepatocyte transformation and plays pivotal roles in hepatocellular carcinoma (HCC) development"* → HCC-specific mTOR→ribosome-biogenesis competitor; stance **COMPETING**.
- PMID:36207533 — verify: *"ribosome biogenesis is most specifically associated with MYC expression in human primary cancers"* → MYC→rRNA directionality/competitor.

**Candidate pathophysiology nodes/edges:**
- Add node: *RNase MRP / pre-rRNA ITS processing / ribosome biogenesis* as a competing bridge parallel to the RNase-P/pre-tRNA node (now with HCC-specific support via HEATR1/fibrillarin/PELP1).
- Add node: *transcription-coupled RNase P within Pol III initiation complexes* and *RNase P moonlighting (chromatin/DSB-repair/innate immunity)* as alternative RPP40 effector routes.
- Add HCC nodes: `mTORC1 → HEATR1 → ribosome biogenesis` (PMID:37247644); `MYC/E2F → fibrillarin/PELP1 → ribosome biogenesis` (PMID:36004921, 39258975).
- Flag edge `RPP40 → RNase P (specific)` as **unconfirmed / confounded** (shared subunit; leader catalysis attributed to Rpp14).
- Flag edge `pre-tRNA maturation → sustains mTOR/MYC` as **unconfirmed / directionality-contested** (canonical + HCC-specific evidence places mTOR/MYC upstream).

**Candidate ontology terms:** GO:0001682 (tRNA 5′-leader removal / tRNA processing), GO:0000469 (cleavage involved in rRNA processing), GO:0042254 (ribosome biogenesis), GO:0006364 (rRNA processing), GO:0004526 (ribonuclease P activity); CL cell types: hepatocyte (CL:0000182), malignant hepatocyte.

**Candidate subtype restriction / status change:** Keep **EMERGING**; add explicit restriction that support is limited to *established HCC bulk/expression associations and a single functional study*, not the RNase-P bridge. Note that RPP40's HCC pattern is shared pan-cancer (not HCC-specific). Add `knowledge_gaps` entries G1–G8 above.

**Candidate discussion prompt (parsimony):** RPP40 is a broadly essential, cell-cycle-coupled RNase P/MRP subunit with the same upregulation/poor-prognosis pattern across many cancers (PMID:41933259, 36091104, 35334008). Curators should weigh whether the HCC "driver via RNase-P bridge" framing survives against a generic proliferation-correlate / pan-essential-housekeeping explanation, and whether a *selective* (not common-essential) HCC dependency has ever been demonstrated (DepMap check outstanding).

**Candidate source/data absence note:** As of 2026-07-26, PubMed returns a single primary RPP40-HCC study; no ClinGen/GenCC gene–disease curation, clinical trial, or public omics dataset was found linking RPP40 to RNase-P catalytic activity in HCC (ClinGen/GenCC/trials/omics endpoints not yet directly queried — flag for follow-up).

---

## Limitations of This Search
- Primary HCC evidence rests on one abstract (full text not parsed); pre-tRNA/RNase-P assays may exist in the full paper's figures but are absent from the abstract.
- Directionality and MRP-route arguments draw partly on review-level sources (labeled as such).
- ClinGen/GenCC/ClinicalTrials/TCGA were identified as follow-up targets but not directly queried.
- Direct DepMap portal API access was attempted programmatically (RPP40 CRISPR gene effect) but returned HTTP 403; the pan-essential classification is taken from the published CRISPR screen (PMID:41933259) instead. Raw-score confirmation is outstanding.
- The seed YAML's reference to "independent HCC evidence linking RPP40 to ribosomal-RNA and ribosomal-gene expression" was **not** corroborated by a separate primary HCC paper in PubMed searches (RPP40+rRNA+HCC returned no hits); it most likely refers to enrichment analyses within PMID:42424930 itself. Curators should verify whether a distinct source exists — otherwise this is a single-source claim (source-absence note).


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)
