# Pheno-CAM Design Specification

## Overview

Pheno-CAMs (Phenotype Causal Activity Models) are structured causal models that connect
disease-causing mutations through molecular mechanisms to clinical phenotypes. They layer
disease-specific perturbation information on top of reusable normal-biology modules derived
from GO-CAMs and other sources.

This spec defines the data model, tooling, and integration plan for adding Pheno-CAM
support to the dismech knowledge base.

## Motivation

The dismech `pathophysiology` entries capture causal relationships between disease mechanisms
and phenotypes, but lack:

- Formal molecular grounding (specific gene products performing specific functions)
- Normal vs. perturbed state distinction
- Typed causal edges (RO relation semantics)
- Reusable mechanistic modules shared across diseases
- Queryable structure for variant interpretation and drug target identification

Pheno-CAMs address these gaps by providing a formally structured causal graph that bridges
molecular biology (GO-CAMs) to disease phenotypes (HPO) through dismech pathophysiology.

### Pivotal Use Cases (from Mar 10, 2026 CZI meeting)

1. **Variant interpretation**: Given a variant in a disease-associated gene, trace the
   predicted perturbation cascade through the causal model to identify expected phenotypes.
2. **Drug target identification**: Given a perturbed node in the causal model, identify
   intervention points that could restore normal state or block downstream effects.

### Funder Focus Areas

Neurodevelopmental, neurodegenerative, neuroimmune, and cardiac diseases — though worked
examples are not limited to these.

## Architecture: Approach C — Separate Data Layer with Shared Module Library

Pheno-CAM data lives in a new `causal_models/` directory, separate from `kb/disorders/`.
This avoids disrupting the existing KB pipeline while allowing aggressive iteration on the
data model. The module structure is designed so that future migration into the main Disease
schema (as a `causal_model:` field replacing or augmenting `pathophysiology:`) is
straightforward.

### Directory Structure

```
causal_models/
  modules/                          # Reusable normal-biology subgraphs
    hedgehog_signaling.yaml
    ras_mapk_cascade.yaml
    mitochondrial_quality_control.yaml
    ...

  diseases/                         # Disease-specific perturbation overlays
    Gorlin_Syndrome.yaml            # imports hedgehog_signaling
    Noonan_Syndrome.yaml            # imports ras_mapk_cascade
    Parkinsons_Disease.yaml         # imports multiple modules
    ...
```

### Relationship to Existing Components

- **`kb/disorders/`**: Cross-referenced via `disorder_ref` field. Not modified.
- **`pathways/reactome/`**: Optionally referenced for variant-reaction data.
- **`src/dismech/graph.py`**: Extended with `build_phenocam_graph()` for visualization.
- **`src/dismech/perturb/graph.py`**: Extended with perturbation state propagation.
- **D3+Dagre pathograph renderer**: Extended with new node types for pheno-CAM display.

## Data Model: Module Files

A module represents a reusable chunk of normal biology — a signaling pathway, a metabolic
process, or a functional unit. Modules are disease-agnostic.

