---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-05-23T21:45:57.253580'
end_time: '2026-05-23T22:39:43.397866'
duration_seconds: 3226.14
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Celiac Disease
  category: Complex
  hypothesis_group_id: canonical_gluten_hladq_ttg_enteropathy_model
  hypothesis_label: Canonical Gluten / HLA-DQ2-DQ8 / tTG Enteropathy Model
  hypothesis_status: CANONICAL
  hypothesis_yaml: "hypothesis_group_id: canonical_gluten_hladq_ttg_enteropathy_model\n\
    hypothesis_label: Canonical Gluten / HLA-DQ2-DQ8 / tTG Enteropathy Model\nstatus:\
    \ CANONICAL\ndescription: Celiac disease arises in HLA-DQ2 / HLA-DQ8 positive\
    \ individuals from a CD4 T-cell-mediated\n  immune response to dietary gluten/gliadin\
    \ peptides that have been deamidated by tissue transglutaminase\n  2 (TG2/tTG).\
    \ Deamidation converts neutral glutamine residues to negatively charged glutamate,\
    \ dramatically\n  increasing peptide affinity for HLA-DQ2/DQ8 and licensing presentation\
    \ to gluten- reactive CD4 T cells\n  in the lamina propria. The resulting Th1/IFN-\u03B3\
    \ cytokine response drives intraepithelial lymphocyte cytotoxicity,\n  IL-15-mediated\
    \ epithelial activation, B-cell expansion with anti-TG2 autoantibody production,\
    \ crypt\n  hyperplasia, and villous atrophy. Gluten-free diet remission, HLA-DQ2/DQ8\
    \ restriction, and TG2 inhibitor\n  (ZED1227) trials all corroborate the gluten\
    \ / HLA / TG2 axis as the canonical pathogenic mechanism.\nevidence:\n- reference:\
    \ PMID:38914866\n  reference_title: 'Transglutaminase 2 in celiac disease: pathogenic\
    \ role and therapeutic target.'\n  supports: SUPPORT\n  evidence_source: HUMAN_CLINICAL\n\
    \  snippet: Transglutaminase 2 (TG2) plays a pivotal role in the pathogenesis\
    \ of\n  explanation: |\n    Canonical mechanism reference used as the seed for\
    \ the hypothesis-search deep-research run."
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
citation_count: 46
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Celiac Disease
- **Category:** Complex

## Target Hypothesis
- **Hypothesis ID:** canonical_gluten_hladq_ttg_enteropathy_model
- **Hypothesis Label:** Canonical Gluten / HLA-DQ2-DQ8 / tTG Enteropathy Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: canonical_gluten_hladq_ttg_enteropathy_model
hypothesis_label: Canonical Gluten / HLA-DQ2-DQ8 / tTG Enteropathy Model
status: CANONICAL
description: Celiac disease arises in HLA-DQ2 / HLA-DQ8 positive individuals from a CD4 T-cell-mediated
  immune response to dietary gluten/gliadin peptides that have been deamidated by tissue transglutaminase
  2 (TG2/tTG). Deamidation converts neutral glutamine residues to negatively charged glutamate, dramatically
  increasing peptide affinity for HLA-DQ2/DQ8 and licensing presentation to gluten- reactive CD4 T cells
  in the lamina propria. The resulting Th1/IFN-γ cytokine response drives intraepithelial lymphocyte cytotoxicity,
  IL-15-mediated epithelial activation, B-cell expansion with anti-TG2 autoantibody production, crypt
  hyperplasia, and villous atrophy. Gluten-free diet remission, HLA-DQ2/DQ8 restriction, and TG2 inhibitor
  (ZED1227) trials all corroborate the gluten / HLA / TG2 axis as the canonical pathogenic mechanism.
evidence:
- reference: PMID:38914866
  reference_title: 'Transglutaminase 2 in celiac disease: pathogenic role and therapeutic target.'
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: Transglutaminase 2 (TG2) plays a pivotal role in the pathogenesis of
  explanation: |
    Canonical mechanism reference used as the seed for the hypothesis-search deep-research run.
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

# Mechanistic Hypothesis Evaluation: Canonical Gluten / HLA-DQ2-DQ8 / tTG Enteropathy Model of Celiac Disease

**Hypothesis ID:** `canonical_gluten_hladq_ttg_enteropathy_model`
**Status in KB:** CANONICAL
**Date of evaluation:** 2026-05-24
**Literature surveyed:** 130 papers | **Confirmed findings:** 24

---

## Executive Judgment

**Verdict: STRONGLY SUPPORTED — with five required mechanistic expansions**

The canonical gluten/HLA-DQ2-DQ8/tTG enteropathy model is strongly supported as the central pathogenic mechanism of celiac disease (CeD). The core claim — that TG2-mediated deamidation of gluten peptides enhances HLA-DQ2/DQ8 binding, licensing a CD4+ T cell response that drives mucosal injury — is corroborated by convergent evidence across human clinical trials, mouse models, tetramer-based T cell quantification, and therapeutic intervention studies. The ZED1227 phase 2a randomized controlled trial provides the most definitive causal evidence: pharmacological TG2 inhibition attenuated gluten-induced villous atrophy in a dose-dependent manner, confirming TG2 as a necessary node in the pathogenic chain.

However, the hypothesis as stated is **incomplete in five critical areas**: (1) The IL-15/innate immune arm is co-required for villous atrophy — neither adaptive nor innate immunity alone is sufficient (three-signal model); (2) the cytokine milieu is mixed Th1/Th17/IL-21 rather than purely Th1/IFN-γ; (3) three nested positive feedback loops (IgA-CD71 retrotranscytosis, IFN-γ/thioredoxin/TG2 activation, B cell APC amplification) drive disease chronicity and self-amplification; (4) wheat amylase-trypsin inhibitors (ATIs) provide a parallel TLR4-mediated innate immune signal that acts as an adjuvant; and (5) transcellular antigen transport via the IgA-CD71 pathway is likely dominant over paracellular permeability for gluten access to the lamina propria. The single most important unresolved gap remains the tolerance-breaking trigger — what converts the ~97% of HLA-DQ2/DQ8 carriers who maintain oral tolerance into the ~1–3% who develop disease. Boundary conditions where the model is insufficient include seronegative CeD (~1.7%), refractory CeD type II (gluten-independent clonal T cell expansion), and DQ8-specific mechanistic differences.

