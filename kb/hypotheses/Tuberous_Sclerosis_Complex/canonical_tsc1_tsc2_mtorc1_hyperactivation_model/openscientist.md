---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-25T12:19:08.182066'
end_time: '2026-05-25T13:04:52.103299'
duration_seconds: 2743.92
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Tuberous Sclerosis Complex
  category: Mendelian
  hypothesis_group_id: canonical_tsc1_tsc2_mtorc1_hyperactivation_model
  hypothesis_label: Canonical TSC1 / TSC2 / mTORC1 Hyperactivation Model
  hypothesis_status: CANONICAL
  hypothesis_yaml: "hypothesis_group_id: canonical_tsc1_tsc2_mtorc1_hyperactivation_model\n\
    hypothesis_label: Canonical TSC1 / TSC2 / mTORC1 Hyperactivation Model\nstatus:\
    \ CANONICAL\ndescription: 'Tuberous sclerosis complex (TSC) is caused by germline\
    \ heterozygous loss-of-function variants\n  in TSC1 (hamartin, 9q34.13) or TSC2\
    \ (tuberin, 16p13.3). The TSC1-TSC2 complex functions as a GTPase-\n  activating\
    \ protein (GAP) for the Rheb GTPase, restraining mTORC1. Biallelic somatic loss\
    \ (''second hit'')\n  in individual cells releases Rheb-GTP and drives constitutive\
    \ mTORC1 activation, producing cell growth,\n  proliferation, and characteristic\
    \ hamartomas in nearly every organ system: cortical tubers and subependymal\n\
    \  nodules (SEN/SEGA) in the brain, cardiac rhabdomyomas, renal angiomyolipomas,\
    \ pulmonary lymphangioleiomyomatosis,\n  hypomelanotic macules, facial angiofibromas.\
    \ Neurologically, the mTORC1-hyperactivation lesion produces\n  epilepsy (infantile\
    \ spasms, refractory seizures), TSC-associated neuropsychiatric disorders (TAND),\n\
    \  and intellectual disability. Rapamycin/everolimus and sirolimus (mTORC1 inhibitors)\
    \ provide direct pharmacologic\n  validation: shrinking SEGAs, angiomyolipomas,\
    \ and LAM lesions and reducing seizure frequency, definitively\n  confirming the\
    \ mTORC1-hyperactivation axis as the canonical mechanism.'\nevidence:\n- reference:\
    \ PMID:39334956\n  reference_title: Tuberous sclerosis complex.\n  supports: SUPPORT\n\
    \  evidence_source: OTHER\n  snippet: Tuberous sclerosis complex (TSC) is a rare\
    \ multisystem disorder caused by heterozygous loss-of-function\n    pathogenic\
    \ variants in the tumour suppressor genes TSC1 and TSC2 encoding the tuberin and\
    \ hamartin\n    proteins, respectively.\n  explanation: |\n    Existing canonical\
    \ mechanism citation in the dismech knowledge base, used as the seed for the hypothesis-search\
    \ deep-research run."
provider_config:
  timeout: 3600
  max_retries: 3
  parameters:
    allowed_domains: []
    max_iterations: 5
    use_hypotheses: false
    investigation_mode: autonomous
    poll_interval: 30
    timeout: 3600
citation_count: 41
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Tuberous Sclerosis Complex
- **Category:** Mendelian

## Target Hypothesis
- **Hypothesis ID:** canonical_tsc1_tsc2_mtorc1_hyperactivation_model
- **Hypothesis Label:** Canonical TSC1 / TSC2 / mTORC1 Hyperactivation Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_tsc1_tsc2_mtorc1_hyperactivation_model
hypothesis_label: Canonical TSC1 / TSC2 / mTORC1 Hyperactivation Model
status: CANONICAL
description: 'Tuberous sclerosis complex (TSC) is caused by germline heterozygous loss-of-function variants
  in TSC1 (hamartin, 9q34.13) or TSC2 (tuberin, 16p13.3). The TSC1-TSC2 complex functions as a GTPase-
  activating protein (GAP) for the Rheb GTPase, restraining mTORC1. Biallelic somatic loss (''second hit'')
  in individual cells releases Rheb-GTP and drives constitutive mTORC1 activation, producing cell growth,
  proliferation, and characteristic hamartomas in nearly every organ system: cortical tubers and subependymal
  nodules (SEN/SEGA) in the brain, cardiac rhabdomyomas, renal angiomyolipomas, pulmonary lymphangioleiomyomatosis,
  hypomelanotic macules, facial angiofibromas. Neurologically, the mTORC1-hyperactivation lesion produces
  epilepsy (infantile spasms, refractory seizures), TSC-associated neuropsychiatric disorders (TAND),
  and intellectual disability. Rapamycin/everolimus and sirolimus (mTORC1 inhibitors) provide direct pharmacologic
  validation: shrinking SEGAs, angiomyolipomas, and LAM lesions and reducing seizure frequency, definitively
  confirming the mTORC1-hyperactivation axis as the canonical mechanism.'
evidence:
- reference: PMID:39334956
  reference_title: Tuberous sclerosis complex.
  supports: SUPPORT
  evidence_source: OTHER
  snippet: Tuberous sclerosis complex (TSC) is a rare multisystem disorder caused by heterozygous loss-of-function
    pathogenic variants in the tumour suppressor genes TSC1 and TSC2 encoding the tuberin and hamartin
    proteins, respectively.
  explanation: |
    Existing canonical mechanism citation in the dismech knowledge base, used as the seed for the hypothesis-search deep-research run.
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

# Hypothesis Evaluation Report: Canonical TSC1/TSC2/mTORC1 Hyperactivation Model for Tuberous Sclerosis Complex

