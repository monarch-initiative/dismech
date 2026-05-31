# Checkpoint Inhibitors: Drug Mechanism Design Pattern

## Status: Phase 1 Complete -- Module + 5 Pilot Entries

## 1. Landscape: Which Diseases Are Treated by Checkpoint Inhibitors?

### Diseases with checkpoint inhibitor treatments currently in dismech

| Disease | Drugs Referenced | Has `target_mechanisms`? | Has Immune Evasion Pathophys Node? |
|---------|-----------------|------------------------|------------------------------------|
| MSI-High Colorectal Cancer | pembrolizumab, nivolumab, ipilimumab, dostarlimab | Yes | Yes ("PD-L1 Upregulation and Immune Evasion") |
| Clear Cell Renal Cell Carcinoma | nivolumab, pembrolizumab, ipilimumab | Yes | Yes ("Immune Evasion via PD-L1 and Immunosuppressive Microenvironment") |
| Hepatocellular Carcinoma | atezolizumab, durvalumab, tremelimumab | Yes | Yes ("Immune Evasion via PD-L1 and Immunosuppressive Microenvironment") |
| BRAF V600 Mutant Melanoma | pembrolizumab, nivolumab, ipilimumab | Yes | Yes ("Immune Evasion via PD-L1 Upregulation") |
| NRAS Mutant Melanoma | checkpoint inhibitors (narrative) | No | Partial |
| KIT Mutant Melanoma | checkpoint inhibitors (narrative) | No | Partial |
| Cutaneous Squamous Cell Carcinoma | cemiplimab | No | Partial |
| Non-Small Cell Lung Cancer | checkpoint inhibitors (narrative) | No | Partial |
| Small Cell Lung Cancer | checkpoint inhibitors (narrative) | No | Partial |
| KRAS G12C Mutant NSCLC | checkpoint inhibitors (narrative) | No | Partial |
| Cervical Cancer | pembrolizumab | No | Partial |
| Triple-Negative Breast Cancer | atezolizumab/pembrolizumab (narrative) | No | Yes (immunomodulatory subtype) |
| Nasopharyngeal Carcinoma | PD-1 inhibitors | Yes | Yes ("Immune Evasion") |
| HPV-Positive Head and Neck Cancer | checkpoint inhibitors (narrative) | No | Yes ("Immune Evasion") |
| Merkel Cell Carcinoma | avelumab (narrative) | No | Partial |
| MSI-High Endometrial Cancer | checkpoint inhibitors (narrative) | No | Partial |
| FGFR-Altered Cholangiocarcinoma | durvalumab | No | No |
| IDH-Mutant Cholangiocarcinoma | durvalumab | No | No |
| Malignant Mesothelioma | checkpoint inhibitors (narrative) | No | Partial |
| Basal Cell Carcinoma | cemiplimab (narrative) | No | Partial |
| EBV-Associated Gastric Cancer | checkpoint inhibitors (narrative) | No | Partial |
| Osteosarcoma | checkpoint inhibitors (narrative) | No | Yes ("Tumor Immune Microenvironment Remodeling") |
| Uveal Melanoma | checkpoint inhibitors (noted as poor response) | No | Noted as "immunologically cold" |

### Diseases where checkpoint molecules appear in pathophysiology (not treatment)

| Disease | Context |
|---------|---------|
| Hepatitis B | T cell exhaustion with PD-1, CTLA-4, TIM-3 upregulation |
| Addison's Disease | CTLA4 as autoimmune susceptibility gene |
| Diabetes Mellitus | Checkpoint inhibitor exposure as disease trigger |
| Type 1 Diabetes | Immune checkpoint pathway involvement |
| Autoimmune diseases (multiple) | CTLA-4/PD-1 polymorphisms in autoimmune susceptibility |

## 2. Current Representation Gaps

### Treatment side
- **No `target_mechanisms` links**: Not a single checkpoint inhibitor treatment uses `target_mechanisms` to connect back to the immune evasion pathophysiology node it addresses. This is the core structural gap.
- **All mapped to generic `MAXO:0000058` (pharmacotherapy) or `MAXO:0001002` (immunotherapy procedure)**: No specific MAXO term for "immune checkpoint inhibitor therapy" exists. The best available terms are `MAXO:0000058` (pharmacotherapy) and `MAXO:0001002` (immunotherapy procedure).
- **No shared mechanism-of-action concept**: Each disease independently describes what PD-1/PD-L1 blockade does in its description text. There's no reusable structure.

