---
name: pheno-cam
description: >
  Skill for building Pheno-CAM (Phenotype Causal Activity Model) diagrams that layer GO-CAM
  molecular models onto dismech disease pathophysiology. Use this skill when creating a causal
  diagram that connects disease mutations through molecular mechanisms (GO-CAMs) to tissue-specific
  pathophysiology and HPO phenotypes for a specific disorder. Produces annotated Mermaid diagrams
  with ontology-grounded nodes and RO-typed edges.
---

# Pheno-CAM Skill

## Overview

Pheno-CAMs are structured causal models that bridge molecular biology (GO-CAM) to disease
phenotypes (HPO) through dismech pathophysiology. They operate at three levels:

1. **GO-CAM molecular level** — curated activity models from the Gene Ontology, shown as boxed
   subgraphs containing gene product activity nodes
2. **Dismech pathophysiology level** — disease-specific causal nodes (mutations, pathway activation,
   tissue-specific effects)
3. **Phenotype/disease level** — HPO phenotype terms and MONDO disease classification

The key insight: GO-CAMs describe *normal biology*. Disease disrupts specific nodes or edges in
that normal biology, causing cascading effects that eventually manifest as phenotypes. The
Pheno-CAM makes this disruption chain explicit and queryable.

## When to Use

- Building a mechanistic diagram for a disease that has known molecular drivers
- Connecting dismech pathophysiology nodes to GO-CAM molecular models
- Illustrating how genetic mutations disrupt normal molecular mechanisms
- Showing hypothesis groups (alternative genetic etiologies for the same disease)
- Demonstrating tissue-specific phenotype routing through molecular intermediates

## Workflow

### Step 1: Identify the Disease and Its Molecular Basis

Read the dismech YAML file for the target disease:

```bash
cat kb/disorders/<Disease>.yaml
```

Extract:
- Pathophysiology nodes and their `downstream` edges
- Biological processes (GO terms) referenced
- Genes (HGNC) identified as causative
- Phenotypes (HPO terms)
- Disease term (MONDO ID)

### Step 2: Identify Candidate GO-CAM Models

**IMPORTANT: The GO-CAM browser at https://go-cam-browser.geneontology.org/ cannot be queried
programmatically by Claude. The user must search manually.**

Suggest searches based on the disease's key molecular actors. Good search terms:
- Gene symbols of causative genes (e.g. "PTCH1", "SUFU", "SMO")
- Key pathway components (e.g. "IFT", "GLI3", "BBSome")
- Biological process keywords (e.g. "hedgehog", "intraflagellar transport")

The user will provide GO-CAM model IDs (format: `gomodel:XXXXXXXXXXXX`).

### Step 3: Fetch and Parse GO-CAM Model Structure

Use the GO-CAM REST API to fetch model data:

```python
import urllib.request, json

def fetch_gocam(model_id):
    """Fetch a GO-CAM model and extract activity units with their relationships."""
    bare_id = model_id.replace('gomodel:', '')
    url = f"https://api.geneontology.org/api/go-cam/{bare_id}"
    with urllib.request.urlopen(url) as r:
        d = json.load(r)

    # Build individual map: id -> {types, root_types}
    ind_map = {}
    for ind in d.get('individuals', []):
        types = [t for t in ind.get('type', [])
                 if isinstance(t, dict) and t.get('type') == 'class']
        root_types = [t.get('label', '') for t in ind.get('root-type', [])
                      if isinstance(t, dict)]
        ind_map[ind['id']] = {'types': types, 'root_types': root_types}

    # Find molecular function activity units
    mf_inds = {k: v for k, v in ind_map.items()
               if 'molecular_function' in v['root_types']}

    print(f"\n=== {model_id} ===")
    for mf_id, mf_data in mf_inds.items():
        mf_label = mf_data['types'][0]['label'] if mf_data['types'] else '?'
        mf_go = mf_data['types'][0]['id'] if mf_data['types'] else '?'
        print(f"\n  Activity: {mf_label} ({mf_go})")
        for fact in d.get('facts', []):
            if fact.get('subject') == mf_id:
                rel = fact.get('property')
                rel_str = rel if isinstance(rel, str) else rel.get('label', str(rel))
                obj_id = fact.get('object')
                obj = ind_map.get(obj_id, {})
                obj_t = obj.get('types', [])
                obj_r = obj.get('root_types', [])
                obj_label = obj_t[0]['label'] if obj_t else obj_id.split('/')[-1]
                obj_go = obj_t[0]['id'] if obj_t else ''
                roots = '|'.join(r for r in obj_r if r and r != 'Molecular Event')
                print(f"    --[{rel_str}]--> {obj_label} ({obj_go}) [{roots}]")

fetch_gocam("gomodel:693b3c0900000716")  # example
```

