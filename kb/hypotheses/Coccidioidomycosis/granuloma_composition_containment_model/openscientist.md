---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-08-08T19:22:41.105569'
end_time: '2026-08-08T19:41:08.421952'
duration_seconds: 1107.32
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Coccidioidomycosis
  category: ''
  hypothesis_group_id: granuloma_composition_containment_model
  hypothesis_label: Coccidioidal Granuloma Composition and Maintenance Model
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: granuloma_composition_containment_model\n\
    hypothesis_label: Coccidioidal Granuloma Composition and Maintenance Model\nstatus:\
    \ EMERGING\ndescription: |-\n  A hypothesis about the cellular and signaling composition\
    \ of the coccidioidal granuloma, and about which features of it determine containment\
    \ versus progression to cavitation and dissemination. The model proposed here\
    \ is that the spherule's resistance to phagocytosis obliges a specific, sustained\
    \ macrophage-transformation program - epithelioid differentiation and giant-cell\
    \ fusion under Th1/Th17 and TNF drive - and that the identity of the recruited\
    \ cells, the signals that maintain the structure, and the immune microenvironment\
    \ inside the granuloma are what distinguish a contained lesion from one that necroses\
    \ and disseminates.\n  The status is EMERGING rather than CANONICAL because the\
    \ intermediate steps are borrowed rather than measured. Granuloma biology in coccidioidomycosis\
    \ is currently modeled largely by analogy to tuberculosis: morphologies have been\
    \ described, but the cells recruited, the maintenance signals, and the interior\
    \ microenvironment are explicitly unresolved in the primary literature. This entry's\
    \ conformance to the `granuloma_formation` module therefore rests on two causal\
    \ edges (Th1/Th17 -> epithelioid transformation, and epithelioid transformation\
    \ -> organized granuloma) whose evidence is PARTIAL for exactly this reason; those\
    \ edges are tagged into this hypothesis group so the dependency is explicit rather\
    \ than implied.\n  Two comparators already in the knowledge base bear on the same\
    \ question through the shared module: Sarcoidosis (`antigen_persistence_granuloma_chronicity_model`)\
    \ and Chronic_Beryllium_Disease. The mouse scRNA-seq time course (GSE274766) and\
    \ Visium spatial transcriptomics (GSE274767) recorded in this entry's `datasets`\
    \ block are the matched data most directly capable of addressing the cell-identity\
    \ and spatial-organization components.\nevidence:\n- reference: PMID:33262956\n\
    \  reference_title: 'Host Response to Coccidioides Infection: Fungal Immunity.'\n\
    \  supports: SUPPORT\n  evidence_source: OTHER\n  snippet: we do not know what\
    \ cells are recruited to the granuloma, what signals form and maintain the\n \
    \   granuloma structure, nor details on the immune microenvironment within the\
    \ granuloma interior\n  explanation: 'States the open question this hypothesis\
    \ group exists to resolve, in the authors'' own\n    words: granuloma cell composition,\
    \ maintenance signals, and interior microenvironment are all unresolved\n    for\
    \ Coccidioides.'\n- reference: PMID:33262956\n  reference_title: 'Host Response\
    \ to Coccidioides Infection: Fungal Immunity.'\n  supports: SUPPORT\n  evidence_source:\
    \ OTHER\n  snippet: Exploring granuloma immunity is imperative for understanding\
    \ infection chronicity as Coccidioides\n    infection often presents with granuloma\
    \ formation.\n  explanation: 'Motivates the hypothesis: granuloma immunity is\
    \ framed as the route to understanding why\n    some infections become chronic\
    \ rather than resolving.'\n- reference: PMID:37367586\n  reference_title: 'Coccidioidomycosis\
    \ Granulomas Informed by Other Diseases: Advancements, Gaps, and\n    Challenges.'\n\
    \  supports: SUPPORT\n  evidence_source: OTHER\n  snippet: However, very little\
    \ is known about granulomas during Coccidioides infection.\n  explanation: Independent\
    \ confirmation from a review dedicated to coccidioidal granulomas that the disease-specific\n\
    \    granuloma biology is largely uncharacterized.\n- reference: PMID:37367586\n\
    \  reference_title: 'Coccidioidomycosis Granulomas Informed by Other Diseases:\
    \ Advancements, Gaps, and\n    Challenges.'\n  supports: PARTIAL\n  evidence_source:\
    \ OTHER\n  snippet: Granulomas are best defined in TB, providing clues that may\
    \ be leveraged to understand Coccidioides\n    infections.\n  explanation: Documents\
    \ that the current model is an extrapolation from tuberculosis. Support is PARTIAL\n\
    \    because this justifies the analogy rather than establishing that it holds\
    \ for Coccidioides - which\n    is the substance of what makes this hypothesis\
    \ EMERGING."
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
- **Disease Name:** Coccidioidomycosis
- **Category:** 

