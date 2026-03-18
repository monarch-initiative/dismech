# Checkpoint Inhibitors: Cross-Cutting Analysis

## Motivation

Immune checkpoint inhibitors (ICIs) are now standard-of-care across dozens of cancer types, yet the dismech knowledge base treats each occurrence independently. The same biological mechanism -- tumor cells exploit PD-1/PD-L1 or CTLA-4 signaling to suppress antitumor T cell activity -- is re-described from scratch in each disorder file. This creates:

1. **Redundancy**: The PD-L1 upregulation / T cell exhaustion / immune evasion causal chain is copy-pasted across files
2. **Inconsistency**: Some files model immune evasion in `pathophysiology`, others only mention ICIs in `treatments`, and most don't link the two via `target_mechanisms`
3. **Missed insight**: No way to query "which disorders share this drug mechanism class?" or "what are the common resistance patterns?"

This project proposes treating checkpoint inhibitor mechanisms as **design patterns** (analogous to the existing `fibrotic_response` module), so disorder entries can declare conformance while specializing to their tumor context.

## Current State Audit

### Diseases Treated by Checkpoint Inhibitors (in KB)

| Disorder | Drug(s) Mentioned | In Treatments? | In Pathophys? | Linked via target_mechanisms? |
|----------|-------------------|:-:|:-:|:-:|
| Non-Small Cell Lung Cancer | nivolumab, pembrolizumab, durvalumab | Yes | Yes ("Immune Evasion" node) | No |
| BRAF V600 Mutant Melanoma | pembrolizumab, nivolumab, ipilimumab | Yes | Yes (immune evasion in TME) | No |
| Clear Cell Renal Cell Carcinoma | nivolumab, pembrolizumab, ipilimumab | Yes | Yes | No |
| Small Cell Lung Cancer | atezolizumab, durvalumab | Yes | Yes | No |
| Cutaneous Squamous Cell Carcinoma | cemiplimab | Yes | Yes ("TME Remodeling & Immune Evasion") | No |
| Triple-Negative Breast Cancer | pembrolizumab | Yes | Yes | No |
| Hepatocellular Carcinoma | atezolizumab, durvalumab | Yes | Yes | No |
| Merkel Cell Carcinoma | avelumab, pembrolizumab | Yes | Yes | No |
| Malignant Mesothelioma | nivolumab + ipilimumab | Yes | Partial | No |
| NRAS Mutant Melanoma | (ICI mentioned in context) | Partial | Yes | No |
| KIT Mutant Melanoma | (ICI mentioned) | Partial | Yes | No |
| Lung Carcinoma | (general ICI reference) | Yes | Yes | No |
| EBV-Associated Gastric Cancer | pembrolizumab, nivolumab | Yes | Yes | No |
| Nasopharyngeal Carcinoma | (ICI mentioned) | Yes | Yes | No |
| HPV-Positive Head and Neck Cancer | (ICI mentioned) | Yes | Yes | No |

### Key Observation: Treatments and Pathophysiology Are Disconnected

The schema already has `target_mechanisms` on the Treatment class (linking to `TreatmentMechanismTarget` with `treatment_effect` enum: INHIBITS, ACTIVATES, MODULATES, BYPASSES, RESTORES). However, **zero checkpoint inhibitor treatments currently use `target_mechanisms`**. The treatment sections say "pembrolizumab for PD-L1 high tumors" and the pathophysiology sections describe "PD-L1 upregulation enables immune evasion" -- but they don't connect.

### How Immune Evasion Is Currently Modeled

Files that do model immune evasion in pathophysiology use varying structures:

**NSCLC pattern** (most complete):
```yaml
- name: Immune Evasion
  description: Cancer cells develop mechanisms to evade detection...
  biological_processes:
  - preferred_term: immune response
    term: {id: GO:0006955, label: immune response}
    modifier: DECREASED
  evidence: [4 PMIDs covering HLA loss, PD-L1, MHC-I downregulation]
```

**Cutaneous SCC pattern**:
```yaml
- name: Tumor Microenvironment Remodeling and Immune Evasion
  description: PD-L1 upregulation suppresses antitumor T cell activity...
  cell_types: [macrophage, T cell]
  biological_processes: [regulation of T cell activation]
```

**Most files**: No immune evasion pathophysiology node at all -- ICIs appear only in treatments.

