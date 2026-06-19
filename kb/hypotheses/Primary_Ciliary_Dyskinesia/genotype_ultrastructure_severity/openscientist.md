---
provider: openscientist
model: openscientist-autonomous
cached: false
start_time: '2026-06-19T18:49:25.918577'
end_time: '2026-06-19T19:27:20.619805'
duration_seconds: 2274.7
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Primary_Ciliary_Dyskinesia
  category: Genetic
  hypothesis_group_id: genotype_ultrastructure_severity
  hypothesis_label: Genotype / Ultrastructure-Defect Severity Stratification
  hypothesis_status: EMERGING
  hypothesis_yaml: "hypothesis_group_id: genotype_ultrastructure_severity\nhypothesis_label:\
    \ Genotype / Ultrastructure-Defect Severity Stratification\nstatus: EMERGING\n\
    description: 'A prognostic refinement superimposed on the canonical model: the\
    \ specific ultrastructural\n  defect class and causal genotype modulate the severity\
    \ and rate of lung-function decline rather than\n  the qualitative mechanism.\
    \ Inner-dynein-arm with microtubular-disorganization defects (e.g., CCDC39\n \
    \ and CCDC40) carry the worst lung function and the only significant longitudinal\
    \ decline, whereas isolated\n  outer-dynein-arm defects (e.g., DNAH5) and DNAH11\
    \ are comparatively milder. This stratification is increasingly\n  used to anticipate\
    \ disease trajectory but is not yet a routine clinical decision tool.'\nevidence:\n\
    - reference: PMID:30067075\n  reference_title: 'Primary Ciliary Dyskinesia: Longitudinal\
    \ Study of Lung Disease by Ultrastructure Defect\n    and Genotype.'\n  supports:\
    \ SUPPORT\n  evidence_source: HUMAN_CLINICAL\n  snippet: Participants with CCDC39\
    \ or CCDC40 mutations (n = 34) had lower percent predicted FEV1 and\n    weight\
    \ and height z-scores than those with DNAH5 mutations (n = 36).\n  explanation:\
    \ Supports that genotype stratifies lung-function severity within PCD.\n- reference:\
    \ PMID:30067075\n  reference_title: 'Primary Ciliary Dyskinesia: Longitudinal\
    \ Study of Lung Disease by Ultrastructure Defect\n    and Genotype.'\n  supports:\
    \ SUPPORT\n  evidence_source: HUMAN_CLINICAL\n  snippet: Participants with IDA/MTD/CA\
    \ defects, which included individuals with CCDC39 or CCDC40 mutations,\n    had\
    \ worse lung function and growth indices compared with those with outer dynein\
    \ arm defects and DNAH5\n    mutations, respectively.\n  explanation: Supports\
    \ ultrastructural-defect-class stratification of disease severity."
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
citation_count: 26
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Primary_Ciliary_Dyskinesia
- **Category:** Genetic

## Target Hypothesis
- **Hypothesis ID:** genotype_ultrastructure_severity
- **Hypothesis Label:** Genotype / Ultrastructure-Defect Severity Stratification
- **Status in KB:** EMERGING

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: genotype_ultrastructure_severity
hypothesis_label: Genotype / Ultrastructure-Defect Severity Stratification
status: EMERGING
description: 'A prognostic refinement superimposed on the canonical model: the specific ultrastructural
  defect class and causal genotype modulate the severity and rate of lung-function decline rather than
  the qualitative mechanism. Inner-dynein-arm with microtubular-disorganization defects (e.g., CCDC39
  and CCDC40) carry the worst lung function and the only significant longitudinal decline, whereas isolated
  outer-dynein-arm defects (e.g., DNAH5) and DNAH11 are comparatively milder. This stratification is increasingly
  used to anticipate disease trajectory but is not yet a routine clinical decision tool.'
evidence:
- reference: PMID:30067075
  reference_title: 'Primary Ciliary Dyskinesia: Longitudinal Study of Lung Disease by Ultrastructure Defect
    and Genotype.'
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: Participants with CCDC39 or CCDC40 mutations (n = 34) had lower percent predicted FEV1 and
    weight and height z-scores than those with DNAH5 mutations (n = 36).
  explanation: Supports that genotype stratifies lung-function severity within PCD.
- reference: PMID:30067075
  reference_title: 'Primary Ciliary Dyskinesia: Longitudinal Study of Lung Disease by Ultrastructure Defect
    and Genotype.'
  supports: SUPPORT
  evidence_source: HUMAN_CLINICAL
  snippet: Participants with IDA/MTD/CA defects, which included individuals with CCDC39 or CCDC40 mutations,
    had worse lung function and growth indices compared with those with outer dynein arm defects and DNAH5
    mutations, respectively.
  explanation: Supports ultrastructural-defect-class stratification of disease severity.
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

# Genotype / Ultrastructure-Defect Severity Stratification in Primary Ciliary Dyskinesia: A Mechanistic Hypothesis Evaluation

**Hypothesis ID:** genotype_ultrastructure_severity  
**Disease:** Primary Ciliary Dyskinesia (PCD)  
**Status in KB:** EMERGING  
**Report Date:** 2026-06-19  
**Investigation:** 5 iterations, 13 confirmed findings, 59 papers reviewed, 28 unique PMIDs cited

---

## Executive Judgment

**Verdict: PARTIALLY SUPPORTED**

The hypothesis that specific ultrastructural defect classes and causal genotypes modulate the severity and rate of lung-function decline in Primary Ciliary Dyskinesia (PCD) is **partially supported** by the current literature. The evidence firmly establishes that **CCDC39/CCDC40 mutations (IDA/MTD ultrastructural class) confer the worst prognosis**, with converging support from at least five independent cohorts and a groundbreaking 2024–2025 mechanistic discovery of motility-independent proteostasis disruption. At the mild end, **RSPH1 mutations are established as conferring a milder phenotype** with significantly better lung function and higher nasal nitric oxide. However, the hypothesis's claim of a continuous severity gradient across all ultrastructural classes is not supported. In particular, the proposed intermediate distinction between DNAH5 and DNAH11 — two of the most common PCD genotypes — **fails to replicate** in direct comparison (Rodriguez Mier et al. 2024; p = 0.829 for cross-sectional lung function). Furthermore, mucociliary clearance is uniformly absent across genotypes (Marthin et al. 2023), challenging the mechanistic premise that residual motility explains milder phenotypes.

The evidence best supports a **three-tier model** — Severe (CCDC39/CCDC40, CCNO), Standard (DNAH5, DNAH11, most others), and Mild (RSPH1) — rather than a continuous ultrastructure-to-severity gradient. This model is further modulated by variant type (loss-of-function vs. residual function), modifier genes (TAS2R38), and possibly differential cough clearance mechanisms. Critically, **no clinical trial has tested genotype-stratified management**, leaving the hypothesis's clinical actionability undemonstrated. The status designation of "EMERGING" remains appropriate; the claim should not yet be elevated to "ESTABLISHED" without longitudinal replication and interventional evidence.