Key relationships to extract from each activity unit:
- `RO:0002333` (enabled_by) — the gene product performing this activity
- `BFO:0000050` (part_of) — the biological process context
- `BFO:0000066` (occurs_in) — the cellular component location
- `RO:0002233` (has_input) — substrate/input molecules
- Causal edges to other activities (see RO vocabulary below)

### Step 4: Identify Shared Nodes Across GO-CAMs

When the same gene product (same UniProt ID) appears as `enabled_by` in multiple GO-CAM models,
it should be shown as a shared node outside the GO-CAM boxes:

- Common shared nodes: receptors (SMO), GPCRs (GPR161), transcription factors
- Shared nodes have the same GO:MF color as other activity nodes but sit outside boxes
- Their cross-box edges make their shared role visually obvious

### Step 5: Build the Disruption Cascade

Identify how the disease mutation connects to the GO-CAM normal biology:

**Level 1 — Node disruption**: Disease mutation directly disrupts a GO-CAM activity node
(e.g. SUFU germline mutation disrupts SUFU protein sequestering activity)

**Level 2 — Edge disruption**: Disease mutation disrupts a regulatory relationship between two
nodes (e.g. PTCH1 loss removes the PTCH1→SMO inhibitory relationship)

**Sign reversal**: When disruption of an inhibitory node/edge ENABLES the downstream target
(e.g. disrupting PTCH1 inhibition constitutively activates SMO). After a sign reversal,
the cascade switches from disruption to constitutive activation.

### Step 6: Route Through Molecular Targets to Tissue-Specific Outcomes

Connect the transcriptional output to tissue-specific phenotypes via specific molecular
intermediates. Use:

- **CL (Cell Ontology)** terms for cell types affected (e.g. CL:0002187 basal cell of epidermis)
- **UBERON** terms for anatomical locations (e.g. UBERON:0002037 cerebellum)
- **GO:BP** terms for the biological processes dysregulated (e.g. GO:0008283 cell population proliferation)

Different target genes may route to different tissue outcomes:
- A cell cycle driver (CCND1) may be shared across tissues
- A tissue-specific transcription factor (MYCN for cerebellum) may route to one phenotype
- An anti-apoptotic factor (BCL2) may contribute specifically to tumor formation

### Step 7: Add Hypothesis Groups

If the disease has alternative genetic etiologies (e.g. PTCH1 vs SUFU in Gorlin syndrome):

- Create separate hypothesis group boxes (amber/gold styled, `:::camhdr` header inside)
- Each hypothesis box contains only its mutation node
- Disruption edges exit the boxes to their molecular targets
- Different hypotheses may affect different parts of the GO-CAM network
- The `hypothesis_group` field in dismech schema tracks this

### Step 8: Generate the Mermaid Diagram

Use the template and conventions below.

## Mermaid Diagram Conventions

### Node Types and Colors

```
classDef dismech fill:#ffcccc,stroke:#cc0000,color:#000     %% Disease pathophysiology (red)
classDef hpo fill:#ede0f7,stroke:#6f42c1,color:#000         %% HPO phenotypes (purple)
classDef gomf fill:#dce8f8,stroke:#4c73c2,color:#000        %% GO Molecular Function (blue)
classDef gobp fill:#fef3d8,stroke:#c8860a,color:#000        %% GO Biological Process (gold)
classDef gocc fill:#dcf5e7,stroke:#2e9a5e,color:#000        %% GO Cellular Component (green)
classDef camhdr fill:#f0f0f0,stroke:#999,color:#444,font-style:italic  %% Metadata headers
classDef mondo fill:#ffd6a5,stroke:#d97706,color:#000       %% MONDO disease (amber)
```