## Target Hypothesis
- **Hypothesis ID:** granuloma_composition_containment_model
- **Hypothesis Label:** Coccidioidal Granuloma Composition and Maintenance Model
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: granuloma_composition_containment_model
hypothesis_label: Coccidioidal Granuloma Composition and Maintenance Model
status: EMERGING
description: |-
  A hypothesis about the cellular and signaling composition of the coccidioidal granuloma, and about which features of it determine containment versus progression to cavitation and dissemination. The model proposed here is that the spherule's resistance to phagocytosis obliges a specific, sustained macrophage-transformation program - epithelioid differentiation and giant-cell fusion under Th1/Th17 and TNF drive - and that the identity of the recruited cells, the signals that maintain the structure, and the immune microenvironment inside the granuloma are what distinguish a contained lesion from one that necroses and disseminates.
  The status is EMERGING rather than CANONICAL because the intermediate steps are borrowed rather than measured. Granuloma biology in coccidioidomycosis is currently modeled largely by analogy to tuberculosis: morphologies have been described, but the cells recruited, the maintenance signals, and the interior microenvironment are explicitly unresolved in the primary literature. This entry's conformance to the `granuloma_formation` module therefore rests on two causal edges (Th1/Th17 -> epithelioid transformation, and epithelioid transformation -> organized granuloma) whose evidence is PARTIAL for exactly this reason; those edges are tagged into this hypothesis group so the dependency is explicit rather than implied.
  Two comparators already in the knowledge base bear on the same question through the shared module: Sarcoidosis (`antigen_persistence_granuloma_chronicity_model`) and Chronic_Beryllium_Disease. The mouse scRNA-seq time course (GSE274766) and Visium spatial transcriptomics (GSE274767) recorded in this entry's `datasets` block are the matched data most directly capable of addressing the cell-identity and spatial-organization components.
evidence:
- reference: PMID:33262956
  reference_title: 'Host Response to Coccidioides Infection: Fungal Immunity.'
  supports: SUPPORT
  evidence_source: OTHER
  snippet: we do not know what cells are recruited to the granuloma, what signals form and maintain the
    granuloma structure, nor details on the immune microenvironment within the granuloma interior
  explanation: 'States the open question this hypothesis group exists to resolve, in the authors'' own
    words: granuloma cell composition, maintenance signals, and interior microenvironment are all unresolved
    for Coccidioides.'
- reference: PMID:33262956
  reference_title: 'Host Response to Coccidioides Infection: Fungal Immunity.'
  supports: SUPPORT
  evidence_source: OTHER
  snippet: Exploring granuloma immunity is imperative for understanding infection chronicity as Coccidioides
    infection often presents with granuloma formation.
  explanation: 'Motivates the hypothesis: granuloma immunity is framed as the route to understanding why
    some infections become chronic rather than resolving.'
- reference: PMID:37367586
  reference_title: 'Coccidioidomycosis Granulomas Informed by Other Diseases: Advancements, Gaps, and
    Challenges.'
  supports: SUPPORT
  evidence_source: OTHER
  snippet: However, very little is known about granulomas during Coccidioides infection.
  explanation: Independent confirmation from a review dedicated to coccidioidal granulomas that the disease-specific
    granuloma biology is largely uncharacterized.
- reference: PMID:37367586
  reference_title: 'Coccidioidomycosis Granulomas Informed by Other Diseases: Advancements, Gaps, and
    Challenges.'
  supports: PARTIAL
  evidence_source: OTHER
  snippet: Granulomas are best defined in TB, providing clues that may be leveraged to understand Coccidioides
    infections.
  explanation: Documents that the current model is an extrapolation from tuberculosis. Support is PARTIAL
    because this justifies the analogy rather than establishing that it holds for Coccidioides - which
    is the substance of what makes this hypothesis EMERGING.
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