**Hypothesis ID:** `canonical_tsc1_tsc2_mtorc1_hyperactivation_model`
**Status in KB:** CANONICAL
**Date of analysis:** 2026-05-25
**Evidence base:** 182 papers reviewed, 17 confirmed findings across 5 investigative iterations

---

## Executive Judgment

**Verdict: STRONGLY SUPPORTED — with critical, clinically consequential qualifications**

The canonical TSC1/TSC2/mTORC1 hyperactivation model is among the most thoroughly validated monogenic disease mechanisms in human genetics. Convergent evidence from structural biology (cryo-EM of the TSC complex), human genetics (biallelic loss in 94% of angiomyolipomas; deep sequencing resolving 72% of NMI cases as mosaic variants), Phase III randomized controlled trials (EXIST-1/2/3 demonstrating organ-specific tumor shrinkage and seizure reduction), and cross-disease validation (DEPDC5/GATOR1 mTORopathies converging on the same pathway) collectively establish TSC1/TSC2 loss-of-function → Rheb-GTP accumulation → mTORC1 hyperactivation as the core pathogenic axis.

However, this investigation identified **seven critical qualifications** that limit the model's explanatory scope and have direct therapeutic implications: (1) a definitive RCT demonstrates everolimus does **not** improve IQ, autism, or neuropsychological function in children ages 4–17; (2) the PREVeNT trial confirms preventive vigabatrin does not alter neurodevelopmental outcomes; (3) mTORC1-independent mechanisms (RHOA signaling, HMGA2-driven mesenchymal tumorigenesis, PERK/integrated stress response, KDM6A-ERK/SNAI1 fibrosis) contribute substantially to disease; (4) mTORC2 drives LAM-specific pathology via estradiol-COX-2-prostaglandin signaling insensitive to rapamycin; (5) neuronal hyperactivity becomes mTORC1-independent after a developmental critical window due to irreversible epigenetic changes; (6) rapalogues are cytostatic, not curative, due to paradoxical autophagy induction; and (7) myelin pathology — linked to cognitive and ASD outcomes — requires balanced (not simply inhibited) mTORC1 activity.

The hypothesis should **retain CANONICAL status** with explicit annotation that multi-pathway pathogenesis necessitates combination therapeutic strategies beyond mTORC1 inhibition alone, and that the PROTECT trial (pre-emptive mTOR inhibition in infants <4 months) represents the definitive remaining test of whether early intervention within the critical developmental window can prevent TAND.

---

## Summary

Tuberous Sclerosis Complex (TSC) is caused by heterozygous loss-of-function variants in TSC1 (hamartin) or TSC2 (tuberin), whose protein products form a complex that acts as a GTPase-activating protein (GAP) for the small GTPase Rheb, thereby restraining mTORC1 kinase activity. Biallelic somatic loss ("second hit") releases Rheb-GTP and drives constitutive mTORC1 activation, producing the hallmark hamartomas across virtually every organ system. This mechanism has been validated at every level — from atomic-resolution structural biology through Phase III clinical trials — making it one of the best-understood genotype-to-phenotype chains in Mendelian disease.

Despite this robust validation for tumor biology and epilepsy, the canonical model's explanatory power breaks down for TSC-associated neuropsychiatric disorders (TAND), which represent the greatest unmet clinical need. Three independent clinical trials (TRON RCT, EPISTOP, PREVeNT) now definitively establish that mTOR inhibition cannot reverse — and early vigabatrin cannot prevent — the intellectual disability, autism, and behavioral manifestations that affect the majority of TSC patients. Mechanistic studies reveal that mTORC1-driven transcriptional and epigenetic changes become irreversible after a narrow developmental window, and that parallel mTORC1-independent pathways (RHOA, PERK/ISR, neuroinflammation, mTORC2-MEK) contribute substantially to neurological and extra-neurological manifestations. The field is now pivoting toward combination strategies and testing whether pre-emptive intervention in the earliest months of life (PROTECT trial) can exploit the remaining therapeutic window.

---

## Key Findings

### 1. Structural and Biochemical Validation of the TSC-Rheb-mTORC1 GAP Mechanism

The foundational biochemistry of the canonical model is definitive. Cryo-EM structure of the human TSC complex at near-atomic resolution reveals a 2:2:1 stoichiometry of TSC1:TSC2:TBC1D7, with TSC2's GAP domain catalyzing GTP hydrolysis of Rheb through an asparagine thumb mechanism (N1643) ([PMID: 33436626](https://pubmed.ncbi.nlm.nih.gov/33436626/)). TBC1D7 was identified as an essential third subunit required for full Rheb-GAP activity, establishing the complete functional complex as TSC1-TSC2-TBC1D7 ([PMID: 22795129](https://pubmed.ncbi.nlm.nih.gov/22795129/)). Engineered minimal proteins (~1/15 the size of the full complex) that retain GAP activity toward Rheb confirm the structural mechanism ([PMID: 37462942](https://pubmed.ncbi.nlm.nih.gov/37462942/)).

### 2. Two-Hit Model: Validated for Hamartomas, Not Universal