## Proposed: Checkpoint Inhibitor Mechanism Module

Following the `fibrotic_response` module pattern, we propose a `checkpoint_inhibitor_response` module that captures the conserved immune evasion → ICI response causal chain.

### Module Structure (Draft)

```
checkpoint_inhibitor_response.yaml
├── Tumor Antigen Presentation                   [trigger]
│   └── Neoantigen generation, MHC-I loading
├── Antitumor T Cell Activation                   [effector]
│   └── CD8+ cytotoxic T cell priming and expansion
├── Adaptive Immune Resistance (Checkpoint Upregulation)  [central_effector]
│   └── Tumor PD-L1 upregulation, CTLA-4 engagement on T cells
│   └── T cell exhaustion, reduced cytotoxicity
├── Immunosuppressive Microenvironment             [amplifier]
│   └── Treg expansion, M2 macrophage polarization, MDSCs
└── Immune Escape and Tumor Progression            [consequence]
    └── Continued tumor growth despite immune recognition
```

### How Disorder Entries Would Conform

```yaml
# In kb/disorders/Non-Small_Cell_Lung_Cancer.yaml
pathophysiology:
- name: Immune Evasion via PD-L1 Upregulation
  conforms_to: "checkpoint_inhibitor_response#Adaptive Immune Resistance (Checkpoint Upregulation)"
  cell_types:
  - preferred_term: CD8-positive cytotoxic T cell
    term: {id: CL:0000794, label: CD8-positive, alpha-beta cytotoxic T cell}
  biological_processes:
  - preferred_term: PD-L1 Expression
    term: {id: GO:0006955, label: immune response}
    modifier: DECREASED
  evidence: [existing NSCLC-specific evidence]
```

### Treatment → Mechanism Linkage

The key value: treatments can now declare which module node they target:

```yaml
treatments:
- name: Pembrolizumab (Anti-PD-1)
  description: Blocks PD-1 receptor on T cells, restoring antitumor immunity
  treatment_term:
    preferred_term: immune checkpoint inhibitor therapy
    term: {id: MAXO:0001002, label: immunotherapy procedure}
  therapeutic_agent:
    preferred_term: pembrolizumab
    term: {id: NCIT:C106432, label: Pembrolizumab}
  target_mechanisms:
  - target: Immune Evasion via PD-L1 Upregulation
    treatment_effect: INHIBITS
    description: Blocks PD-1/PD-L1 interaction, restoring CD8+ T cell cytotoxicity
```

This closes the loop: you can now traverse `treatment → target_mechanisms → pathophysiology node → downstream consequences` to reason about which phenotypes should respond.

## Drug Mechanism Classes as Design Patterns

Beyond checkpoint inhibitors, this pattern generalizes to other drug mechanism classes:

| Drug Mechanism Class | Conserved Target | Example Drugs | Candidate Disorders |
|---------------------|-----------------|---------------|-------------------|
| **Anti-PD-1/PD-L1** | PD-1/PD-L1 checkpoint axis | pembrolizumab, nivolumab, atezolizumab | NSCLC, melanoma, RCC, TNBC, SCLC, HCC, UC |
| **Anti-CTLA-4** | CTLA-4 on T cells (priming phase) | ipilimumab, tremelimumab | melanoma, RCC, mesothelioma |
| **Combination ICI** | Both checkpoints | nivo+ipi, pembro+ipi | melanoma, RCC, NSCLC, MSI-H CRC |
| **VEGF/VEGFR inhibitors** | Tumor angiogenesis | bevacizumab, sunitinib | RCC, CRC, HCC, GBM |
| **BRAF/MEK inhibitors** | MAPK pathway | dabrafenib+trametinib | BRAF melanoma, BRAF NSCLC |
| **CDK4/6 inhibitors** | Cell cycle G1/S | palbociclib, ribociclib | ER+ breast cancer |
| **PARP inhibitors** | DNA damage repair | olaparib, niraparib | BRCA-mutant ovarian, breast, prostate |
| **BCR-ABL TKIs** | Fusion kinase | imatinib, dasatinib | CML |

Each class could become a **mechanism module** that disorder files conform to. The module defines the conserved causal chain; the disorder entry specializes cell types, biomarkers, and tumor context.

### Advantages of the Design Pattern Approach