# Hypothesis-Search Report: Coccidioidal Granuloma Composition and Maintenance Model

**Disease:** Coccidioidomycosis (Valley Fever)
**Hypothesis ID:** `granuloma_composition_containment_model`
**KB status:** EMERGING
**Search date:** 2026-08-08
**Sources reviewed:** ~44 PubMed records; 9 findings recorded to the knowledge state.

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED (bookended, not bridged).**

The seed hypothesis is a chain: *spherule anti-phagocytosis → forced sustained macrophage-transformation program (epithelioid + giant-cell fusion) under Th1/Th17 + TNF drive → organized granuloma → containment; failure → necrosis/cavitation/dissemination.* Current literature strongly supports **both ends** of the chain but leaves the **Coccidioides-specific middle** unmeasured:

- **Well supported (the two bookends):**
  1. **The premise** — *Coccidioides* is genuinely anti-phagocytic and resistant to killing (arthroconidial antiphagocytic wall; only 20–30% of ingested organisms killed by PMNs; 30–80 µm spherules exceed phagocytic capacity; spherules actively suppress macrophage NO/iNOS) (PMID 6300253, 21129481).
  2. **The drive signals** — loss-of-function evidence pins containment on Th1 (IL-12/IFN-γ/STAT4/STAT3) in humans and mice (PMID 28098554, 35149520), on Th17 in *Coccidioides*-inclusive vaccine models (PMID 21206087, 21859851), and on TNF pharmacologically (anti-TNF → dissemination; PMID 33933122).
  3. **The clinical dichotomy** — organized macrophage/T-cell granulomas track with containment (resistant mouse strains, canine lesions) while neutrophilic suppuration and, at the human cavitary endpoint, loss of organized granuloma + caseous necrosis track with progression (PMID 18852250, 20930107, 24321524).

- **Not yet established (the inferred middle):** The specific *intermediate* steps the hypothesis asserts — that Th1/Th17+TNF drive **epithelioid transformation and giant-cell fusion** *within Coccidioides granulomas specifically*, and that this transformation is what **organizes and maintains** the lesion — are **borrowed from tuberculosis and other granulomas, not directly measured in Coccidioides.** The generic IFN-γ→macrophage-priming→TNF→epithelioid/giant-cell cascade is established (PMID 9306503, 7977642) but only in TB/hypersensitivity/schistosome models, and etiology-matched transcriptomics show granuloma molecular programs **differ markedly by cause despite identical histology** (PMID 33276795). So the analogy is a hypothesis, not a demonstrated fact.

**Most important caveats:**
1. **The two flagged causal edges remain PARTIAL for a real reason** — no *Coccidioides* study yet demonstrates the Th1/Th17→epithelioid and epithelioid→organized-granuloma edges *in situ*. The matched datasets (GSE274766 scRNA-seq; GSE274767 Visium) are the right instruments but their edge-resolving analysis is not yet in the primary literature captured here.
2. **A competing/parallel axis is underweighted.** Neutrophils and inflammasome-driven regulated cell death shape outcome independent of the macrophage program: CXCR2/IL-8R2-KO mice are *more* resistant and caspase-1-KO mice are *more* tolerant at equal fungal burden (PMID 33106296, 42386736). A macrophage-centric containment model does not, by itself, explain these.
3. **Maintenance is more than "drive."** Comparator granuloma diseases show that **Treg balance and B-cell/ectopic-lymphoid structures** are decisive for the contained-vs-injurious outcome (PMID 24912188, 31094704) — nodes absent from the seed model.

Net: the hypothesis is a **reasonable, partially-evidenced framework whose EMERGING status is correctly assigned.** It should not be promoted to CANONICAL until the intermediate edges are measured in *Coccidioides* tissue.

---

## Evidence Matrix

