---
provider: falcon
model: Edison Scientific Literature
cached: false
start_time: '2026-06-09T22:17:03.105523'
end_time: '2026-06-09T22:31:15.865769'
duration_seconds: 852.76
template_file: templates/hypothesis_deep_research.md
template_variables:
  disease_name: Apical Neuroependyma Integrity Failure Module
  category: Module
  hypothesis_group_id: apical_neuroependyma_integrity_model
  hypothesis_label: Apical Neuroependyma Integrity Failure Model
  hypothesis_status: CANONICAL
  hypothesis_yaml: "hypothesis_group_id: apical_neuroependyma_integrity_model\nhypothesis_label:\
    \ Apical Neuroependyma Integrity Failure Model\nstatus: CANONICAL\ndescription:\
    \ Radial glia and neural progenitors maintain an apical ventricular interface\
    \ through actin\n  scaffolding, cadherin/catenin adhesion, vesicle trafficking,\
    \ ciliary/basal-body positioning, and regulated\n  progenitor signaling. Pathogenic\
    \ variants or perturbations in FLNA, ARFGEF2, FAT4, DCHS1, NEDD4L, ERMARD/C6orf70,\n\
    \  GNAI2, TMEM67-associated complexes, or interacting pathways can weaken this\
    \ apical scaffold. The resulting\n  ventricular-lining disruption mispositions\
    \ progenitors or neurons near the lateral ventricles, alters\n  local progenitor\
    \ output, and can produce periventricular heterotopic nodules with secondary neuronal\n\
    \  migration or terminal-translocation defects.\nevidence:\n- reference: PMID:25097827\n\
    \  supports: SUPPORT\n  evidence_source: OTHER\n  snippet: PH results in a disruption\
    \ of the neuroependyma, inhibition of neural proliferation and differentiation,\n\
    \    and altered neuronal migration.\n  explanation: Review-level synthesis of\
    \ FLNA/BIG2/apical-abscission biology supporting the module skeleton\n    as neuroependyma\
    \ disruption with progenitor and migration consequences.\n- reference: PMID:18996916\n\
    \  supports: SUPPORT\n  evidence_source: OTHER\n  snippet: Our current findings\
    \ suggest that PH formation arises from a final common pathway involving\n   \
    \ disruption of vesicle trafficking, leading to impaired cell adhesion and loss\
    \ of neuroependymal integrity.\n  explanation: Human postmortem and mouse/cell\
    \ evidence support loss of neuroependymal integrity as a\n    common endpoint\
    \ across FLNA, ARFGEF2/BIG2, and related vesicle-trafficking mechanisms."
provider_config:
  timeout: null
  max_retries: 3
  parameters:
    allowed_domains: []
    temperature: 0.1
    max_embedded_images: 8
citation_count: 34
artifact_count: 1
artifact_sources:
  edison_answer_artifacts: 1
artifacts:
- filename: artifact-00.md
  path: falcon_artifacts/artifact-00.md
  media_type: text/markdown
  source: edison_answer_artifacts
  data_storage_id: null
  description: Edison artifact artifact-00
---

## Question

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Apical Neuroependyma Integrity Failure Module
- **Category:** Module

## Target Hypothesis
- **Hypothesis ID:** apical_neuroependyma_integrity_model
- **Hypothesis Label:** Apical Neuroependyma Integrity Failure Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: apical_neuroependyma_integrity_model
hypothesis_label: Apical Neuroependyma Integrity Failure Model
status: CANONICAL
description: Radial glia and neural progenitors maintain an apical ventricular interface through actin
  scaffolding, cadherin/catenin adhesion, vesicle trafficking, ciliary/basal-body positioning, and regulated
  progenitor signaling. Pathogenic variants or perturbations in FLNA, ARFGEF2, FAT4, DCHS1, NEDD4L, ERMARD/C6orf70,
  GNAI2, TMEM67-associated complexes, or interacting pathways can weaken this apical scaffold. The resulting
  ventricular-lining disruption mispositions progenitors or neurons near the lateral ventricles, alters
  local progenitor output, and can produce periventricular heterotopic nodules with secondary neuronal
  migration or terminal-translocation defects.
evidence:
- reference: PMID:25097827
  supports: SUPPORT
  evidence_source: OTHER
  snippet: PH results in a disruption of the neuroependyma, inhibition of neural proliferation and differentiation,
    and altered neuronal migration.
  explanation: Review-level synthesis of FLNA/BIG2/apical-abscission biology supporting the module skeleton
    as neuroependyma disruption with progenitor and migration consequences.
- reference: PMID:18996916
  supports: SUPPORT
  evidence_source: OTHER
  snippet: Our current findings suggest that PH formation arises from a final common pathway involving
    disruption of vesicle trafficking, leading to impaired cell adhesion and loss of neuroependymal integrity.
  explanation: Human postmortem and mouse/cell evidence support loss of neuroependymal integrity as a
    common endpoint across FLNA, ARFGEF2/BIG2, and related vesicle-trafficking mechanisms.
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

Question: You are an expert researcher providing comprehensive, well-cited information.

Provide detailed information focusing on:
1. Key concepts and definitions with current understanding
2. Recent developments and latest research (prioritize 2023-2024 sources)
3. Current applications and real-world implementations
4. Expert opinions and analysis from authoritative sources
5. Relevant statistics and data from recent studies

Format as a comprehensive research report with proper citations. Include URLs and publication dates where available.
Always prioritize recent, authoritative sources and provide specific citations for all major claims.

# Mechanistic Hypothesis Search

You are evaluating a specific disease mechanism hypothesis for the Disorder
Mechanisms Knowledge Base. This is not a general disease overview. Use the
hypothesis YAML below as the seed claim, then search for evidence that supports,
refutes, qualifies, or competes with this hypothesis.

## Target Disease
- **Disease Name:** Apical Neuroependyma Integrity Failure Module
- **Category:** Module

## Target Hypothesis
- **Hypothesis ID:** apical_neuroependyma_integrity_model
- **Hypothesis Label:** Apical Neuroependyma Integrity Failure Model
- **Status in KB:** CANONICAL

## Seed Hypothesis YAML