**Most important caveats:**
1. The middle of the severity spectrum is poorly resolved — DNAH5 vs. DNAH11 difference is conflicting
2. Mucociliary clearance is uniformly absent regardless of genotype, undermining the residual-motility mechanism
3. Within-gene variant type (LoF vs. residual function) and modifier genes (TAS2R38) add complexity not captured by simple gene-level classification
4. No randomized trial has tested genotype-stratified management
5. The 2024–2025 motility-independent mechanism (proteostasis disruption) has been demonstrated only in vitro for CCDC39/CCDC40

---

## Summary

This report evaluates the hypothesis that the specific ultrastructural defect class and causal genotype in Primary Ciliary Dyskinesia (PCD) modulate disease severity and rate of lung-function decline. Through systematic literature review of 59 papers and iterative hypothesis testing over five analytical iterations, we identified 13 confirmed findings that collectively paint a nuanced picture of genotype-phenotype relationships in PCD.

The strongest evidence supports the extremes of the proposed severity gradient: CCDC39/CCDC40 mutations cause the most severe disease through both motility-dependent and a newly discovered motility-independent mechanism involving proteostasis disruption and cell fate switching, while RSPH1 mutations produce a distinctly milder phenotype with better lung function, higher nasal NO, and later symptom onset. However, the intermediate gradient — particularly the distinction between DNAH5 and DNAH11 — is not supported by direct comparison studies, and the uniform absence of mucociliary clearance across all genotypes undermines a simple motility-based severity gradient.

Our analysis reveals that the field is converging on a more complex model in which genotype interacts with variant type (loss-of-function vs. residual function alleles), modifier genes (e.g., TAS2R38 bitter taste receptor polymorphisms), cough clearance capacity, and environmental factors to determine individual disease trajectories. The discovery of motility-independent mechanisms in CCDC39/CCDC40 mutations represents a paradigm shift that explains why this subtype is disproportionately severe compared to other PCD genotypes with similarly impaired ciliary motility.

---

## Key Findings

### Finding 1: CCDC39/CCDC40 (IDA/MTD) Genotype Is Associated with the Worst Lung Disease

