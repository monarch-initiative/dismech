# Checkpoint Inhibitors in dismech: Analysis & Curation Project

## Status: Analysis Complete

## 1. Diseases Treated by Checkpoint Inhibitors

The knowledge base contains **18 disorders** with checkpoint inhibitor treatments or strong checkpoint inhibitor relevance:

### Diseases with explicit checkpoint inhibitor treatment entries

| Disease | Drug(s) | Target | Pathophys Link? |
|---------|---------|--------|-----------------|
| MSI-High Colorectal Cancer | pembrolizumab, nivolumab+ipilimumab, dostarlimab | PD-1, CTLA-4 | YES - "PD-L1 Upregulation and Immune Evasion" |
| Non-Small Cell Lung Cancer | nivolumab, pembrolizumab, durvalumab | PD-1, PD-L1 | PARTIAL - "Immune Evasion" exists but no explicit PD-L1 step |
| Cutaneous Squamous Cell Carcinoma | cemiplimab | PD-1 | YES - "Tumor Microenvironment Remodeling and Immune Evasion" |
| Hepatocellular Carcinoma | atezolizumab+bevacizumab, durvalumab+tremelimumab | PD-L1, CTLA-4 | NO - no immune evasion pathophys step |
| Triple-Negative Breast Cancer | pembrolizumab | PD-1 | NO - immunomodulatory subtype mentioned but no mechanism step |
| Small Cell Lung Cancer | atezolizumab, durvalumab | PD-L1 | NO - no immune evasion step at all |
| Merkel Cell Carcinoma | avelumab, pembrolizumab | PD-L1, PD-1 | NO - immunogenicity in notes only |
| Cervical Cancer | pembrolizumab | PD-1 | NO - no immune evasion step |
| MSI-High Endometrial Cancer | pembrolizumab, pembrolizumab+lenvatinib | PD-1 | PARTIAL - neoantigen load discussed |
| EBV-Associated Gastric Cancer | pembrolizumab, nivolumab | PD-1 | YES - "PD-L1/PD-L2 Expression" pathophys step |
| BRAF V600 Mutant Melanoma | pembrolizumab, nivolumab, ipilimumab | PD-1, CTLA-4 | NO - no immune evasion step |
| NRAS Mutant Melanoma | pembrolizumab, nivolumab, ipilimumab | PD-1, CTLA-4 | NO - no immune evasion step |
| Uveal Melanoma | ipilimumab, nivolumab | CTLA-4, PD-1 | NO - "cold TME" noted but not structured |
| KIT Mutant Melanoma | pembrolizumab, nivolumab | PD-1 | NO |
| HPV+ Head and Neck Cancer | pembrolizumab, nivolumab | PD-1 | YES - "Immune Evasion" pathophys step |
| HPV- Head and Neck Cancer | pembrolizumab, nivolumab | PD-1 | NO |
| Malignant Mesothelioma | nivolumab+ipilimumab | PD-1, CTLA-4 | NO |
| IDH-Mutant Cholangiocarcinoma | durvalumab | PD-L1 | NO |
| FGFR-Altered Cholangiocarcinoma | durvalumab | PD-L1 | NO |
| FGFR-Altered Urothelial Carcinoma | PD-1/PD-L1 inhibitors (generic) | PD-1/PD-L1 | NO |
| Gastric Cancer (H. pylori) | PD-1 inhibitors (generic) | PD-1 | NO |
| Clear Cell Renal Cell Carcinoma | nivolumab, pembrolizumab, ipilimumab | PD-1, CTLA-4 | NO |
| Basal Cell Carcinoma | cemiplimab | PD-1 | NO |
| HER2+ Gastric Cancer | pembrolizumab (with trastuzumab) | PD-1 | NO |
| Aflatoxin-Related HCC | nivolumab, pembrolizumab | PD-1 | NO |

### Also relevant (checkpoint biology in pathophysiology, not treatment)

| Disease | Role |
|---------|------|
| Hepatitis B | PD-1/CTLA-4/TIM-3 T-cell exhaustion drives chronicity |
| Long COVID | T-cell exhaustion pathophysiology |
| Lynch Syndrome | Immune Checkpoint Blockade Sensitivity as pathophys step |
| Pancreatic Ductal Adenocarcinoma | Immune Evasion pathophys but checkpoint tx largely ineffective |
| Nasopharyngeal Carcinoma | Immune Evasion step + PD-L1 upregulation |