| # | Citation (PMID) | Evidence type | Stance | Mechanistic claim tested | Key finding | Subtype/context | Confidence & limitations |
|---|---|---|---|---|---|---|---|
| 1 | 6300253 (Drutz & Huppert 1983) | In vitro / pathology (review-classic) | **Supports** (premise) | Spherule/arthroconidia resist phagocytic killing | Antiphagocytic outer wall; only 20–30% of ingested organisms killed by PMNs; 30–80 µm spherules tax immune reserves; macrophages ingest but may not kill without lymphokine activation | Human/animal *C. immitis* | Moderate; foundational but old, descriptive |
| 2 | 21129481 (Gonzalez 2011) | In vitro (mouse macrophages) | **Supports** (interior microenvironment) | Fungus suppresses macrophage effectors | Spherule initials secrete a soluble factor suppressing NO/iNOS in IFN-γ/LPS-activated macrophages; NO not essential for killing | Parasitic-phase *Coccidioides* | Moderate; in vitro; factor unidentified |
| 3 | 28098554 (Odio 2017) | Human clinical/genetic | **Supports** (Th1 edge) | Th1 axis required for containment | 8 disseminated cases had IL-12/IFN-γ and STAT3 defects | Disseminated (~1% of symptomatic; 1/3 fatal) | High for the edge; small N, extreme subtype |
| 4 | 35149520 (Powell 2022) | Model organism (STAT4 knock-in) | **Supports** (Th1 edge) | STAT4/Th1 required for resistance | Human STAT4 mutation predisposes mice to dissemination; no Th1 without STAT4 | Mouse model of human mutation | High; direct perturbation |
| 5 | 21206087 (Wüthrich 2011) | Model organism (vaccine) | **Supports** (Th17 edge) | Th17 necessary/sufficient for protection | Th17 necessary & sufficient vs 3 mycoses incl. *C. posadasii*; acts by recruiting neutrophils + macrophages; MyD88-dep, Dectin-1-indep | Vaccine/adaptive-primed mouse | High for edge; vaccine (not natural granuloma maintenance) |
| 6 | 21859851 (Hung 2011) | Model organism (vaccine) | **Supports** (Th17 edge) | Th17 contributes to protection | Loss of functional Th17 increased susceptibility; mixed Th1/Th2/Th17 lung response with containment | ΔT-vaccinated C57BL/6 | Moderate–high; vaccine context |
| 7 | 33933122 (Trainor 2021) | Human clinical (case) | **Supports** (TNF maintenance edge) | TNF required to maintain containment | Anti-TNF (infliximab) → disseminated disease; improved on withdrawal | Reactivation, immunosuppressed | Moderate; single case, but mechanistically pointed |
| 8 | 18852250 (Shubitz 2008) | Model organism (strain histopathology) | **Supports** (composition/containment) | Organized macrophage/T-cell granuloma = containment | Resistant SW: well-formed granulomas, macrophage/lymphocyte mantle, few fungi; susceptible B6: neutrophils + spherules, few T cells, death | Mouse strain susceptibility | High (correlational); no architecture perturbation |
| 9 | 20930107 (Shubitz 2011) | Model organism (natural canine) | **Supports** (cell identity/spatial) | Granulomas are T-cell predominant, peripherally organized | T > B lymphocytes; T cells concentrated at granuloma periphery, independent of tissue/burden | Natural canine disease | Moderate; descriptive IHC |
| 10 | 24321524 (Sobonya 2014) | Human clinical (pathology, n=21) | **Supports** (containment→cavitation dichotomy) | Progression = loss of organized granuloma | Cavity wall: chronic inflammation, occasional giant cells, **no granulomas**; lining: neutrophils + caseous necrosis; satellite granulomas variable | Cavitary pulmonary disease | Moderate–high; cross-sectional, cannot infer temporal direction |
| 11 | 9306503 (Suga 1997) | Review/model (hypersensitivity pneumonitis) | **Supports by analogy** (epithelioid edge) | IFN-γ→macrophage priming→TNF→epithelioid/giant cells | Th1 IFN-γ primes macrophages to make TNF/IL-1 → epithelioid + giant-cell granuloma | Non-*Coccidioides* granuloma | Low for *Coccidioides*; mechanism borrowed |
| 12 | 7977642 (Chensue 1994) | Model organism (bead granuloma) | **Supports by analogy** (epithelioid edge) | Antigen-driven Th1 granuloma needs TNF | PPD-bead Th1 granulomas with epithelioid/giant cells; TNF-dependent | Non-*Coccidioides* granuloma | Low for *Coccidioides*; borrowed |
| 13 | 33276795 (Casanova 2020) | Human computational (granuloma transcriptomics) | **Qualifies** (limits TB analogy) | Do granuloma programs generalize across etiology? | Despite histologic similarity, DEGs/pathways differ markedly across sarcoid/cocci/TB and by tissue | Micro-dissected human granulomas | High; directly undercuts extrapolation |
| 14 | 33106296 (Carlin 2020) | Model organism (KO) | **Competing/parallel** | Neutrophil recruitment drives pathology | IL-8R2(CXCR2)-KO mice **more resistant**; human pathology = many neutrophils around ruptured spherules | Pulmonary mouse + human pathology | High; reframes neutrophils as harmful, not just protective |
| 15 | 42386736 (Yau 2026) | Model organism (KO, mechanistic) | **Competing/parallel** | Inflammasome/regulated cell death set outcome | Caspase-1-KO → improved tolerance at equal burden, ↑NETs in granulomas; TLR2-NLRP3-pyrin-IL-18 promotes spherule growth; only ruptured spherules trigger IL-1β | Mouse macrophage/neutrophil + in vivo | High; recent, mechanistically detailed |
| 16 | 24912188 (Mack 2014) | Model organism (CBD comparator) | **Competing/complementary** (missing node) | Tregs modulate granuloma outcome | Treg depletion exacerbates inflammation & enhances granuloma formation; antigen-specific Th1 CD4 drive | HLA-DP2 Tg beryllium disease | Moderate; comparator disease, transfer uncertain |
| 17 | 31094704 (Atif 2019) | Model organism (CBD comparator) | **Competing/complementary** (missing node) | B cells/ectopic lymphoid protect | B-cell depletion → loss of granulomas/aggregates, ↑ lung injury | HLA-DP2 Tg beryllium disease | Moderate; comparator disease |
| 18 | 36891233 (Sacco 2023) | Review | **Supports** (structural definition) | Granuloma = macrophage core→giant cells, T-cell corona | Standard granuloma architecture; *Coccidioides* can be a sentinel presentation of immunodeficiency | Inborn errors of immunity | Review-level orientation |