### Pathophysiology side
- **Inconsistent immune evasion modeling**: Some cancers have explicit "Immune Evasion" or "PD-L1 Upregulation" pathophysiology nodes; many only mention checkpoint molecules in narrative text.
- **No shared immune evasion module**: Unlike `fibrotic_response`, there is no `immune_evasion` module that defines the conserved pattern of: neoantigen presentation → T cell infiltration → adaptive PD-L1 upregulation → T cell exhaustion → immune escape.
- **Cell type and GO term inconsistency**: When immune cells are annotated, the terms vary (CL:0000625 for CD8+ T cells in some, CL:0000084 for generic T cells in others).

### The disconnect
The treatment and pathophysiology sections describe the **same biological process from opposite directions** but are not structurally linked:
- Pathophysiology says: "Tumor upregulates PD-L1 → suppresses T cells → immune evasion"
- Treatment says: "Anti-PD-1 blocks this interaction → restores T cell function"

But there's no `target_mechanisms` edge connecting the treatment to the pathophysiology node.

## 3. Proposal: Drug Mechanism Classes as Design Patterns

### Concept

Just as `kb/modules/fibrotic_response.yaml` defines a conserved pathological process that multiple diseases `conforms_to`, we should create **mechanism-of-action modules** that capture conserved drug response patterns. These would serve as design patterns for how treatments connect to pathophysiology.

### Proposed Module: `immune_checkpoint_blockade`

```
kb/modules/immune_checkpoint_blockade.yaml
```

This module would define the conserved pattern:

```
Pathophysiology side (the disease process being targeted):
  1. Neoantigen Generation → high TMB produces immunogenic peptides
  2. Anti-Tumor Immune Response → CD8+ T cells recognize and infiltrate tumor
  3. Adaptive Immune Resistance → tumor upregulates PD-L1/PD-L2 in response to IFN-gamma
  4. T Cell Exhaustion and Immune Escape → chronic checkpoint engagement → dysfunctional T cells → tumor evades destruction

Treatment side (the therapeutic intervention):
  Anti-PD-1/PD-L1 therapy:
    target_mechanisms:
      - target: "Adaptive Immune Resistance"
        treatment_effect: INHIBITS
      - target: "T Cell Exhaustion"
        treatment_effect: INHIBITS
    → downstream effect: restores "Anti-Tumor Immune Response"

  Anti-CTLA-4 therapy:
    target_mechanisms:
      - target: "T Cell Exhaustion" (priming phase)
        treatment_effect: INHIBITS
    → downstream effect: expands T cell repertoire
```

### How diseases would conform

```yaml
# In kb/disorders/MSI_High_Colorectal_Cancer.yaml
pathophysiology:
- name: Neoantigen-Driven Immune Response
  conforms_to: "immune_checkpoint_blockade#Anti-Tumor Immune Response"
  # organ-specific: high TMB from dMMR
  ...
- name: PD-L1 Upregulation and Immune Evasion
  conforms_to: "immune_checkpoint_blockade#Adaptive Immune Resistance"
  ...

treatments:
- name: Pembrolizumab
  ...
  target_mechanisms:
  - target: PD-L1 Upregulation and Immune Evasion
    treatment_effect: INHIBITS
    description: Anti-PD-1 blocks PD-1/PD-L1 interaction, restoring T cell cytotoxicity
```

### Why this matters

1. **Consistency**: Every cancer with checkpoint inhibitor treatment would model immune evasion the same way, with organ-specific substitutions (just like fibrotic_response uses organ-specific fibroblasts).

2. **Predictive power**: If a cancer has a pathophysiology node conforming to the immune evasion pattern, it suggests checkpoint inhibitor sensitivity. Conversely, cancers like Uveal Melanoma that lack the pattern ("immunologically cold") explain treatment resistance.

3. **Completeness checking**: If a disease has a checkpoint inhibitor treatment but no immune evasion pathophysiology node (e.g., FGFR-Altered Cholangiocarcinoma), that's a curation gap.

4. **Bidirectional linking**: `target_mechanisms` formally connects treatment → pathophysiology, closing the current structural gap.

### Additional mechanism-of-action modules to consider

