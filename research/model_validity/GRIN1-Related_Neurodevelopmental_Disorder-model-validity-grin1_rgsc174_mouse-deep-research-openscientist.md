---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-11-11T00:57:50.728572'
end_time: '2026-11-11T01:21:48.923655'
duration_seconds: 1438.2
template_file: templates/disease_model_validity_research.md
template_sha: "563ccd9ace418f34b50c9e525cc2a3c18b33ebb6"
template_variables:
  disease_name: GRIN1-Related Neurodevelopmental Disorder
  model: Grin1 Rgsc174 mouse
  mechanism_nodes: GRIN1 Variant and Altered GluN1/NMDA Receptor Function; NMDA Receptor
    Gain-of-Function; Gain-of-Function Cortical Maldevelopment; NMDA Receptor Loss-of-Function;
    Disrupted Excitatory Neurotransmission and E/I Imbalance; Impaired Neurodevelopment
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
    save_artifacts: true
    artifact_max_bytes: 5242880
citation_count: 11
reference_validation:
  total_references: 11
  verified: 11
  not_found: 0
  unverifiable: 0
  confabulation_rate: 0.0
  relevance_assessed: 11
  on_topic: 5
  validator_version: 0.5.1
term_validation:
  total_terms: 0
  verified: 0
  not_found: 0
  obsolete: 0
  unverifiable: 0
  confabulation_rate: 0.0
  adapter: 'ols:'
  validator_version: 0.4.5
artifact_count: 2
artifact_sources:
  openscientist_artifacts_zip: 2
artifacts:
- filename: final_report.html
  path: GRIN1-Related_Neurodevelopmental_Disorder-model-validity-grin1_rgsc174_mouse-deep-research-openscientist_artifacts/final_report.html
  media_type: text/html
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
- filename: final_report.pdf
  path: GRIN1-Related_Neurodevelopmental_Disorder-model-validity-grin1_rgsc174_mouse-deep-research-openscientist_artifacts/final_report.pdf
  media_type: application/pdf
  source: openscientist_artifacts_zip
  data_storage_id: null
  description: OpenScientist final report
---

## Question

# Animal Model Validity Research Template

## Target Question

- **Disease:** GRIN1-Related Neurodevelopmental Disorder
- **Model or paradigm:** Grin1 Rgsc174 mouse
- **Mechanism nodes in the knowledge base:** GRIN1 Variant and Altered GluN1/NMDA Receptor Function; NMDA Receptor Gain-of-Function; Gain-of-Function Cortical Maldevelopment; NMDA Receptor Loss-of-Function; Disrupted Excitatory Neurotransmission and E/I Imbalance; Impaired Neurodevelopment

## Research Objectives

A disease knowledge base records animal models of **GRIN1-Related Neurodevelopmental Disorder** and links each
one to the mechanism nodes it informs. **Grin1 Rgsc174 mouse** is widely used as a model of
GRIN1-Related Neurodevelopmental Disorder. Please determine **what Grin1 Rgsc174 mouse models of GRIN1-Related Neurodevelopmental Disorder, what it
does not, and where its validity is disputed.**

This report will be used to decide which mechanism nodes the model is linked to, how
faithful each link is, and which translational caveats must be recorded with it.
Evidence that the model is invalid or disputed is as useful as evidence that it is
valid. Report it with the same care.

Every claim MUST cite a primary-literature source by PMID (or DOI) and include a short
verbatim quote from the cited paper's abstract that contains the claim. Do not
paraphrase. Do not invent PMIDs. If a claim is supported only by full text, say so.

---

### 1. Face, construct and predictive validity

- What features of GRIN1-Related Neurodevelopmental Disorder does Grin1 Rgsc174 mouse reproduce, and by what readouts?
- What is the argument for construct validity (does the inducing manipulation
  resemble a cause of the human disease)?
- Predictive validity: which treatments effective in humans reverse the model's
  phenotype, on what time course, and which do not?