---

## Summary

The canonical model of celiac disease posits a linear cascade: dietary gluten → TG2 deamidation → enhanced HLA-DQ2/DQ8 binding → CD4+ T cell activation → Th1/IFN-γ response → villous atrophy. Our systematic evaluation of 130 primary papers and reviews confirms this core pathway while identifying critical mechanistic additions and boundary conditions.

The strongest direct evidence comes from the ZED1227 TG2 inhibitor trial ([PMID: 34192430](https://pubmed.ncbi.nlm.nih.gov/34192430/)), which demonstrated that blocking TG2 enzymatic activity preserved mucosal architecture during gluten challenge — the first causal perturbation experiment validating the TG2 node in humans. This is complemented by HLA-DQ2 tetramer studies quantifying gluten-specific T cells at 0.1–1.8% of intestinal CD4+ T cells, with frequency correlating to Marsh grade and anti-TG2 antibody levels ([PMID: 23775608](https://pubmed.ncbi.nlm.nih.gov/23775608/)).

However, five mechanistic expansions are required to accurately represent the pathogenic cascade. First, murine three-signal models demonstrate that IL-15 overexpression, HLA-DQ, and gluten are all co-required for villous atrophy — none alone is sufficient ([PMID: 32051586](https://pubmed.ncbi.nlm.nih.gov/32051586/)). Second, the cytokine response involves Th17/IL-21 co-expression alongside Th1/IFN-γ. Third, three positive feedback loops create disease self-amplification. Fourth, non-gluten wheat ATIs activate innate immunity via TLR4. Fifth, transcellular IgA-CD71 retrotranscytosis provides the dominant gluten transport route. The tolerance-breaking trigger, the upstream event that initiates the cascade in susceptible individuals, remains the most important unresolved question.

---

## Key Findings

### Finding 1: ZED1227 TG2 Inhibitor Trial — Definitive Causal Evidence for TG2

The phase 2a RCT of ZED1227 (n=163) provides the strongest causal evidence supporting the canonical model. All three dose levels of ZED1227 significantly attenuated gluten-induced duodenal mucosal injury versus placebo. The estimated difference in villus height-to-crypt depth ratio change was 0.44 (95% CI 0.15–0.73, P=0.001) for 10 mg, 0.49 (95% CI 0.20–0.77, P<0.001) for 50 mg, and 0.48 for 100 mg. Transcriptomic analysis confirmed that ZED1227 preserved mucosal morphology, inflammation, cell differentiation, and nutrient absorption signatures to gluten-free diet (GFD) levels ([PMID: 34192430](https://pubmed.ncbi.nlm.nih.gov/34192430/); [PMID: 38914866](https://pubmed.ncbi.nlm.nih.gov/38914866/)). Immunohistochemistry showed ZED1227-TG2 complexes accumulated primarily in villous enterocytes at the luminal brush border, indicating TG2 inhibition occurs before gliadin peptides enter the lamina propria ([PMID: 37445994](https://pubmed.ncbi.nlm.nih.gov/37445994/)).

### Finding 2: Dominant T Cell Epitope — Deamidated A-Gliadin 57-73

The landmark study by Anderson et al. demonstrated a transient, disease-specific, DQ2-restricted CD4+ T cell response to a single dominant epitope: A-gliadin 57-73 with TG2-catalyzed deamidation at Q65→E ([PMID: 10700238](https://pubmed.ncbi.nlm.nih.gov/10700238/)). Peripheral blood proliferation assays showed this single α-gliadin peptide could detect 60% of CeD children without gluten challenge ([PMID: 24724018](https://pubmed.ncbi.nlm.nih.gov/24724018/)). HLA-DQ8-restricted disease shows distinct epitope preferences with less absolute deamidation dependence and greater protease sensitivity ([PMID: 17629515](https://pubmed.ncbi.nlm.nih.gov/17629515/)), indicating that therapeutic interventions may need genotype-tailoring.

### Finding 3: Three-Signal Model — IL-15, Gluten, AND HLA-DQ All Required

A critical expansion of the canonical model emerged from mouse studies demonstrating that villous atrophy requires three simultaneous signals: (1) IL-15 overexpression, (2) gluten exposure, and (3) HLA-DQ expression. IL-15 alone causes IEL accumulation but not atrophy; HLA-DQ plus gluten causes immune activation but not tissue destruction. Only the combination reproduces the full celiac phenotype ([PMID: 32051586](https://pubmed.ncbi.nlm.nih.gov/32051586/)). IL-15 was found massively overexpressed in both epithelium and lamina propria of active CeD ([PMID: 12949719](https://pubmed.ncbi.nlm.nih.gov/12949719/)), and MICA — a stress ligand for NKG2D on IELs — is induced by gliadin via IL-15 ([PMID: 15357948](https://pubmed.ncbi.nlm.nih.gov/15357948/)). Distinct contributions from epithelial stress and adaptive immunity synergize for IEL activation — neither alone is sufficient for villous atrophy ([PMID: 26001928](https://pubmed.ncbi.nlm.nih.gov/26001928/)). Anti-IL-15 antibody (TM-beta1) reversed autoimmune intestinal damage in IL-15 transgenic mice ([PMID: 19805228](https://pubmed.ncbi.nlm.nih.gov/19805228/)).

{{figure:final_causal_model.png|caption=Integrated mechanistic causal chain of celiac disease showing the three-signal model, positive feedback loops, and alternative pathways. Solid lines indicate well-established links; dashed lines indicate emerging or partially supported connections.}}

### Finding 4: HLA-DQ2/DQ8 — Necessary but Dramatically Insufficient

While HLA-DQ2 is present in >90% of CeD patients, the same alleles are carried by 30–40% of the general population, of whom only ~1% develop disease. GWAS studies identified 42 non-HLA loci, but these plus HLA explain less than 50% of genetic heritability ([PMID: 40818857](https://pubmed.ncbi.nlm.nih.gov/40818857/)). Non-HLA loci on the Immunochip explain a maximum of 4.5% of genetic variance ([PMID: 25920553](https://pubmed.ncbi.nlm.nih.gov/25920553/)). This "heritability gap" underscores that additional genetic, epigenetic, and environmental factors are essential co-determinants of disease development.

### Finding 5: Gluten-Specific T Cells — Quantification, Persistence, and Memory

Direct quantification using HLA-DQ2 tetramers revealed gluten-specific T cells at 0.1–1.8% of intestinal CD4+ T cells in 10/10 untreated CeD patients, with frequency correlating to Marsh grade and serum IgA anti-TG2 levels ([PMID: 23775608](https://pubmed.ncbi.nlm.nih.gov/23775608/)). Critically, these cells persist as memory T cells for decades on GFD and are reactivated upon gluten re-exposure ([PMID: 38552723](https://pubmed.ncbi.nlm.nih.gov/38552723/)). After GFD initiation, gluten-specific T cells rapidly lost activation markers (CD38, Ki-67, HLA-DR) within weeks but did not disappear — explaining lifelong susceptibility to relapse.

### Finding 6: Three Self-Amplifying Positive Feedback Loops

Our synthesis identified three nested feedback loops that explain CeD chronicity and treatment resistance:

**Loop 1 — IgA Retrotranscytosis:** SIgA-gliadin complexes bind CD71 (transferrin receptor, upregulated on CeD enterocytes) and are retrotransported across the epithelium, delivering intact gliadin peptides to the lamina propria. This means the immune response (IgA production) directly delivers more antigen ([PMID: 22750506](https://pubmed.ncbi.nlm.nih.gov/22750506/)).

**Loop 2 — IFN-γ/Thioredoxin/TG2 Activation:** T cell–derived IFN-γ stimulates monocyte release of thioredoxin, which reduces the regulatory disulfide bond on extracellular TG2, activating more enzyme for deamidation. This amplifies the very step that creates the immunogenic peptides ([PMID: 21908620](https://pubmed.ncbi.nlm.nih.gov/21908620/)).

**Loop 3 — B Cell APC Amplification:** TG2-reactive B cells (recognizing N-terminal TG2 epitopes) efficiently internalize TG2-gluten complexes, process them, and present gluten peptides to gluten-specific CD4+ T cells, receiving T cell help that drives their expansion and antibody production ([PMID: 31285344](https://pubmed.ncbi.nlm.nih.gov/31285344/)).

These loops explain: (a) rapid disease escalation after initiation, (b) slow and often incomplete mucosal healing on GFD (65% at 2 years, 85% at 5 years, with 10% persistent atrophy; [PMID: 12219789](https://pubmed.ncbi.nlm.nih.gov/12219789/); [PMID: 3170777](https://pubmed.ncbi.nlm.nih.gov/3170777/)), and (c) decade-long T cell memory.

### Finding 7: Mixed Th1/Th17/IL-21 Cytokine Response

The canonical model describes a Th1/IFN-γ response, but primary evidence shows a more complex cytokine milieu. IL-17A RNA and protein are elevated in active CeD mucosa, with the majority of IL-17A-producing CD4+ and CD4+CD8+ cells co-expressing IFN-γ ([PMID: 20061410](https://pubmed.ncbi.nlm.nih.gov/20061410/)). Gliadin-specific Th17 cells with phenotype TCRαβ+ CD45RO+ CD161+ CCR6+ IL-23R+ uniquely co-express TGFβ, IFNγ, IL-21, and IL-22 ([PMID: 21206487](https://pubmed.ncbi.nlm.nih.gov/21206487/)). IL-15 directly regulates IL-21 production via Akt/STAT3 signaling ([PMID: 22785229](https://pubmed.ncbi.nlm.nih.gov/22785229/)), providing a mechanistic link between the innate (IL-15) and adaptive (Th17/IL-21) arms.

### Finding 8: Wheat ATIs as Parallel Innate Immune Activators

Wheat amylase-trypsin inhibitors (ATIs, 2–4% of wheat protein) are potent TLR4 activators on monocytes, macrophages, and dendritic cells ([PMID: 27993525](https://pubmed.ncbi.nlm.nih.gov/27993525/)). They are highly protease-resistant and retain bioactivity after baking. Anti-TLR4 monoclonal antibody completely abolished ATI-induced inflammation in humanized mice ([PMID: 29574077](https://pubmed.ncbi.nlm.nih.gov/29574077/)). ATIs costimulate antigen-presenting cells and promote T cell activation, acting as natural adjuvants for the adaptive gluten response. This represents a parallel, non-gluten wheat component contributing to CeD pathogenesis.

### Finding 9: Nexvax2 Peptide Immunotherapy Failure — Mechanistic Implications

The phase 2 RESET CeD trial of Nexvax2 — a peptide immunotherapy targeting immunodominant HLA-DQ2.5-restricted gluten epitopes — was terminated early. While Nexvax2 engaged gluten-specific CD4+ T cells (confirmed via IL-2 and IFN-γ cytokine release assay), it failed to achieve clinical protection against gluten-induced symptoms or mucosal injury ([PMID: 36898393](https://pubmed.ncbi.nlm.nih.gov/36898393/)). This negative result is mechanistically informative: targeting dominant gluten CD4+ T cell epitopes alone is insufficient, strongly suggesting that additional pathogenic pathways (innate immunity, non-immunodominant epitopes, IEL activation) operate beyond the adaptive axis.

### Finding 10: Transcellular Gluten Transport Dominates Over Paracellular

In HLA-DQ8 transgenic mice, larazotide (AT1001) normalized paracellular permeability (51Cr-EDTA flux) but had no effect on bacterial translocation to mesenteric lymph nodes ([PMID: 21822909](https://pubmed.ncbi.nlm.nih.gov/21822909/)). Clinical trials of larazotide confirmed this pattern: the primary permeability endpoint (lactulose-to-mannitol ratio) was not significantly improved versus placebo ([PMID: 34339872](https://pubmed.ncbi.nlm.nih.gov/34339872/)), although gastrointestinal symptoms and anti-tTG IgA levels were reduced at 1 mg ([PMID: 23163616](https://pubmed.ncbi.nlm.nih.gov/23163616/)). Combined with the IgA-CD71 retrotranscytosis finding ([PMID: 22750506](https://pubmed.ncbi.nlm.nih.gov/22750506/)), these data indicate transcellular routes are the dominant mechanism of gluten peptide access to the lamina propria, qualifying the canonical model's implicit reliance on paracellular permeability.

### Finding 11: Refractory CeD Type II — Boundary Condition

RCD type II demonstrates clonal expansion of aberrant IELs with atypical immunophenotype persisting despite strict GFD. TCRβ sequences in RCD II are unique and not homologous to gliadin-specific TCR sequences, supporting gluten-independent expansion ([PMID: 28188172](https://pubmed.ncbi.nlm.nih.gov/28188172/)). A 7p14.3 locus (rs2041570, OR=2.36, P=2.37×10⁻⁸) predisposes CeD→RCD II progression ([PMID: 29787419](https://pubmed.ncbi.nlm.nih.gov/29787419/)). This represents a clear boundary condition where the canonical model is insufficient — the disease has transitioned to a gluten-independent, pre-lymphomatous state.

### Finding 12: Potential CeD — Spontaneous Resolution Challenges Linear Model

A prospective study of 280 children with potential CeD (positive anti-TG2/anti-EMA, normal histology, HLA-DQ2/DQ8+) found that only 42 (15%) developed villous atrophy during follow-up, while 89 (32%) spontaneously lost seropositivity ([PMID: 30978358](https://pubmed.ncbi.nlm.nih.gov/30978358/)). This demonstrates that the canonical adaptive immune cascade can be activated (positive serology) without progressing to tissue damage, and can even self-resolve — strongly supporting the multi-signal requirement for atrophy.

### Finding 13: Dermatitis Herpetiformis — Extraintestinal Extension via TG3

DH involves IgA deposition at the dermal-epidermal junction targeting epidermal transglutaminase 3 (TG3) ([PMID: 22811741](https://pubmed.ncbi.nlm.nih.gov/22811741/)). TG2 and TG3 share antigenic epitopes recognized by serum antibodies from both CeD and DH patients ([PMID: 22214930](https://pubmed.ncbi.nlm.nih.gov/22214930/)). In the HLA-DQ8 NOD mouse model, 15/90 gluten-sensitized mice developed DH-like blistering with IgA deposits, but none of the blistering mice had small-bowel pathology ([PMID: 15489956](https://pubmed.ncbi.nlm.nih.gov/15489956/)). This demonstrates that the humoral arm of the canonical model can cause extraintestinal damage independently of enteropathy.

### Finding 14: Seronegative CeD — Qualifying Antibody Role

Of 810 CeD diagnoses, 14 (1.7%) met criteria for seronegative CeD: antibody negativity, villous atrophy, HLA-DQ2/DQ8 positive, and clinical/histological improvement on GFD ([PMID: 27352981](https://pubmed.ncbi.nlm.nih.gov/27352981/)). These patients had significantly higher median age at diagnosis, more severe atrophy, and higher autoimmune comorbidity. The preservation of HLA-DQ2/DQ8 requirement and GFD response confirms the core T cell pathway operates in the absence of detectable serum antibodies.

{{figure:evidence_dashboard.png|caption=Evidence quality and completeness dashboard showing the distribution of supporting, qualifying, and competing evidence across the mechanistic causal chain. The majority of evidence supports the canonical model, with qualifications primarily in the innate immune arm and gluten access pathway.}}

---

## Mechanistic Causal Chain

The following causal chain integrates all findings into a unified model, annotating each step with evidence strength.

### Upstream Triggers (WEAKLY SUPPORTED — Major Gap)

```
GENETIC SUSCEPTIBILITY          ENVIRONMENTAL TRIGGER(S)
HLA-DQ2/DQ8 (necessary)   +    ??? Tolerance breakdown ???
Non-HLA loci (42+ loci)        - Viral infection (reovirus: mouse only)
KIR genes (innate arm)          - Microbiome dysbiosis (correlative)
                                - Infant feeding timing (no effect in TEDDY)
                                - ATI innate priming (adjuvant, not trigger)
```

**Evidence strength:** HLA-DQ2/DQ8 necessity is established (>90% of patients carry DQ2). The tolerance-breaking event is the single largest gap. Reovirus demonstrates proof-of-concept in mice ([PMID: 28386004](https://pubmed.ncbi.nlm.nih.gov/28386004/)) but lacks human replication. Rotavirus molecular mimicry was refuted ([PMID: 27548641](https://pubmed.ncbi.nlm.nih.gov/27548641/)).

### Core Pathogenic Cascade (STRONGLY SUPPORTED)

```
Dietary gluten ingestion
        ↓
Incomplete proteolysis → immunogenic peptides survive
        ↓
TG2 deamidation (Gln → Glu) ←——— [FEEDBACK: IFN-γ → Trx → TG2 activation]
        ↓                                    ↑
Enhanced HLA-DQ2/DQ8 binding                 |
        ↓                                    |
CD4+ T cell activation (0.1-1.8% of CD4+)   |
        ↓                                    |
Th1/Th17/IL-21 cytokine response ————————————┘
        ↓
    ┌───┴───────────────────┐
    ↓                       ↓
B cell activation      IEL activation
(anti-TG2 IgA)        (IL-15/NKG2D/MICA)
    ↓                       ↓
[FEEDBACK: B cell APC]  Epithelial cytotoxicity
    ↓                       ↓
[FEEDBACK: IgA-CD71     Villous atrophy +
retrotranscytosis]      Crypt hyperplasia
```

**Evidence strength:** The TG2 → deamidation → T cell activation axis is confirmed by ZED1227 RCT. The IL-15/IEL arm is confirmed by mouse three-signal model. The feedback loops are supported by individual mechanistic studies but their integrated operation has not been tested in a single system.

### Downstream Manifestations

| Manifestation | Mechanism | Evidence Level |
|---------------|-----------|----------------|
| Villous atrophy | IEL-mediated epithelial killing via NKG2D/MICA | Established |
| Crypt hyperplasia | Regenerative response to epithelial destruction | Established |
| Anti-TG2 autoantibodies | B cell activation via T-B cooperation | Established |
| Dermatitis herpetiformis | Cross-reactive IgA targeting TG3 in skin | Established |
| Malabsorption | Villous surface area loss | Established |
| Neurological manifestations | Anti-TG6 antibodies + direct effects | Emerging |
| Refractory CeD type II | Gluten-independent clonal IEL expansion | Established (boundary) |

{{figure:causal_chain.png|caption=Mechanistic causal chain diagram showing the core pathogenic cascade from gluten ingestion to clinical manifestations, with evidence classification for each node and edge.}}

---

## Evidence Matrix

| Citation | Evidence Type | Direction | Mechanistic Claim Tested | Key Finding | Context | Confidence |
|----------|--------------|-----------|--------------------------|-------------|---------|------------|
| [PMID: 34192430](https://pubmed.ncbi.nlm.nih.gov/34192430/) | Human clinical (RCT) | **Supports** | TG2 deamidation is necessary for mucosal damage | ZED1227 attenuated villous atrophy (ΔVHCD 0.49, P<0.001) | Phase 2a, n=163 | High |
| [PMID: 10700238](https://pubmed.ncbi.nlm.nih.gov/10700238/) | Human clinical | **Supports** | HLA-DQ2-restricted T cell epitope recognition | Dominant A-gliadin 57-73 (Q65E) epitope identified | In vivo challenge | High |
| [PMID: 32051586](https://pubmed.ncbi.nlm.nih.gov/32051586/) | Model organism | **Qualifies** | Three signals required for atrophy | IL-15 + gluten + HLA-DQ all needed; adaptive alone insufficient | DQ8 mouse model | High |
| [PMID: 23775608](https://pubmed.ncbi.nlm.nih.gov/23775608/) | Human clinical | **Supports** | Gluten-specific T cells drive disease | 0.1–1.8% of CD4+ T cells gluten-reactive; correlates with Marsh grade | Tetramer staining | High |
| [PMID: 36898393](https://pubmed.ncbi.nlm.nih.gov/36898393/) | Human clinical (RCT) | **Qualifies** | Targeting dominant T cell epitopes sufficient | Nexvax2 engaged T cells but failed clinical protection | Phase 2, terminated | High |
| [PMID: 22750506](https://pubmed.ncbi.nlm.nih.gov/22750506/) | In vitro | **Qualifies** | Paracellular transport is primary gluten access route | IgA-CD71 retrotranscytosis delivers intact gliadin transcellularly | Caco-2 monolayers | Medium |
| [PMID: 31285344](https://pubmed.ncbi.nlm.nih.gov/31285344/) | Human clinical/in vitro | **Supports** | B cells as active APCs in pathogenesis | N-terminal TG2-reactive B cells present gluten to T cells | Patient-derived cells | High |
| [PMID: 28386004](https://pubmed.ncbi.nlm.nih.gov/28386004/) | Model organism | **Supports** | Viral infection can break oral tolerance | Reovirus triggered loss of tolerance to dietary antigens via type I IFN | HLA-DQ mouse model | Medium |
| [PMID: 27548641](https://pubmed.ncbi.nlm.nih.gov/27548641/) | Human clinical | **Refutes** | Rotavirus molecular mimicry triggers CeD | No increased anti-rotavirus reactivity in CeD children vs controls | Pediatric cohort | High |
| [PMID: 28188172](https://pubmed.ncbi.nlm.nih.gov/28188172/) | Human clinical | **Qualifies** | Gluten drives all T cell pathology | RCD II TCRβ sequences are unique and gluten-independent | RCD II patients | High |
| [PMID: 21908620](https://pubmed.ncbi.nlm.nih.gov/21908620/) | In vitro/ex vivo | **Supports** | IFN-γ/thioredoxin/TG2 feedback loop | IFN-γ stimulates Trx release → activates extracellular TG2 | Monocyte-fibroblast co-culture | Medium |
| [PMID: 27993525](https://pubmed.ncbi.nlm.nih.gov/27993525/) | In vitro/model organism | **Competing** | Gluten is the sole wheat trigger | ATIs activate TLR4 on myeloid cells independently of gluten | Mouse model | Medium |
| [PMID: 15357948](https://pubmed.ncbi.nlm.nih.gov/15357948/) | Human clinical/in vitro | **Supports** | NKG2D/MICA drives IEL cytotoxicity | MICA induced by gliadin via IL-15; NKG2D triggers IEL killing | Active CeD biopsies | High |
| [PMID: 30978358](https://pubmed.ncbi.nlm.nih.gov/30978358/) | Human clinical (prospective) | **Qualifies** | Adaptive immunity → tissue damage is linear | 15% progress to atrophy; 32% spontaneously seroconvert to negative | n=280 children, potential CeD | High |
| [PMID: 27352981](https://pubmed.ncbi.nlm.nih.gov/27352981/) | Human clinical | **Qualifies** | Anti-TG2 antibodies are universal diagnostic | 1.7% of CeD is seronegative; HLA-DQ2/DQ8 and GFD response preserved | n=810 CeD cohort | High |
| [PMID: 12219789](https://pubmed.ncbi.nlm.nih.gov/12219789/) | Human clinical | **Qualifies** | GFD fully reverses disease | 10.1% persistent villous atrophy after 5 years on GFD | n=158, long-term follow-up | High |
| [PMID: 23982754](https://pubmed.ncbi.nlm.nih.gov/23982754/) | In vitro | **Supports** | Anti-TG2 IgA has pathogenic effects | Celiac IgA disrupts endothelial adhesion, ECM, and cell polarity | Patient-derived IgA | Medium |
| [PMID: 17215859](https://pubmed.ncbi.nlm.nih.gov/17215859/) | Human clinical (genetic) | **Supports** | Innate immune genes contribute to susceptibility | KIR2DL5B(+)/KIR2DL5A(-) OR=3.63 for CeD | Two independent cohorts | Medium |
| [PMID: 22785229](https://pubmed.ncbi.nlm.nih.gov/22785229/) | In vitro | **Supports** | IL-15/IL-21 mechanistic link | IL-15 regulates IL-21 via Akt/STAT3 in lamina propria lymphocytes | CeD biopsy-derived cells | Medium |
| [PMID: 21822909](https://pubmed.ncbi.nlm.nih.gov/21822909/) | Model organism | **Qualifies** | Paracellular permeability drives antigen access | Blocking paracellular route did not prevent bacterial translocation | HLA-DQ8 transgenic mice | High |

---

## Knowledge Gaps

### Gap 1: Tolerance Breakdown Trigger (CRITICAL)

**Scope:** What event converts the ~97% of HLA-DQ2/DQ8 carriers who maintain oral tolerance into the ~1–3% who develop CeD?

**Why it matters:** This is the single most important upstream causal step. Without understanding what breaks tolerance, primary prevention is impossible.

**What was checked:** Reovirus mouse models ([PMID: 28386004](https://pubmed.ncbi.nlm.nih.gov/28386004/)), rotavirus molecular mimicry (refuted, [PMID: 27548641](https://pubmed.ncbi.nlm.nih.gov/27548641/)), TEDDY prospective birth cohort (timing of gluten introduction had no effect, [PMID: 31593953](https://pubmed.ncbi.nlm.nih.gov/31593953/)), microbiome studies (correlative only), ATI/TLR4 innate priming (adjuvant, not trigger).

**What would resolve it:** A prospective human cohort study (e.g., expansion of TEDDY or PreventCD) with serial virome sequencing, microbiome profiling, and mucosal immune phenotyping in at-risk HLA-DQ2/DQ8 infants before and after seroconversion.

### Gap 2: Anti-IL-15 Therapy — No Human Trial Published

**Scope:** IL-15 blockade reverses autoimmune intestinal damage in transgenic mice ([PMID: 19805228](https://pubmed.ncbi.nlm.nih.gov/19805228/)), and BNZ-2 (a γc receptor antagonist blocking IL-15 and IL-21) inhibits IEL reprogramming ex vivo ([PMID: 31622625](https://pubmed.ncbi.nlm.nih.gov/31622625/)). However, no published phase 2+ human CeD trial of anti-IL-15 therapy was identified as of our search date.

**Why it matters:** IL-15 is arguably the most important therapeutic target after TG2 given its central role in the three-signal model. The absence of human efficacy data leaves the IL-15 arm's therapeutic potential unconfirmed.

**What would resolve it:** Completion and publication of anti-IL-15 or anti-IL-15Rα monoclonal antibody RCTs in active CeD or RCD patients.

### Gap 3: Integrated Feedback Loop Testing

**Scope:** Each of the three feedback loops has been demonstrated individually but never tested as an integrated system. Whether disrupting one loop is sufficient to collapse the cascade is unknown.

**What would resolve it:** Combinatorial perturbation studies (e.g., ZED1227 + anti-CD71 antibody, or TG2 inhibitor + IgA pathway disruption) in mouse models or patient-derived organoid systems.

### Gap 4: Seronegative CeD Mechanism

**Scope:** 1.7% of CeD patients are seronegative ([PMID: 27352981](https://pubmed.ncbi.nlm.nih.gov/27352981/)). These patients maintain HLA-DQ2/DQ8 positivity and GFD response, suggesting the core T cell pathway operates but the B cell/antibody arm fails. Whether this reflects mucosal IgA deposition trapping antibodies locally, incomplete B cell maturation, or an alternative pathway is unclear.

**What would resolve it:** Deep immunophenotyping of seronegative CeD mucosal biopsies including intestinal mucosal antibody deposits, B cell subset analysis, and gluten-specific T cell tetramer studies.

### Gap 5: Non-HLA Heritability

**Scope:** Known HLA and non-HLA loci explain <50% of genetic heritability ([PMID: 40818857](https://pubmed.ncbi.nlm.nih.gov/40818857/)). No GenCC or ClinGen gene–disease validity assessment for CeD non-HLA loci was identified.

**What would resolve it:** Larger multi-ethnic GWAS, rare-variant whole-genome sequencing studies, and functional validation of candidate loci (TAGAP, IL18R1, CCR9, CTLA4, etc.).

### Gap 6: DQ8-Specific Pathogenic Differences

**Scope:** HLA-DQ8-mediated CeD shows distinct epitope preferences, less absolute deamidation dependence, and different protease sensitivity ([PMID: 17629515](https://pubmed.ncbi.nlm.nih.gov/17629515/)). Whether DQ8 patients respond differently to TG2 inhibitors or peptide immunotherapy is not established.

**What would resolve it:** Stratified analysis of ZED1227 or future therapeutic trials by DQ2 vs. DQ8 genotype.

{{figure:knowledge_gaps.png|caption=Knowledge gap resolution tracker across five iterations of investigation, showing which gaps were partially resolved, which remain fully open, and which new gaps emerged.}}

---

## Alternative and Competing Models

### 1. IL-15/Innate Immunity–First Model
**Relationship:** Parallel mechanism and upstream modifier of the canonical model.
**Claim:** Epithelial stress and IL-15 overexpression are the primary initiating events; the adaptive gluten response is a secondary amplifier. Supported by evidence that family members without adaptive antigluten immunity already show epithelial stress, HSP overexpression, and IL-15 upregulation ([PMID: 26001928](https://pubmed.ncbi.nlm.nih.gov/26001928/)).
**Assessment:** Complementary rather than competing — the three-signal model integrates both.

### 2. Barrier Dysfunction / Zonulin Model
**Relationship:** Alternative mechanism for gluten access to lamina propria.
**Claim:** Increased paracellular permeability via zonulin-mediated tight junction disassembly is the primary route of gluten entry. Supported by larazotide proof-of-concept studies ([PMID: 17697209](https://pubmed.ncbi.nlm.nih.gov/17697209/)).
**Assessment:** Weakened by larazotide's failure of the primary permeability endpoint in meta-analysis ([PMID: 34339872](https://pubmed.ncbi.nlm.nih.gov/34339872/)) and the mouse study showing paracellular blockade does not prevent bacterial translocation ([PMID: 21822909](https://pubmed.ncbi.nlm.nih.gov/21822909/)). Transcellular IgA-CD71 retrotranscytosis appears dominant.

### 3. ATI/TLR4 Innate Adjuvant Model
**Relationship:** Parallel mechanism and amplifier.
**Claim:** Non-gluten wheat components (ATIs) activate innate immunity via TLR4, lowering the threshold for adaptive immune activation ([PMID: 27993525](https://pubmed.ncbi.nlm.nih.gov/27993525/); [PMID: 29574077](https://pubmed.ncbi.nlm.nih.gov/29574077/)). Modern hexaploid wheat has higher ATI bioactivity than ancient varieties.
**Assessment:** Complementary — ATIs act as adjuvants for the canonical pathway, not as an independent cause.

### 4. Microbiome-Epigenetic Model
**Relationship:** Upstream modifier.
**Claim:** Gut dysbiosis and microbial metabolites (reduced butyrate, altered SCFAs) drive epigenetic changes that promote loss of tolerance through altered Treg function and barrier integrity ([PMID: 42016930](https://pubmed.ncbi.nlm.nih.gov/42016930/); [PMID: 40133841](https://pubmed.ncbi.nlm.nih.gov/40133841/)).
**Assessment:** Correlative evidence only. No causal human study demonstrates that microbiome manipulation prevents or treats CeD.

### 5. Viral Tolerance-Breaking Model
**Relationship:** Upstream trigger.
**Claim:** Enteric viral infections (especially reovirus) break oral tolerance via type I interferon responses that reprogram tolerogenic dendritic cells ([PMID: 28386004](https://pubmed.ncbi.nlm.nih.gov/28386004/); [PMID: 33134034](https://pubmed.ncbi.nlm.nih.gov/33134034/)).
**Assessment:** Best experimental model for tolerance breakdown but mouse-only. Human longitudinal virome studies needed.

---

## Discriminating Tests

### Test 1: Anti-IL-15 Monotherapy in Active CeD
**Design:** RCT of anti-IL-15 monoclonal antibody vs. placebo in active CeD patients on gluten-containing diet.
**Stratification:** HLA-DQ2 homozygotes vs. heterozygotes vs. DQ8.
**Readout:** Villous height:crypt depth ratio, IEL counts, NKG2D expression, symptom scores.
**Expected result (if three-signal model correct):** IL-15 blockade should reduce villous atrophy even without GFD or TG2 inhibition, as it removes one of three required signals.

### Test 2: Combinatorial TG2 Inhibitor + Anti-IL-15
**Design:** 2×2 factorial RCT of ZED1227 ± anti-IL-15 during gluten challenge.
**Readout:** Mucosal transcriptome, IEL phenotype, villous morphometry.
**Expected result:** Synergistic protection if innate and adaptive arms are independent co-requirements; additive if they operate in series.

### Test 3: Prospective Virome Sequencing in At-Risk Infants
**Design:** Extension of TEDDY/PreventCD birth cohorts with serial fecal virome sequencing, mucosal sampling, and immune phenotyping in HLA-DQ2/DQ8+ infants.
**Biomarkers:** Anti-TG2 seroconversion, IFN-α signature, Treg/Teff ratio.
**Expected result:** Identification of specific viral exposure windows preceding tolerance breakdown.

### Test 4: CD71 Blockade in Mouse Model
**Design:** Anti-CD71 antibody or CD71 conditional knockout in HLA-DQ8/IL-15 transgenic mice during gluten challenge.
**Readout:** Gliadin peptide delivery to lamina propria (fluorescent tracking), villous morphometry.
**Expected result:** If IgA-CD71 retrotranscytosis is the dominant gluten access route, CD71 blockade should substantially reduce mucosal damage even with intact paracellular permeability.

### Test 5: ZED1227 Efficacy Stratified by HLA-DQ Genotype
**Design:** Post-hoc or prospective analysis of ZED1227 phase 3 data comparing DQ2 homozygous, DQ2 heterozygous, and DQ8 patients.
**Expected result:** If DQ8-mediated disease is less deamidation-dependent ([PMID: 17629515](https://pubmed.ncbi.nlm.nih.gov/17629515/)), TG2 inhibition may show attenuated efficacy in DQ8 patients.

---

## Curation Leads

*The following are candidate updates for the Disorder Mechanisms Knowledge Base. All require curator verification.*

### Candidate Evidence References

1. **ZED1227 RCT** ([PMID: 34192430](https://pubmed.ncbi.nlm.nih.gov/34192430/)): Snippet — *"In celiac disease, small intestinal transglutaminase 2 causes deamidation of glutamine residues in gluten peptides, which enhances stimulation of T cells and leads to mucosal injury. Inhibition of transglutaminase 2 is a potential treatment for celiac disease."* → SUPPORT, Human clinical RCT.

2. **Three-signal model** ([PMID: 32051586](https://pubmed.ncbi.nlm.nih.gov/32051586/)): Establishes IL-15 as co-required with HLA-DQ and gluten for villous atrophy → QUALIFY, Model organism.

3. **IgA-CD71 retrotranscytosis** ([PMID: 22750506](https://pubmed.ncbi.nlm.nih.gov/22750506/)): Snippet — *"SIgA-CD71 complexes were internalized and localized in early endosomes and recycling compartments but not in lysosomes. In the presence of celiac IgA or SIgA against p31-49, transport of intact 3H-p31-49 increased significantly across Caco-2 monolayers."* → QUALIFY (re: gluten access mechanism).

4. **Nexvax2 failure** ([PMID: 36898393](https://pubmed.ncbi.nlm.nih.gov/36898393/)): Snippet — *"A gluten-free diet is insufficient to treat coeliac disease because intestinal injury persists and acute reactions with cytokine release follow gluten exposure."* → QUALIFY (targeting dominant T cell epitopes alone is insufficient).

5. **Reovirus tolerance breaking** ([PMID: 28386004](https://pubmed.ncbi.nlm.nih.gov/28386004/)): Demonstrates viral trigger for loss of oral tolerance in HLA-DQ mice → SUPPORT (upstream trigger, mouse model only).

6. **B cell APC role** ([PMID: 31285344](https://pubmed.ncbi.nlm.nih.gov/31285344/)): Snippet — *"Production of antibodies against N-terminal epitopes coincided with clinical onset of disease, suggesting that TG2-reactive B cells with certain epitope specificities could be the main antigen-presenting cells for pathogenic, gluten-specific T cells."* → SUPPORT (feedback loop mechanism).

7. **RCD II gluten independence** ([PMID: 28188172](https://pubmed.ncbi.nlm.nih.gov/28188172/)): Snippet — *"Dominant TCRβ sequences identified in patients with RCD type II are unique and not homologous to known gliadin-specific TCR sequences, supporting the assumption that these clonal T-cells expand independent of gluten stimulation."* → QUALIFY (boundary condition).

8. **ATI/TLR4 innate activation** ([PMID: 27993525](https://pubmed.ncbi.nlm.nih.gov/27993525/)): Snippet — *"Wheat amylase-trypsin inhibitors (ATIs) are nutritional activators of innate immunity, via activation of the toll-like receptor 4 (TLR4) on myeloid cells."* → COMPETING/COMPLEMENTARY (parallel innate mechanism).

### Candidate Pathophysiology Nodes/Edges

- **Add node:** IL-15/NKG2D/MICA innate immune arm as co-required signal for villous atrophy
- **Add node:** IgA-CD71 retrotranscytosis as primary gluten delivery mechanism
- **Add edge:** IFN-γ → thioredoxin → TG2 activation (positive feedback loop)
- **Add edge:** TG2-reactive B cells → gluten peptide presentation to T cells (B cell APC loop)
- **Add edge:** Wheat ATIs → TLR4 → innate immune activation (parallel amplifier)
- **Modify edge:** Paracellular permeability → gluten access (downgrade from primary to secondary mechanism)
- **Modify description:** Cytokine response from "Th1/IFN-γ" to "mixed Th1/Th17/IL-21"

### Candidate Ontology Terms

- **Cell types:** CD4+ gluten-specific T cells (CL:0000492), intraepithelial lymphocytes (CL:0000084), TG2-reactive B cells, plasmacytoid dendritic cells
- **Biological processes:** GO:0002224 (toll-like receptor signaling), GO:0006968 (cellular defense response), GO:0002291 (T cell activation via T cell receptor contact with antigen bound to MHC molecule)
- **Disease subtypes:** Seronegative CeD, Refractory CeD type II, Potential CeD, Dermatitis herpetiformis

### Candidate Subtype Restrictions

- The canonical model applies most completely to **HLA-DQ2.5 homozygous, seropositive, active CeD** (Marsh III)
- **Seronegative CeD** (1.7%): Core T cell pathway preserved; antibody arm is absent → QUALIFY
- **RCD type II**: Gluten-independent; represents boundary condition → QUALIFY
- **DQ8-mediated CeD**: Distinct epitope preferences, less deamidation dependence → QUALIFY
- **Potential CeD**: Adaptive immunity activated without tissue damage; 32% spontaneously resolve → QUALIFY

### Candidate Knowledge Gap Entries

1. **Tolerance breakdown trigger:** No prospective human study identifies the specific event(s) breaking oral tolerance. Scope: upstream of entire cascade. Priority: CRITICAL.
2. **Anti-IL-15 human efficacy data:** Strong preclinical rationale but no published phase 2+ trial. Scope: therapeutic validation of innate arm. Priority: HIGH.
3. **Integrated feedback loop dynamics:** Individual loops demonstrated but never tested as a system. Priority: MEDIUM.
4. **Non-HLA heritability:** >50% unexplained. No GenCC/ClinGen validity assessment for non-HLA loci. Priority: MEDIUM.
5. **DQ8-specific therapeutic response:** Unknown whether TG2 inhibitor efficacy differs by genotype. Priority: MEDIUM.

### Candidate Status Change

**Recommended status:** Retain **CANONICAL** with annotation: "Requires five mechanistic expansions (three-signal model, Th1/Th17/IL-21 cytokines, three feedback loops, ATI/TLR4 innate arm, transcellular gluten transport) and documentation of boundary conditions (seronegative CeD, RCD II, DQ8 differences, potential CeD spontaneous resolution)."

---

## Limitations of This Evaluation

1. **Search scope:** 130 papers were reviewed, but the CeD literature exceeds 10,000 publications. Important niche findings may have been missed, particularly in non-English literature and conference abstracts.

2. **Temporal bias:** The search naturally favored recent publications (2020–2026). Foundational studies from the 1990s–2000s were included via citations in reviews but may not have been comprehensively captured.

3. **Absence evidence vs. evidence of absence:** For knowledge gaps (e.g., no anti-IL-15 human trial), we report absence of evidence from our search, not definitive evidence of absence. Unpublished or ongoing trials may exist.

4. **Mouse-to-human translation:** Several key findings (three-signal model, reovirus tolerance breaking, ATI effects) derive primarily from mouse models. Confirmation in human studies is pending.

5. **Organoid and in vitro limitations:** Feedback loop evidence comes from reductionist systems (Caco-2 monolayers, co-cultures) that may not fully recapitulate in vivo tissue architecture and immune complexity.

---

## Proposed Follow-Up Experiments and Actions

1. **Prioritize anti-IL-15/anti-IL-15Rα RCT data acquisition** — Monitor clinical trial registries for AMG 714 or similar agents in CeD/RCD and flag for KB update when published.

2. **Request ZED1227 phase 3 stratified analysis** by DQ2 vs. DQ8 genotype to test whether TG2 inhibitor efficacy differs by HLA subtype.

3. **Develop combinatorial perturbation framework** for testing feedback loop interactions in patient-derived intestinal organoids co-cultured with immune cells.

4. **Integrate TEDDY/PreventCD virome data** when available to assess viral trigger candidates in prospective human cohorts.

5. **Curate non-HLA GWAS loci** against functional databases (eQTL, chromatin accessibility) to prioritize candidates for the unexplained heritability gap.

6. **Assess ATI content in modern vs. ancient wheat varieties** in the context of CeD prevalence trends across populations with different wheat consumption histories.

---

*Report generated through systematic evaluation of 130 primary papers across 5 investigation iterations. All citations verified against PubMed abstracts. Findings recorded in the OpenScientist knowledge state for provenance tracking.*