```yaml
module:
  id: hedgehog_signaling
  name: Hedgehog Signaling Pathway
  description: >
    Core Hedgehog signal transduction from SMO activation through
    GLI transcription factor processing.

  # Provenance: which GO-CAMs and/or other sources informed this module
  sources:
  - type: go_cam
    id: "gomodel:693b3c0900001501"
    name: "GLI3 activator"
  - type: go_cam
    id: "gomodel:693b3c0900000157"
    name: "GLI3 repressor"
  - type: reactome
    id: R-HSA-5358351
    name: "Signaling by Hedgehog"
  - type: literature
    reference: PMID:29149591

  # Activity nodes: gene product performing a molecular function
  activities:
  - id: ptch1_inhibition
    gene:
      symbol: PTCH1
      hgnc_id: HGNC:9585
    molecular_function:
      id: GO:0038108
      label: smoothened inhibitor activity
    location:
      id: GO:0005929
      label: cilium

  - id: smo_activity
    gene:
      symbol: SMO
      hgnc_id: HGNC:11119
    molecular_function:
      id: GO:0004930
      label: G protein-coupled receptor activity
    location:
      id: GO:0005929
      label: cilium

  - id: sufu_sequestering_gli3
    gene:
      symbol: SUFU
      hgnc_id: HGNC:16466
    molecular_function:
      id: GO:0140311
      label: protein sequestering activity
    substrate:
      symbol: GLI3
      hgnc_id: HGNC:4319
    location:
      id: GO:0005737
      label: cytoplasm

  # ... additional activities in the full module (abbreviated here):
  # - sufu_sequestering_gli1 (SUFU sequesters GLI1)
  # - gli3a_activation (GLI3A transcriptional activator activity)
  # - gli3r_production (GLI3R transcriptional repressor activity)
  # - gli1_activation (GLI1 transcriptional activator activity)
  # - gpr161_activity (GPR161 GPCR activity in cilium)
  # - pka_activity (PRKACA cAMP-dependent kinase)
  # See the Gorlin Syndrome example for the complete set.

  # Edges between activities: RO-typed causal relations
  edges:
  - source: ptch1_inhibition
    target: smo_activity
    relation:
      id: RO:0002630
      label: directly negatively regulates
    evidence:
    - type: literature
      reference: PMID:29149591
      snippet: "..."

  - source: smo_activity
    target: sufu_sequestering_gli3
    relation:
      id: RO:0002407
      label: indirectly positively regulates
    evidence:
    - type: go_cam
      id: "gomodel:693b3c0900001501"
```

### Module Design Principles

- **Activity nodes** are the fundamental unit: gene product + molecular function + location
- **Substrate** field captures specificity (SUFU sequesters GLI3 vs GLI1 = different activities)
- **Edges carry RO relations** for formal causal semantics
- **Evidence on edges** can be literature (PMID), GO-CAM (model ID), or Reactome sourced
- **No disease or perturbation information** — purely normal biology
- **Modules are reusable** across diseases that share the same pathway

### Evidence Structure

Pheno-CAM evidence items use a simplified structure distinct from the dismech `EvidenceItem`
class (which has `supports`, `evidence_source`, `snippet`, `explanation`). Pheno-CAM evidence
focuses on provenance tracking:

```yaml
evidence:
- type: literature          # literature | go_cam | reactome
  reference: PMID:29149591  # PMID, GO-CAM model ID, or Reactome pathway ID
  snippet: "..."            # exact quote (for literature type)
```

The `type` field replaces dismech's `evidence_source` (which classifies the study type).
The existing reference validator could be extended to validate `type: literature` entries
against PubMed abstracts. GO-CAM and Reactome references are validated by checking that the
referenced model/pathway exists.

### Perturbation State Scope

The `perturbed_state` controlled vocabulary applies to two entity types:
- **Module activities** (in `propagated_states`) — e.g., `smo_activity: constitutively_active`
- **Phenotype route intermediates** (in `phenotype_routes`) — e.g., `CCND1 upregulation: increased`

Both use the same enum. The distinction is structural: module activities are formal nodes in
the causal graph; intermediates are disease-specific molecular effects that bridge the graph
to clinical phenotypes.

### Variant Class vs Mechanism

The `variant_class` field (GENO-typed) describes the genetic variant category (e.g., loss of
function variant, missense variant). The `mechanism` field describes the molecular consequence
(e.g., `loss_of_function`, `gain_of_function`). These can diverge: a missense variant
(`variant_class`) can cause loss of function (`mechanism`) if the amino acid change disrupts
a critical domain

## Data Model: Disease Perturbation Files

A disease file imports modules, defines how mutations perturb them, and routes downstream
to phenotypes.