---

## Mechanistic Causal Chain (with evidence strength)

```
Inhaled arthroconidia (antiphagocytic wall)                     [STRONG: PMID 6300253]
        │  only 20–30% killed by PMNs; 30–80 µm spherules exceed phagocytosis
        ▼
Spherules resist killing + suppress macrophage NO/iNOS          [STRONG in vitro: 6300253, 21129481]
        │  → simple phagocytic clearance insufficient
        ▼
Adaptive Th1 (IL-12/IFN-γ/STAT4) + Th17 drive                   [STRONG: 28098554, 35149520, 21206087]
        │  (loss-of-function → dissemination in humans & mice)
        ▼
[INFERRED EDGE] IFN-γ primes macrophages → TNF/IL-1 →           [WEAK for Cocci: analogy only
 epithelioid differentiation + giant-cell fusion                 9306503, 7977642; NOT measured in Cocci]
        │  ── TNF maintenance required (anti-TNF → dissemination) [MODERATE: 33933122]
        ▼
[INFERRED EDGE] Organized granuloma (macrophage core,           [PARTIAL: composition supported
 T-cell corona, few fungi)                                       18852250, 20930107, 36891233;
        │                                                        organizing role of epithelioid cells inferred]
        ▼
CONTAINMENT  ── vs ──  PROGRESSION                               [SUPPORTED dichotomy: 18852250, 24321524]
   (organized granuloma)   (neutrophilic suppuration →
                            loss of granuloma → caseous
                            necrosis → cavitation/dissemination)

PARALLEL AXIS (not in seed model):                              [STRONG: 33106296, 42386736]
   Neutrophil recruitment + inflammasome/regulated cell death → tissue tolerance vs injury
REGULATORY ARM (not in seed model, comparator-derived):        [MODERATE: 24912188, 31094704]
   Treg balance + B-cell/ectopic lymphoid → contained vs injurious granuloma
```

**Where the literature is strong:** the anti-phagocytic premise; the requirement for Th1/Th17/TNF; the clinical containment-vs-cavitation dichotomy.
**Where links are inferred:** the two flagged edges (Th1/Th17→epithelioid transformation; epithelioid→organized granuloma) rest on TB/other-granuloma analogy.
**Missing causal steps:** (a) direct demonstration that *Coccidioides* granuloma macrophages undergo the epithelioid/giant-cell program under these signals; (b) that the giant-cell/epithelioid compartment *causally* maintains organization (vs being a bystander marker); (c) the identity and role of the interior microenvironment (hypoxia, metabolism, cell death).

---

## Knowledge Gaps

