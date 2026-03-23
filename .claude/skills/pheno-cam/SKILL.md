---
name: pheno-cam
description: >
  Skill for building Pheno-CAM (Phenotype Causal Activity Model) files that connect disease
  mutations through molecular mechanisms (GO-CAMs) to tissue-specific pathophysiology and HPO
  phenotypes. Produces structured YAML modules (normal biology) and disease overlay files with
  interactive D3 visualization.
---

# Pheno-CAM Skill

## Overview

Pheno-CAMs are structured causal models that bridge molecular biology (GO-CAM) to disease
phenotypes (HPO) through tissue-specific pathophysiology. They use two file types:

1. **Modules** (`causal_models/modules/`) — reusable normal-biology pathway graphs (activities + RO-typed edges)
2. **Disease files** (`causal_models/diseases/`) — disease-specific perturbation overlays (mutations, propagated states, phenotype routes)

Output: YAML files in `causal_models/` + interactive D3 HTML in `causal_models/viz/`.

**Full data model specification**: [`causal_models/PHENOCAM_DATA_MODEL.md`](../../../causal_models/PHENOCAM_DATA_MODEL.md)

## When to Use

- Building a mechanistic model for a disease with known molecular drivers
- Connecting dismech pathophysiology to GO-CAM molecular models
- Illustrating how genetic mutations disrupt normal molecular mechanisms
- Showing alternative genetic etiologies (hypothesis groups) for a disease
- Demonstrating tissue-specific phenotype routing through molecular intermediates

## Workflow

### Step 1: Read the KB Entry and Existing Pheno-CAMs

Read the dismech YAML file for the target disease:

```bash
cat kb/disorders/<Disease>.yaml
```

Extract: genes (HGNC), pathophysiology nodes, biological processes (GO), phenotypes (HPO), disease term (MONDO).

Then check for reusable modules and related disease files:

```bash
ls causal_models/modules/      # Existing reusable modules
ls causal_models/diseases/     # Existing disease files that may share pathways
```

If a module already exists for the relevant pathway (e.g., `ras_mapk_cascade` for any RASopathy), plan to reuse it rather than creating a new one.

### Step 2: Fetch GO-CAM Models

Use the automated script to find GO-CAM models for the disease's causative genes:

```bash
uv run python scripts/fetch_gocam_models.py GENE1 GENE2 ...
```

The script:
- Searches the GO-CAM browser index for models involving the specified genes
- Fetches full model detail from the GO-CAM API
- Extracts activities (gene products + molecular functions) and causal edges
- Output is cached in `causal_models/.cache/`

Review the output for relevant activities and edges to incorporate into the module.

### Step 3: Assemble or Reuse Module

If a suitable module exists, reuse it. Otherwise, assemble a new module from GO-CAM output + literature.

A module defines normal biology with:

**Activities** — gene products performing molecular functions:
```yaml
- id: shp2_phosphatase
  source:
    type: go_cam
    id: "gomodel:67c10cc400009089"
  gene:
    symbol: PTPN11
    hgnc_id: HGNC:9644
  molecular_function:
    id: GO:0004725
    label: protein tyrosine phosphatase activity
  location:
    id: GO:0005829
    label: cytosol
  biological_process:
    id: GO:0007265
    label: Ras protein signal transduction
```

**Edges** — causal relations between activities:
```yaml
- source: shp2_phosphatase
  target: ras_gtpase
  relation:
    id: RO:0002629
    label: directly positively regulates
  eco:
    id: ECO:0000304
    label: traceable author statement used in manual assertion
  evidence:
  - type: literature
    reference: PMID:17143285
    snippet: "Exact quote from paper abstract"
```

Module edges use "direct" RO relations: `RO:0002629` (directly positively regulates), `RO:0002630` (directly negatively regulates), `RO:0002413` (directly provides input for).

Save to `causal_models/modules/<pathway_name>.yaml`.

### Step 4: Build Disease File — Top-Level

Create the disease file with top-level metadata:

```yaml
disease_model:
  id: <disease_id>
  name: <Disease Name>
  disorder_ref: <Disease>.yaml
  disease_term:
    id: MONDO:XXXXXXX
    label: <disease label>

  has_phenotype: []      # Filled in Step 7
  imports:
  - module: <module_id>
  activities: []         # Disease-local activities if needed (Step 5)
  hypothesis_groups: []  # Filled in Step 5
  phenotype_routes: []   # Filled in Step 6
```