```yaml
disease_model:
  id: gorlin_syndrome
  name: Gorlin Syndrome
  disorder_ref: Gorlin_Syndrome.yaml   # cross-ref to kb/disorders/
  disease_term:
    id: MONDO:0007187
    label: nevoid basal cell carcinoma syndrome

  # Which modules does this disease perturb?
  imports:
  - module: hedgehog_signaling

  # Hypothesis groups: alternative genetic etiologies
  hypothesis_groups:
  - id: ptch1_driven
    name: PTCH1-driven
    frequency: "~85%"
    description: >
      Germline PTCH1 loss-of-function removes constitutive SMO inhibition,
      causing constitutive Hedgehog pathway activation.

    # Perturbation entry points
    perturbations:
    - target_activity: hedgehog_signaling:ptch1_inhibition
      variant_class:
        id: GENO:0000134
        label: loss of function variant
      perturbed_state: absent
      mechanism: loss_of_function
      evidence:
      - type: literature
        reference: PMID:29149591
        snippet: "..."

    # Propagated perturbation states
    # provenance: how this state was derived
    # evidence: what supports it (independent of provenance)
    propagated_states:
    - activity: hedgehog_signaling:smo_activity
      perturbed_state: constitutively_active
      cause: hedgehog_signaling:ptch1_inhibition
      provenance: topology_inferred
      evidence:
      - type: literature
        reference: PMID:29149591
        snippet: "..."

    - activity: hedgehog_signaling:gli3r_production
      perturbed_state: absent
      cause: hedgehog_signaling:smo_activity
      provenance: literature_grounded
      evidence:
      - type: literature
        reference: PMID:18275819
        snippet: "..."

  - id: sufu_driven
    name: SUFU-driven
    frequency: "~10%"
    description: >
      Germline SUFU loss-of-function frees GLI3A and GLI1 from
      sequestration. GLI3R branch still partially active.
    perturbations:
    - target_activity: hedgehog_signaling:sufu_sequestering_gli3
      variant_class:
        id: GENO:0000134
        label: loss of function variant
      perturbed_state: absent
      mechanism: loss_of_function
    propagated_states: []  # different from PTCH1 hypothesis

  # Downstream phenotype routing
  phenotype_routes:
  - id: bcc_route
    name: Basal cell carcinoma pathway
    description: >
      Constitutive GLI activation drives CCND1/BCL2 upregulation
      in basal cells of the epidermis.
    intermediates:
    - name: CCND1 upregulation
      gene:
        symbol: CCND1
        hgnc_id: HGNC:1582
      perturbed_state: increased
      driven_by:
      - hedgehog_signaling:gli3a_activation
      - hedgehog_signaling:gli1_activation
      biological_process:
        id: GO:0044843
        label: cell cycle G1/S phase transition
    target_phenotype:
      preferred_term: Basal cell carcinoma
      term:
        id: HP:0002671
        label: Basal cell carcinoma
    tissue:
      cell_type:
        id: CL:0002187
        label: basal cell of epidermis
      anatomy:
        id: UBERON:0002097
        label: skin of body
    evidence:
    - type: literature
      reference: PMID:22820643
      snippet: "..."

  # Optional Reactome variant data
  reactome_variants:
    source: Gorlin_Syndrome.yaml
```

### Disease File Design Principles

- **`imports`** lists which modules are perturbed
- **Hypothesis groups** each define their own entry points AND propagated states
- **`provenance`** on propagated states: `topology_inferred`, `literature_grounded`, or
  `model_grounded` (e.g., an edge sourced directly from a GO-CAM model)
- **`evidence`** on propagated states: independent of provenance — a topology-inferred
  claim can also have literature support
- **Phenotype routes** bridge molecular perturbation to clinical phenotype through
  tissue-specific intermediates (CL/UBERON/HPO)
- **`disorder_ref`** is a loose cross-reference to `kb/disorders/`; the two files evolve
  independently

## Controlled Vocabulary: Perturbation States

| State | Description | Ontology Mapping |
|---|---|---|
| `absent` | Activity completely lost | PATO:0000462 |
| `decreased` | Activity reduced but present | PATO:0000912 |
| `increased` | Activity elevated above normal | PATO:0000911 |
| `constitutively_active` | Activity always on, unregulated | Custom |
| `haploinsufficient` | ~50% activity from single copy | GENO:0000134 + PATO context |
| `mislocalized` | Present but wrong compartment | PATO:0000628 (closest) |
| `aggregated` | Unavailable due to aggregation | Custom |
| `substrate_accumulated` | Substrate builds up, upstream block | Custom |
| `substrate_depleted` | Substrate unavailable | Custom |
| `neomorphic` | Novel activity not in wild-type | Custom (GENO context) |
| `dominant_negative` | Interferes with wild-type product | Custom (GENO context) |
| `temporally_dysregulated` | Activity at wrong time | Custom |