### 2. Disputes about validity

- Quote published critiques of Grin1 Rgsc174 mouse as a model of GRIN1-Related Neurodevelopmental Disorder, and say who
  makes them. Include critiques of the behavioral readouts the model relies on.
- Quote any argument that the model better resembles a different human disorder.

### 3. Individual differences

- If the model splits animals into vulnerable and resilient groups, is that split
  presented as a model of human vulnerability?
- What evidence directly connects the split to human data (postmortem tissue,
  transcriptomic comparison, peripheral biomarkers, genetics)? Distinguish findings
  tested in humans from findings that are only proposed to apply.

### 4. Mechanisms

- For each mechanism node listed above, report findings from Grin1 Rgsc174 mouse that bear on
  it, with the direction of the change.
- Report findings that do not fit any of those nodes, for example circuit-level or
  network findings.

### 5. Sex

- Was the model developed in one sex? What adaptations exist for the other sex, and
  how do their results compare?
- Does the literature state that this limits the model?

### 6. Assessment

- Summarize which aspects of GRIN1-Related Neurodevelopmental Disorder the model is a good, partial, or poor
  model of.
- List the caveats a curator should attach to any link between Grin1 Rgsc174 mouse and a
  mechanism of GRIN1-Related Neurodevelopmental Disorder.


## Output

# Animal Model Validity Report: *Grin1^Rgsc174^* Mouse as a Model of GRIN1-Related Neurodevelopmental Disorder

## Summary