**Disease-local activities** are needed only when the disease has activities not in any reusable module (e.g., Gorlin's CCND1/BCL2/MYCN transcriptional targets).

Save to `causal_models/diseases/<Disease>.yaml`.

### Step 5: Build Hypothesis Groups

One hypothesis group per genetic etiology. Each contains:

**Perturbations** — entry point mutations targeting module activities:
```yaml
perturbations:
- target_activity: module_id:activity_id
  variant_class:
    id: GENO:0000134
    label: loss of function variant
  perturbed_state: decreased
  eco:
    id: ECO:0000315
    label: mutant phenotype evidence used in manual assertion
  evidence:
  - type: literature
    reference: PMID:XXXXXXXX
    snippet: "Exact quote from abstract"
```

**Propagated states** — downstream activity perturbations following module topology:
```yaml
propagated_states:
- activity: module_id:activity_id
  perturbed_state: increased
```

For module-internal propagation, no `driven_by` is needed — the module's edges define connectivity. Only **cross-boundary** propagated states (module activity → disease-local activity) need explicit `driven_by`:

```yaml
- activity: ccnd1_upregulation
  perturbed_state: increased
  driven_by:
  - source: hedgehog_signaling:gli1_activation
    relation: {id: RO:0002304, label: causally upstream of, positive effect}
    eco: {id: ECO:0000305, label: curator inference used in manual assertion}
    evidence: []
```

**Constraint**: One propagated state per activity per hypothesis group.

### Step 6: Build Phenotype Routes

One route per phenotype (or group of related phenotypes). Routes are **hypothesis-agnostic** — defined at the disease level, not within hypothesis groups.

Each route has **intermediates** (tissue-specific states) and **targets** (HPO phenotypes):

```yaml
phenotype_routes:
- id: joint_hypermobility_route
  name: Joint hypermobility pathway
  description: >
    How reduced collagen leads to joint hypermobility.

  intermediates:
  - id: ligament_ecm_weakness
    name: Ligamentous ECM weakness
    perturbed_state: decreased
    driven_by:
    - source: collagen_v_assembly:heterotypic_fibril_formation
      relation: {id: RO:0002304, label: causally upstream of, positive effect}
      eco: {id: ECO:0000305, label: curator inference used in manual assertion}
      evidence:
      - type: literature
        reference: PMID:34807421
        snippet: "Exact quote from abstract"
    biological_process:
      id: GO:0030198
      label: extracellular matrix organization
    tissue:
      cell_type: {id: CL:0000057, label: fibroblast}
      anatomy: {id: UBERON:0000211, label: ligament}

  targets:
  - id: joint_hypermobility
    preferred_term: Joint hypermobility
    perturbed_state: increased
    term: {id: HP:0001382, label: Joint hypermobility}
    driven_by:
    - source: ligament_ecm_weakness
      relation: {id: RO:0003303, label: causes condition}
      eco: {id: ECO:0000305, label: curator inference used in manual assertion}
      evidence: []
```

Key conventions:
- **Evidence goes on the first intermediate's first `driven_by` entry** — the entry point edge for the route
- Intermediate `driven_by` uses `RO:0002304`/`RO:0002305` (causally upstream of)
- Target `driven_by` uses `RO:0003303` (causes condition)

### Step 7: Add has_phenotype Entries

Connect the disease to all target phenotypes via `RO:0002200`. This is the only **non-causal** edge — it expresses classification, not causation.

```yaml
has_phenotype:
- phenotype: joint_hypermobility    # References target id from phenotype_routes
  relation: {id: RO:0002200, label: has phenotype}
  eco: {id: ECO:0000305, label: curator inference used in manual assertion}
  evidence: []
```

### Step 8: Visualize and Validate

Generate the interactive D3 visualization:

```bash
uv run python scripts/visualize_phenocam.py causal_models/diseases/<Disease>.yaml
```

This produces an HTML file in `causal_models/viz/` with:
- Dagre-layouted graph with color-coded node types
- Hypothesis group toggle (switch between genetic etiologies)
- Hover tooltips showing ontology IDs, evidence, and perturbed states
- Module boundaries shown as dashed boxes

Open the HTML file to verify the model visually. Check:
- All activities are connected (no orphan nodes)
- Perturbation propagation follows the expected path
- Each hypothesis group shows the correct subset of perturbed activities
- Phenotype routes trace complete paths from module activities to HPO terms

## Key Conventions

### Edge Types

| Context | Common Relations | Semantics |
|---------|-----------------|-----------|
| Module edges | `RO:0002629` directly positively regulates, `RO:0002630` directly negatively regulates, `RO:0002413` directly provides input for | Normal-biology molecular interactions |
| Intermediate driven_by | `RO:0002304` causally upstream of, positive effect; `RO:0002305` causally upstream of, negative effect | Activity perturbation → tissue pathology |
| Target driven_by | `RO:0003303` causes condition | Tissue pathology → clinical phenotype |
| has_phenotype | `RO:0002200` has phenotype | Disease classification (non-causal) |

### perturbed_state Enum

| Value | Description | Example |
|-------|-------------|---------|
| `increased` | Activity elevated above normal | ERK kinase hyperactivated |
| `decreased` | Activity reduced below normal | COL5A1 haploinsufficient |
| `absent` | Activity completely lost | PTCH1 inhibition absent |
| `constitutively_active` | Always active, ignores upstream regulation | SHP2 gain-of-function |
| `substrate_accumulated` | Substrate builds up due to impaired degradation | RAS accumulation from LZTR1 loss |

### Evidence

- Evidence lives on **edges**, not containers (routes, hypothesis groups, disease_model)
- Propagated states within a module don't need evidence — the module edges already carry it
- Evidence snippets must be exact quotes from paper abstracts

See `PHENOCAM_DATA_MODEL.md` for the complete controlled vocabulary (ECO codes, GENO variant classes, RO relations).

## Ontology ID Sources

| Entity type | Ontology | Lookup command |
|-------------|----------|----------------|
| Genes | HGNC | `uv run runoak -i sqlite:obo:hgnc search "GENE_NAME"` |
| Molecular functions | GO | `uv run runoak -i sqlite:obo:go info GO:XXXXXXX` |
| Cell types | CL | `uv run runoak -i sqlite:obo:cl search "cell type"` |
| Anatomy | UBERON | `uv run runoak -i sqlite:obo:uberon search "tissue"` |
| Phenotypes | HPO | `uv run runoak -i sqlite:obo:hp search "phenotype"` |
| Diseases | MONDO | `uv run runoak -i sqlite:obo:mondo search "disease"` |
| Relations | RO | `uv run runoak -i sqlite:obo:ro info RO:XXXXXXX` |

## Cross-Disease Module Reuse

A key value of Pheno-CAM: the same module can be imported by multiple disease files with different perturbation entry points. Current examples:

| Module | Used by | Entry points |
|--------|---------|-------------|
| `ras_mapk_cascade` | Noonan Syndrome | PTPN11, SOS1, RAF1, LZTR1 |
| `ras_mapk_cascade` | CFC Syndrome | BRAF, MEK1, MEK2, KRAS |
| `hedgehog_signaling` | Gorlin Syndrome | PTCH1, SUFU |
| `collagen_v_assembly` | EDS COL5A1 | COL5A1 |

When building a Pheno-CAM, always check if existing modules cover the relevant pathway before creating a new one.

## Known Limitations

1. **GO-CAM coverage varies** — some genes lack GO-CAM models entirely (e.g., PTCH1, BRAF). The fetch script reports coverage gaps; supplement with literature.
2. **AND/OR logic** is not expressible — multiple inputs to a node are implicitly combined without specifying whether all are required (AND) or any is sufficient (OR).
3. **Temporal progression** is not modeled — the current model captures the steady-state perturbation cascade, not the time course of disease progression.
4. **No formal validation schema yet** — YAML structure is validated by the visualization script but not by a LinkML schema (planned for Phase 4).

## Related Dismech Skills

- **dismech-terms**: For looking up and validating ontology terms (HPO, CL, GO, UBERON)
- **dismech-references**: For validating evidence references (PMIDs) on edges
- **cancer-curator**: For cancer-specific pathophysiology patterns
- **initiate-new-disorder-creation**: For creating new disorder YAML files

## Example: Gorlin Syndrome

See the worked example files:
- **Module**: `causal_models/modules/hedgehog_signaling.yaml` — 15 activities, 15 edges, sourced from 4 GO-CAMs + literature
- **Disease**: `causal_models/diseases/Gorlin_Syndrome.yaml` — 2 hypothesis groups, 4 disease-local activities, 8 phenotype routes

For a detailed walkthrough of the Gorlin Syndrome Pheno-CAM structure, see
[`example-gorlin-syndrome.md`](example-gorlin-syndrome.md).