This vocabulary will be defined as a LinkML enum with `meaning` fields pointing to
ontology terms where available. Expected to grow as worked examples expose gaps.

## Evidence Provenance Types

Each edge or perturbation state has a `provenance` indicating how the claim was derived,
and an optional `evidence` list providing supporting references.

| Provenance | Meaning | Example |
|---|---|---|
| `literature_grounded` | Claim comes from a published paper | PMID with snippet |
| `model_grounded` | Claim comes from a curated model | GO-CAM model ID, Reactome pathway ID |
| `topology_inferred` | Derived from graph structure + sign propagation | "Loss of inhibitor = constitutive activation" |

Provenance and evidence are independent: a topology-inferred claim can have literature
evidence supporting it, and a literature-grounded claim can also have a GO-CAM model
corroborating it.

## GO-CAM Programmatic Access

### Script: `scripts/fetch_gocam_models.py`

Fully automated — no human review of intermediate results.

**Input**: Gene symbols (e.g., `PTCH1 SMO SUFU GLI3`)

**API approach (validated in Phase 1)**: Two-step static index + model detail API:

1. **Static index**: `go-cam-browser.geneontology.org/data.json` — complete index of all
   GO-CAM models (1,862 as of Mar 2026, 1,093 human) with gene labels, gene IDs, GO terms,
   organism, and model IDs. Searchable locally, cached, no API fragility.
2. **Model detail**: `api.geneontology.org/api/go-cam/{model_id}` — returns full JSON with
   individuals (activities, gene products, locations, processes) and facts (RO-typed causal
   edges between activity units).

Approaches that did NOT work: REST gene-product endpoint (`/api/gp/{id}/models`) returns
500 errors; SPARQL endpoint (`rdf.geneontology.org/sparql`) returns 524 timeouts.

**Coverage note**: GO-CAM `enabled_by` links are curated for genes that *perform* molecular
functions, not genes that act as inhibitors/substrates. PTCH1 (inhibitor of SMO) and
BRAF/RAF1/KRAS are not yet in GO-CAMs as `enabled_by` actors. The hedgehog and RAS-MAPK
pathways are reachable via SMO, SUFU, GLI1/2, PTPN11, SOS1, and HRAS.

**Process** (once API approach is validated):
1. Query for GO-CAM models involving each input gene
2. Fetch full model data for each candidate
3. Parse activity units: extract `enabled_by` (gene product), molecular function,
   cellular component, biological process
4. Parse causal edges: extract RO-typed relations between activity units
5. Identify shared nodes across models (same gene product in multiple models)
6. Filter: only include models where gene is `enabled_by` an activity (not just mentioned)
7. Cross-check against input gene list — exclude models with no overlap

**Output**: Structured YAML with activities and edges, ready to be assembled into modules.

**Caching**: Local cache in `causal_models/.cache/` (same pattern as Reactome script).

**Usage**:
```bash
uv run python scripts/fetch_gocam_models.py PTCH1 SMO SUFU GLI3
uv run python scripts/fetch_gocam_models.py --from-disorder kb/disorders/Noonan_Syndrome.yaml
```

**Safeguards** (replacing human review):
- Only include models where gene is `enabled_by` an activity
- Validate extracted GO/RO terms exist via OAK
- Cross-check against disease gene list
- Transparent provenance: every node/edge traces to a GO-CAM model ID

## Visualization

Extends the existing D3+Dagre pathograph renderer (documented in `docs/pathographs.md`).

### New Node Types