### Autoimmune diseases where checkpoint biology is pathogenic (not therapeutic)

| Disease | Role |
|---------|------|
| Addison's Disease | CTLA-4 risk variants; checkpoint inhibitors can *cause* adrenalitis |
| Graves' Disease | CTLA-4 immune checkpoint gene variants |
| Type 1 Diabetes | CTLA-4 risk variants; checkpoint inhibitors can *trigger* T1D |
| Rheumatoid Arthritis | CTLA-4 polymorphisms associated with RA risk |
| Diabetes Mellitus | Checkpoint inhibitor-induced diabetes as a comorbidity |

---

## 2. The Drug-Process Pattern

There is a clear **common pattern** for how checkpoint inhibitors (and other drug classes) relate to disease mechanisms:

### The Causal Chain

```
Genetic/Epigenetic Driver
  → Oncogenic Signaling
    → Immune Evasion Mechanism (PD-L1 upregulation, checkpoint ligand expression)
      → Suppressed Anti-Tumor Immunity
        → Uncontrolled Proliferation / Metastasis
          → Clinical Phenotypes (tumor growth, symptoms)
```

**Checkpoint inhibitors act at the "Immune Evasion" node**, specifically:
- **Anti-PD-1** (pembrolizumab, nivolumab, cemiplimab, dostarlimab): Block PD-1 receptor on T cells
- **Anti-PD-L1** (atezolizumab, durvalumab, avelumab): Block PD-L1 ligand on tumor cells
- **Anti-CTLA-4** (ipilimumab, tremelimumab): Block CTLA-4 co-inhibitory receptor, enhancing T cell priming

### The General Pattern for Drug Classes

| Drug Class | Disrupted Process | Pathophys Step Pattern |
|-----------|-------------------|----------------------|
| Checkpoint inhibitors (PD-1/PD-L1) | PD-1/PD-L1 immune checkpoint | "Immune Evasion" / "PD-L1 Upregulation" |
| Checkpoint inhibitors (CTLA-4) | T-cell priming inhibition | "Immune Evasion" (broader) |
| Targeted kinase inhibitors | Oncogenic signaling cascades | "Constitutive Kinase Activation" |
| VEGF inhibitors | Tumor angiogenesis | "Angiogenesis and VEGF Signaling" |
| PARP inhibitors | DNA repair bypass | "DNA Repair Deficiency" |
| Hormone therapy | Hormone-dependent growth | "Hormone Receptor Signaling" |

**Key insight**: Each drug class maps to a specific *biological process* node in the pathophysiology graph. The `target_mechanisms` schema field was designed exactly for this linkage.

---

## 3. Gap Analysis: What's Missing

### 3a. Missing Immune Evasion Pathophysiology Steps

Most checkpoint-inhibitor-treated diseases **lack a structured immune evasion pathophysiology step**. Only 4/25 entries have a well-formed one:

**Have it**: MSI-H CRC, cSCC, EBV Gastric, HPV+ Head & Neck
**Need it**: All others with checkpoint treatments (~20 entries)

A standard "Immune Evasion / PD-L1 Upregulation" pathophysiology step should include:
- Description of the PD-L1/checkpoint upregulation mechanism
- Cell types: CD8+ T cell, regulatory T cell, macrophage/TAM
- Biological processes: immune response (DECREASED), T cell activation
- Links to upstream oncogenic drivers
- Links to downstream uncontrolled proliferation

### 3b. Missing `target_mechanisms` Linkages

Only **10 files** in the entire KB use `target_mechanisms`. **Zero** checkpoint inhibitor treatments use it. This is the primary structural gap.

Every checkpoint inhibitor treatment entry should have:
```yaml
target_mechanisms:
- target: <Immune Evasion pathophys step name>
  treatment_effect: INHIBITS
  description: Blocks PD-1/PD-L1 interaction, restoring T cell cytotoxicity
```

### 3c. Inconsistent Drug Agent Annotations