1. **Queryability**: "Show all disorders where anti-PD-1 therapy INHIBITS immune evasion" becomes a graph query
2. **Consistency**: New cancer entries inherit a validated causal structure for immune evasion
3. **Resistance modeling**: ICI resistance mechanisms (e.g., beta-2-microglobulin loss, JAK1/2 mutations) can be modeled as nodes that BYPASS the module
4. **Adverse event linkage**: Checkpoint inhibitor-induced autoimmunity (thyroiditis, diabetes, colitis) can reference the same module to explain why restoring T cell activity has off-target effects
5. **Combination rationale**: Why nivo+ipi works can be explained by targeting two different module nodes (CTLA-4 at priming, PD-1 at effector phase)

## ICI-Induced Adverse Events (irAEs)

A unique aspect: checkpoint inhibitors cause disease as well as treat it. The KB already has:
- **Diabetes Mellitus**: documents checkpoint inhibitor-induced insulin-deficient diabetes (PMID:37960733)

Other irAE candidates for KB entries or cross-references:
- Checkpoint inhibitor-induced thyroiditis
- Checkpoint inhibitor-induced colitis
- Checkpoint inhibitor-induced pneumonitis
- Checkpoint inhibitor-induced myocarditis
- Checkpoint inhibitor-induced hepatitis

These could reference the same module in reverse: the treatment that INHIBITS immune evasion in tumors also ACTIVATES autoimmune pathways in normal tissue.

## Implementation Plan

### Phase 1: Module Creation
- [ ] Create `kb/modules/checkpoint_inhibitor_response.yaml` with conserved immune evasion causal chain
- [ ] Validate against schema (modules use same Disease class)
- [ ] Add evidence from landmark ICI mechanism papers (PMID:22658127 Topalian et al., PMID:28060077 Wei et al.)

### Phase 2: Retrofit Existing Entries (Top 5)
- [ ] Non-Small Cell Lung Cancer: Add `conforms_to`, populate `target_mechanisms`
- [ ] BRAF V600 Mutant Melanoma: Add `conforms_to`, populate `target_mechanisms`
- [ ] Clear Cell Renal Cell Carcinoma: Add `conforms_to`, populate `target_mechanisms`
- [ ] Cutaneous Squamous Cell Carcinoma: Add `conforms_to`, populate `target_mechanisms`
- [ ] Hepatocellular Carcinoma: Add `conforms_to`, populate `target_mechanisms`

### Phase 3: Fill Gaps
- [ ] Add immune evasion pathophysiology nodes to cancer entries that only have ICIs in treatments
- [ ] Cross-reference irAE entries with the module
- [ ] Add ICI resistance mechanism nodes (beta-2-microglobulin loss, JAK mutations, WNT/beta-catenin activation)

### Phase 4: Generalize
- [ ] Create additional drug mechanism modules (VEGF inhibition, MAPK pathway inhibition, PARP inhibition)
- [ ] Document the "drug mechanism module" pattern in CLAUDE.md
- [ ] Add schema support for querying across conforming entries

## Key Questions for Discussion

1. **Module granularity**: Should anti-PD-1 and anti-CTLA-4 be separate modules (they target different phases of T cell response) or one combined "checkpoint inhibitor response" module?
2. **Biomarker integration**: PD-L1 expression (TPS/CPS), TMB, and MSI-H are ICI response biomarkers. Should these be formalized in the module or left to individual entries?
3. **Resistance as a module**: ICI resistance mechanisms are themselves conserved across cancers. Separate module or extension of the response module?
4. **irAE modeling**: Should irAEs be modeled as separate disorders that reference the ICI module, or as adverse_effects within the treatment itself?

## References

- Topalian et al. (2012) PMID:22658127 - Safety, activity, and immune correlates of anti-PD-1 antibody in cancer
- Wei et al. (2017) PMID:28060077 - Distinct cellular mechanisms underlie anti-CTLA-4 and anti-PD-1 checkpoint blockade
- Sharma et al. (2017) PMID:28187290 - Primary, adaptive, and acquired resistance to cancer immunotherapy
- Chen & Mellman (2013) PMID:23890059 - Oncology meets immunology: the cancer-immunity cycle
- Ribas & Wolchok (2018) PMID:29236940 - Cancer immunotherapy using checkpoint blockade