### Node Label Format

Each node shows both human-readable name and ontology ID:

- **GO:MF activity nodes**: `"GeneName (hgnc:XXXXX) · MF label (GO:XXXXXXX)"`
- **Protein complexes**: `"Complex name (GO:XXXXXXX) · MF label (GO:XXXXXXX)"`
- **Processed isoforms**: Use UniProt chain IDs: `"GLI3A (P10071-PRO_0000047202) · ..."`
- **Dismech nodes**: `"Description · GO:XXXXXXX"` (or CL/UBERON terms)
- **HPO phenotypes**: `"Phenotype name (HP:XXXXXXX)"`
- **MONDO disease**: `"Disease name (MONDO:XXXXXXX)"`

### Edge Types

| Style | Meaning | When to use |
|-------|---------|-------------|
| `-->` solid | GO-CAM sourced edge | Source node is a GO-CAM activity unit |
| `-.->` dashed | Non-GO-CAM edge | Disruption cascade, dismech→dismech, dismech→HPO, HPO→MONDO |

All edges should have the same weight. Use `linkStyle default stroke-width:2px,fill:none`.

### Edge Labels

Always show both the RO relation label and ID: `"relation label (RO:XXXXXXX)"`

For disruption edges from mutations: `"disrupts"`

### Container Boxes

**GO-CAM boxes**: Use subgraphs with blank labels `[" "]` and a `:::camhdr` header node inside
connected to the first content node with `~~~` (invisible link):

```mermaid
subgraph CAM1[" "]
    CAM1_H["📦 gomodel:XXXXXXXXXXXX — Brief description"]:::camhdr
    NODE1["..."]:::gomf
    CAM1_H ~~~ NODE1
end
```

**Hypothesis boxes**: Same pattern with amber styling:

```
subgraph HYPA[" "]
    HYPA_H["Hypothesis A · Gene-driven · ~X% · hypothesis_group: id"]:::camhdr
    MUT_GENE["Gene (hgnc:XXXXX) · Germline Mutation"]:::dismech
    HYPA_H ~~~ MUT_GENE
end

style HYPA fill:#fef9e7,stroke:#f39c12,stroke-width:2px
```

### Disease Node (MONDO)

Place at the bottom of the diagram. Use reversed `has phenotype` edges (phenotype → disease)
to maintain top-down layout:

```
BCC -.->|"has phenotype (RO:0002200)"| GORLIN
```

The visual arrow direction is reversed from the semantic direction (which is
disease→phenotype). This is a Mermaid layout compromise — explain in presentations.

## RO Relation Vocabulary

### Causal Relations (for edges between activity nodes)

| RO ID | Label | Use case |
|-------|-------|----------|
| RO:0002629 | directly positively regulates | Direct activation (physical interaction) |
| RO:0002630 | directly negatively regulates | Direct inhibition (physical interaction) |
| RO:0002407 | indirectly positively regulates | Indirect activation (intermediaries omitted) |
| RO:0002409 | indirectly negatively regulates | Indirect inhibition (intermediaries omitted) |
| RO:0002413 | directly provides input for | Direct substrate handoff in a cascade |
| RO:0002304 | causally upstream of, positive effect | Upstream positive causal influence |
| RO:0002305 | causally upstream of, negative effect | Upstream negative causal influence |
| RO:0002212 | negatively regulates | General negative regulation |

### Phenotype/Disease Relations

| RO ID | Label | Use case |
|-------|-------|----------|
| RO:0002296 | results in development of | Pathophysiology → HPO phenotype |
| RO:0002200 | has phenotype | MONDO disease → HPO phenotype (reversed in viz) |

### GO-CAM Internal Relations

| RO/BFO ID | Label | Use case |
|-----------|-------|----------|
| RO:0002333 | enabled_by | Activity unit → gene product |
| BFO:0000050 | part_of | Activity → biological process context |
| BFO:0000066 | occurs_in | Activity → cellular component location |
| RO:0002233 | has_input | Activity → substrate/input molecule |
| RO:0002234 | has_output | Activity → product |