```yaml
hypothesis_group_id: apical_neuroependyma_integrity_model
hypothesis_label: Apical Neuroependyma Integrity Failure Model
status: CANONICAL
description: Radial glia and neural progenitors maintain an apical ventricular interface through actin
  scaffolding, cadherin/catenin adhesion, vesicle trafficking, ciliary/basal-body positioning, and regulated
  progenitor signaling. Pathogenic variants or perturbations in FLNA, ARFGEF2, FAT4, DCHS1, NEDD4L, ERMARD/C6orf70,
  GNAI2, TMEM67-associated complexes, or interacting pathways can weaken this apical scaffold. The resulting
  ventricular-lining disruption mispositions progenitors or neurons near the lateral ventricles, alters
  local progenitor output, and can produce periventricular heterotopic nodules with secondary neuronal
  migration or terminal-translocation defects.
evidence:
- reference: PMID:25097827
  supports: SUPPORT
  evidence_source: OTHER
  snippet: PH results in a disruption of the neuroependyma, inhibition of neural proliferation and differentiation,
    and altered neuronal migration.
  explanation: Review-level synthesis of FLNA/BIG2/apical-abscission biology supporting the module skeleton
    as neuroependyma disruption with progenitor and migration consequences.
- reference: PMID:18996916
  supports: SUPPORT
  evidence_source: OTHER
  snippet: Our current findings suggest that PH formation arises from a final common pathway involving
    disruption of vesicle trafficking, leading to impaired cell adhesion and loss of neuroependymal integrity.
  explanation: Human postmortem and mouse/cell evidence support loss of neuroependymal integrity as a
    common endpoint across FLNA, ARFGEF2/BIG2, and related vesicle-trafficking mechanisms.
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


# Mechanistic Hypothesis Search Report: Apical Neuroependyma Integrity Failure Model (apical_neuroependyma_integrity_model)

**Scope.** This report evaluates whether a *primary failure of the apical ventricular zone (VZ)/neuroependyma integrity*—mediated by actin scaffolding, cadherin/catenin adherens junctions, vesicle trafficking, cilia/basal-body positioning, and related progenitor signaling—causally generates **periventricular heterotopia/periventricular nodular heterotopia (PVH/PVNH)** nodules. Evidence is curated around the seed genes/processes (FLNA, ARFGEF2/BIG2, ARF1, FAT4, DCHS1, NEDD4L, ERMARD/C6orf70, GNAI2, ciliopathy complexes) and closely related apical junction biology.

---

## Executive Judgment

**Verdict: Partially supported.**

The hypothesis is **strongly supported** for the **FLNA–ARFGEF2(BIG2)–vesicle trafficking/actin–cadherin/catenin** axis by convergent **human postmortem pathology** (disrupted neuroependyma adjacent to nodules) and **causal perturbation experiments** (dominant-negative FLNA; brefeldin A inhibition of ARFGEF2-like trafficking) that induce apical junction disruption and periventricular nodules in vivo (ferland2009disruptionofneural pages 1-2, ferland2009disruptionofneural pages 7-8, ferland2009disruptionofneural pages 9-10). It is **mechanistically plausible** for ARF-pathway PVNH, supported by 2023 human genetics expanding PVNH association to ARF1 and pointing to apical adhesion/trafficking processes (agathe2023arf1relateddisorderphenotypic pages 7-7).

However, the model’s **scope is limited** by strong subtype-specific data showing PVH can arise via **parallel/competing mechanisms** that do not explicitly require primary ventricular-lining denudation in the tested assays, including **PI3K–AKT–mTOR signaling and neuronal positioning/terminal translocation defects** (NEDD4L) (broix2016mutationsinthe pages 6-8) and **cell-intrinsic migration defects linked to autophagy and focal-adhesion (paxillin) recycling** (FAT4/DCHS1) (bressan2023metforminrescuesmigratory pages 7-9). Reviews emphasize PVNH mechanistic heterogeneity and caution against a single “migration-only” or single “lining-only” explanation across all PVNH etiologies (watrin2015causesandconsequences pages 1-2).

Key caveat: for several seed genes (e.g., **ERMARD/C6orf70, GNAI2, TMEM67**), the present tool-run retrieved **insufficient primary mechanistic evidence** tying them directly to apical neuroependyma failure in PVNH; thus, KB-level “module canon” is best justified as a **common pathway for a subset** of PVNH rather than a universal proximal lesion.

---

## Key Concepts and Definitions (Current Understanding)

### Apical neuroependyma / ventricular lining
In developmental context, the “neuroependyma” refers to the **ventricular surface epithelium composed of neuroepithelial/radial glial apical endfeet** that later transitions into ependymal lining. This apical interface depends on **adherens junction belts (cadherins–catenins)** coupled to **actin** to maintain epithelial integrity and VZ architecture. Disruption can produce **local denudation**, altered progenitor behavior, and ectopic neuronal accumulations.

### Periventricular heterotopia / PVNH
PVH/PVNH is characterized by **ectopic neuronal nodules lining the lateral ventricles**. The apical integrity model predicts that nodules form where **ventricular lining integrity fails**, causing **neurons or progenitors to remain adjacent to ventricle** and secondarily affecting migration.

### Apical abscission
Apical abscission is a proposed mechanism for neuronal progenitor exit involving actin-dependent severing of apical attachments; disruption could prevent orderly detachment and contribute to periventricular retention (review-level synthesis) (sheen2014filaminamediated pages 3-4).

---

## Recent Developments and Latest Research (Prioritizing 2023–2024)

### 1) FAT4/DCHS1 PVH: autophagy–paxillin recycling and metformin rescue (2023)
Bressan et al. (EMBO Mol Med, Aug 2023; DOI: **10.15252/emmm.202216908**, URL: https://doi.org/10.15252/emmm.202216908) studied patient-derived hNPCs with **DCHS1 or FAT4 mutations** and found migration deficits linked to **impaired autophagy** and **paxillin recycling**, with rescue by **metformin** (AMPK-dependent autophagy enhancer). Quantitatively, migration distances differed and showed altered responsiveness to bafilomycin A1 (autophagosome–lysosome fusion blocker):
- Control: **26 ± 3.1 μm** baseline vs **9.9 ± 2.7 μm** with bafilomycin A1
- DCHS1: **19.0 ± 1.5 μm** baseline vs **14.6 ± 1.7 μm** with bafilomycin A1
- FAT4: **12.8 ± 1.9 μm** baseline vs **10.7 ± 2.4 μm** with bafilomycin A1 (bressan2023metforminrescuesmigratory pages 7-9)

Interpretation for the module: this is strong evidence for **cell-intrinsic migration/homeostatic autophagy defects** as a proximate mechanism in this PVH subtype, qualifying the necessity of primary apical-lining failure as the initiating lesion—at least as directly tested in this study (bressan2023metforminrescuesmigratory pages 7-9).

### 2) ARF-pathway expansion: ARF1-related disorder includes PVNH (2023)
de Sainte Agathe et al. (J Med Genet, Apr 2023; DOI: **10.1136/jmg-2022-108803**, URL: https://doi.org/10.1136/jmg-2022-108803) describe a 17-individual ARF1 variant cohort with PVNH among core phenotypes, and explicitly situate ARF-pathway dysfunction in the broader biology of **apical adhesion/junction formation and vesicle trafficking**, consistent with the apical integrity failure module (agathe2023arf1relateddisorderphenotypic pages 7-7).

### 3) Radial glia polarity synthesis (2024)
Viola et al. (Front Cell Dev Biol, Oct 2024; DOI: **10.3389/fcell.2024.1478283**, URL: https://doi.org/10.3389/fcell.2024.1478283) synthesize evidence that disruption of **adherens junctions, actin coupling, trafficking, and cilia-regulated polarity** yields progenitor delamination and PVH-like phenotypes. While review-level, it consolidates the mechanistic landscape and highlights multiple apical-scaffold regulators (viola2024radialgliaprogenitor pages 2-5, viola2024radialgliaprogenitor pages 11-11, viola2024radialgliaprogenitor pages 6-7).

---

## Evidence Matrix

| Citation | Evidence type | Supports / refutes / qualifies / competing | Mechanistic claim tested | Key finding | Disease context / subtype | Confidence & limitations |
|---|---|---|---|---|---|---|
| Ferland et al., 2009, *Human Molecular Genetics*, https://doi.org/10.1093/hmg/ddn377 | Human postmortem + mouse electroporation + cell assays | Supports | PH/PVNH arises from disrupted ventricular zone/neuroependyma integrity with impaired adhesion and progenitor mispositioning | In 4 postmortem PH brains, neuroependyma was disrupted adjacent to nodules; mouse dominant-negative FLNA disrupted apical β-catenin/α-catenin and impaired precursor departure from ventricle; authors propose a common pathway of vesicle-trafficking failure → impaired adhesion → neuroependymal loss (ferland2009disruptionofneural pages 1-2, ferland2009disruptionofneural pages 7-8, ferland2009disruptionofneural pages 6-7) | FLNA- and ARFGEF2-related PH; human PH broadly | High for association of ventricular lining disruption with PH; limits: mixed model systems, convergence of FLNA vs ARFGEF2 still partly inferential (ferland2009disruptionofneural pages 1-2) |
| Ferland et al., 2009, *Human Molecular Genetics*, https://doi.org/10.1093/hmg/ddn377 | Mouse pharmacology + mutant model + human contextual pathology | Supports | Vesicle-trafficking disruption can directly compromise apical adhesion and generate periventricular nodules | Brefeldin A caused β-catenin/N-cadherin/F-actin disruption at neuroepithelium and induced periventricular nodules; hyh/αSNAP-related denudation preceded nodules, which formed only next to denuded lining (ferland2009disruptionofneural pages 9-10) | Periventricular heterotopia-like nodules; neuroepithelial denudation models | Moderate-high; pharmacologic BFA is not gene-specific and hyh is not a canonical PVNH gene, but causally supports ventricular-lining mechanism (ferland2009disruptionofneural pages 9-10) |
| Lu et al., 2006, *Journal of Comparative Neurology*, https://doi.org/10.1002/cne.20806 | Human developmental expression + cell trafficking assay | Supports | ARFGEF2/BIG2 and FLNA act in overlapping apical progenitors; ARFGEF2-dependent trafficking helps target FLNA to neuroependymal membrane | ARFGEF2 and FLNA overlapped in neuroependymal progenitors; dominant-negative ARFGEF2 partially blocked FLNA transport from Golgi to plasma membrane, supporting trafficking-dependent maintenance of ventricular lining (lu2006overlappingexpressionof pages 1-2) | FLNA-/ARFGEF2-related PH | Moderate; strong spatial/mechanistic plausibility but limited direct in vivo proof that this trafficking defect alone is sufficient for nodules (lu2006overlappingexpressionof pages 1-2) |
| Sheen, 2014, *Tissue Barriers*, https://doi.org/10.4161/tisb.29431 | Review-level synthesis of primary studies | Supports / qualifies | FLNA/BIG2-dependent actin, vesicle trafficking, cilia, and apical abscission regulate neuroependyma integrity and progenitor exit | Synthesizes evidence that FLNA/BIG2 loss reduces apical actin and adhesion, perturbs primary cilium/Shh-related proliferation, and may delay/alter apical abscission, providing a unifying apical-scaffold model for PH (sheen2014filaminamediated pages 3-4) | PH/PVNH, especially FLNA and ARFGEF2 | Moderate; useful integrative framework, but review-level and several steps (exact abscission defect, cilia contribution) remain unconfirmed (sheen2014filaminamediated pages 3-4) |
| Broix et al., 2016, *Nature Genetics*, https://doi.org/10.1038/ng.3676 | Human genetics + functional model data | Qualifies / competing | NEDD4L-associated PVNH may arise primarily through AKT-mTOR dysregulation rather than classic apical lining failure | NEDD4L HECT-domain mutations caused PVNH via AKT/mTOR deregulation; available snippet notes consequences tested in apical progenitors, but strongest headline mechanism is signaling dysregulation rather than direct junctional failure (paper search context) | NEDD4L-related PVNH | Moderate; relevant PVNH gene but current extracted context here is limited, so placement as qualifier/parallel mechanism is cautious |
| Bressan et al., 2023, *EMBO Molecular Medicine*, https://doi.org/10.15252/emmm.202216908 | Patient-derived hNPCs + isogenic lines + organoids/xenografts | Qualifies / competing | FAT4/DCHS1 PH can be explained by altered neuronal migration via autophagy/focal adhesion defects, not only apical neuroependyma failure | DCHS1/FAT4 mutant hNPCs had altered migratory dynamics in vivo, autophagy defects, paxillin accumulation, and migration rescue by metformin; this supports a strong cell-migration/autophagy mechanism (paper search context) | FAT4/DCHS1-related PH | High for migration/autophagy phenotype; limits apical model scope because direct ventricular-lining failure was not the main tested mechanism |
| Viola et al., 2024, *Frontiers in Cell and Developmental Biology*, https://doi.org/10.3389/fcell.2024.1478283 | Review-level synthesis | Supports / qualifies | Disruption of apical adhesion/polarity in radial glia causes delamination, rosettes, and PVH-like malformations | Summarizes evidence that FAT4/DCHS1 knockdown causes RG detachment and PVH-like phenotypes; αE-catenin, PLEKHA7, DLGAP4, trafficking and cilia pathways regulate ventricular boundary integrity and progenitor localization (viola2024radialgliaprogenitor pages 2-5, viola2024radialgliaprogenitor pages 11-11, viola2024radialgliaprogenitor pages 6-7) | PVH/PVNH and related cortical malformations | Moderate; broad and mechanistically rich, but mostly synthesis rather than new primary evidence and not specific to all seed genes (viola2024radialgliaprogenitor pages 2-5, viola2024radialgliaprogenitor pages 11-11, viola2024radialgliaprogenitor pages 6-7) |
| Oliver et al., 2013, *Journal of Neuropathology & Experimental Neurology*, https://doi.org/10.1097/NEN.0b013e3182a2d5fe | Primary experimental ependymal biology | Supports | N-cadherin adherens junction loss is sufficient to cause ependymal apoptosis/denudation, a pathology implicated in PVH | Disruption of CDH2/N-cadherin-based adherens junctions led to ependymal cell apoptosis and denudation of ventricular walls; paper explicitly connects this pathology to disorders including periventricular heterotopia (paper search context) | Ventricular wall denudation relevant to PVH/hydrocephalus | Moderate; strong for junctional biology and denudation, but not a PVNH-gene-specific model |
| Matsumoto et al., 2017, *Human Molecular Genetics*, https://doi.org/10.1093/hmg/ddx038 | Gyrencephalic mammal model + human comparative pathology | Supports | Disrupted ventricular lining is a conserved proximate lesion in some heterotopia syndromes | In a gyrencephalic model, ventricular lining disruption accompanied periventricular nodular heterotopia-like pathology; authors note similar lining disruption in human cases, extending the mechanism beyond lissencephalic rodent systems (paper search context) | Gyrencephalic PNH models / transmantle dysplasia contexts | Moderate; strengthens translational relevance, though disease gene/context may differ from canonical FLNA/ARFGEF2 PVNH |
| Deleo et al., 2020, *Neurology*, https://doi.org/10.1212/WNL.0000000000010648 | Computational MRI phenotyping in patients | Qualifies | If apical/ventricular injury seeds PVNH, overlying cortex and connected structures should show patterned downstream abnormalities | MRI in 40 PVNH patients showed structural/functional abnormalities in cortex overlying nodules and hippocampal changes; discussion cites preclinical models suggesting ventricular ependymal disruption as an upstream insult (paper search context) | PVNH with normal-appearing cortex on routine MRI | Moderate; human systems-level support only, not direct mechanistic proof of lining failure |
| Watrin et al., 2015, *CNS Neuroscience & Therapeutics*, https://doi.org/10.1111/cns.12322 | Review | Qualifies / competing | PVNH is not solely a neuronal migration disorder; apical/radial glial integrity is important but not exclusive | Review emphasizes FLNA/radial glial integrity, ARFGEF2 trafficking, C6orf70/ERMARD, and FAT4/DCHS1, while explicitly arguing for multiple mechanisms including progenitor, scaffold, and migration defects (watrin2015causesandconsequences pages 1-2) | Gray matter heterotopia broadly; PVNH subtypes | Moderate; balanced synthesis helpful for scope-limiting the seed hypothesis, but review-level and predates recent organoid work (watrin2015causesandconsequences pages 1-2) |
| de Sainte Agathe et al., 2023, *Journal of Medical Genetics*, https://doi.org/10.1136/jmg-2022-108803 | Human genetics cohort + molecular interpretation | Supports / qualifies | ARF-pathway perturbation is a credible upstream cause of PVNH through vesicle trafficking and apical junction biology | ARF1-related disorder cohort confirmed PVNH among core phenotypes and explicitly linked ARF1 biology to apical adhesion, junction formation, vesicle trafficking, and membrane turnover, reinforcing the trafficking arm of the apical-integrity model (agathe2023arf1relateddisorderphenotypic pages 7-7) | ARF1-related neurodevelopmental disorder with PVNH | Moderate; strong genetic plausibility but less direct tissue-level demonstration of ventricular denudation than FLNA/ARFGEF2 studies (agathe2023arf1relateddisorderphenotypic pages 7-7) |


*Table: This table summarizes key supporting, qualifying, and competing evidence for the Apical Neuroependyma Integrity Failure Model in periventricular heterotopia/PVNH. It highlights where the model is strongly supported by human tissue and experimental studies, and where alternative mechanisms such as migration/autophagy or AKT-mTOR signaling may better explain specific subtypes.*

---

## Strongest Direct Evidence Supporting the Hypothesis

### A. Human postmortem PVH shows neuroependyma disruption adjacent to nodules (2009)
Ferland et al. (Human Molecular Genetics, Feb 2009; DOI: **10.1093/hmg/ddn377**, URL: https://doi.org/10.1093/hmg/ddn377) provide the most direct human tissue support: in **four postmortem PH brains**, the **neuroependyma was disrupted in all cases** near nodules, while neurons were reported to have “migrated appropriately into the cortex,” suggesting nodules are not simply due to global neuronal motility failure (ferland2009disruptionofneural pages 1-2).

### B. Causal perturbations disrupt apical adhesion markers and induce periventricular nodules
In the same Ferland et al. study, **dominant-negative FLNA** electroporation in mouse embryonic progenitors caused impaired departure from ventricle and **localized loss/redistribution of β-catenin/α-catenin at apical contacts**, directly linking FLNA/actin scaffolding to adherens junction integrity (ferland2009disruptionofneural pages 7-8, ferland2009disruptionofneural pages 6-7).

Further, **brefeldin A (BFA)**—a vesicle trafficking inhibitor—caused **β-catenin accumulation in Golgi**, disrupted β-catenin/N-cadherin/F-actin continuity at the neuroepithelium, and **postnatal intraventricular BFA induced periventricular nodules** (ferland2009disruptionofneural pages 9-10). While not gene-specific, this provides strong causal evidence that **trafficking-dependent delivery of adhesion machinery** can be sufficient to generate nodular periventricular pathology.

### C. Mechanistic linkage between ARFGEF2 trafficking and FLNA localization (2006)
Lu et al. (J Comp Neurol, Jan 2006; DOI: **10.1002/cne.20806**, URL: https://doi.org/10.1002/cne.20806) show ARFGEF2 and FLNA **overlap in neuroependymal progenitors**, and that dominant-negative ARFGEF2 in a neuronal cell line can **partially block FLNA transport from Golgi to plasma membrane**, providing a trafficking-to-cytoskeletal-scaffold linkage consistent with the seed chain (lu2006overlappingexpressionof pages 1-2).

---

## Evidence That Qualifies, Competes With, or Limits the Hypothesis

### 1) NEDD4L PVNH: signaling and positioning defects without demonstrated lining denudation
Broix et al. (Nature Genetics, Oct 2016; DOI: **10.1038/ng.3676**, URL: https://doi.org/10.1038/ng.3676) show that NEDD4L HECT-domain PVNH mutants cause **neuronal positioning arrest in VZ/SVZ/IZ with depletion of cortical plate**, increased mitotic index of apical progenitors, and implicate **AKT/mTOR and Smad2/3** dysregulation. Importantly, **Nedd4l RNAi knockdown did not show significant differences** vs control, arguing against simple haploinsufficiency, and the excerpted evidence focuses on signaling/migration/terminal translocation rather than apical junction failure per se (broix2016mutationsinthe pages 6-8). This supports a **parallel mechanism** where PVNH can arise through perturbed **growth-factor signaling and neuronal positioning programs**.

### 2) FAT4/DCHS1 PVH: autophagy/focal-adhesion migration mechanism (2023)
Bressan et al. provide quantitative migration and pharmacologic response data consistent with an **autophagy-mediated focal adhesion recycling defect** in patient-derived cells, and demonstrate **metformin rescue** of migration (bressan2023metforminrescuesmigratory pages 7-9). This competes with an interpretation that FAT4/DCHS1 PVH requires primary ventricular lining disruption, though it does not rule it out as an upstream contributor.

### 3) Explicit heterogeneity statements from authoritative sources
Watrin et al. (CNS Neurosci Ther, Feb 2015; DOI: **10.1111/cns.12322**, URL: https://doi.org/10.1111/cns.12322) explicitly caution that heterotopia should not be viewed only as a migration defect and that causative genes also affect **radial glia, proliferation, and differentiation programs**, implying multiple mechanistic routes to PVNH (watrin2015causesandconsequences pages 1-2).

---

## Mechanistic Causal Chain (Seed Model) With Evidence Strength Annotations

1. **Upstream trigger:** pathogenic variants/perturbations in apical scaffold genes (e.g., FLNA; ARFGEF2/BIG2; ARF1; cadherin modules).
   - Strong for FLNA/ARFGEF2 as causal PVNH genes and apical-associated expression/perturbation (ferland2009disruptionofneural pages 1-2, lu2006overlappingexpressionof pages 1-2).
   - Emerging for ARF1 PVNH association (2023 cohort) (agathe2023arf1relateddisorderphenotypic pages 7-7).

2. **Cell biological lesion:** defective vesicle trafficking and/or actin coupling causes **mislocalization or loss of adherens junction components (cadherins/β-catenin/α-catenin)** at the apical endfeet.
   - Strong causal perturbation evidence: dominant-negative FLNA disrupts apical catenin localization (ferland2009disruptionofneural pages 7-8, ferland2009disruptionofneural pages 6-7).
   - Strong causal perturbation evidence: BFA disrupts cadherin/catenin/actin organization and yields nodules (ferland2009disruptionofneural pages 9-10).
   - Mechanistic plausibility that ARFGEF2 controls FLNA membrane targeting (lu2006overlappingexpressionof pages 1-2).

3. **Tissue-scale consequence:** focal **neuroependyma/ventricular lining disruption (denudation)** and/or progenitor delamination/mispositioning near ventricle.
   - Strong human evidence: disrupted neuroependyma adjacent to nodules in postmortem PH (ferland2009disruptionofneural pages 1-2).
   - Supported by developmental model systems summarized in later synthesis (viola2024radialgliaprogenitor pages 2-5, viola2024radialgliaprogenitor pages 11-11).

4. **Neurodevelopmental output:** altered progenitor fate/output and/or retention of later-born neurons near ventricle → **periventricular nodules**, with secondary migration/terminal translocation defects.
   - Supported by Ferland et al. human and model evidence that nodules are later-born neurons and align with denuded regions; BrdU data argue against postnatal SVZ overproliferation as the nodule source (ferland2009disruptionofneural pages 1-2, ferland2009disruptionofneural pages 9-10).

**Main inferred/missing steps:** For several genes, the causal route from variant → specific apical junction failure event → nodule formation remains inferred rather than directly tested (sheen2014filaminamediated pages 3-4, watrin2015causesandconsequences pages 1-2).

---

## Current Applications and Real-World Implementations

### A. Precision mechanism-informed rescue (experimental/early translational)
A concrete mechanism-targeted intervention is shown by **metformin rescuing migration deficits** in FAT4/DCHS1 patient-derived hNPCs in vivo slice imaging after xenograft, consistent with **AMPK-dependent autophagy modulation** (Bressan et al., 2023; DOI:10.15252/emmm.202216908) (bressan2023metforminrescuesmigratory pages 7-9).

### B. Diagnostic interpretation and patient stratification by mechanism
The evidence supports stratifying PVNH into mechanistic classes:
- **Apical lining/trafficking–adhesion class:** FLNA, ARFGEF2/BIG2, ARF-pathway (ARF1) (ferland2009disruptionofneural pages 1-2, lu2006overlappingexpressionof pages 1-2, agathe2023arf1relateddisorderphenotypic pages 7-7)
- **Signaling/positioning class:** NEDD4L (AKT/mTOR; terminal translocation/positioning) (broix2016mutationsinthe pages 6-8)
- **Autophagy/focal adhesion migration class:** FAT4/DCHS1 (bressan2023metforminrescuesmigratory pages 7-9)

This supports real-world implementation in clinical genetics as an interpretive framework for variant prioritization and counseling (review-level orientation) (watrin2015causesandconsequences pages 1-2).

---

## Expert Opinions and Authoritative Analyses

- Ferland et al. propose a “final common pathway” where **vesicle trafficking disruption impairs cell adhesion and neuroependymal integrity** (primary mechanistic stance aligned to the seed hypothesis) (ferland2009disruptionofneural pages 1-2, ferland2009disruptionofneural pages 9-10).
- Watrin et al. emphasize that gray matter heterotopia should not be framed as migration-only and highlight diversity of developmental program disruptions, supporting a **pluralistic causal architecture** (watrin2015causesandconsequences pages 1-2).
- Sheen’s synthesis highlights apical abscission, actin, vesicle trafficking, adhesion and cilia as a coordinated apical mechanism but explicitly notes unresolved steps (review-level) (sheen2014filaminamediated pages 3-4).

---

## Relevant Statistics and Data (from retrieved evidence)

- **Migration assay quantitative data (2023, FAT4/DCHS1):** multiple migration metrics with sample sizes and significance testing; e.g., **n = 17 cells/11 mice** (control) for time-lapse imaging and significant bafilomycin effect in controls but not mutants (bressan2023metforminrescuesmigratory pages 7-9).
- **PVNH prevalence statistic (2016, NEDD4L paper background):** PNH is noted as **~31% of malformations of cortical development** in Broix et al. background text (broix2016mutationsinthe pages 3-4).

---

## Knowledge Gaps (Checked vs Not Found)

### Gap 1: Gene-by-gene confirmation that ventricular lining disruption is the proximate lesion
**Why it matters:** The seed hypothesis lists multiple genes; the strongest direct ventricular denudation evidence is concentrated in **FLNA/ARFGEF2** contexts.
**What was checked:** searches and evidence extraction across 2023–2024 literature plus key foundational studies; retrieved direct FLNA/ARFGEF2 human postmortem and in vivo perturbation data (ferland2009disruptionofneural pages 1-2, ferland2009disruptionofneural pages 9-10, lu2006overlappingexpressionof pages 1-2), but not equivalently direct data for ERMARD, GNAI2, TMEM67.
**What would resolve it:** targeted histopathology/immunostaining of ventricular lining markers (N-cadherin, β-catenin, ZO proteins, apical actin) in **genetically confirmed** ERMARD, GNAI2, TMEM67 PVNH cases and corresponding iPSC-derived organoids with engineered variants.

### Gap 2: Apical abscission as a causal step remains under-tested in PVNH genetics
**Checked:** apical abscission appears in synthesis and hypothesis framing (sheen2014filaminamediated pages 3-4) but was not supported by direct quantitative evidence in retrieved primary PVNH subtype papers.
**Resolution:** live imaging of apical abscission in human cortical organoids carrying FLNA/ARFGEF2 variants with CRISPR-rescues; quantification of abscission timing, ciliary disassembly, and junctional remodeling vs controls.

### Gap 3: Mechanistic integration across “apical integrity” vs “intrinsic migration” classes
**Why it matters:** FAT4/DCHS1 and NEDD4L data support strong non-apical proximate mechanisms. It is unknown whether these converge upstream on subtle apical defects or represent distinct etiologic routes.
**Checked:** Bressan 2023 excerpt did not test ventricular lining integrity directly (bressan2023metforminrescuesmigratory pages 7-9); Broix 2016 excerpts emphasize migration/positioning signaling without lining integrity readouts (broix2016mutationsinthe pages 6-8).
**Resolution:** combined assays measuring apical junction integrity and delamination *and* migration dynamics in the same models, e.g., organoids with ventricular-like surfaces + xenograft migration assays.

### Gap 4: GNAI2 as a PVNH mechanism node (2024 claim) lacks accessible primary details
**Checked:** tool search surfaced an unobtainable 2024 Neurological Sciences report claiming a new GNAI2 variant as a rare PVNH cause (DOI:10.1007/s10072-024-07764-6; unobtainable in current run). No mechanistic evidence extractable.
**Resolution:** obtain full text and extract phenotype, variant interpretation, and any functional assays; follow with pathway experiments linking GNAI2 to apical polarity/junction maintenance.

---

## Alternative / Competing Mechanistic Models

1. **Intrinsic neuronal migration/autophagy–focal adhesion model (FAT4/DCHS1 subtype):** DCHS1/FAT4 mutations impair autophagy and paxillin recycling, directly altering migration and rescuable by metformin (parallel mechanism; may be upstream or independent of apical lining loss) (bressan2023metforminrescuesmigratory pages 7-9).

2. **PI3K–AKT–mTOR and terminal translocation/positioning model (NEDD4L subtype):** NEDD4L mutants disrupt AKT/mTOR/Smad signaling and lead to arrested positioning of neurons and altered progenitor dynamics; does not require demonstrated ventricular denudation in the extracted evidence (competing proximate lesion) (broix2016mutationsinthe pages 6-8).

3. **Cell-autonomous mosaic migration defect model (FLNA mosaicism):** some accounts support mutant neurons failing to migrate while others migrate normally in FLNA X-inactivation mosaics, potentially explaining nodularity without requiring widespread lining failure (complementary/parallel) (sheen2012periventricularheterotopiashuttling pages 2-3).

4. **Radial glial scaffold/basal lamina attachment failure:** broader cortical malformation literature and synthesis emphasize basement membrane/ECM attachment and scaffold disruption as heterotopia drivers (parallel; often intersects with apical polarity) (viola2024radialgliaprogenitor pages 6-7).

---

## Discriminating Tests (Most Efficient Next Studies)

1. **Patient-stratified ventricular lining pathology study**
- **Cohort:** genetically confirmed PVNH for FLNA, ARFGEF2, ARF1, NEDD4L, FAT4/DCHS1, ERMARD, GNAI2.
- **Assay:** postmortem or surgical tissue (when available) + high-resolution immunostaining for apical junctions (CDH2, β-catenin, α-catenin), apical actin, basal bodies/cilia markers; correlate with MRI nodule location.
- **Expected outcomes:** apical integrity model predicts consistent focal denudation/junction loss adjacent to nodules for “apical class” genes; signaling/autophagy classes may show preserved lining with downstream migration abnormalities.

2. **Unified organoid platform measuring apical integrity and migration**
- **Model:** cortical organoids with ventricle-like rosettes; CRISPR engineered variants and isogenic controls.
- **Readouts:** live imaging of apical junction continuity, apical abscission dynamics, delamination rates; plus neuronal migration tracking.
- **Perturbation:** rescue with trafficking enhancers, actin stabilizers, mTOR inhibitors (rapamycin), AMPK/autophagy modulators (metformin).
- **Expected outcomes:** differential rescue signatures distinguish apical-junction primary failure vs mTOR vs autophagy mechanisms.

3. **Mechanistic epistasis: trafficking → adhesion delivery → lining integrity**
- **Test:** in FLNA/ARFGEF2 contexts, quantify delivery of E-cadherin/N-cadherin/β-catenin to apical surface, and determine whether correcting trafficking restores lining integrity and prevents nodule formation.
- **Anchor evidence:** BFA effects on adhesion/actin continuity and nodule induction motivate this direct causality test (ferland2009disruptionofneural pages 9-10).

---

## Curation Leads (Require Curator Verification)

### Lead 1: Strong support references for apical integrity failure mechanism
- **Ferland et al., 2009** (HMG; DOI:10.1093/hmg/ddn377; URL: https://doi.org/10.1093/hmg/ddn377): verify exact human histopathology language that “neuroependyma was disrupted in all PH cases” and map to nodes: *ventricular zone disruption* → *loss of adherens junction/catenin localization* → *periventricular nodules* (ferland2009disruptionofneural pages 1-2, ferland2009disruptionofneural pages 9-10).
- **Lu et al., 2006** (J Comp Neurol; DOI:10.1002/cne.20806; URL: https://doi.org/10.1002/cne.20806): verify trafficking claim “dominant negative ARFGEF2 partially blocks FLNA transport from Golgi to plasma membrane” and encode edge: **ARFGEF2 → FLNA membrane targeting** (lu2006overlappingexpressionof pages 1-2).

### Lead 2: Qualifier/competing-mechanism references to add as subtype restrictions
- **Bressan et al., 2023** (EMBO Mol Med; DOI:10.15252/emmm.202216908; URL: https://doi.org/10.15252/emmm.202216908): curator to verify abstract statements and key quantitative migration metrics; add edges: **FAT4/DCHS1 → impaired autophagy → paxillin accumulation → migration deficit**; include intervention node **metformin → AMPK/autophagy → rescue migration** (bressan2023metforminrescuesmigratory pages 7-9).
- **Broix et al., 2016** (Nat Genet; DOI:10.1038/ng.3676; URL: https://doi.org/10.1038/ng.3676): add competing mechanism edges: **NEDD4L mutants → AKT/mTOR/Smad deregulation → neuronal positioning arrest / altered progenitor mitotic index** (broix2016mutationsinthe pages 6-8).

### Lead 3: Candidate new PVNH gene evidence (unverified in this run)
- **Decio et al., 2024** (*Neurological Sciences*; DOI:10.1007/s10072-024-07764-6): “A new variant confirms GNAI2 as a rare cause of periventricular nodular heterotopia.” *Full text unobtainable here; requires curator retrieval and verification.* (unobtainable paper noted during search)

### Candidate ontology terms (suggested)
- Cell types: radial glia; apical radial glia (aRG); neuroepithelial progenitor.
- Processes: adherens junction organization; apical–basal polarity; vesicle-mediated transport (Golgi-to-plasma membrane); ependymal/ventricular lining integrity; neuronal migration; terminal translocation; autophagy; focal adhesion turnover; PI3K–AKT–mTOR signaling.

---

## Summary

The **apical neuroependyma integrity failure** mechanism is best supported as a **high-confidence pathway for FLNA/ARFGEF2(BIG2)-linked PVNH** where human tissue and experimental perturbations converge on **apical junction disruption and ventricular lining denudation** (ferland2009disruptionofneural pages 1-2, ferland2009disruptionofneural pages 9-10, lu2006overlappingexpressionof pages 1-2). Recent 2023–2024 work underscores **mechanistic heterogeneity**: FAT4/DCHS1 PVH can involve **autophagy–paxillin migration defects with metformin rescue**, and NEDD4L PVNH can involve **AKT/mTOR-driven neuronal positioning defects**—both of which qualify the seed module as **canonical but not exclusive** across PVNH etiologies (bressan2023metforminrescuesmigratory pages 7-9, broix2016mutationsinthe pages 6-8, watrin2015causesandconsequences pages 1-2).

References

1. (ferland2009disruptionofneural pages 1-2): Russell J. Ferland, Luis Federico Batiz, Jason Neal, Gewei Lian, Elizabeth Bundock, Jie Lu, Yi-Chun Hsiao, Rachel Diamond, Davide Mei, Alison H. Banham, Philip J. Brown, Charles R. Vanderburg, Jeffrey Joseph, Jonathan L. Hecht, Rebecca Folkerth, Renzo Guerrini, Christopher A. Walsh, Esteban M. Rodriguez, and Volney L. Sheen. Disruption of neural progenitors along the ventricular and subventricular zones in periventricular heterotopia. Human molecular genetics, 18 3:497-516, Feb 2009. URL: https://doi.org/10.1093/hmg/ddn377, doi:10.1093/hmg/ddn377. This article has 221 citations and is from a domain leading peer-reviewed journal.

2. (ferland2009disruptionofneural pages 7-8): Russell J. Ferland, Luis Federico Batiz, Jason Neal, Gewei Lian, Elizabeth Bundock, Jie Lu, Yi-Chun Hsiao, Rachel Diamond, Davide Mei, Alison H. Banham, Philip J. Brown, Charles R. Vanderburg, Jeffrey Joseph, Jonathan L. Hecht, Rebecca Folkerth, Renzo Guerrini, Christopher A. Walsh, Esteban M. Rodriguez, and Volney L. Sheen. Disruption of neural progenitors along the ventricular and subventricular zones in periventricular heterotopia. Human molecular genetics, 18 3:497-516, Feb 2009. URL: https://doi.org/10.1093/hmg/ddn377, doi:10.1093/hmg/ddn377. This article has 221 citations and is from a domain leading peer-reviewed journal.

3. (ferland2009disruptionofneural pages 9-10): Russell J. Ferland, Luis Federico Batiz, Jason Neal, Gewei Lian, Elizabeth Bundock, Jie Lu, Yi-Chun Hsiao, Rachel Diamond, Davide Mei, Alison H. Banham, Philip J. Brown, Charles R. Vanderburg, Jeffrey Joseph, Jonathan L. Hecht, Rebecca Folkerth, Renzo Guerrini, Christopher A. Walsh, Esteban M. Rodriguez, and Volney L. Sheen. Disruption of neural progenitors along the ventricular and subventricular zones in periventricular heterotopia. Human molecular genetics, 18 3:497-516, Feb 2009. URL: https://doi.org/10.1093/hmg/ddn377, doi:10.1093/hmg/ddn377. This article has 221 citations and is from a domain leading peer-reviewed journal.

4. (agathe2023arf1relateddisorderphenotypic pages 7-7): Jean-Madeleine de Sainte Agathe, Ben Pode-Shakked, Sophie Naudion, Vincent Michaud, Benoit Arveiler, Patricia Fergelot, Jean Delmas, Boris Keren, Céline Poirsier, Fowzan S Alkuraya, Brahim Tabarki, Eric Bend, Kellie Davis, Martina Bebin, Michelle L Thompson, Emily M Bryant, Matias Wagner, Iris Hannibal, Jerica Lenberg, Martin Krenn, Kristen M Wigby, Jennifer R Friedman, Maria Iascone, Anna Cereda, Térence Miao, Eric LeGuern, Emanuela Argilli, Elliott Sherr, Oana Caluseriu, Timothy Tidwell, Pinar Bayrak-Toydemir, Caroline Hagedorn, Melanie Brugger, Katharina Vill, Francois-Dominique Morneau-Jacob, Wendy Chung, Kathryn N Weaver, Joshua W Owens, Ammar Husami, Bimal P Chaudhari, Brandon S Stone, Katie Burns, Rachel Li, Iris M de Lange, Margaux Biehler, Emmanuelle Ginglinger, Bénédicte Gérard, Rolf W Stottmann, and Aurélien Trimouille. Arf1-related disorder: phenotypic and molecular spectrum. Journal of Medical Genetics, 60:999-1005, Apr 2023. URL: https://doi.org/10.1136/jmg-2022-108803, doi:10.1136/jmg-2022-108803. This article has 17 citations and is from a domain leading peer-reviewed journal.

5. (broix2016mutationsinthe pages 6-8): Loïc Broix, Hélène Jagline, Ekaterina L Ivanova, Stephane Schmucker, N. Drouot, J. Clayton-Smith, A. Pagnamenta, K. Metcalfe, B. Isidor, U. W. Louvier, A. Poduri, Jenny C. Taylor, Peggy Tilly, K. Poirier, Yoann Saillour, N. Lebrun, Tristan Stemmelen, G. Rudolf, G. Muraca, B. Saintpierre, Adrienne Elmorjani, Martin Moïse, Nathalie Bednarek Weirauch, R. Guerrini, A. Boland, R. Olaso, C. Masson, Ratna Tripathy, David A. Keays, C. Beldjord, L. Nguyen, Juliette D. Godin, U. Kini, Patrick Nischké, J. Deleuze, N. Bahi-Buisson, I. Sumara, M. Hinckelmann, and J. Chelly. Mutations in the hect domain of nedd4l lead to akt/mtor pathway deregulation and cause periventricular nodular heterotopia. Nature genetics, 48:1349-1358, Oct 2016. URL: https://doi.org/10.1038/ng.3676, doi:10.1038/ng.3676. This article has 134 citations and is from a highest quality peer-reviewed journal.

6. (bressan2023metforminrescuesmigratory pages 7-9): Cedric Bressan, Marta Snapyan, Marina Snapyan, Johannes Klaus, Francesco di Matteo, Stephen P Robertson, Barbara Treutlein, Martin Parent, Silvia Cappello, and Armen Saghatelyan. Metformin rescues migratory deficits of cells derived from patients with periventricular heterotopia. EMBO Molecular Medicine, Aug 2023. URL: https://doi.org/10.15252/emmm.202216908, doi:10.15252/emmm.202216908. This article has 3 citations and is from a highest quality peer-reviewed journal.

7. (watrin2015causesandconsequences pages 1-2): Françoise Watrin, Jean‐Bernard Manent, Carlos Cardoso, and Alfonso Represa. Causes and consequences of gray matter heterotopia. CNS Neuroscience & Therapeutics, 21:112-122, Feb 2015. URL: https://doi.org/10.1111/cns.12322, doi:10.1111/cns.12322. This article has 87 citations and is from a peer-reviewed journal.

8. (sheen2014filaminamediated pages 3-4): Volney L Sheen. Filamin a mediated big2 dependent endocytosis. Tissue Barriers, 2:e29431, Jan 2014. URL: https://doi.org/10.4161/tisb.29431, doi:10.4161/tisb.29431. This article has 22 citations and is from a peer-reviewed journal.

9. (viola2024radialgliaprogenitor pages 2-5): Valeria Viola, Kaviya Chinnappa, and Fiona Francis. Radial glia progenitor polarity in health and disease. Frontiers in Cell and Developmental Biology, Oct 2024. URL: https://doi.org/10.3389/fcell.2024.1478283, doi:10.3389/fcell.2024.1478283. This article has 8 citations.

10. (viola2024radialgliaprogenitor pages 11-11): Valeria Viola, Kaviya Chinnappa, and Fiona Francis. Radial glia progenitor polarity in health and disease. Frontiers in Cell and Developmental Biology, Oct 2024. URL: https://doi.org/10.3389/fcell.2024.1478283, doi:10.3389/fcell.2024.1478283. This article has 8 citations.

11. (viola2024radialgliaprogenitor pages 6-7): Valeria Viola, Kaviya Chinnappa, and Fiona Francis. Radial glia progenitor polarity in health and disease. Frontiers in Cell and Developmental Biology, Oct 2024. URL: https://doi.org/10.3389/fcell.2024.1478283, doi:10.3389/fcell.2024.1478283. This article has 8 citations.

12. (ferland2009disruptionofneural pages 6-7): Russell J. Ferland, Luis Federico Batiz, Jason Neal, Gewei Lian, Elizabeth Bundock, Jie Lu, Yi-Chun Hsiao, Rachel Diamond, Davide Mei, Alison H. Banham, Philip J. Brown, Charles R. Vanderburg, Jeffrey Joseph, Jonathan L. Hecht, Rebecca Folkerth, Renzo Guerrini, Christopher A. Walsh, Esteban M. Rodriguez, and Volney L. Sheen. Disruption of neural progenitors along the ventricular and subventricular zones in periventricular heterotopia. Human molecular genetics, 18 3:497-516, Feb 2009. URL: https://doi.org/10.1093/hmg/ddn377, doi:10.1093/hmg/ddn377. This article has 221 citations and is from a domain leading peer-reviewed journal.

13. (lu2006overlappingexpressionof pages 1-2): Jie Lu, Grace Tiao, Rebecca Folkerth, Jonathon Hecht, Christopher Walsh, and Volney Sheen. Overlapping expression of arfgef2 and filamin a in the neuroependymal lining of the lateral ventricles: insights into the cause of periventricular heterotopia. Journal of Comparative Neurology, 494:476-484, Jan 2006. URL: https://doi.org/10.1002/cne.20806, doi:10.1002/cne.20806. This article has 63 citations and is from a peer-reviewed journal.

14. (broix2016mutationsinthe pages 3-4): Loïc Broix, Hélène Jagline, Ekaterina L Ivanova, Stephane Schmucker, N. Drouot, J. Clayton-Smith, A. Pagnamenta, K. Metcalfe, B. Isidor, U. W. Louvier, A. Poduri, Jenny C. Taylor, Peggy Tilly, K. Poirier, Yoann Saillour, N. Lebrun, Tristan Stemmelen, G. Rudolf, G. Muraca, B. Saintpierre, Adrienne Elmorjani, Martin Moïse, Nathalie Bednarek Weirauch, R. Guerrini, A. Boland, R. Olaso, C. Masson, Ratna Tripathy, David A. Keays, C. Beldjord, L. Nguyen, Juliette D. Godin, U. Kini, Patrick Nischké, J. Deleuze, N. Bahi-Buisson, I. Sumara, M. Hinckelmann, and J. Chelly. Mutations in the hect domain of nedd4l lead to akt/mtor pathway deregulation and cause periventricular nodular heterotopia. Nature genetics, 48:1349-1358, Oct 2016. URL: https://doi.org/10.1038/ng.3676, doi:10.1038/ng.3676. This article has 134 citations and is from a highest quality peer-reviewed journal.

15. (sheen2012periventricularheterotopiashuttling pages 2-3): Volney L. Sheen. Periventricular heterotopia: shuttling of proteins through vesicles and actin in cortical development and disease. Scientifica, 2012:1-13, Oct 2012. URL: https://doi.org/10.6064/2012/480129, doi:10.6064/2012/480129. This article has 26 citations and is from a peer-reviewed journal.

## Artifacts

- [Edison artifact artifact-00](falcon_artifacts/artifact-00.md)