| Gap | Scope | Why it matters | What was checked | What would resolve it |
|---|---|---|---|---|
| **G1. Th1/Th17 → epithelioid transformation edge unmeasured in Coccidioides** | Core inferred edge | Central to the module's conformance; currently borrowed from TB | PubMed cocci + epithelioid/giant-cell/IFN-γ; only non-cocci mechanistic papers found (9306503, 7977642) | Spatial/scRNA-seq of cocci granulomas correlating macrophage state with local Th1/Th17 cytokine niches; cytokine-KO effect on epithelioid fraction |
| **G2. Epithelioid → organized-granuloma maintenance edge causally untested** | Core inferred edge | Distinguishes "marker" from "driver" | No cocci perturbation of macrophage differentiation found | Conditional macrophage-differentiation perturbation in mouse cocci model; longitudinal architecture readout |
| **G3. Granuloma interior microenvironment uncharacterized in Coccidioides** | Interior niche | The seed hypothesis names it explicitly as unresolved (PMID 33262956) | Found only NO-suppression in vitro (21129481) and inflammasome/cell-death (42386736) | Spatial metabolomics/hypoxia probes + Visium (GSE274767) on contained vs necrotic lesions |
| **G4. Neutrophil/inflammasome vs macrophage-program contribution not partitioned** | Competing axis | KO data show neutrophils/caspase-1 can be *harmful*; seed model is macrophage-centric | 33106296, 42386736 found | Cell-type-specific depletion timed to granuloma phases; compare containment metrics |
| **G5. No Treg/B-cell node for Coccidioides granuloma** | Missing maintenance nodes | Comparator diseases show these govern outcome | CBD comparator found (24912188, 31094704); no cocci-specific data located | Treg depletion/expansion and B-cell depletion in mouse cocci granuloma model |
| **G6. Matched omics datasets not yet edge-resolving in primary literature** | Dataset absence | GSE274766/GSE274767 are the right instruments but analyses answering the cell-identity/spatial edges not captured | Searched cocci scRNA-seq/spatial; found dataset papers (PMID 39611685, 40704794) but abstracts truncated; edge-level conclusions not retrievable here | Direct reanalysis of GSE274766/GSE274767 for macrophage-state × spatial organization × outcome |
| **G7. TNF mechanism of action in maintenance unproven for Coccidioides** | Treatment/biomarker MoA | Anti-TNF clearly raises dissemination risk, but whether via giant-cell maintenance vs macrophage activation is unknown | 33933122 (clinical) found; no mechanistic cocci study | Anti-TNF timing experiments in mouse cocci granuloma with architecture + fungal-burden readouts |
| **G8. Human genetic evidence is confined to extreme dissemination subtype** | Subtype scope | Th1-axis defects explain rare disseminators, not the common contained majority | 28098554, 30690602 found | Cohort immunophenotyping across contained vs progressive (non-Mendelian) patients |

---

## Alternative / Competing Models

1. **Neutrophil-immunopathology / inflammasome model** (*parallel + partly alternative*). Outcome is set by neutrophil recruitment and inflammasome-driven regulated cell death, not primarily by the macrophage epithelioid program. Supported by CXCR2-KO resistance and caspase-1-KO tolerance at equal burden (PMID 33106296, 42386736). Explains neutrophilic suppuration/caseation at the cavitary endpoint (PMID 24321524) more directly than a macrophage-centric model.
2. **Regulatory-balance model (Treg/B-cell)** (*complementary; missing node*). Containment vs injurious granuloma is governed by Teff/Treg ratio and B-cell/ectopic-lymphoid support, as in CBD (PMID 24912188, 31094704). Upstream/parallel to the seed model's "drive" emphasis.
3. **Adaptive-deficiency / host-genetics model** (*upstream cause*). Dissemination is a readout of specific host immune defects (IL-12/IFN-γ/STAT3/STAT4) (PMID 28098554, 35149520). This is the upstream trigger for the seed model's failure branch, not a competitor.
4. **Fungal-burden / spherule-rupture model** (*upstream driver*). Endospore release from ruptured spherules "taxes immunologic reserves" (PMID 6300253) and only ruptured spherules trigger IL-1β (PMID 42386736); disease may track burden/rupture kinetics rather than granuloma quality per se. Parallel to the seed model.
5. **Antigen-persistence chronicity model (Sarcoidosis comparator).** Shared `granuloma_formation` module framing where persistent antigen sustains chronic granuloma; relevant as a comparator but transcriptomically distinct (PMID 33276795).