| Module | Diseases | Pattern |
|--------|----------|---------|
| `immune_checkpoint_blockade` | ~23 cancers | Neoantigen → immune infiltration → adaptive resistance → checkpoint blockade restores immunity |
| `kinase_inhibition` | ALK NSCLC, BRAF Melanoma, FGFR cancers, CML | Constitutive kinase activation → oncogenic signaling → TKI blocks kinase → pathway shutdown |
| `antibody_dependent_cellular_cytotoxicity` | HER2+ cancers, lymphomas | Surface antigen overexpression → antibody binding → Fc-mediated immune recruitment |
| `angiogenesis_inhibition` | RCC, HCC, CRC | VEGF overproduction → neovascularization → anti-VEGF starves tumor |
| `differentiation_therapy` | APL (ATRA/ATO) | Differentiation block → pharmacologic override → terminal differentiation |
| `synthetic_lethality` | BRCA-mutant cancers (PARP inhibitors) | DNA repair deficiency → PARP inhibition → unrepaired damage → cell death |
| `cdk_inhibition` | HR+ breast cancer, liposarcoma | Cyclin D-CDK4/6 overactivation → Rb phosphorylation → CDK4/6i arrests G1/S → senescence |

## 4. Implementation Plan

### Phase 1 (DONE)
- [x] Verify MAXO terms -- no specific "immune checkpoint inhibitor therapy" term in MAXO; `MAXO:0000058` (pharmacotherapy) and `MAXO:0001002` (immunotherapy procedure) are the best available
- [x] Create `kb/modules/immune_checkpoint_blockade.yaml` with 4-node conserved pattern:
  - Neoantigen Generation (GO:0019882)
  - Anti-Tumor T Cell Response (CL:0000625, GO:0042110, GO:0001913)
  - Adaptive Immune Resistance (GO:0002710) -- **primary conforms_to target**
  - T Cell Exhaustion and Immune Escape (CL:0011025, GO:0160083)
- [x] Update 5 pilot cancer entries with `conforms_to` and `target_mechanisms`:
  - MSI-High Colorectal Cancer -- 3 ICI treatments linked, 2 pathophys nodes with conforms_to
  - Clear Cell Renal Cell Carcinoma -- new immune evasion node added, ICI treatment linked
  - Hepatocellular Carcinoma -- new immune evasion node added, 2 ICI treatments linked (atezo+bev also targets angiogenesis)
  - BRAF V600 Mutant Melanoma -- new immune evasion node added, ICI treatment linked
  - Nasopharyngeal Carcinoma -- existing "Immune Evasion" node gets conforms_to, immunotherapy treatment linked
- [x] Standardize: all immune evasion nodes use CL:0000625 (CD8+ T cell) and GO:0002710 (negative regulation of T cell mediated immunity)

### Phase 2 (TODO)
- [ ] Extend to remaining ~18 cancers with checkpoint inhibitor treatments
- [ ] Add specific therapeutic_agent annotations to entries that currently lack them (NCIT/CHEBI IDs)
- [ ] Create additional mechanism modules: `kinase_inhibition`, `angiogenesis_inhibition`, `synthetic_lethality`
- [ ] Document the "drug mechanism module" pattern in CLAUDE.md
- [ ] Consider schema evolution: `mechanism_class` slot on Treatment, `conforms_to` on Treatment
- [ ] Model irAE (immune-related adverse events) as cross-disease comorbidity pattern
- [ ] Add CDK4/6 inhibitor mechanism module (from second analysis)

## 5. Key Questions

1. **Schema evolution**: Should `conforms_to` on Treatment (not just pathophysiology) point to a mechanism module? Currently only pathophysiology nodes conform to modules.
2. **Granularity**: Should anti-PD-1 and anti-CTLA-4 be separate sub-patterns within the module, or one unified checkpoint blockade pattern?
3. **Resistance modeling**: How to represent acquired resistance (e.g., loss of B2M, JAK1/2 mutations) that breaks the checkpoint blockade pattern?
4. **Adverse events as pattern**: Checkpoint inhibitor-induced autoimmunity (irAEs) is itself a conserved pattern -- model as a separate module or within the same one?
5. **Biomarker integration**: PD-L1 expression, TMB, and MSI status predict checkpoint response. Should the module include biomarker nodes?

## 6. Observations on Autoimmune Mirror

Checkpoint inhibitors work by *removing* immune brakes. This is the mirror image of autoimmune diseases where checkpoint pathways are *insufficient*. The same module could potentially be used bidirectionally:
- **Cancer**: Checkpoint engagement = disease mechanism → blockade = treatment
- **Autoimmune**: Checkpoint insufficiency = disease mechanism → checkpoint agonism = (theoretical) treatment
- **irAEs**: Checkpoint blockade (cancer treatment) → autoimmune pathology (adverse event)

This triangulation supports the "design pattern" framing -- the same biological pattern manifests differently depending on which direction it's perturbed.