## Sign Propagation and Disruption Cascades

When tracing the effect of a mutation through the GO-CAM network:

1. **Disruption of an activating relationship** → downstream target is REDUCED
2. **Disruption of an inhibitory relationship** → downstream target is CONSTITUTIVELY ACTIVE
   (sign reversal)
3. After a sign reversal, subsequent edges represent normal biology running constitutively
4. When constitutive activation of one pathway removes a substrate needed by another pathway,
   that second pathway is DISRUPTED (e.g. constitutive GPR161 export prevents GLI3R production)

The cascade alternates between disruption and constitutive activation depending on the sign
of each relationship. Annotate these sign changes when discussing the model.

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
| Protein isoforms | UniProt | Check GO-CAM model data for `-PRO_XXXXXXX` suffixes |

## Cross-Disease GO-CAM Reuse

A key value of Pheno-CAM: the same GO-CAM box can appear in multiple disease diagrams with
different disruption entry points. For example, the Hedgehog/GLI3 GO-CAMs connect:

- **Gorlin Syndrome** (PTCH1 → SMO constitutive, SUFU → GLI3A freed)
- **Pallister-Hall Syndrome** (GLI3 truncation → constitutive repressor)
- **Meckel Syndrome** (BBSome/IFT-B disrupted → GPR161 not exported)
- **Medulloblastoma SHH-activated** (SMO/PTCH1/SUFU mutations in cerebellum context)

When building a Pheno-CAM, check if GO-CAM models used by other dismech diseases overlap.
This surfaces mechanistic connections between diseases.

## Known Limitations

1. **GO-CAM search** requires manual user interaction via the browser — no reliable
   programmatic search exists currently
2. **Mermaid cannot draw edge-to-edge connections** — when a disruption targets a regulatory
   relationship (Level 2), the visualization must use labeled dashed edges rather than true
   hyperedges. A custom renderer (Cytoscape.js, D3) could show this properly.
3. **No RO term for "indicates"** — the phenotype→disease diagnostic direction lacks a
   standard RO relation. Use `has phenotype (RO:0002200)` with reversed visual direction.
4. **AND/OR logic** is not expressible in GO-CAM or the current Pheno-CAM model — multiple
   inputs to a node are implicitly combined without specifying whether all are required (AND)
   or any is sufficient (OR). SBGN-PD handles this with explicit logical operator nodes.
5. **PTCH1→SMO inhibition** has no GO-CAM model — this is a known gap. Normal biology nodes
   outside GO-CAM boxes may lack GO IDs for their molecular function.

## Related Dismech Skills

- **dismech-terms**: For looking up and validating ontology terms (HPO, CL, GO, UBERON)
- **dismech-references**: For validating evidence references (PMIDs) on edges
- **cancer-curator**: For cancer-specific pathophysiology patterns
- **initiate-new-disorder-creation**: For creating new disorder YAML files

## Example: Gorlin Syndrome Pheno-CAM

See the working example developed in the initial Pheno-CAM design session, which produced
a full Mermaid diagram with:
- 4 GO-CAM boxes (GPR161 export, GLI3 activator, GLI3 repressor, GLI1 TF activation)
- 2 hypothesis groups (PTCH1-driven ~85%, SUFU-driven ~10%)
- 3 shared nodes (SMO, GPR161, PTCH1 activity)
- Molecular target routing (CCND1 → all tissues, MYCN → cerebellum, BCL2 → BCC)
- 3 tissue-specific proliferation nodes with CL/UBERON annotations
- MONDO disease node at bottom with reversed `has phenotype` edges

The GO-CAM model IDs used:
- `gomodel:693b3c0900000716` — GPR161 export via BBSome/IFT-B
- `gomodel:693b3c0900001501` — SMO/DYRK2 → GLI3 activator
- `gomodel:693b3c0900000157` — GPR161 → GLI3 repressor
- `gomodel:693b3c0900001389` — GLI1 transcription factor activation