---

## Discriminating Tests

1. **Spatial multi-omics of contained vs necrotic human/mouse cocci lesions** (Visium GSE274767 + scRNA-seq GSE274766, plus new samples). *Stratify:* organized granuloma vs neutrophilic/caseous lesion. *Readout:* macrophage epithelioid/giant-cell signatures vs neutrophil/NET/inflammasome signatures mapped to spatial niches and local Th1/Th17 cytokines. *Expected if seed model:* epithelioid/giant-cell macrophage program spatially coupled to Th1/Th17 niches and to containment; *if competing model:* outcome tracks neutrophil/inflammasome burden independent of macrophage state. **Directly tests G1, G3, G4, G6.**
2. **Timed cell-type-specific depletion in mouse (C. posadasii).** Deplete/neutralize (a) TNF, (b) neutrophils/CXCR2, (c) caspase-1, (d) Tregs, at defined granuloma phases. *Readout:* granuloma architecture, fungal burden, dissemination. *Expected:* dissociates "drive/maintenance" (TNF) from "immunopathology" (neutrophil/inflammasome) and "regulation" (Treg). **Tests G2, G4, G5, G7.**
3. **Conditional macrophage-differentiation perturbation.** Block giant-cell fusion (e.g., DC-STAMP) or epithelioid programming and measure whether organized granuloma and containment are lost while burden held constant. **Directly tests the epithelioid→organized-granuloma edge (G2).**
4. **Human contained-vs-progressive cohort immunophenotyping** (non-Mendelian patients). Peripheral + lesional Th1/Th17/Treg profiling, TNF signaling, and (where tissue available) granuloma composition. *Expected if seed model:* progressive disease shows attenuated Th1/Th17/TNF and disorganized/neutrophilic lesions. **Tests G8.**

---

## Curation Leads (require curator verification)

**Candidate evidence references + snippets to verify (exact quotes):**
- PMID 6300253 — "Arthroconidia possess an antiphagocytic surface derived from the original hyphal outer wall layer. Only 20%-30% of arthroconidia or endospores that are ingested by PMNs are killed." → premise (anti-phagocytosis). **Supports.**
- PMID 21129481 — "spherule initials, suppressed NO production as well as iNOS mRNA expression by activated macrophages" → interior microenvironment / immune evasion. **Supports.**
- PMID 28098554 — "We identified 8 patients with disseminated coccidioidomycosis who had defects in the interleukin-12/interferon-γ and STAT3 axes, indicating that these are critical host defense pathways." → Th1 edge. **Supports.**
- PMID 35149520 — "In the absence of STAT4, Th1 responses, critical for resistance to fungal disease, do not occur." → Th1 edge. **Supports.**
- PMID 21206087 — "vaccine-induced Th17 cells were necessary and sufficient to protect against the three major systemic mycoses in North America" / "Th17 cells engendered protection by recruiting and activating neutrophils and macrophages to the alveolar space" → Th17 edge + effector mechanism. **Supports.**
- PMID 33933122 — "…tumor necrosis factor alpha (TNF-α) inhibitors have increased risk of disseminated coccidioidomycosis" → TNF-maintenance edge. **Supports.**
- PMID 18852250 — "Resistant Swiss-Webster mice developed prominent perivascular/peribronchiolar lymphocytic cuffing and well-formed granulomas with few fungal elements…surrounded by a mantle of macrophages, lymphocytes, and fibrocytes." → composition/containment. **Supports.**
- PMID 20930107 — "T lymphocytes were more numerous than B lymphocytes and were distributed throughout the lesion with concentration in the periphery of granulomas" → cell identity/spatial. **Supports.**
- PMID 24321524 — "The cavity wall showed chronic inflammation and occasional giant cells but no granulomas…" / "the cavity lining showed neutrophils and caseous necrosis" → containment→cavitation dichotomy. **Supports.**
- PMID 33276795 — "Despite histologic similarities, DEGs and pathway enrichment markedly differed" → **Qualifies** TB analogy.
- PMID 33106296 — "The pathology of human coccidioidomycosis is granulomatous inflammation with many neutrophils surrounding ruptured spherules" → **Competing/parallel** (neutrophil axis).
- PMID 42386736 — "Caspase-1-deficient mice show improved disease tolerance to coccidioidomycosis despite equivalent fungal burdens, correlating with enhanced neutrophil extracellular trap formation in lung granulomas" → **Competing/parallel** (inflammasome/cell death).
- PMID 24912188 — "Depletion of Treg cells…exacerbated lung inflammation and enhanced granuloma formation." → **Competing/complementary** (missing Treg node; CBD comparator).
- PMID 31094704 — "B cell depletion was associated with a loss of lymphoid aggregates and granulomas as well as a significant increase in lung injury…" → **Competing/complementary** (missing B-cell node; CBD comparator).