Some entries list drug agents with NCIT IDs; others use bare text. Standardize:
- pembrolizumab → NCIT:C106432
- nivolumab → NCIT:C68814
- atezolizumab → NCIT:C106250
- durvalumab → NCIT:C103194
- ipilimumab → NCIT:C2654
- tremelimumab → NCIT:C49085
- cemiplimab → NCIT:C162611
- avelumab → NCIT:C116870
- dostarlimab → NCIT:C126799

---

## 4. Proposed Curation Work

### Phase 1: Add Immune Evasion pathophysiology steps (Priority: HIGH)

For each disease with checkpoint inhibitor treatments but no immune evasion mechanism:
- [ ] Hepatocellular Carcinoma
- [ ] Triple-Negative Breast Cancer
- [ ] Small Cell Lung Cancer
- [ ] Merkel Cell Carcinoma
- [ ] Cervical Cancer
- [ ] MSI-High Endometrial Cancer
- [ ] BRAF V600 Mutant Melanoma
- [ ] NRAS Mutant Melanoma
- [ ] KIT Mutant Melanoma
- [ ] HPV- Head and Neck Cancer
- [ ] Malignant Mesothelioma
- [ ] IDH-Mutant Cholangiocarcinoma
- [ ] FGFR-Altered Cholangiocarcinoma
- [ ] FGFR-Altered Urothelial Carcinoma
- [ ] Clear Cell Renal Cell Carcinoma
- [ ] Basal Cell Carcinoma
- [ ] Uveal Melanoma
- [ ] Gastric Cancer (H. pylori)
- [ ] Aflatoxin-Related HCC
- [ ] Non-Small Cell Lung Cancer (enhance existing)

### Phase 2: Add `target_mechanisms` to all checkpoint inhibitor treatments (Priority: HIGH)

Link each checkpoint inhibitor treatment entry to its corresponding immune evasion pathophysiology step using the `target_mechanisms` field with `treatment_effect: INHIBITS`.

### Phase 3: Standardize drug agent NCIT annotations (Priority: MEDIUM)

Ensure all checkpoint inhibitor drug agents have proper NCIT term IDs.

### Phase 4: Template for checkpoint inhibitor pattern (Priority: LOW)

Create a reusable pathophysiology template:
```yaml
- name: Immune Evasion via PD-L1 Upregulation
  description: >-
    Tumor cells upregulate PD-L1 (programmed death-ligand 1) in response to
    interferon-gamma from tumor-infiltrating lymphocytes. PD-L1 engagement of
    PD-1 on CD8+ T cells suppresses cytotoxic function, enabling immune escape.
    [Disease-specific details here.]
  cell_types:
  - preferred_term: CD8-positive, alpha-beta T cell
    term:
      id: CL:0000625
      label: CD8-positive, alpha-beta T cell
  - preferred_term: regulatory T cell
    term:
      id: CL:0000815
      label: regulatory T cell
  biological_processes:
  - preferred_term: immune response
    modifier: DECREASED
    term:
      id: GO:0006955
      label: immune response
  downstream:
  - target: [Uncontrolled Proliferation step]
    description: Immune escape permits unchecked tumor growth
```

---

## 5. Cross-Cutting Observations

### Predictors of checkpoint inhibitor response (reflected in KB)

| Biomarker | Diseases where modeled | Diseases where missing |
|-----------|----------------------|----------------------|
| PD-L1 expression | NSCLC, cSCC, EBV Gastric | Most others |
| MSI-H/dMMR | MSI-H CRC, MSI-H Endometrial, Lynch | Should propagate to all MSI-H tumors |
| TMB (tumor mutational burden) | MSI-H CRC (biomarker entry) | NSCLC, melanoma, others |
| Viral antigens (MCPyV, HPV, EBV) | HPV+ H&N, EBV Gastric, Merkel | Partially |

### Ironic flip: Autoimmune checkpoint biology

The same PD-1/CTLA-4 pathways that tumors exploit for immune evasion are *protective* in autoimmune diseases. The KB captures this duality:
- **Cancer**: Checkpoint ligands suppress anti-tumor immunity → treat with checkpoint *inhibitors*
- **Autoimmune**: Checkpoint pathways maintain self-tolerance → checkpoint inhibitors can *cause* autoimmunity (adrenalitis, thyroiditis, T1D)

This is a rich area for cross-disease annotation and comorbidity modeling.