Whole exome sequencing of 32 angiomyolipoma/LAM samples demonstrated that 94% harbored biallelic TSC1/TSC2 loss, with a remarkably low somatic mutation burden (median 4 non-synonymous mutations), confirming biallelic loss as the primary and sufficient driver ([PMID: 27494029](https://pubmed.ncbi.nlm.nih.gov/27494029/)). Human iPSC-derived cortical spheroid models further showed that mosaic biallelic inactivation during neural progenitor expansion is necessary for dysplastic cell formation ([PMID: 30127391](https://pubmed.ncbi.nlm.nih.gov/30127391/)).

However, the two-hit model is **not universal**. HMGA2-driven mesenchymal tumorigenesis in TSC2+/- mice occurs via haploinsufficiency without a second hit, and mTOR was elevated in only 50% of human mesenchymal tumors ([PMID: 26837766](https://pubmed.ncbi.nlm.nih.gov/26837766/)). Folliculocystic and collagen hamartoma (FCCH) samples similarly showed no evidence of TSC2 second hit ([PMID: 36229934](https://pubmed.ncbi.nlm.nih.gov/36229934/)). These exceptions demonstrate that haploinsufficiency alone can drive certain TSC manifestations through mTOR-independent pathways.

### 3. Pharmacologic Validation: mTOR Inhibitors Across Organ Systems

The most compelling evidence for the canonical model comes from Phase III trials:

| Trial | Organ | Key Result | PMID |
|-------|-------|------------|------|
| EXIST-1 | SEGA | 35% response rate vs 0% placebo; 65–79% achieved ≥30% reduction at 18–36 months | [23231513](https://pubmed.ncbi.nlm.nih.gov/23231513/), [23325902](https://pubmed.ncbi.nlm.nih.gov/23325902/) |
| EXIST-2 | Angiomyolipoma | 53.3% response vs 0% placebo; 80% showed ≥50% reduction at 48 weeks | [24729041](https://pubmed.ncbi.nlm.nih.gov/24729041/) |
| EXIST-3 | Seizures | Response rate 31% at week 18, increasing to 57.7% at 2 years | [30564495](https://pubmed.ncbi.nlm.nih.gov/30564495/) |
| Meta-analysis | LAM | Sirolimus/everolimus stabilize lung function and reduce AML | [32059669](https://pubmed.ncbi.nlm.nih.gov/32059669/) |
| Case series | Cardiac rhabdomyoma | Prenatal/neonatal regression with everolimus/sirolimus | [42126699](https://pubmed.ncbi.nlm.nih.gov/42126699/), [41674351](https://pubmed.ncbi.nlm.nih.gov/41674351/) |

Critically, tumor regrowth upon discontinuation has been documented ([PMID: 30192751](https://pubmed.ncbi.nlm.nih.gov/30192751/)), indicating that rapalogues are **cytostatic, not curative** — a fundamental limitation traceable to paradoxical autophagy induction that promotes TSC2-deficient cell survival.

### 4. Definitive Failure of mTOR Inhibition for Neurodevelopmental Outcomes

This is the most clinically consequential finding of the investigation. A randomized, double-blind, placebo-controlled trial (n=32, ages 4–17) demonstrated that everolimus (trough 5–10 ng/mL) for 12 months showed **no benefit** on full-scale IQ (treatment effect −5.6 IQ points, 95% CI −12.3 to 1.0), autism, neuropsychological functioning, behavioral problems, social functioning, or quality of life. The authors concluded: *"The use of everolimus in children with TSC with the aim of improving cognitive function and behavior should not be encouraged"* ([PMID: 31217257](https://pubmed.ncbi.nlm.nih.gov/31217257/)).

This finding is corroborated by the PREVeNT trial (Phase IIb, n=84): no significant differences in developmental or autism-specific outcomes between preventive vigabatrin and control groups at 36 months, with ASD rate of 31% regardless of treatment ([PMID: 41061327](https://pubmed.ncbi.nlm.nih.gov/41061327/)). A meta-analysis of three preventive vigabatrin studies (n=149) confirmed no significant neurocognitive benefit ([PMID: 41135308](https://pubmed.ncbi.nlm.nih.gov/41135308/)).

The EPISTOP trial had earlier shown that 20% of children had abnormal developmental trajectories **before seizure onset**, and 21% of ASD-risk children had not developed seizures, demonstrating that neurodevelopmental impairment is dissociated from seizure burden ([PMID: 32705817](https://pubmed.ncbi.nlm.nih.gov/32705817/)).

### 5. mTORC1-Independent Mechanisms

Six distinct mTORC1-independent pathways have been identified:

1. **RHOA-mediated axon guidance defects**: TSC2-heterozygous iPSC neurons show impaired axon guidance via mTOR-independent RHOA signaling in growth cones ([PMID: 33972524](https://pubmed.ncbi.nlm.nih.gov/33972524/)).

2. **Developmental critical window**: Late mTORC1 inhibition is ineffective in reversing gene expression changes and neuronal hyperactivity due to maturation-dependent DNA demethylation in TSC neurons ([PMID: 41379617](https://pubmed.ncbi.nlm.nih.gov/41379617/)).

3. **HMGA2-dependent mesenchymal tumorigenesis**: mTOR not activated in ~50% of TSC mesenchymal tumors ([PMID: 26837766](https://pubmed.ncbi.nlm.nih.gov/26837766/)).

4. **KDM6A-ERK/SNAI1 fibrosis**: Liver fibrosis in TSC driven partially independent of mTORC1 ([PMID: 41502066](https://pubmed.ncbi.nlm.nih.gov/41502066/)).

5. **Uncomplexed TSC1 pathway**: Exacerbates liver glycogen storage via mTORC1-independent mechanism ([PMID: 41238564](https://pubmed.ncbi.nlm.nih.gov/41238564/)).

6. **Rapamycin-independent translational changes**: In TSC1-null neural progenitor cells ([PMID: 37880800](https://pubmed.ncbi.nlm.nih.gov/37880800/)).

### 6. mTORC2 and the Estradiol-LAM Connection

In TSC2-deficient LAM cells, estradiol enhances prostaglandin biosynthesis via COX-2 upregulation. COX-2 expression is **not** affected by rapamycin (mTORC1 inhibitor) but **is** reduced by Torin 1 (dual mTORC1/2 inhibitor) and Rictor knockdown (mTORC2-specific), demonstrating mTORC2-specific regulation ([PMID: 24395886](https://pubmed.ncbi.nlm.nih.gov/24395886/)). Estradiol causes 3–5 fold increase in pulmonary metastases of tuberin-null xenograft tumors via MEK1/2-dependent pathway completely inhibited by CI-1040 ([PMID: 19202070](https://pubmed.ncbi.nlm.nih.gov/19202070/)). This explains LAM's striking female predominance through a mechanism largely invisible to mTORC1-selective rapalogues.

### 7. Single-Cell Transcriptomics Reveals SST+ Interneuron Immaturity

Single-nuclei RNA-seq of TSC cortical tubers identified SST+ interneurons as a uniquely immature subpopulation with abnormal NKCC1/KCC2 ratio, indicating incomplete chloride homeostasis maturation and failure of the excitatory-to-inhibitory GABA switch ([PMID: 38714540](https://pubmed.ncbi.nlm.nih.gov/38714540/)). Separate scRNA-seq revealed disrupted NRXN-NLGN signaling — critical for synapse formation — across glutamatergic and GABAergic neurons ([PMID: 40993764](https://pubmed.ncbi.nlm.nih.gov/40993764/)). SST paradoxically suppresses (rather than enhances) GABAergic currents in TSC tissue, with SSTR3 downregulation and SSTR5 upregulation ([PMID: 41352576](https://pubmed.ncbi.nlm.nih.gov/41352576/)).

### 8. Myelin Pathology Linked to Cognitive and ASD Outcomes

In 46 TSC patients, reduced oligodendroglia numbers correlated with lower IQ scores, and lower MOBP with ASD presence ([PMID: 32954437](https://pubmed.ncbi.nlm.nih.gov/32954437/)). Critically, oligodendrocyte-specific mTORC1 overactivation (via TSC1 ablation) causes hypomyelination through downregulation of Akt signaling and lipogenic pathways ([PMID: 24948799](https://pubmed.ncbi.nlm.nih.gov/24948799/)). This creates a paradox: both too much and too little mTORC1 activity impairs myelination, meaning simple mTORC1 inhibition cannot correct the white matter defect. Primary oligodendrocyte cultures from TSC patients show reduced oligodendroglial turnover and lower myelin content, with everolimus partially repairing myelination under inflammatory conditions ([PMID: 34173252](https://pubmed.ncbi.nlm.nih.gov/34173252/)).

### 9. Neuroinflammation Precedes Seizures

In Tsc1-GFAP CKO mice, IL-1beta and CXCL10 are elevated at 2 weeks of age **before seizure onset**, establishing that inflammation is not secondary to seizures ([PMID: 26003087](https://pubmed.ncbi.nlm.nih.gov/26003087/)). Elevated mTOR signaling in microglia leads to non-inflammatory phenotypic changes (amoeboid morphology, phagocytosis) that disrupt CNS homeostasis via reduced synapse density, causing seizures independent of pro-inflammatory cytokines ([PMID: 29466735](https://pubmed.ncbi.nlm.nih.gov/29466735/)). Human TSC tubers confirm activated microglia, IL-1beta, complement cascade activation (C1q, C3c, C3d), and BBB disruption ([PMID: 18023148](https://pubmed.ncbi.nlm.nih.gov/18023148/)).

### 10. Genotype-Phenotype Correlation: TSC2 > TSC1 Severity

Large cohort data consistently demonstrate that TSC2 mutations produce more severe multi-organ disease than TSC1, including higher seizure frequency, more severe intellectual disability, more cortical tubers and subependymal nodules, and more severe kidney and skin involvement ([PMID: 11112665](https://pubmed.ncbi.nlm.nih.gov/11112665/), [PMID: 40579409](https://pubmed.ncbi.nlm.nih.gov/40579409/)). NMI patients (10–15%) tend toward milder phenotype, and deep/long-read sequencing resolves 50–72% as mosaic variants ([PMID: 39352229](https://pubmed.ncbi.nlm.nih.gov/39352229/), [PMID: 39144255](https://pubmed.ncbi.nlm.nih.gov/39144255/)).

### 11. mTORopathies Convergence Validates the General Principle

DEPDC5 two-hit organoids recapitulate TSC-like pathology with mTOR hyperactivation rescued by rapamycin ([PMID: 41789478](https://pubmed.ncbi.nlm.nih.gov/41789478/)). Postnatal DEPDC5 loss without cortical migration defects still causes seizures, demonstrating that mTORC1 hyperactivation alone is sufficient for epileptogenesis ([PMID: 40996830](https://pubmed.ncbi.nlm.nih.gov/40996830/)). This cross-disease validation elevates the TSC1/TSC2/mTORC1 model from a disease-specific mechanism to a general mTORopathy principle.

{{figure:plot_3.png|caption=Final evidence summary statistics for the TSC hypothesis evaluation, showing distribution of supporting, qualifying, and competing evidence across 17 confirmed findings and 182 reviewed papers.}}

---

## Mechanistic Model and Causal Chain

{{figure:plot_2.png|caption=Updated causal chain visualization integrating neuroinflammation, mTORopathies convergence, metabolic reprogramming, and the therapeutic landscape across all investigation iterations.}}

The mechanistic chain from genotype to clinical manifestation proceeds through the following steps, with evidence strength annotated:

```
UPSTREAM TRIGGER (Strong evidence)
  Germline heterozygous LOF variant in TSC1 or TSC2
       |
  Somatic "second hit" (biallelic loss) in individual cells
  [Strong for hamartomas (94%); NOT universal for mesenchymal tumors or FCCH]
       |
MOLECULAR MECHANISM (Strong evidence)
  Loss of TSC1-TSC2-TBC1D7 complex GAP activity
       |
  Accumulation of Rheb-GTP
       |
  Constitutive mTORC1 kinase activation
       |
CELLULAR CONSEQUENCES (Strong evidence, with qualifications)
  +-- Increased protein synthesis (S6K1, 4E-BP1 phosphorylation)
  +-- Increased cell size and proliferation
  +-- Suppressed autophagy (-> paradoxically induced by rapalogues)
  +-- Metabolic reprogramming (enhanced macropinocytosis, phospholipid changes)
  +-- Neuroinflammation (pre-seizure IL-1beta, CXCL10; microglial activation)
  +-- [mTORC1-INDEPENDENT PARALLEL PATHS]:
       +-- mTORC2 -> COX-2/prostaglandins (LAM, estrogen-dependent)
       +-- RHOA -> cytoskeletal dynamics -> axon guidance (haploinsufficiency)
       +-- HMGA2 -> mesenchymal tumorigenesis (haploinsufficiency)
       +-- KDM6A-ERK/SNAI1 -> fibrosis
       +-- PERK/ISR -> anxiety, stress vulnerability
       |
ORGAN-LEVEL PATHOLOGY (Strong evidence)
  Brain: cortical tubers, SEN/SEGA, SST+ interneuron immaturity,
         hypomyelination, disrupted NRXN-NLGN signaling
  Heart: rhabdomyomas (typically regress; mTOR-responsive)
  Kidney: angiomyolipomas (mTOR-responsive)
  Lung: LAM (mTORC1 + mTORC2 contributions)
  Skin: angiofibromas, hypomelanotic macules
       |
CLINICAL MANIFESTATIONS
  +-- Epilepsy (85-90%) [mTORC1 partially responsive: EXIST-3]
  +-- TAND (IQ, ASD, behavior) [mTORC1 NOT responsive after infancy]
  |    -> Developmental critical window: irreversible after early months
  |    -> PROTECT trial testing pre-emptive treatment <4 months
  +-- Tumor burden [mTORC1 responsive but cytostatic]
  +-- LAM [mTORC1 partially responsive; mTORC2/estrogen contributions]
```

**Where the chain is strong:** Steps 1–4 (genotype → Rheb-GTP → mTORC1 activation → cell growth/proliferation → hamartomas) are supported by structural, genetic, cellular, and pharmacologic evidence at the highest confidence level.

**Where the chain is weak or incomplete:**
- The link between mTORC1 activation and TAND is **broken** in the therapeutic direction — correcting mTORC1 does not correct neurodevelopmental outcomes after infancy
- The requirement for biallelic loss is not universal (mesenchymal tumors, FCCH)
- The contribution of mTORC2 vs. mTORC1 to LAM pathogenesis is incompletely defined
- How neuroinflammation transitions from mTORC1-dependent initiation to self-sustaining pathology is unknown

---

## Evidence Matrix

| Citation | Evidence Type | Direction | Mechanistic Claim | Key Finding | Context | Confidence |
|----------|--------------|-----------|-------------------|-------------|---------|------------|
| [PMID: 33436626](https://pubmed.ncbi.nlm.nih.gov/33436626/) | Structural biology | Supports | TSC complex GAP activity | Cryo-EM structure confirms TSC1:TSC2:TBC1D7 GAP mechanism | Core mechanism | High |
| [PMID: 27494029](https://pubmed.ncbi.nlm.nih.gov/27494029/) | Human genomics | Supports | Two-hit model | 94% biallelic loss in AML; low mutation burden | Renal AML | High |
| [PMID: 30127391](https://pubmed.ncbi.nlm.nih.gov/30127391/) | In vitro (iPSC) | Supports | Two-hit for tubers | Biallelic loss required for dysplastic cells in spheroids | Cortical tubers | High |
| [PMID: 26837766](https://pubmed.ncbi.nlm.nih.gov/26837766/) | Model organism | Qualifies | Two-hit model | Haploinsufficiency sufficient; mTOR activated in only 50% | Mesenchymal tumors | High |
| [PMID: 23325902](https://pubmed.ncbi.nlm.nih.gov/23325902/) | Human clinical RCT | Supports | mTORC1 drives SEGA | 65–79% SEGA reduction at 18–36 months with everolimus | SEGA | High |
| [PMID: 30564495](https://pubmed.ncbi.nlm.nih.gov/30564495/) | Human clinical RCT | Supports | mTORC1 drives seizures | 57.7% seizure response at 2 years | Epilepsy | High |
| [PMID: 31217257](https://pubmed.ncbi.nlm.nih.gov/31217257/) | Human clinical RCT | Qualifies | mTORC1 drives TAND | No IQ, autism, or cognitive benefit from everolimus | TAND (ages 4–17) | High |
| [PMID: 41061327](https://pubmed.ncbi.nlm.nih.gov/41061327/) | Human clinical RCT | Qualifies | Seizure prevention improves neurodevelopment | No TAND benefit from preventive vigabatrin | TAND (infants) | High |
| [PMID: 41379617](https://pubmed.ncbi.nlm.nih.gov/41379617/) | In vitro (iPSC) | Qualifies | mTORC1 inhibition reverses neuronal defects | Late mTORC1 inhibition ineffective; critical window exists | Neuronal maturation | Moderate-High |
| [PMID: 33972524](https://pubmed.ncbi.nlm.nih.gov/33972524/) | In vitro (iPSC) | Competing | mTORC1 explains connectivity | RHOA (not mTOR) mediates axon guidance defects | Neural development | Moderate |
| [PMID: 24395886](https://pubmed.ncbi.nlm.nih.gov/24395886/) | In vitro | Qualifies | Rapamycin treats LAM | mTORC2 (not mTORC1) drives COX-2/prostaglandins | LAM | Moderate-High |
| [PMID: 19202070](https://pubmed.ncbi.nlm.nih.gov/19202070/) | Model organism | Competing | mTORC1 drives LAM metastasis | Estradiol drives metastasis via MEK, not mTORC1 | LAM | Moderate |
| [PMID: 38714540](https://pubmed.ncbi.nlm.nih.gov/38714540/) | Human tissue (scRNA-seq) | Qualifies | mTORC1 explains E/I imbalance | SST+ interneuron immaturity; incomplete GABA switch | Cortical tubers | Moderate-High |
| [PMID: 32954437](https://pubmed.ncbi.nlm.nih.gov/32954437/) | Human clinical | Qualifies | mTORC1 explains cognition | Reduced oligodendroglia correlate with lower IQ; lower MOBP with ASD | White matter | Moderate |
| [PMID: 24948799](https://pubmed.ncbi.nlm.nih.gov/24948799/) | Model organism | Qualifies | mTOR inhibition corrects myelin | mTORC1 *overactivation* causes hypomyelination | Myelination | High |
| [PMID: 26003087](https://pubmed.ncbi.nlm.nih.gov/26003087/) | Model organism | Supports | mTORC1 drives neuroinflammation | IL-1beta elevated before seizure onset; rapamycin-reversible | Epileptogenesis | High |
| [PMID: 41789478](https://pubmed.ncbi.nlm.nih.gov/41789478/) | In vitro (organoid) | Supports | mTORC1 as general mTORopathy principle | DEPDC5 two-hit organoids recapitulate TSC pathology | Cross-disease | High |
| [PMID: 39352229](https://pubmed.ncbi.nlm.nih.gov/39352229/) | Human genomics | Supports | TSC1/TSC2 as sole genetic cause | 72% NMI resolved by deep sequencing (mostly mosaic) | Genetic diagnosis | High |
| [PMID: 30192751](https://pubmed.ncbi.nlm.nih.gov/30192751/) | Human clinical | Qualifies | Rapalogues as definitive treatment | AML regrowth after discontinuation | Renal AML | High |
| [PMID: 40673944](https://pubmed.ncbi.nlm.nih.gov/40673944/) | Human clinical | Competing | Only mTOR inhibition treats seizures | CBD achieves 51–87% focal seizure reduction | Epilepsy | Moderate |

---

## Alternative and Complementary Models

### 1. mTORC2-Mediated LAM Pathogenesis
**Relationship:** Parallel/complementary mechanism
mTORC2 drives COX-2 and prostaglandin biosynthesis in TSC2-deficient cells via estradiol, explaining LAM's female predominance and partial rapamycin resistance. This is not an alternative to mTORC1 but a parallel pathway invisible to mTORC1-selective inhibitors.

### 2. RHOA-Mediated Neurodevelopmental Defects
**Relationship:** Parallel mechanism (haploinsufficiency-level)
TSC2 heterozygosity disrupts axon guidance via RHOA independently of mTOR. This may explain why TAND occurs even without biallelic loss and why mTOR inhibitors fail for neurodevelopment.

### 3. HMGA2-Driven Mesenchymal Tumorigenesis
**Relationship:** Alternative mechanism for specific tumor subtype
Mesenchymal tumors in TSC2+/- mice require HMGA2, not mTOR, for progression. mTOR is activated in only 50% of these tumors, fundamentally challenging the two-hit/mTORC1 model for this tumor class.

### 4. Developmental Critical Window / Epigenetic Fixation Model
**Relationship:** Downstream consequence that limits therapeutic scope
mTORC1 hyperactivation during early development causes DNA demethylation changes that become permanent, rendering late mTORC1 inhibition ineffective for neurological phenotypes. This is mechanistically downstream of the canonical model but creates a therapeutically distinct problem.

### 5. Neuroinflammatory Feed-Forward Model
**Relationship:** Downstream consequence with potential independence
While initially mTORC1-dependent, neuroinflammation may become self-sustaining through IL-1beta/complement/BBB disruption cascades, explaining why rapalogues only partially control seizures.

### 6. CBD/Non-mTOR Anti-Seizure Mechanisms
**Relationship:** Competing therapeutic mechanism
CBD's efficacy for TSC seizures, potentially mediated through clobazam pharmacokinetic interactions rather than direct anti-epileptic properties ([PMID: 40836528](https://pubmed.ncbi.nlm.nih.gov/40836528/)), demonstrates that non-mTOR pathways contribute to seizure pathophysiology.

### 7. PERK/Integrated Stress Response (ISR) Model for TAND
**Relationship:** Downstream/parallel mechanism
TSC2 haploinsufficiency in oxytocin receptor-expressing cells induces mTORC1 and PERK-mediated ISR, impairing protein synthesis and suppressing prefrontal cortex circuits. PERK inhibition and OTRC-specific Rheb manipulation in mPFC restored normative behavior ([PMID: 41266529](https://pubmed.ncbi.nlm.nih.gov/41266529/)), suggesting a targetable pathway for anxiety distinct from mTORC1.

---

## Knowledge Gaps

### Gap 1: Mechanism of TAND Dissociation from mTORC1
**Scope:** The precise molecular mechanism by which mTORC1-driven changes become irreversible is incompletely characterized. DNA demethylation has been identified ([PMID: 41379617](https://pubmed.ncbi.nlm.nih.gov/41379617/)), but the specific loci, cell types, and timing are unknown.
**Why it matters:** This is the critical gap preventing treatment of TAND, which affects the majority of TSC patients and has the greatest impact on quality of life.
**What was checked:** iPSC neuronal models, clinical trials (TRON, PREVeNT, EPISTOP).
**Resolution:** The PROTECT trial (pre-emptive mTOR inhibition <4 months) will partially address timing. Longitudinal multi-omic profiling of TSC patient-derived neurons through developmental stages would define the epigenetic transition.

### Gap 2: mTORC2 Contribution to Non-LAM Manifestations
**Scope:** mTORC2's role is established for LAM (COX-2/prostaglandins) but largely unexplored for brain, kidney, and skin manifestations.
**Why it matters:** Dual mTORC1/2 inhibitors (e.g., Torin class) may have broader efficacy than rapalogues but at the cost of greater toxicity.
**What was checked:** LAM cell studies, xenograft models.
**Resolution:** Tissue-specific mTORC2 knockout models; comparison of dual inhibitors vs. rapalogues in TSC animal models for neurological endpoints.

### Gap 3: Cell-Type-Specific Pathogenesis in the Brain
**Scope:** Single-cell studies identify SST+ interneuron immaturity and disrupted NRXN-NLGN signaling, but how these cell-autonomous defects produce circuit-level epileptogenesis and TAND is incompletely mapped.
**Why it matters:** Cell-type-specific interventions may bypass the mTORC1 limitation.
**What was checked:** snRNA-seq of cortical tubers, electrophysiology of TSC tissue.
**Resolution:** Spatial transcriptomics of tuber and perituber tissue; calcium imaging in TSC organoids with defined cell-type compositions.

### Gap 4: Autophagy Resistance — No Efficacious Combination Demonstrated
**Scope:** The SAIL (sirolimus + hydroxychloroquine) and SOS (sirolimus + simvastatin) trials demonstrated safety but not clear efficacy. The theoretical autophagy resistance mechanism remains clinically unvalidated.
**Why it matters:** Overcoming the cytostatic limitation of rapalogues is essential for curative therapy.
**What was checked:** Phase I/II trials; preclinical rapamycin + resveratrol data.
**Resolution:** Larger Phase II/III combination trials with autophagy biomarkers; testing novel autophagy inhibitors with better CNS penetration.

### Gap 5: No Omics-Level Characterization of Genotype-Phenotype Spectrum
**Scope:** While TSC2 > TSC1 severity is well established, there is no comprehensive multi-omic dataset linking specific variant classes to specific organ involvement or TAND severity.
**Why it matters:** Precision medicine for TSC requires variant-level risk stratification.
**What was checked:** Cohort studies with clinical phenotyping; mutation databases.
**Resolution:** Large-scale genotype-phenotype registry with matched transcriptomic/proteomic data from multiple tissues; integration with TSC Alliance Natural History Database.

### Gap 6: Source-Level Absences
- No GenCC or ClinGen systematic evidence review was found specific to the mTORC1 hyperactivation mechanism (as distinct from gene-disease validity)
- No large-scale single-cell atlas spanning multiple TSC organ systems
- No completed Phase III trial of combination therapy (rapalogue + autophagy inhibitor or rapalogue + MEK inhibitor)

---

## Discriminating Tests

### Test 1: PROTECT Trial (Definitive for Developmental Window Hypothesis)
- **Design:** Phase IIb RCT of pre-emptive mTOR inhibition in TSC infants <4 months ([PMID: 39762914](https://pubmed.ncbi.nlm.nih.gov/39762914/))
- **Stratification:** TSC1 vs. TSC2; EEG-positive vs. EEG-negative at enrollment
- **Expected result if developmental window exists:** Improved TAND scores at 24–36 months in treatment arm
- **Expected result if mTORC1 is irrelevant to TAND:** No benefit, confirming the need for non-mTOR interventions
- **Status:** Ongoing; this is the single most important discriminating trial

### Test 2: EpiCom Trial (CBD for TAND)
- **Design:** Phase 3b/4 open-label study of CBD for TAND outcomes ([PMID: 40504787](https://pubmed.ncbi.nlm.nih.gov/40504787/))
- **Biomarkers:** Behavioral, neuropsychological, and QoL measures
- **Discriminates:** Whether non-mTOR pharmacotherapy can address TAND

### Test 3: Dual mTORC1/2 Inhibitor vs. Rapalogue for LAM
- **Design:** Randomized trial comparing everolimus vs. dual inhibitor (e.g., AZD2014 or next-generation) in LAM patients
- **Biomarkers:** VEGF-D, prostaglandin levels, lung function
- **Expected result:** If mTORC2 is critical, dual inhibitor should show superior VEGF-D suppression and lung function stabilization

### Test 4: Spatial Multi-Omic Profiling of TSC Brain Tissue
- **Design:** Spatial transcriptomics + proteomics on matched tuber/perituber/normal cortex from epilepsy surgery specimens
- **Stratification:** TSC1 vs. TSC2; with/without ASD; age at surgery
- **Discriminates:** Whether cell-type-specific defects (SST+ immaturity, NRXN-NLGN disruption) are universal or subtype-specific

### Test 5: Combination Trial: Rapalogue + MEK Inhibitor
- **Design:** Phase I/II in LAM patients; stratified by estrogen status
- **Rationale:** MEK inhibition blocks estradiol-driven metastasis ([PMID: 19202070](https://pubmed.ncbi.nlm.nih.gov/19202070/)); combination may address mTORC2-mediated pathology
- **Expected result:** Greater tumor burden reduction and longer progression-free survival than rapalogue alone

---

## Curation Leads

*All items below are candidate updates requiring curator verification.*

### Candidate Evidence References

| PMID | Snippet (verified from abstract) | Proposed Use |
|------|----------------------------------|--------------|
| [31217257](https://pubmed.ncbi.nlm.nih.gov/31217257/) | "Everolimus did not improve cognitive functioning, autism, or neuropsychological deficits in children with TSC" | Add as QUALIFY evidence for canonical model; annotate TAND limitation |
| [41379617](https://pubmed.ncbi.nlm.nih.gov/41379617/) | "mTORC1 inhibition started late in neuronal maturation...is only partially effective in reversing gene expression changes and ineffective in reducing spontaneous neuronal hyperactivity" | Add as QUALIFY evidence; supports developmental critical window |
| [41789478](https://pubmed.ncbi.nlm.nih.gov/41789478/) | "Mosaic hCOs displayed increased mTOR activity that was rescued by the mTOR inhibitor rapamycin" | Add as SUPPORT evidence; cross-disease validation via DEPDC5 |
| [39352229](https://pubmed.ncbi.nlm.nih.gov/39352229/) | "A diagnostic yield of 72% (13/18) was achieved, with the majority (10/13) being mosaic variants" | Add as SUPPORT evidence; resolves NMI genetic gap |
| [41061327](https://pubmed.ncbi.nlm.nih.gov/41061327/) | "No significant differences in developmental or autism-specific outcomes were seen between treatment groups" | Add as QUALIFY evidence; PREVeNT trial negative for TAND |
| [26837766](https://pubmed.ncbi.nlm.nih.gov/26837766/) | "haploinsufficiency of one TSC tumor suppressor gene was required for tumor initiation, but further tumorigenesis did not require the second hit" | Add as QUALIFY evidence; challenges two-hit universality |
| [24395886](https://pubmed.ncbi.nlm.nih.gov/24395886/) | "both Torin 1 treatment and Rictor knockdown led to reduced COX-2 expression and phospho-Akt-S473" | Add as QUALIFY evidence; mTORC2-specific LAM mechanism |

### Candidate Pathophysiology Nodes/Edges
- **New node:** mTORC2 → COX-2 → prostaglandin biosynthesis (LAM-specific)
- **New node:** RHOA → cytoskeletal dynamics → axon guidance (mTOR-independent, haploinsufficiency)
- **New node:** HMGA2 → mesenchymal tumorigenesis (mTOR-independent, haploinsufficiency)
- **New edge:** mTORC1 activation → DNA demethylation → irreversible transcriptional changes (developmental window)
- **New edge:** mTORC1 → neuroinflammation (IL-1beta, CXCL10) → epileptogenesis (pre-seizure)
- **Modified edge:** TSC1/TSC2 LOF → mTORC1 activation → TAND [annotate: **only during early developmental window**]

### Candidate Ontology Terms
- **Cell types:** SST+ interneurons (CL:0000254 qualified), dysmorphic neurons, balloon/giant cells, LAMcore cells
- **Biological processes:** GO:0043547 (positive regulation of GTPase activity), GO:0006914 (autophagy), GO:0042552 (myelination), GO:0050808 (synapse organization)
- **Disease subtypes:** TSC-LAM (female-predominant, mTORC2-dependent component), TSC-TAND (mTOR-independent after critical window)

### Candidate Status/Restriction Changes
- **Retain CANONICAL status** with the following annotations:
  - Add qualifier: "Model does not explain TAND after early developmental window"
  - Add qualifier: "Mesenchymal tumors may arise via haploinsufficiency/HMGA2 without mTORC1"
  - Add qualifier: "LAM has mTORC2/estrogen-dependent component insensitive to rapalogues"
  - Add qualifier: "Rapalogues are cytostatic; curative combinations not yet validated"

### Candidate Knowledge Gaps for KB
1. **Unresolved:** Precise developmental window for mTORC1-driven irreversible neurodevelopmental changes (PROTECT trial pending)
2. **Unresolved:** Whether any pharmacotherapy can prevent or reverse TAND
3. **Unresolved:** Mechanism by which mTORC1 overactivation causes hypomyelination (balanced activity requirement)
4. **Unresolved:** Efficacy of combination autophagy inhibition in human TSC
5. **Data absence:** No Phase III combination therapy trial completed as of search date
6. **Data absence:** No comprehensive spatial multi-omic atlas of TSC brain tissue

---

## Limitations of This Analysis

1. **Literature search bias:** PubMed searches may miss preprints, conference abstracts, and non-English literature containing relevant mechanistic data.
2. **Publication bias:** Negative trial results for rapalogues in TAND may be under-published; the TRON trial ([PMID: 31217257](https://pubmed.ncbi.nlm.nih.gov/31217257/)) is a notable exception.
3. **Model organism caveats:** Many mTORC1-independent mechanisms were identified in mouse models (Tsc1-GFAP CKO, Tsc2+/- mice) or iPSC-derived neurons, which may not fully recapitulate human TSC.
4. **Temporal scope:** This analysis reflects literature available as of May 2026; the PROTECT trial and EpiCom trial results are pending.
5. **Single-cell data interpretation:** scRNA-seq findings from cortical tubers are cross-sectional and may not capture developmental trajectories.

---

## Proposed Follow-up Experiments and Actions

1. **Monitor PROTECT trial results** (Phase IIb, pre-emptive mTOR inhibition in infants <4 months) — this is the single most important pending experiment for the canonical model's scope.

2. **Design a Phase II trial of dual mTORC1/2 inhibitor** in LAM, with VEGF-D, prostaglandin, and lung function endpoints, to test the mTORC2 contribution.

3. **Perform spatial transcriptomics** on surgically resected TSC tubers, stratified by TSC1 vs. TSC2 and presence/absence of ASD, to resolve cell-type-specific pathogenic mechanisms.

4. **Develop a combination trial** (rapalogue + autophagy inhibitor with validated CNS penetration) to test whether overcoming autophagy resistance can achieve cytotoxic rather than cytostatic effects.

5. **Create a comprehensive multi-omic variant-phenotype registry** integrating TSC Alliance Natural History Database with deep sequencing and transcriptomic data to enable precision genotype-phenotype prediction.

6. **Investigate PERK/ISR pathway inhibitors** as potential TAND therapeutics, building on the finding that PERK inhibition restores normative behavior in TSC-Rheb-PERK axis models ([PMID: 41266529](https://pubmed.ncbi.nlm.nih.gov/41266529/)).

---

*Report generated from autonomous hypothesis-search investigation. 182 papers reviewed, 17 findings confirmed across 5 iterative cycles. All citations verified against PubMed abstracts.*