**Candidate pathophysiology nodes/edges to add:**
- Node: *Neutrophil / NET* (HP:—; CL:0000775 neutrophil) in granuloma interior; Edge: `spherule_rupture → NLRP3/pyrin inflammasome → IL-1β/IL-18 → neutrophil recruitment` (PMID 42386736).
- Node: *Regulatory T cell* (CL:0000815) as granuloma-maintenance modulator; Edge: `Treg balance → contained vs injurious granuloma` (comparator-derived; PMID 24912188).
- Node: *B cell / ectopic lymphoid aggregate* (CL:0000236) as protective peripheral component (PMID 31094704).
- Edge annotation: `spherule anti-phagocytosis (SOWgp/outer wall) → obligate macrophage-transformation program` (PMID 6300253) — currently implicit premise; make explicit.
- Edge: `TNF → giant-cell/epithelioid granuloma maintenance` — supported clinically (PMID 33933122) but MoA UNCONFIRMED in Coccidioides (flag as knowledge_gap).

**Candidate ontology terms (cell types / processes):** epithelioid macrophage (CL:0000878 activated macrophage / epithelioid), multinucleated giant cell (CL:0000647 osteoclast-like / foreign-body giant cell), GO:0002432 granuloma formation, GO:0002697 regulation of immune effector process, GO:0070269 pyroptosis, GO:1990266 neutrophil migration.

**Candidate status/subtype notes:**
- **Retain EMERGING.** The two flagged edges remain PARTIAL; promotion to CANONICAL is not justified until G1/G2 are measured in *Coccidioides*.
- **Subtype restriction lead:** human genetic support is specific to the **disseminated** subtype (IL-12/IFN-γ/STAT3/STAT4); do not generalize the Th1-defect evidence to common contained infection.

**Candidate `knowledge_gaps` / discussion prompts:** G1–G8 above, especially:
- *Unconfirmed edge:* "Th1/Th17 → epithelioid transformation" has **no direct Coccidioides measurement** (only TB analogy) — flag for perturbation/longitudinal evidence.
- *Conflicting-evidence prompt:* neutrophils are protective in Th17 vaccine models (PMID 21206087) yet harmful in CXCR2/caspase-1 loss (PMID 33106296, 42386736) — reconcile as phase/context-dependent.
- *Dataset absence:* as of search date, edge-resolving analyses of GSE274766/GSE274767 answering the cell-identity/spatial-organization edges were not retrievable in the indexed primary literature.

---

## Limitations of this search

- Reliance on abstract-level text; several directly relevant dataset papers (PMID 39611685, 40704794) returned truncated abstracts, so their edge-level conclusions could not be fully extracted.
- No hands-on reanalysis of GSE274766/GSE274767 was performed (no data files provided).
- Comparator-disease (CBD/sarcoidosis) evidence is transferred by analogy and is itself subject to the etiology-specificity caveat (PMID 33276795).
- Single-case and small-N human evidence for the TNF and genetic edges.

---

## Bottom line

The coccidioidal granuloma composition/containment model is **partially supported**: its premise (anti-phagocytic spherule), its drive signals (Th1/Th17/TNF), and its clinical containment-vs-cavitation dichotomy are each backed by direct evidence, but the **Coccidioides-specific intermediate edges** (Th1/Th17→epithelioid transformation→organized granuloma) remain **inferred by analogy to tuberculosis and unmeasured**, and a **neutrophil/inflammasome axis plus Treg/B-cell regulation** compete to explain outcome. EMERGING is the correct status; the matched scRNA-seq/spatial datasets are the most direct route to resolution.


## Artifacts

- [OpenScientist final report](openscientist_artifacts/final_report.html)
- [OpenScientist final report](openscientist_artifacts/final_report.pdf)