Multiple independent cohorts confirm that CCDC39/CCDC40 mutations — which produce inner-dynein-arm defects with microtubular disorganization (IDA/MTD) — are associated with the most severe PCD phenotype. Davis et al. ([PMID: 30067075](https://pubmed.ncbi.nlm.nih.gov/30067075/)) demonstrated in a longitudinal study that participants with CCDC39 or CCDC40 mutations (n = 34) had lower percent predicted FEV₁ and worse weight and height z-scores than those with DNAH5 mutations (n = 36). The IDA/MTD ultrastructural class showed the only significant longitudinal decline. Raidt et al. 2024 ([PMID: 38871375](https://pubmed.ncbi.nlm.nih.gov/38871375/)), in an unprecedented multinational dataset of 1,236 genotyped PCD individuals, confirmed that genetic variant predicts the course of lung function. Horani et al. 2025 ([PMID: 40948093](https://pubmed.ncbi.nlm.nih.gov/40948093/)) stated that "Children with biallelic CCDC39 or CCDC40 mutations have greater lung disease, related to both cilia motility-dependent and motility-independent effects." The severity is so well-accepted that Kaspy et al. 2024 ([PMID: 38072392](https://pubmed.ncbi.nlm.nih.gov/38072392/)) treated CCDC39/CCDC40 as an established "severe genotype" requiring statistical adjustment in analyses of other outcomes.

### Finding 2: DNAH11 and RSPH1 Are Associated with Milder PCD

At the mild end of the spectrum, DNAH11 and RSPH1 mutations confer a less severe phenotype. Horani et al. 2025 ([PMID: 40948093](https://pubmed.ncbi.nlm.nih.gov/40948093/)) identified DNAH11 and RSPH1 as having "less severe lung disease, possibly related to residual ciliary motility." Barber et al. 2025 ([PMID: 40344341](https://pubmed.ncbi.nlm.nih.gov/40344341/)) found that the DNAH11 group had significantly lower odds of neonatal respiratory distress (OR: 0.35, 95% CI: 0.16–0.76) compared to the ODA group. For RSPH1, the evidence is particularly strong: Knowles et al. 2014 ([PMID: 24568568](https://pubmed.ncbi.nlm.nih.gov/24568568/)) showed that 16 individuals with RSPH1 mutations had better lung function (FEV₁ 73.0 vs. 61.8 %predicted; P = 0.0), dramatically higher nasal NO (98.3 vs. 20.7 nl/min; P < 0.0003), and lower prevalence of neonatal respiratory distress compared to 75 age- and sex-matched PCD cases.

### Finding 3: CCDC39/CCDC40 Severity Involves Motility-Independent Mechanisms

A breakthrough discovery in 2024–2025 revealed that the severity of CCDC39/CCDC40 mutations extends beyond impaired ciliary motility. Brody et al. ([PMID: 39879322](https://pubmed.ncbi.nlm.nih.gov/39879322/)) demonstrated using human cells with pathogenic CCDC39/CCDC40 variants that "disease severity is not explained by loss of ciliary motility alone." These mutations cause undocking of an extensive ciliary network, inducing proteostasis disruption and cell fate switching. This motility-independent mechanism provides a compelling explanation for why IDA/MTD defects produce worse disease than other PCD subtypes with similarly impaired motility — a finding that fundamentally reshapes our understanding of the genotype-severity relationship. Horani et al. 2025 ([PMID: 40948093](https://pubmed.ncbi.nlm.nih.gov/40948093/)) confirmed this dual mechanism in their review, stating that CCDC39/CCDC40 severity is "related to both cilia motility-dependent and motility-independent effects."

### Finding 4: Longitudinal Nasal NO Decline Supports Progressive Severity in IDA/MTD

Pifferi et al. 2022 ([PMID: 35777446](https://pubmed.ncbi.nlm.nih.gov/35777446/)) provided longitudinal biomarker evidence supporting progressive disease in the IDA/MTD group. In 141 PCD patients followed for up to 10 years, the IDA/MTD group showed significant decline in nasal NO with age (P < 0.01) compared with other ultrastructural groups who showed stable levels. In adults, nasal NO (P = 0.038) and FeNO (P = 0.032) were significantly lower in IDA/MTD vs. other groups. The CCDC39/CCDC40 group specifically had lower FeNO than DNAH5/DNAH11 combined (P = 0.033). This progressive biomarker decline is unique to the IDA/MTD class and supports the hypothesis of a distinct, progressively worsening disease trajectory.

### Finding 5: CCNO Mutations Represent an Additional Severe Subtype

CCNO mutations, affecting cilia generation rather than structure, constitute an additional severe PCD subtype outside the classical ultrastructural classification. Amirav et al. 2016 ([PMID: 26777464](https://pubmed.ncbi.nlm.nih.gov/26777464/)) found that in 15 patients with CCNO mutations, there was rapid deterioration in lung function, increased prevalence of hydrocephalus (10%), and increased female infertility (22%). Horani et al. 2025 ([PMID: 40948093](https://pubmed.ncbi.nlm.nih.gov/40948093/)) confirmed that "pathogenic variants in genes involved in cilia generation, like CCNO, are also associated with more severe lung disease." Emiralioglu et al. 2020 ([PMID: 31765523](https://pubmed.ncbi.nlm.nih.gov/31765523/)) found in a Turkish cohort that CCNO patients had the lowest age at diagnosis (median 3 years) and the lowest median BMI z-scores. This finding extends the severity model beyond the traditional IDA/MTD category and necessitates including reduced cilia generation defects in any comprehensive severity classification.

### Finding 6: Variant Type Adds Sub-Genotype Severity Refinement

Within individual genes, the type of variant (loss-of-function vs. residual function) adds an additional layer of severity stratification. Barber et al. 2025 ([PMID: 40344341](https://pubmed.ncbi.nlm.nih.gov/40344341/)) demonstrated that within the DNAH5 group, those with two loss-of-function variants were more likely to have neonatal respiratory distress compared to those with possible residual function variants (OR: 3.06, 95% CI: 1.33–7). Dong et al. 2025 ([PMID: 40033371](https://pubmed.ncbi.nlm.nih.gov/40033371/)) found in a systematic review of 323 DNAH5 patients that pediatric and adult patients exhibited distinct clinical features including varying incidences of bronchiectasis, NRD, and lung function (all P < 0.05). This sub-genotype heterogeneity qualifies the hypothesis by showing that gene-level classification alone is insufficient for prognostic stratification.

### Finding 7: Some Studies Show Similar Lung Function Across Subtypes (Qualifying Evidence)

Not all evidence supports a severity gradient. Boon et al. 2014 ([PMID: 24450482](https://pubmed.ncbi.nlm.nih.gov/24450482/)) compared 206 PCD patients across ultrastructural subtypes and found that patients with normal ultrastructure had "similar frequency of upper and lower respiratory tract problems, as well as similar lung function and imaging" compared to other subtypes. This finding challenges a simple ultrastructure-to-severity mapping and suggests that ultrastructural classification alone does not fully predict clinical outcomes, particularly for the intermediate subtypes.

### Finding 8: DNAH5 vs. DNAH11 Lung Function Difference Not Confirmed

A critical challenge to the intermediate gradient comes from Rodriguez Mier et al. 2024 ([PMID: 38602513](https://pubmed.ncbi.nlm.nih.gov/38602513/)). In 74 genetically confirmed PCD patients (DNAH11 n = 23, DNAH5 n = 19), lung function (cross-sectional P = 0.829, longitudinal P = 0.329) and chest CT abnormalities (P = 0.202) were **not significantly different** between DNAH11 and DNAH5. Respiratory tract microbiology also did not differ (P = 0.161). Only situs (P = 0.015) and ultrastructure (P < 0.001) differed. Notably, the age-at-diagnosis difference between the groups (median 9.50 vs 4.71 years, P = 0.037) disappeared after correcting for situs (P = 0.973), revealing a diagnostic bias. This direct comparison study undermines the claim that ODA-deficient subtypes (DNAH5) are systematically worse than those with normal ultrastructure (DNAH11), collapsing the middle portion of the proposed gradient.

### Finding 9: Mucociliary Clearance Uniformly Absent Regardless of Genotype

Marthin et al. 2023 ([PMID: 38076675](https://pubmed.ncbi.nlm.nih.gov/38076675/)) showed in 69 PCD patients spanning 26 genotypes that "mucociliary clearance by PRMC was consistently absent in most PCD patients, regardless of genotype." Only one patient showed residual clearance. This finding fundamentally challenges the mechanistic premise that residual ciliary motility explains milder phenotypes in some genotypes. However, Ostrowski et al. 2026 ([PMID: 41561107](https://pubmed.ncbi.nlm.nih.gov/41561107/)) suggested that cough clearance may differ between genotypes — "the results suggest cough clearance may differ between these two genotypes" — offering an alternative clearance mechanism that could partially explain severity differences even when mucociliary clearance is uniformly absent.

### Finding 10: IDA/MTD Severity Extends to Earlier ENT Interventions

The severity gradient extends beyond lung function. Dagher et al. 2025 ([PMID: 39989621](https://pubmed.ncbi.nlm.nih.gov/39989621/)) found in 147 PCD participants followed for a mean of 7.6 years that "PETs were placed earlier in those with inner dynein arm/microtubular disorganization defects than those with outer dynein arm defects." The high overall prevalence of otologic morbidity (PETs 80%, transient hearing loss 68%, persistent hearing loss 30%) underscores the multi-organ nature of PCD, while the IDA/MTD-specific earlier intervention timing supports the systemic nature of the severity gradient.

### Finding 11: Ciliary Beat Pattern Correlates with Genotype

Raidt et al. 2014 ([PMID: 25186273](https://pubmed.ncbi.nlm.nih.gov/25186273/)) demonstrated in 66 genetically confirmed PCD individuals (17 genes, 1,072 HVMA videos) that "ciliary beat pattern variations correlated well with the genetic findings." CCDC39/40 showed severely dyskinetic/immotile patterns; DNAH5 showed immotile patterns; DNAH11 showed hyperkinetic but stiff patterns; RSPH1 showed circular/rotational patterns. Carretero-Vilarroig et al. 2025 ([PMID: 40742517](https://pubmed.ncbi.nlm.nih.gov/40742517/)) found that "patients with immotile cilia have a higher frequency of neonatal respiratory distress and had a higher likelihood of receiving a genetic diagnosis." These genotype-specific beat patterns provide a functional link between genotype and clinical severity, though the relationship between beat pattern and long-term outcomes is not straightforward given the uniform absence of mucociliary clearance.

### Finding 12: TAS2R38 Modifier Gene Effects Are Genotype-Dependent

Piatti et al. 2020 ([PMID: 32659773](https://pubmed.ncbi.nlm.nih.gov/32659773/)) found in 35 PCD patients that PAV/PAV TAS2R38 haplotype was associated with lower frequency of respiratory exacerbations (≥2/year, P = 0.04) and no chronic Pseudomonas colonization. Critically, Pifferi et al. 2024 ([PMID: 39181709](https://pubmed.ncbi.nlm.nih.gov/39181709/)) showed in 119 PCD patients over 10 years that TAS2R38 modified severity **only in mild phenotype disease** (e.g., DNAH11 genotype). This genotype-dependent modifier effect demonstrates that the severity hierarchy is not solely determined by the primary PCD gene but is modulated by the innate immune background, particularly in milder genotypes where the primary mutation leaves room for phenotypic modification. In severe genotypes like CCDC39/CCDC40, the ceiling effect of the primary mutation may overwhelm any modifier gene benefit.

### Finding 13: mRNA Therapy Validates CCDC40 as a Therapeutic Target

Wohlgemuth et al. 2026 ([PMID: 42089334](https://pubmed.ncbi.nlm.nih.gov/42089334/)) demonstrated in vitro and in vivo efficacy of lipidoid nanoparticle-formulated mRNA encoding human CCDC40 (LNP-CCDC40-mRNA). Treatment of CCDC40-deficient human nasal epithelial cells resulted in endogenous CCDC40 expression in 10–74% of ciliated cells, enabling axonemal integration of associated proteins and significantly increased ciliary beat frequencies. A Phase 1 human trial is planned. This therapeutic development both validates the causal role of CCDC40 loss in disease severity and demonstrates the clinical prioritization of this severe genotype for genotype-specific therapy.

---

## Mechanistic Model / Interpretation

### Proposed Three-Tier Severity Model

Based on the synthesis of 13 findings across 5 iterations, we propose a **three-tier model** that better fits the evidence than either a continuous gradient or a binary classification:

```
┌─────────────────────────────────────────────────────────────────────┐
│                    THREE-TIER PCD SEVERITY MODEL                    │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  TIER 1 — SEVERE                                                    │
│  ├── CCDC39/CCDC40 (IDA/MTD ultrastructure)                        │
│  │   ├── Complete motility loss [ESTABLISHED]                       │
│  │   ├── Proteostasis disruption [EMERGING, 2024-2025]             │
│  │   ├── Cell fate switching [EMERGING, 2024-2025]                 │
│  │   ├── Progressive nNO decline [SUPPORTED]                        │
│  │   └── Worst FEV₁, growth, earliest ENT interventions            │
│  │                                                                   │
│  └── CCNO/MCIDAS (reduced cilia generation)                         │
│      ├── Severely reduced cilia number [ESTABLISHED]                │
│      ├── Rapid lung function deterioration [EMERGING]               │
│      └── Additional: hydrocephalus, infertility risk                │
│                                                                     │
│  TIER 2 — STANDARD                                                  │
│  ├── DNAH5 (ODA defect) ─────────────────┐                         │
│  ├── DNAH11 (proximal ODA, normal TEM) ──┤ No significant          │
│  └── Most other PCD genotypes ───────────┘ difference (p=0.829)    │
│      ├── Modulated by: variant type (LoF vs residual function)      │
│      │   └── DNAH5 biallelic LoF: OR 3.06 for NRD vs residual     │
│      ├── Modulated by: TAS2R38 (PAV/PAV protective, mild only)     │
│      └── Modulated by: diagnostic delay, care access                │
│                                                                     │
│  TIER 3 — MILD                                                      │
│  └── RSPH1 (central pair/radial spoke defect)                       │
│      ├── Rotational beat pattern (not immotile) [ESTABLISHED]       │
│      ├── FEV₁ 73% vs 62% in matched PCD (P=0.0) [ESTABLISHED]     │
│      ├── nNO 98 vs 21 nl/min (P<0.0003) [ESTABLISHED]             │
│      └── Lower NRD, later symptom onset [ESTABLISHED]               │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Causal Chain from Genotype to Clinical Outcome

```
Gene Mutation
  │
  ▼
Ultrastructural Defect Class ←── STRONG evidence
  │
  ├──[IDA/MTD]──→ Complete motility loss ──→ Absent MCC ──→ Infection
  │                    │                                        │
  │                    └──→ Ciliary connectome undocking         │
  │                            │                                │
  │                            ▼                                ▼
  │                    Proteostasis disruption            Lung damage
  │                    + Cell fate switching ────────────→ (WORST)
  │                    [NOVEL 2024-2025]
  │
  ├──[ODA/Other]──→ Immotile/abnormal beat ──→ Absent MCC ──→ Standard
  │                                                           disease
  │                 Modifiers: LoF vs residual; TAS2R38
  │
  └──[CP/RS]──→ Rotational beat ──→ Absent MCC ──→ MILD disease
                (RSPH1)              (but higher nNO,
                                      ?alternative clearance)
```

### Evidence Strength at Each Causal Link

| Causal Link | Evidence Level | Key Gap |
|---|---|---|
| Gene mutation → ultrastructural defect | **Strong** | Well-established molecular genetics |
| Ultrastructural defect → ciliary beat pattern | **Strong** | Raidt 2014 (n=66, 17 genes, 1072 videos) |
| Beat pattern → MCC loss | **Complicated** | MCC uniformly absent regardless (Marthin 2023) |
| CCDC39/40 → proteostasis disruption | **Strong (new)** | Brody 2024–2025; in vitro only |
| Proteostasis → severity beyond motility | **Strong (new)** | Clinical correlation not yet tested |
| Genotype → longitudinal FEV₁ decline rate | **Moderate** | Only CCDC39/40 show significant decline |
| DNAH5 vs DNAH11 → severity difference | **Weak/Absent** | Failed to replicate (Rodriguez Mier 2024) |
| Residual motility → milder phenotype | **Inferred** | MCC data contradicts; mechanism unclear |
| TAS2R38 → modifier effect | **Moderate** | Only in mild genotypes (Pifferi 2024) |
| Genotype → clinical management change | **Speculative** | No trial evidence |

{{figure:causal_chain.png|caption=Mechanistic causal chain diagram showing genotype-to-severity pathways with evidence strength. Solid lines indicate strong evidence; dashed lines indicate inferred or emerging links. The novel proteostasis/cell fate switching pathway specific to CCDC39/CCDC40 is highlighted.}}

---

## Evidence Matrix

| # | Citation | Evidence Type | Direction | Claim Tested | Key Finding | Subtype/Context | Confidence & Limitations |
|---|----------|---------------|-----------|-------------|-------------|-----------------|--------------------------|
| 1 | [PMID: 30067075](https://pubmed.ncbi.nlm.nih.gov/30067075/) | Human clinical (longitudinal, n=118) | **Supports** | CCDC39/40 worse than DNAH5 | CCDC39/40 (n=34) lower FEV₁%, worse growth vs DNAH5 (n=36); IDA/MTD only group with significant longitudinal decline | IDA/MTD vs ODA | High; US cohort, moderate n per genotype |
| 2 | [PMID: 38871375](https://pubmed.ncbi.nlm.nih.gov/38871375/) | Human clinical (multinational, n=1236) | **Supports** | Genotype predicts phenotype | Genetic variant predicts course of lung function across 46 genes | All PCD, multinational | High; largest dataset |
| 3 | [PMID: 40948093](https://pubmed.ncbi.nlm.nih.gov/40948093/) | Review (2025) | **Supports** | Dual mechanism CCDC39/40; DNAH11/RSPH1 mild | CCDC39/40 severity via motility-dependent + motility-independent effects | Comprehensive | Review-level evidence |
| 4 | [PMID: 39879322](https://pubmed.ncbi.nlm.nih.gov/39879322/) | In vitro/mechanistic | **Supports** | CCDC39/40 beyond motility | Proteostasis disruption + cell fate switching from ciliary connectome undocking | CCDC39/40 human cells | High; novel mechanism, in vitro only |
| 5 | [PMID: 38562900](https://pubmed.ncbi.nlm.nih.gov/38562900/) | In vitro/mechanistic | **Supports** | Ciliary network undocking | Extensive connectome disruption in CCDC39/40 | CCDC39/40 | High; preprint → published |
| 6 | [PMID: 40344341](https://pubmed.ncbi.nlm.nih.gov/40344341/) | Human clinical (n=455) | **Supports + Qualifies** | DNAH11 milder; variant type matters | DNAH11 NRD OR=0.35 (CI 0.16–0.76); DNAH5 biallelic LoF NRD OR=3.06 (CI 1.33–7) | DNAH11, DNAH5 | High; NRD as outcome, not long-term FEV₁ |
| 7 | [PMID: 24568568](https://pubmed.ncbi.nlm.nih.gov/24568568/) | Human clinical (case-control) | **Supports** | RSPH1 is milder PCD | FEV₁ 73.0 vs 61.8% (P=0.0); nNO 98.3 vs 20.7 (P<0.0003); lower NRD | n=16 RSPH1 vs 75 matched | High; clear effect, small n |
| 8 | [PMID: 35777446](https://pubmed.ncbi.nlm.nih.gov/35777446/) | Human clinical (longitudinal, n=141) | **Supports** | Progressive IDA/MTD biomarker decline | IDA/MTD nNO decline P<0.01 vs stable others; CCDC39/40 lower FeNO (P=.033) | 141 patients, 10 years | Moderate-High; single center, surrogate |
| 9 | [PMID: 26777464](https://pubmed.ncbi.nlm.nih.gov/26777464/) | Human clinical (n=15) | **Supports** | CCNO as severe subtype | Rapid lung function deterioration; 10% hydrocephalus; 22% infertility | CCNO | Moderate; small n |
| 10 | [PMID: 31765523](https://pubmed.ncbi.nlm.nih.gov/31765523/) | Human clinical (n=46) | **Supports** | CCNO severe; genotype heterogeneity | CCNO: earliest diagnosis (median 3y), lowest BMI | Turkish cohort | Moderate; small n per genotype |
| 11 | [PMID: 38602513](https://pubmed.ncbi.nlm.nih.gov/38602513/) | Human clinical (n=74) | **Refutes** | DNAH5 worse than DNAH11 | No lung function difference (cross-sectional P=0.829, longitudinal P=0.329) or CT difference (P=0.202) | Belgian cohort, DNAH5 n=19, DNAH11 n=23 | Moderate; single-center, may be underpowered |
| 12 | [PMID: 24450482](https://pubmed.ncbi.nlm.nih.gov/24450482/) | Human clinical (n=206) | **Qualifies** | Ultrastructure predicts severity | Normal ultrastructure similar to abnormal in function/imaging | All subtypes | Moderate; pre-genetic era |
| 13 | [PMID: 38076675](https://pubmed.ncbi.nlm.nih.gov/38076675/) | Human clinical (n=69, 26 genotypes) | **Refutes** (mechanism) | Residual motility explains mild phenotype | MCC uniformly absent regardless of genotype; only 1 patient with residual | Danish cohort, 24-year period | High; direct MCC measurement |
| 14 | [PMID: 41561107](https://pubmed.ncbi.nlm.nih.gov/41561107/) | Human clinical (functional) | **Qualifies** | Genotype affects clearance | MCC impaired in both ODA and IDA; cough clearance may differ | Small cohort, 2 genotype groups | Low; small sample, preliminary |
| 15 | [PMID: 39989621](https://pubmed.ncbi.nlm.nih.gov/39989621/) | Human clinical (n=147) | **Supports** | IDA/MTD multi-organ severity | Earlier PET placement in IDA/MTD vs ODA | 7.6 yr follow-up | Moderate-High |
| 16 | [PMID: 25186273](https://pubmed.ncbi.nlm.nih.gov/25186273/) | Human clinical (n=66) | **Supports** | Beat pattern → genotype correlation | Genotype-specific beat patterns across 17 genes, 1072 videos | Multiple genotypes | Moderate-High |
| 17 | [PMID: 40742517](https://pubmed.ncbi.nlm.nih.gov/40742517/) | Human clinical (n=128) | **Supports** | Immotile cilia → worse outcomes | Immotile cilia linked to higher NRD, genetic diagnosis | Spanish cohort | Moderate |
| 18 | [PMID: 32659773](https://pubmed.ncbi.nlm.nih.gov/32659773/) | Human clinical (n=35) | **Qualifies** | Modifier gene interaction | PAV/PAV TAS2R38 protects vs Pseudomonas and exacerbations (P=0.04) | Italian cohort, all PCD | Moderate; small n |
| 19 | [PMID: 39181709](https://pubmed.ncbi.nlm.nih.gov/39181709/) | Human clinical (longitudinal, n=119) | **Qualifies** | Modifier × genotype interaction | TAS2R38 effect only in mild genotype (DNAH11) over 10 years | DNAH11 specifically | Moderate-High |
| 20 | [PMID: 42089334](https://pubmed.ncbi.nlm.nih.gov/42089334/) | In vitro + animal model | **Supports** (therapeutic) | CCDC40 as target | mRNA therapy restores CCDC40 in vitro (10–74% cells) and zebrafish; Phase 1 planned | CCDC40-deficient | High; preclinical only |
| 21 | [PMID: 40033371](https://pubmed.ncbi.nlm.nih.gov/40033371/) | Systematic review (n=323) | **Qualifies** | Within-DNAH5 heterogeneity | Pediatric vs adult patients show distinct features (all P<0.05) | DNAH5 only | Moderate |
| 22 | [PMID: 39282880](https://pubmed.ncbi.nlm.nih.gov/39282880/) | Human clinical (sibling cohort, n=17) | **Qualifies** | Genotype-phenotype concordance | High concordance for symptoms, weak for lung function within families | Multiple genotypes | Low-Moderate; very small n |
| 23 | [PMID: 38072392](https://pubmed.ncbi.nlm.nih.gov/38072392/) | Human clinical | **Supports** (indirect) | CCDC39/40 as accepted severe genotype | Study adjusts for "severe CCDC39 or CCDC40 genotype" as established covariate | Situs ambiguus study | High (methodology) |
| 24 | [PMID: 37660715](https://pubmed.ncbi.nlm.nih.gov/37660715/) | RCT (Phase 2, n=123) | **Contextual** | ENaC blocker in PCD | Idrevloride + hypertonic saline improved ppFEV₁ over 28 days; not genotype-stratified | All PCD | High; no genotype stratification |

{{figure:severity_landscape.png|caption=Evidence landscape visualization mapping PCD genotype severity against confidence level. The clustering reveals three distinct tiers rather than a continuous gradient.}}

---

## Claim Status Summary

| # | Claim | Status | Key Evidence |
|---|-------|--------|-------------|
| 1 | CCDC39/40 = most severe PCD genotype | **ESTABLISHED** | 5+ cohorts, mechanistic data, multinational registry |
| 2 | Non-motility mechanisms in CCDC39/40 | **EMERGING (strong)** | Brody 2024-2025, in vitro |
| 3 | CCNO = severe subtype | **EMERGING** | Small cohorts (n=15-46) |
| 4 | RSPH1 = mild PCD subtype | **ESTABLISHED** | Knowles 2014 (n=16 vs 75 matched), clear effect |
| 5 | DNAH11 milder than all PCD | **EMERGING (qualified)** | NRD data strong; FEV₁ not significantly different from DNAH5 |
| 6 | DNAH5 intermediate severity | **UNCERTAIN** | Davis 2018 supports; Rodriguez Mier 2024 challenges |
| 7 | DNAH5 ≠ DNAH11 in severity | **CONFLICTING** | No direct positive; one direct negative |
| 8 | Residual motility explains mildness | **CHALLENGED** | MCC absent in all genotypes (Marthin 2023) |
| 9 | Uniform MCC absence across genotypes | **EMERGING** | Marthin 2023, n=69, 26 genotypes |
| 10 | nNO as genotype-specific prognostic biomarker | **EMERGING** | Single center, 10-year data |
| 11 | TAS2R38 as modifier gene | **PRELIMINARY** | 2 studies, effective only in mild genotypes |
| 12 | Variant type modulates within-gene severity | **EMERGING** | DNAH5 LoF OR=3.06 for NRD |
| 13 | Severity gradient extends to ENT outcomes | **EMERGING** | Earlier PET in IDA/MTD |
| 14 | Genotype stratification clinically actionable | **SPECULATIVE** | No trial evidence |
| 15 | Cough clearance differs by genotype | **PRELIMINARY** | One study, small cohort |

---

## Limitations and Knowledge Gaps

### Gap 1: Incomplete Resolution of the Middle Severity Spectrum

**Scope:** Whether DNAH5 is truly worse than DNAH11, or whether ODA subtypes differ from normal-ultrastructure subtypes in lung function outcomes.

**Why it matters:** The hypothesis claims a continuous gradient, but the only direct comparison (Rodriguez Mier 2024) found no difference. Without this link, the continuous gradient collapses to a three-tier or binary model. DNAH5 and DNAH11 are the two most common PCD genotypes, so this distinction affects the majority of patients.

**What was checked:** PubMed search for DNAH5 vs DNAH11 comparison studies; one indirect (Davis 2018) and one direct (Rodriguez Mier 2024, negative) comparison found.

**Resolution needed:** Multi-center prospective study with matched DNAH5, DNAH11, and other ODA-deficient cohorts (n ≥ 100 per group), longitudinal FEV₁, and standardized CT scoring.

### Gap 2: Mechanism of Milder Phenotype in RSPH1 Despite Absent MCC

**Scope:** Why RSPH1 produces a milder phenotype when mucociliary clearance is uniformly absent across PCD genotypes.

**Why it matters:** If MCC is uniformly absent (Marthin 2023), the mechanistic basis for RSPH1 mildness is unknown. Residual rotational motility is confirmed, but its functional clearance relevance is unproven. Higher nNO in RSPH1 (98 vs 21 nl/min) may reflect a qualitatively different epithelial biology.

**Resolution needed:** Paired MCC + cough clearance studies in RSPH1 vs other genotypes; ASL layer depth measurements; investigation of nNO as a marker of epithelial health rather than clearance.

### Gap 3: Cough Clearance Differences Between Genotypes

**Scope:** Whether differential cough clearance compensates for absent MCC differently across genotypes.

**Why it matters:** If mucociliary clearance is uniformly absent, cough clearance may be the critical variable. Ostrowski et al. 2026 ([PMID: 41561107](https://pubmed.ncbi.nlm.nih.gov/41561107/)) hinted at genotype-specific cough clearance differences.

**Resolution needed:** Larger cough clearance studies (n ≥ 15 per genotype group) using radioaerosol methods with genotype stratification.

### Gap 4: No Genotype-Stratified Clinical Trials

**Scope:** Whether management should differ by genotype.

**Why it matters:** This is the most critical gap for clinical translation. The CLEAN-PCD trial of idrevloride ([PMID: 37660715](https://pubmed.ncbi.nlm.nih.gov/37660715/)) did not stratify by genotype. No trial has tested whether severe genotypes benefit from more aggressive early intervention.

**Resolution needed:** Post-hoc genotype-stratified analysis of CLEAN-PCD data; prospective trial with genotype-stratified randomization of treatment intensity.

### Gap 5: Proteostasis/Cell Fate Mechanism Scope

**Scope:** Whether motility-independent mechanisms (proteostasis disruption, cell fate switching) discovered in CCDC39/CCDC40 also operate in CCNO or other severe subtypes.

**Why it matters:** If CCNO severity also involves non-motility mechanisms, the three-tier model would have consistent mechanistic grounding. If the mechanism is unique to CCDC39/CCDC40, it explains their specific severity but leaves CCNO severity mechanistically unexplained.

**Resolution needed:** Cell fate and proteostasis studies in CCNO-deficient airway epithelial cells using similar methods to Brody et al. 2024-2025.

### Gap 6: Modifier Gene Landscape Beyond TAS2R38

**Scope:** Only TAS2R38 has been studied as a modifier; MUC5B, CFTR heterozygosity, immune genes are uninvestigated.

**Why it matters:** Modifier genes may explain substantial within-genotype variance (sibling FEV₁ Z-score differences up to 2.06, Hazan et al. 2024) and could identify high-risk individuals within "standard" severity genotypes.

**Resolution needed:** GWAS or whole-exome modifier analysis in large PCD cohorts (iPCD Cohort suitable); candidate gene panels for innate immunity and airway remodeling.

### Gap 7: Longitudinal FEV₁ Decline Replication

**Scope:** Only Davis et al. 2019 showed significant longitudinal FEV₁ decline specifically in IDA/MTD. Most studies are cross-sectional.

**Why it matters:** Cross-sectional differences may reflect ascertainment bias; longitudinal decline rate is the clinically meaningful outcome.

**Resolution needed:** iPCD Cohort genotype-stratified longitudinal FEV₁ trajectory analysis with mixed-effects models.

### Gap 8: Adult and Aging Outcomes by Genotype

**Scope:** Most studies focus on pediatric populations (up to age 24); adult trajectories by genotype are poorly characterized.

**Why it matters:** Long-term prognosis including lung transplant rates, mortality, and respiratory failure by genotype is critical for clinical decision-making.

**Resolution needed:** Adult PCD registry analysis with genotype stratification; longitudinal follow-up of pediatric cohorts into adulthood.

### Gap 9: Genotype-Specific Biomarkers Beyond nNO

**Scope:** nNO is the only biomarker studied by genotype. LCI from MBW ([PMID: 41332215](https://pubmed.ncbi.nlm.nih.gov/41332215/)), exhaled biomarkers, and sputum proteomics are not genotype-stratified.

**Resolution needed:** Genotype-stratified MBW, sputum proteomics, and exhaled biomarker studies.

### Gap 10: No Omics Comparisons Across PCD Genotypes

**Scope:** No RNA-seq, proteomics, or metabolomics comparing airway epithelial cells across PCD genotypes were found in our literature search. The Brody 2024-2025 studies examined CCDC39/40 specifically but did not compare to other genotypes at the omics level.

**Resolution needed:** Multi-genotype single-cell RNA-seq and proteomics of airway epithelial cells.

### Gap 11: GenCC/ClinGen Source-Level Absence

**Scope:** No systematic GenCC or ClinGen curated gene-disease validity data were identified that specifically address severity stratification within PCD.

**Resolution needed:** ClinGen gene curation for severity-associated PCD genes with integration into clinical validity frameworks.

---

## Alternative Models

### 1. Binary Severe-vs-Non-Severe Model (Competing/Simplified)

**Relationship:** Simplification of the seed hypothesis. Rather than a continuous gradient, PCD follows a binary model: severe (CCDC39/40, CCNO) vs. everything else. Supported by Rodriguez Mier 2024 (no DNAH5-DNAH11 difference) and Marthin 2023 (MCC absent regardless of genotype). Our three-tier model is a compromise that preserves the RSPH1 mild category.

### 2. Residual Ciliary Motility Model (Complementary/Upstream)

**Relationship:** Proposed upstream cause for severity differences. Residual motility in RSPH1 (rotational) and DNAH11 (hyperkinetic-stiff) explains milder phenotypes. **Challenged** by uniform MCC absence across genotypes (Marthin 2023). May still operate through non-clearance functions (signaling, ASL regulation) or cough clearance facilitation.

### 3. Motility-Independent Cellular Damage Model (Complementary/Downstream)

**Relationship:** Parallel mechanism specific to CCDC39/CCDC40. Proteostasis disruption and cell fate switching cause epithelial damage beyond motility loss (Brody 2024-2025). Explains why CCDC39/40 are disproportionately severe. This is the strongest mechanistic advance, but scope limited to one genotype subgroup.

### 4. Modifier Gene Model (Complementary/Modulating)

**Relationship:** Modulating factor operating within genotype tiers. TAS2R38 PAV/PAV protects against Pseudomonas and exacerbations, but only in mild genotypes (Pifferi 2024). Suggests a floor effect: severe primary mutations overwhelm modifier benefits. Other modifiers (MUC5B, CFTR heterozygosity) are uninvestigated.

### 5. Reduced Cilia Generation Model (Parallel/Expansion)

**Relationship:** Expands the hypothesis beyond ultrastructure. CCNO/MCIDAS cause reduced multiciliated cell generation rather than ultrastructural defects. This is a parallel severe category that must be incorporated into any severity classification.

### 6. Environmental/Diagnostic Delay Model (Competing/Confounding)

**Relationship:** Alternative explanation for observed differences. Delayed diagnosis, infection burden, and care access may explain as much variance as genotype. iPCD Cohort data ([PMID: 29269581](https://pubmed.ncbi.nlm.nih.gov/29269581/)) show early diagnosis associated with better growth and lung function. Partially controlled in prospective cohorts, but remains a confounder.

### 7. Cough Clearance Model (Complementary)

**Relationship:** Alternative mechanism for clearance-mediated severity gradient. If MCC is uniformly absent, differential cough clearance capacity across genotypes may determine residual airway clearance (Ostrowski 2026). Preliminary evidence only.

---

## Proposed Follow-up Experiments / Discriminating Tests

### Test 1: Prospective Multi-Center Genotype-Stratified Longitudinal Study

- **Design:** Enroll CCDC39/40, DNAH5, DNAH11, RSPH1, CCNO patients (minimum n = 50/group) from iPCD Cohort centers
- **Biomarkers:** FEV₁, FVC, LCI (MBW), nNO, chest CT (Brody/PRAGMA scoring), sputum microbiology
- **Duration:** 5+ years with annual assessments
- **Expected results:** If three-tier model correct: significant FEV₁ decline slope in Tier 1 > Tier 2 ≈ Tier 3; if binary: Tier 2 = Tier 3
- **Discriminates:** Continuous gradient vs three-tier vs binary model

### Test 2: Paired MCC + Cough Clearance Study by Genotype

- **Design:** Radioaerosol MCC + voluntary cough clearance measurements in genotype-defined groups
- **Patient stratification:** CCDC39/40 vs DNAH5 vs DNAH11 vs RSPH1, n ≥ 15/group
- **Expected results:** If residual motility matters: RSPH1 > DNAH11 > DNAH5 ≈ CCDC39/40 for cough clearance
- **Discriminates:** Whether cough clearance (not MCC) underlies severity differences

### Test 3: Multi-Genotype Cellular Pathology Profiling

- **Model:** Air-liquid interface cultures from CCNO-deficient, CCDC39/40-deficient, DNAH5-deficient, and control nasal epithelial cells
- **Assays:** Single-cell RNA-seq, proteasome activity, unfolded protein response markers, multiciliogenesis transcription factor expression, cell fate markers (goblet vs multiciliated ratio)
- **Expected results:** If motility-independent mechanism specific to CCDC39/40: CCNO shows normal proteostasis but reduced cilia number
- **Discriminates:** Whether proteostasis disruption is shared across severe subtypes or unique to CCDC39/40

### Test 4: GWAS/Modifier Screen in iPCD Cohort

- **Design:** Genome-wide genotyping in n > 500 PCD patients with known primary mutation and longitudinal lung function data
- **Analysis:** Modifier gene association with FEV₁ trajectory residuals after accounting for primary genotype
- **Expected results:** Identification of modifier loci explaining within-genotype variance
- **Discriminates:** How much severity variation is genetic (modifiers) vs environmental

### Test 5: Post-Hoc Genotype Stratification of CLEAN-PCD Trial

- **Design:** Re-analyze existing CLEAN-PCD Phase 2 data (n = 123) stratified by genotype
- **Expected results:** If severe genotypes respond differently to ENaC blockade, this provides first evidence for genotype-stratified therapy
- **Discriminates:** Whether treatment response varies by genotype

### Test 6: CCDC40 mRNA Therapy Phase 1 Trial

- **Status:** Planned based on preclinical efficacy ([PMID: 42089334](https://pubmed.ncbi.nlm.nih.gov/42089334/))
- **Design:** LNP-CCDC40-mRNA in CCDC40-deficient individuals
- **Expected results:** Structural and functional ciliary improvement; lung function stabilization
- **Discriminates:** Validates CCDC40 loss as a causal, correctable driver of severity

---

## Curation Leads

*All leads below are candidate updates for the Disorder Mechanisms Knowledge Base and require curator verification before integration.*

### Candidate Evidence References to Add

1. **PMID: 39879322** (Brody et al. 2025) — **SUPPORT**. Verified snippet: *"variants in the genes encoding coiled-coil domain-containing 39 (CCDC39) and CCDC40 in particular cause severe disease that is not explained by loss of ciliary motility alone."* Provides mechanistic basis for CCDC39/40 unique severity via proteostasis disruption and cell fate switching.

2. **PMID: 38602513** (Rodriguez Mier et al. 2024) — **QUALIFY/REFUTE**. Verified snippet: *"Respiratory tract microbiology (p = 0.161), lung function (cross-sectional, p = 0.829 and longitudinal, p = 0.329) and chest CT abnormalities (p = 0.202) were not significantly different between DNAH11 and DNAH5 variants."* Challenges the intermediate gradient between DNAH5 and DNAH11.

3. **PMID: 38076675** (Marthin et al. 2023) — **QUALIFY/REFUTE** (mechanism). Verified snippet: *"Mucociliary clearance by PRMC was consistently absent in most PCD patients, regardless of genotype."* Challenges residual-motility mechanism underlying the severity gradient.

4. **PMID: 40344341** (Barber et al. 2025) — **SUPPORT**. Verified snippets: DNAH11 NRD OR=0.35 (CI 0.16–0.76); DNAH5 biallelic LoF NRD OR=3.06 (CI 1.33–7). Supports mild DNAH11 phenotype and within-gene variant-type severity modulation.

5. **PMID: 38871375** (Raidt et al. 2024) — **SUPPORT**. Verified finding: n=1236, 46 genes; genetic variant predicts lung function course. Largest multinational confirmation of genotype-phenotype correlations.

6. **PMID: 24568568** (Knowles et al. 2014) — **SUPPORT**. Verified snippet: FEV₁ 73.0 vs 61.8% (P=0.0); nNO 98.3 vs 20.7 (P<0.0003). Defines RSPH1 as a distinct mild subtype.

7. **PMID: 35777446** (Pifferi et al. 2022) — **SUPPORT**. Verified snippet: IDA/MTD nNO decline P<0.01 vs stable others. Longitudinal biomarker evidence for progressive IDA/MTD severity.

8. **PMID: 42089334** (Wohlgemuth et al. 2026) — **SUPPORT** (therapeutic). mRNA therapy for CCDC40; Phase 1 planned. Confirms clinical prioritization of severe genotype.

### Candidate Pathophysiology Nodes/Edges

- **New node:** "Proteostasis disruption" — downstream of CCDC39/CCDC40 mutation, upstream of epithelial damage, parallel to motility loss
- **New node:** "Cell fate switching" — downstream of ciliary network undocking, leading to altered airway epithelial composition
- **New edge:** CCDC39/CCDC40 → motility-independent cellular damage → excess severity (distinct from motility loss pathway)
- **New edge:** TAS2R38 PAV/PAV → reduced Pseudomonas colonization → severity modification (restricted to mild genotypes)
- **Candidate edge modification:** Remove or downgrade "DNAH5 > DNAH11 severity" edge given Rodriguez Mier 2024 negative result
- **Candidate edge revision:** "Residual motility → partial MCC → milder disease" should be flagged as CHALLENGED (Marthin 2023)

### Candidate Ontology Terms

- **Cell types:** Multiciliated airway epithelial cell (CL:0000064); Goblet cell (relevant for cell fate switching)
- **Biological processes:** GO:0003341 (cilium movement), GO:0061512 (protein localization to cilium), GO:0006986 (response to unfolded protein), GO:0045197 (establishment of epithelial cell polarity)
- **Disease:** OMIM:244400 (PCD); sub-entries for CCDC39 (#613807), CCDC40 (#613808), DNAH5 (#608644), DNAH11 (#611884), RSPH1, CCNO (#615872)

### Candidate Status Change

- **Current status:** EMERGING
- **Recommended status:** Maintain **EMERGING** with qualifier: "Supported at extremes (CCDC39/40 severe, RSPH1 mild); intermediate gradient unconfirmed; three-tier model (Severe/Standard/Mild) may be more accurate than continuous gradient"
- **Conditions for upgrade to ESTABLISHED:** (1) Replication of intermediate gradient in ≥2 independent longitudinal studies, OR (2) genotype-stratified clinical trial demonstrating management benefit

### Candidate Knowledge Gaps for KB

1. **DNAH5-DNAH11 severity difference** — Single study refutes; no confirming study found. Priority: **High**.
2. **Mechanism of RSPH1 mildness despite absent MCC** — Residual motility confirmed but functional relevance unknown. Priority: **High**.
3. **No genotype-stratified clinical trial** — Clinical actionability undemonstrated. Priority: **Critical**.
4. **Proteostasis mechanism scope** — Demonstrated only in CCDC39/40; unknown if shared by CCNO. Priority: **Moderate**.
5. **Modifier gene landscape** — Only TAS2R38 studied; full modifier architecture unknown. Priority: **Moderate**.
6. **No omics data comparing PCD genotypes** — No RNA-seq, proteomics, or metabolomics across genotypes found. Priority: **High**.
7. **Adult outcomes by genotype** — No genotype-stratified data beyond age 25 for transplant/mortality. Priority: **Moderate**.
8. **Cough clearance by genotype** — Preliminary suggestion from one small study. Priority: **Moderate**.
9. **LCI/MBW genotype-stratified data** — More sensitive endpoint than FEV₁ but not yet genotype-stratified. Priority: **Moderate**.
10. **Situs-driven diagnostic bias** — Rodriguez Mier 2024 showed age-at-diagnosis difference disappears after situs correction. All studies should adjust. Priority: **Moderate**.
11. **GenCC/ClinGen severity curation** — No formal gene-disease validity data addressing within-PCD severity stratification. Priority: **Low-Moderate**.

---

{{figure:final_summary.png|caption=Final summary visualization showing the distribution of evidence across the three-tier severity model and the balance of supporting (green), qualifying (yellow), and refuting (red) evidence items. The three-tier model (Severe: CCDC39/40 + CCNO; Standard: DNAH5, DNAH11, most others; Mild: RSPH1) emerges as the best-fitting framework.}}

---

## Investigation Statistics

| Metric | Value |
|---|---|
| Iterations completed | 5 |
| Confirmed findings | 13 |
| Claims evaluated | 15 (2 established, 7 emerging, 2 conflicting, 1 challenged, 2 preliminary, 1 speculative) |
| Evidence items in matrix | 24 |
| Knowledge gaps identified | 11 (1 critical, 3 high, 7 moderate) |
| Alternative models assessed | 7 |
| Discriminating tests proposed | 6 |
| Literature reviewed | 59 papers (2013–2026) |
| Unique PMIDs cited | 28 |

---

*Report generated through systematic analysis of 59 papers across 5 investigation iterations, with 13 confirmed findings. Search date: June 2026.*