**The *Grin1^Rgsc174^* mouse is a poor, repurposed model of GRIN1-Related Neurodevelopmental Disorder (GRIN1-NDD).** It is a RIKEN ENU-mutagenesis allele isolated from a *behavioral screen for hyperlocomotion*, not from a human GRIN1-NDD patient. The mutation is an arginine→cysteine (R→C) substitution in the **intracellular C0 domain** of GluN1 — a region that mediates GluN1–αCaMKII coupling and receptor trafficking, *not* channel gating or pore function. This is mechanistically distinct from the locations where pathogenic human GRIN1-NDD variants cluster (the M2 re-entrant pore loop and other transmembrane gating elements). Its creators and independent reviewers explicitly classify it as a partial model of **ADHD, schizophrenia, and bipolar disorder**, not of GRIN1-NDD ([PMID: 23688147](https://pubmed.ncbi.nlm.nih.gov/23688147/), [PMID: 32798374](https://pubmed.ncbi.nlm.nih.gov/32798374/)).

A critical correction occurred during this investigation and must be stated plainly for curation purposes. Early iterations conflated "Grin1 Rgsc174" with a *different* allele — the **Grin1 Y647S/+ CRISPR knock-in** ([PMID: 39229143](https://pubmed.ncbi.nlm.nih.gov/39229143/)), which *is* a patient-derived GRIN1-NDD model with high construct validity (seizures, intellectual disability, NMDAR hypofunction). That is **not** the Rgsc174 line. The Y647S findings are retained below in a clearly flagged section because they are informative about GRIN1-NDD modeling in general and may be what a curator is actually seeking, but **they must not be attributed to Rgsc174.** The true Rgsc174 allele reproduces *none* of the core features of GRIN1-NDD (no reported epilepsy, intellectual disability, or hypotonia); it instead produces a psychiatric-endophenotype profile (hyperactivity, novelty-seeking, fear-memory deficits, decreased acoustic startle with intact prepulse inhibition, immature dentate gyrus).

For knowledge-base curation, *Grin1^Rgsc174^* should be linked — if at all — only to the **NMDA Receptor Loss-of-Function** node, and even then with heavy caveats: the link rests on gene identity (Grin1/GluN1) and a glutamate–dopamine hypofunction mechanism, not on faithful reproduction of GRIN1-NDD pathophysiology. It must **not** be linked to any gain-of-function node. Its only human-tissue anchor (an immature-dentate-gyrus endophenotype) points to schizophrenia/bipolar disorder, not GRIN1-NDD, and its behavioral characterization was performed in males only.

---

## Key Findings

### The identity of the Rgsc174 allele (central correction)

The decisive finding of this investigation is that **Grin1^Rgsc174^ is an ENU-induced behavioral-screen mutant, not a human patient variant.** Grin1(Rgsc174) was isolated in the RIKEN ENU-mutagenesis project from behavioral mutant line M100174, which had been flagged in a screen for *increased spontaneous locomotor activity*. The causal lesion is a missense mutation producing an arginine→cysteine substitution in the intracellular C0 domain of the GluN1 subunit. The original report states: *"We identified a missense mutation in the Grin1 gene, which encodes NMDA receptor subunit 1, and designated the mutant gene Grin1(Rgsc174). This mutation results in an arginine to cysteine substitution in the C0 domain of the protein"* and that it derived from the *"isolated behavioral mutant M100174, which exhibited a significant increase in spontaneous locomotor activity"* ([PMID: 20345915](https://pubmed.ncbi.nlm.nih.gov/20345915/)). This origin — forward genetics from a hyperactivity phenotype rather than reverse engineering of a patient's variant — fundamentally shapes its validity profile.

### Construct validity is poor: the variant is in the wrong part of the receptor

Pathogenic human GRIN1-NDD variants concentrate in the channel machinery. Li et al. reported 18 patients harboring 12 de novo missense variants in GRIN1/GRIN2A/GRIN2B that *"alter residues in the M2 re-entrant loop, a region that lines the pore and is intolerant to missense variation"* ([PMID: 31429998](https://pubmed.ncbi.nlm.nih.gov/31429998/)). By contrast, the Rgsc174 lesion is an *"arginine to cysteine substitution in the C0 domain"* — an intracellular, cytoplasmic region that couples GluN1 to αCaMKII and governs signaling and trafficking rather than ion permeation or gating ([PMID: 20345915](https://pubmed.ncbi.nlm.nih.gov/20345915/)). The spatial mismatch between where Rgsc174 sits (intracellular C0) and where disease variants cluster (transmembrane pore) is the single clearest argument against construct validity for GRIN1-NDD.

### Face validity for GRIN1-NDD is poor; the profile is psychiatric

A comprehensive behavioral battery characterized Rgsc174/+ heterozygotes with a profile unlike GRIN1-NDD. Furuse et al. noted the line is distinct from other Grin1 mutants: *"In contrast to other Grin1 mutant mice, this mutant exhibited no evidence of heightened anxiety"* ([PMID: 20345915](https://pubmed.ncbi.nlm.nih.gov/20345915/)). Umemori et al. reported that *"Both contextual and cued fear memory were severely deficient in the fear conditioning test"* and that *"The startle amplitude was markedly decreased in Grin1(Rgsc174)/Grin1+ mice, whereas no significant differences between genotypes were detected in the prepulse inhibition (PPI) test"* ([PMID: 23688147](https://pubmed.ncbi.nlm.nih.gov/23688147/)). The core readouts are therefore hyperactivity, fear-memory loss, and decreased acoustic startle with intact PPI — a psychiatric-endophenotype pattern. Crucially, the hallmark features of GRIN1-NDD — spontaneous seizures, intellectual disability, and hypotonia — are not reported in this line.

### The model's creators frame it as ADHD/schizophrenia/bipolar, not GRIN1-NDD

The authors are explicit about the intended disease context. Umemori et al. state the gene's framing: *"Grin1 is a candidate susceptibility gene for neuropsychiatric disorders, including schizophrenia, bipolar disorder, and attention deficit/hyperactivity disorder (ADHD)"* and conclude that *"Although Grin1(Rgsc174)/Grin1+ mice only partially recapitulate symptoms of patients with ADHD, schizophrenia, and bipolar disorder, they may serve as a unique animal model of a certain subpopulation of patients with these disorders"* ([PMID: 23688147](https://pubmed.ncbi.nlm.nih.gov/23688147/)). GRIN1-NDD is not mentioned as the target disorder.

### Independent corroboration of the differential-disorder placement

A separate group's review catalogues the line among schizophrenia models. Ang et al., *Behavioral Tasks Evaluating Schizophrenia-like Symptoms in Animal Models* ([PMID: 32798374](https://pubmed.ncbi.nlm.nih.gov/32798374/)), lists Grin1(Rgsc174)/Grin1+ alongside other schizophrenia models (e.g., GCLM-KO, DBA/2J, PTPRG-KO). This independent classification (in the review's full text) confirms the field treats Rgsc174 as a schizophrenia-spectrum model rather than a GRIN1-NDD model.

### Mechanism in Rgsc174: NMDAR hypofunction via glutamate–dopamine and CaMKII signaling

The mechanistic data point to loss-of-function (hypofunction). Furuse et al. report that *"impaired interaction between the glutamatergic pathway and dopaminergic pathway may underlie the behavioral phenotypes of the Grin1(Rgsc174) mutant"* ([PMID: 20345915](https://pubmed.ncbi.nlm.nih.gov/20345915/)). Full-text work localizes the lesion mechanistically: *"Grin1 binds to αCaMKII through the C0 domain"* ([PMID: 23688147](https://pubmed.ncbi.nlm.nih.gov/23688147/)), placing the Rgsc174 defect at the GluN1–CaMKII signaling/trafficking interface rather than at channel gating. This supports a loss-of-function assignment but through an indirect, signaling-level route.

### Individual differences: a social-rank split not tied to human data

The line shows a vulnerable/resilient-style split along social dominance, but it is not anchored to human vulnerability data. Ujita et al. report that *"Grin1Rgsc174/+ mice exhibited social subordination characterised by decreased corner visit frequency and occupancy time at the beginning of the task"* ([PMID: 29150978](https://pubmed.ncbi.nlm.nih.gov/29150978/)), indicating Grin1 influences competitive social dominance. This social-rank split is a behavioral-ecology finding and is **not** connected to human GRIN1-NDD postmortem, transcriptomic, biomarker, or genetic data.

### The only human-tissue anchor points to schizophrenia/bipolar, not GRIN1-NDD

The strongest cross-species link for Rgsc174 is an **immature dentate gyrus (iDG)** phenotype (upregulated *Drd1a*, downregulated desmoplakin/*Tdo2*). The authors explicitly tie this to psychiatric postmortem tissue: *"iDG-like phenotypes have been found in the hippocampi of postmortem brains in human schizophrenia/bipolar patients, indicating that iDG represents a candidate endophenotype for the etiology of these diseases"* ([PMID: 23688147](https://pubmed.ncbi.nlm.nih.gov/23688147/)). This is the only direct human-tissue connection, and it directs the model toward schizophrenia/bipolar disorder, reinforcing the differential-disorder concern.

### Sex: male-only characterization

The behavioral phenotyping was conducted exclusively in males. Full text of Umemori et al. states *"All behavioral tests were carried out with male mice that were at least 10 weeks old"* ([PMID: 23688147](https://pubmed.ncbi.nlm.nih.gov/23688147/)). No female cohort was characterized for the core behavioral profile, so sex-generalizability is unknown — a limitation a curator should record.

---

## Flagged — DO NOT attribute to Rgsc174: the Grin1 Y647S/+ knock-in

During early iterations, "Grin1 Rgsc174" was mistakenly equated with the **Grin1 Y647S/+ CRISPR knock-in**, a genuinely patient-derived GRIN1-NDD model. These are **different alleles** (Y647S is in the M3 helix / transmembrane domain; Rgsc174 is R→C in the intracellular C0 domain). The following Y647S findings are retained for completeness and because they may describe the model a curator actually intends — but they belong to Y647S, **not** Rgsc174.

- **High construct validity (Y647S):** *"The identified p.Tyr647Ser (Y647S) variant - carried by a 33-year-old female with seizures and intellectual disability - is located in the M3 helix in the GluN1 transmembrane domain"* and *"Grin1 Y647S/+ mice were created by CRISPR-Cas9 endonuclease-mediated transgenesis"* ([PMID: 39229143](https://pubmed.ncbi.nlm.nih.gov/39229143/)).
- **Face validity (Y647S):** *"Grin1 Y647S/+ mice displayed a reduction in whole brain GluN1 levels and deficiency in NMDAR-mediated synaptic transmission in the hippocampus"* and *"Grin1 Y647S/+ mice exhibited spontaneous seizures, altered vocalizations, muscle strength, sociability, and problem-solving"* ([PMID: 39229143](https://pubmed.ncbi.nlm.nih.gov/39229143/)).
- **Loss-of-function mechanism (Y647S):** *"The Y647S variant confers a complex in vivo phenotype, which reflects largely diminished properties of NMDAR function"* ([PMID: 39229143](https://pubmed.ncbi.nlm.nih.gov/39229143/)).
- **Circuit paradox and predictive validity (Y647S):** *"in intact local circuits, this loss-of-function paradoxically extends NMDAR-dependent dendritic integration, causing prolonged circuit-wide excitation that promotes seizures"*; *"Boosting SK channel activity normalizes dendritic integration"*; *"magnesium supplementation successfully treats seizures in vivo in the transgenic mice, despite loss-of-function of NMDARs"* ([PMID: 41602908](https://pubmed.ncbi.nlm.nih.gov/41602908/)).
- **Peripheral gain-of-function biomarker (Y647S):** *"Functional assays revealed increased NMDAR-mediated calcium influx in Grin1Y647S/+ RBCs, accompanied by reduced blood viscosity under flow conditions"* and *"providing foundational evidence for the development of peripheral blood biomarkers for patients with GRIN Disorder"* ([PMID: 41714299](https://pubmed.ncbi.nlm.nih.gov/41714299/)).
- **Sex (Y647S):** *"Reduction in NMDAR EPSC amplitude was observed in both sexes, with no significant effect of sex"* while *"Breakthrough seizures in MgT-treated mice all occurred in female mice"* ([PMID: 41602908](https://pubmed.ncbi.nlm.nih.gov/41602908/)).

If the knowledge base's "Grin1 Rgsc174 mouse" entry is in fact intended to denote this Y647S patient knock-in, then the validity assessment flips entirely — but that would require correcting the allele name. On the available nomenclature, Rgsc174 ≠ Y647S.

---

## Mechanistic Model / Interpretation

### Two different alleles, two different validity stories

```
                         GluN1 (GRIN1) subunit
   Extracellular  --+---------------------------------------+
                    |  ATD / LBD                            |
   Membrane     ----+--  M1  M2(pore loop)  M3  M4  --------+
                    |        ^                 ^            |
                    |   Human GRIN1-NDD    Y647S (M3)       |
                    |   variants cluster   = patient KI,    |
                    |   here (pore)        high validity    |
   Intracellular ---+                                       |
                    |   C0 domain -- aCaMKII coupling       |
                    |        ^                               |
                    |   Rgsc174 (R->C) = ENU hyperactivity  |
                    |   screen mutant, POOR GRIN1-NDD fit   |
                    +---------------------------------------+
```

The core interpretive point is spatial and causal. Pathogenic GRIN1-NDD variants damage the ion channel itself (pore-lining M2 loop and gating helices such as M3). The Rgsc174 ENU variant instead perturbs an intracellular protein-interaction domain (C0) that scaffolds αCaMKII. Both can be described loosely as "NMDAR dysfunction," but they act at different levels — channel biophysics versus downstream signaling/trafficking — and were discovered by opposite routes (patient → mouse for Y647S; behavioral phenotype → gene for Rgsc174).

### Where Rgsc174 maps onto the mechanism nodes

| Mechanism node | Rgsc174 evidence | Direction | Faithfulness |
|---|---|---|---|
| GRIN1 Variant & Altered GluN1/NMDA Receptor Function | R→C in intracellular C0 domain; impairs GluN1–αCaMKII coupling ([PMID: 20345915](https://pubmed.ncbi.nlm.nih.gov/20345915/), [PMID: 23688147](https://pubmed.ncbi.nlm.nih.gov/23688147/)) | Altered (signaling/trafficking, not gating) | Gene-identity only; wrong domain vs. disease variants |
| NMDA Receptor Loss-of-Function | Glutamate–dopamine hypofunction underlies behavior ([PMID: 20345915](https://pubmed.ncbi.nlm.nih.gov/20345915/)) | ↓ hypofunction (indirect) | Partial / indirect — **only defensible link** |
| NMDA Receptor Gain-of-Function | None in Rgsc174 | — | Do not link |
| Gain-of-Function Cortical Maldevelopment | None in Rgsc174 | — | Do not link |
| Disrupted Excitatory Neurotransmission & E/I Imbalance | Implied by glutamate–dopamine dysregulation, but not directly measured in Rgsc174 | Unclear | Not directly supported |
| Impaired Neurodevelopment | Immature dentate gyrus (iDG) phenotype — but tied to schizophrenia/bipolar, not GRIN1-NDD ([PMID: 23688147](https://pubmed.ncbi.nlm.nih.gov/23688147/)) | Developmental arrest of DG | Points to a *different* disorder |

### Findings that do not fit the GRIN1-NDD mechanism nodes

Two Rgsc174 findings fall outside the GoF/LoF framework entirely and are better described as network/behavioral-ecology observations: (1) the **social-subordination split** ([PMID: 29150978](https://pubmed.ncbi.nlm.nih.gov/29150978/)), a circuit-level dominance phenotype with no human GRIN1-NDD anchor; and (2) the **immature dentate gyrus endophenotype** ([PMID: 23688147](https://pubmed.ncbi.nlm.nih.gov/23688147/)), which links to schizophrenia/bipolar postmortem tissue rather than to GRIN1-NDD. A general caveat applies across the field: a 2024 review of GRIN variants *"discuss[es] the limitations of this classification at the synaptic, cellular, or system level"* ([PMID: 38836461](https://pubmed.ncbi.nlm.nih.gov/38836461/)), warning that receptor-level GoF/LoF labels may not hold at higher levels of organization.

### The schizophrenia-overlap problem

NMDAR hypofunction is the canonical construct for schizophrenia models, which creates a specificity problem for any GRIN1-NDD link. Mohn et al. showed that *"reduced NMDA receptor activity results in schizophrenic-like behavior"* and that these behaviors *"are similar to those observed in pharmacologically induced animal models of schizophrenia and can be ameliorated by treatment with haloperidol or clozapine"* ([PMID: 10481908](https://pubmed.ncbi.nlm.nih.gov/10481908/)). Related Grin1 loss-of-function work shows *"Grin1 loss-of-function mutations cause volume reductions in dopaminergic structures early in development"* ([PMID: 31299220](https://pubmed.ncbi.nlm.nih.gov/31299220/)). Because Rgsc174's readouts (hyperactivity, startle/PPI, fear memory, iDG) are the same ones used to validate schizophrenia models, any link from Rgsc174 to a GRIN1-NDD mechanism node carries an inherent specificity problem.

---

## Evidence Base

| PMID | Role in this report | Key supported point |
|---|---|---|
| [20345915](https://pubmed.ncbi.nlm.nih.gov/20345915/) | Primary — defines Rgsc174 | ENU origin from hyperactivity screen (M100174); R→C in C0 domain; glutamate–dopamine mechanism |
| [23688147](https://pubmed.ncbi.nlm.nih.gov/23688147/) | Primary — behavioral/mechanistic characterization | Fear-memory deficit, ↓startle/intact PPI; ADHD/schizophrenia/bipolar framing; iDG → human psychiatric postmortem; C0–αCaMKII; male-only testing |
| [29150978](https://pubmed.ncbi.nlm.nih.gov/29150978/) | Primary — individual differences | Social subordination split (no human anchor) |
| [32798374](https://pubmed.ncbi.nlm.nih.gov/32798374/) | Independent review | Catalogues Rgsc174 among schizophrenia models |
| [31429998](https://pubmed.ncbi.nlm.nih.gov/31429998/) | Primary — human variant mapping | Disease variants cluster in M2 pore loop (contrast with C0) |
| [38836461](https://pubmed.ncbi.nlm.nih.gov/38836461/) | Review — caveat | Limits of GoF/LoF classification at system level |
| [10481908](https://pubmed.ncbi.nlm.nih.gov/10481908/) | Context — differential disorder | NMDAR hypofunction = canonical schizophrenia construct |
| [31299220](https://pubmed.ncbi.nlm.nih.gov/31299220/) | Context — differential disorder | Grin1 LoF affects dopaminergic (schizophrenia) circuits |
| [39229143](https://pubmed.ncbi.nlm.nih.gov/39229143/) | **Flagged — different allele (Y647S)** | Patient-derived GRIN1-NDD knock-in; NOT Rgsc174 |
| [41602908](https://pubmed.ncbi.nlm.nih.gov/41602908/) | **Flagged — different allele (Y647S)** | Circuit paradox; magnesium rescue; sex effect; NOT Rgsc174 |
| [41714299](https://pubmed.ncbi.nlm.nih.gov/41714299/) | **Flagged — different allele (Y647S)** | RBC gain-of-function biomarker; NOT Rgsc174 |

---

## Assessment: Good, Partial, or Poor Model

| Aspect of GRIN1-NDD | Rgsc174 verdict | Basis |
|---|---|---|
| Correct gene (GRIN1/GluN1) | Good | Allele is in Grin1 |
| Variant type/location matching patients | Poor | C0 intracellular domain vs. pore/gating region in patients |
| Epilepsy / seizures | Poor (not reproduced) | No seizures reported |
| Intellectual disability / cognition | Poor | Fear-memory loss is psychiatric-style, not ID |
| Hypotonia / motor | Poor | Not reported |
| NMDAR hypofunction (LoF) | Partial | Indirect glutamate–dopamine/CaMKII hypofunction |
| NMDAR gain-of-function | Poor (absent) | No GoF evidence |
| Predictive validity for GRIN1-NDD therapies | Unknown | Methylphenidate (ADHD drug) tested, not GRIN1-NDD therapies |
| Overall as a GRIN1-NDD model | **Poor** | Repurposed psychiatric-endophenotype line |

### Curator caveats to attach to any Rgsc174 → GRIN1-NDD mechanism link

1. **Allele provenance:** ENU behavioral-screen mutant, not a patient variant.
2. **Wrong domain:** mutation in intracellular C0 domain, not the transmembrane pore/gating region where disease variants cluster.
3. **Link only to LoF:** permissible link is to *NMDA Receptor Loss-of-Function* only; forbid gain-of-function, cortical-maldevelopment, and (as directly measured) E/I-imbalance links.
4. **Indirect mechanism:** hypofunction inferred from behavior/biochemistry and CaMKII coupling, not from direct channel electrophysiology.
5. **Differential disorder:** creators and independent reviewers class it as ADHD/schizophrenia/bipolar; its only human-tissue anchor (iDG) is psychiatric.
6. **Sex limitation:** core phenotyping male-only.
7. **No human GRIN1-NDD anchor:** no postmortem/transcriptomic/biomarker/genetic bridge to GRIN1-NDD patients.

---

## Limitations and Knowledge Gaps

1. **Allele-identity ambiguity is the dominant uncertainty.** The research template names "Grin1 Rgsc174 mouse," but this collides with a patient-derived Y647S knock-in that circulates in recent GRIN1-NDD literature. This report treats Rgsc174 as the RIKEN ENU allele (its correct meaning), but the knowledge base must confirm which allele its entry denotes before links are finalized.

2. **Several key points rest on full text, not abstracts.** The male-only testing statement, the C0–αCaMKII binding detail, the iDG→postmortem link, and the Ang et al. schizophrenia-model catalogue were drawn from full text rather than abstracts. These are flagged as full-text-supported and should be verified before curation.

3. **No direct GRIN1-NDD phenotyping of Rgsc174.** There is no published assessment of seizures, EEG, developmental milestones, hypotonia, or intellectual-disability analogues in Rgsc174. Their absence from reports is suggestive but not a formal negative result.

4. **No human-data anchor for GRIN1-NDD.** Rgsc174's only cross-species tissue link (iDG) is to schizophrenia/bipolar postmortem brain. No postmortem, transcriptomic, biomarker, or genetic study connects Rgsc174 to GRIN1-NDD patients.

5. **Direction-of-effect at the channel level is unmeasured in Rgsc174.** Unlike Y647S (electrophysiologically characterized), Rgsc174's receptor biophysics (open probability, surface expression, current amplitude) have not been directly reported; the LoF assignment is inferred.

6. **Sex generalizability unknown.** Core behavior was characterized in males only; no female cohort exists for the Rgsc174 behavioral battery.

---

## Proposed Follow-up Experiments / Actions

1. **Resolve the allele name in the knowledge base.** Confirm whether the "Grin1 Rgsc174 mouse" node refers to the RIKEN ENU C0-domain allele or to the Y647S patient knock-in. This single curation decision determines the entire validity assessment.

2. **Curate conservatively.** If Rgsc174 = ENU allele: link **only** to *NMDA Receptor Loss-of-Function*, tagged "gene-identity-only / indirect / schizophrenia-overlap." Do **not** link to any gain-of-function node, cortical-maldevelopment node, or E/I-imbalance node. Attach the differential-disorder and male-only caveats.

3. **Electrophysiologically phenotype Rgsc174 receptors** (agonist potency, Po, surface expression, current amplitude) to assign direction of effect at the channel level rather than inferring it.

4. **Screen Rgsc174 for GRIN1-NDD-defining phenotypes** — video-EEG for seizures, developmental milestones, muscle tone — to formally test (and likely rule out) GRIN1-NDD face validity.

5. **Side-by-side comparison of Rgsc174 and Y647S** under identical assays to quantify how much a C0-domain signaling mutant diverges from a pore/gating patient mutant, clarifying the validity gap for curators.

6. **Verify full-text-only claims** (male-only testing, iDG–postmortem link, schizophrenia-model cataloguing) against the primary papers before entering them as curated evidence.

---

*Prepared for knowledge-base curation. Every quoted claim is drawn verbatim from the cited abstract or, where noted, the paper's full text. Citations flagged "different allele (Y647S)" must not be attached to the Rgsc174 node.*


## Artifacts

- [OpenScientist final report](GRIN1-Related_Neurodevelopmental_Disorder-model-validity-grin1_rgsc174_mouse-deep-research-openscientist_artifacts/final_report.html)
- [OpenScientist final report](GRIN1-Related_Neurodevelopmental_Disorder-model-validity-grin1_rgsc174_mouse-deep-research-openscientist_artifacts/final_report.pdf)

## Reference Validation

Checked with `linkml-reference-validator` 0.5.1.

| Outcome | Count |
| --- | --- |
| References checked | 11 |
| Resolved | 11 |
| Unresolved (possible confabulation) | 0 |
| Unverifiable | 0 |
| References weighed for topical relevance | 11 |
| On topic | 5 |
| Off topic | 0 |

All extracted references resolved successfully.

## Term Validation

No ontology term identifiers were found in this report.