| Node Type | Shape | Color | Source |
|---|---|---|---|
| Activity (normal) | Octagon | Blue (#dce8f8) | Module activity nodes |
| Activity (perturbed) | Octagon, dashed border | Red (#ffcccc) | Propagated states |
| Hypothesis group | Rounded container | Amber (#fef9e7) | Hypothesis groups |
| Molecular intermediate | Small diamond | Pink (#fce7f3) | Phenotype route intermediates |

### Rendering Modes

Disorder pages would offer a toggle between:
- **Pathograph** (existing) — current dismech causal graph
- **Pheno-CAM** (new) — molecular-level graph from `causal_models/`

### Implementation

- Add new `build_phenocam_graph()` function to `graph.py` (alongside existing
  `build_causal_graph()`) that loads causal model YAML and produces a `CausalGraph`
  with the new node types
- Extend the existing `graph_to_json()` to serialize new node types
- Add new shapes to the D3 renderer in the Jinja2 template
- Add mode toggle UI element

## Skill and Tooling Architecture

### Skill: `pheno-cam` (rework of existing)

Workflow:
1. Read KB entry — pull genes, pathophysiology, phenotypes
2. Read Reactome data (if available) — pull variant-reaction mappings
3. Run GO-CAM script — `scripts/fetch_gocam_models.py` with disease genes
4. Assemble module draft(s) — reuse existing modules where they exist
5. Build disease perturbation file — map genetic causes to perturbation entry points,
   propagate states, connect to phenotypes
6. Add evidence — reuse `dismech-references` for literature, tag GO-CAM sources,
   mark topology-inferred propagations
7. Validate — schema validation, term validation, graph integrity

### Validation Hook (eventual)

`validate_causal_model_hook.py` — intercepts writes to `causal_models/`, validates
against pheno-CAM LinkML schema. Same pattern as existing `validate_disorder_hook.py`.

## Phases and Demoable Milestones

### Phase 1: GO-CAM Programmatic Access

Build `scripts/fetch_gocam_models.py`. Test against known Gorlin GO-CAM model IDs,
then against Noonan genes (PTPN11, SOS1, RAF1, BRAF).

**Demo**: "Given a gene list, we can automatically find and parse relevant GO-CAM models.
Here's what the script found for Noonan's genes."

### Phase 2: Data Model and Worked Examples

Define YAML structure. Create Gorlin Syndrome module + disease file using GO-CAM script
output. Create Noonan Syndrome as second example.

**Demo**: "Here's a formal causal model for Gorlin and Noonan. Here's how PTCH1 vs SUFU
hypotheses produce different downstream states. Here's how the same RAS/MAPK module
connects Noonan to Cardiofaciocutaneous Syndrome."

### Phase 3: Skill-Driven Curation

Rework the `pheno-cam` skill with automated workflow. Curate Parkinson's Disease as the
complex/temporal test case.

**Demo**: "We can now say 'build a pheno-CAM for X' and the skill orchestrates the full
pipeline. Here's Parkinson's with multiple hypothesis groups and shared modules."

### Phase 4: Visualization and Validation

Extend D3+Dagre renderer. Build LinkML schema. Add validation hook.

**Demo**: "Pheno-CAMs render as interactive graphs on disorder pages alongside existing
pathographs. Schema validation catches structural errors."

### Phase 5: Pivotal Use Case Prototyping

Variant interpretation prototype. Drug target identification prototype.

**Demo**: "Given a novel PTPN11 variant, here's what the Noonan pheno-CAM predicts for
downstream phenotypes. Given constitutive RAS activation, here are candidate intervention
points."

## Worked Examples

| Disease | Why | Tests |
|---|---|---|
| Gorlin Syndrome | Two hypothesis groups (PTCH1 ~85%, SUFU ~10%), well-characterized Hh pathway, existing GO-CAM models | Multi-hypothesis, sign propagation, tissue routing |
| Noonan Syndrome | RASopathy with multiple genes (PTPN11, SOS1, RAF1, BRAF, KRAS), cardiac + developmental phenotypes, Reactome data available | Multi-gene same-pathway, module reuse potential (CFC syndrome) |
| Parkinson's Disease | Multiple hypothesis groups (LRRK2, PINK1/Parkin, SNCA, GBA), progressive/temporal, rich existing KB entry | Module reuse, complex disease, temporal modeling |

## Migration Path

The separate `causal_models/` architecture is designed for eventual integration:

1. **Current**: `causal_models/` is independent, cross-references `kb/disorders/` loosely
2. **Near-term**: Renderer reads both and produces combined views
3. **Eventually**: `causal_model:` field added to Disease schema, referencing or inlining
   the module+overlay structure. `pathophysiology:` coexists or is gradually replaced.
4. **Long-term**: Pheno-CAM becomes the primary pathophysiology representation
