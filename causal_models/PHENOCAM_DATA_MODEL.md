# Pheno-CAM Data Model

A **Pheno-CAM** (Phenotypic Causal Activity Model) is a structured causal model that traces the full chain from disease-causing mutation through molecular activities, tissue-specific pathophysiology, and phenotypic manifestation to disease classification. Every node and edge is grounded in ontology terms and evidence.

Pheno-CAMs are analogous to [GO-CAMs](https://geneontology.org/docs/gocam-overview/) for normal biology. Where a GO-CAM models what a gene product does in a healthy cell (molecular function + biological process + cellular location), a Pheno-CAM layers disease perturbation on top: which activities are altered, how they propagate through the pathway, what tissue-specific consequences follow, and which clinical phenotypes result.

## Conceptual Flow

```
Genetic variant
    ↓ perturbs
Module activity (e.g., PTCH1 inhibition of SMO)
    ↓ propagates through module topology
Downstream activities (e.g., GLI1 activation)
    ↓ drives (via driven_by edge)
Tissue-specific intermediate (e.g., basal cell proliferation in epidermis)
    ↓ causes condition (via driven_by edge)
Clinical phenotype (e.g., basal cell carcinoma, HP:0002671)
    ↑ has_phenotype (annotation, not causation)
Disease (e.g., Gorlin Syndrome, MONDO:0007187)
```

## Architecture

The model uses two file types in `causal_models/`:

```
causal_models/
  modules/                    # Reusable normal-biology pathway graphs
    ras_mapk_cascade.yaml     # Used by Noonan, CFC
    hedgehog_signaling.yaml   # Used by Gorlin
    collagen_v_assembly.yaml  # Used by EDS

  diseases/                   # Disease-specific perturbation overlays
    Noonan_Syndrome.yaml      # Imports ras_mapk_cascade
    Gorlin_Syndrome.yaml      # Imports hedgehog_signaling
    Ehlers-Danlos_Syndrome_COL5A1.yaml  # Imports collagen_v_assembly
```

**Modules** define normal biology: gene products performing molecular functions, connected by RO-typed causal edges. They are disease-agnostic and reusable — the same RAS-MAPK module serves both Noonan Syndrome and Cardiofaciocutaneous Syndrome.

**Disease files** import modules and overlay disease-specific information: which mutations perturb which activities, how perturbation propagates, and which tissue-specific pathways lead to clinical phenotypes.

---

## Modules

A module represents a reusable chunk of normal biology — a signaling pathway, a metabolic process, or a structural assembly.

### Top-Level Structure

```yaml
module:
  id: ras_mapk_cascade
  name: RAS-MAPK Signaling Cascade
  description: >
    Core RAS-MAPK signal transduction from receptor tyrosine kinase activation
    through SHP2/SOS1-mediated RAS-GTP loading, the RAF-MEK-ERK kinase cascade,
    and LZTR1-mediated RAS proteostasis.

  sources:
  - type: go_cam
    id: "gomodel:67c10cc400009089"
    name: "EGF signaling pathway (Human)"
  - type: literature
    reference: PMID:11992261

  activities: [...]    # Gene products performing molecular functions
  edges: [...]         # Causal relations between activities
```

The `sources` field tracks provenance — which GO-CAM models, Reactome pathways, and/or literature informed the module.

### Activities

An activity is the fundamental unit: **a gene product (or complex) performing a molecular function at a cellular location, participating in a biological process.**

```yaml
- id: sos1_gef
  gene:
    symbol: SOS1
    hgnc_id: HGNC:11187
  molecular_function:
    id: GO:0005088
    label: Ras guanyl-nucleotide exchange factor activity
  location:
    id: GO:0005886
    label: plasma membrane
  biological_process:
    id: GO:0007265
    label: Ras protein signal transduction
```

For multi-subunit complexes, `complex` replaces `gene`:

```yaml
- id: colv_heterotrimer
  complex: Type V collagen heterotrimer
  molecular_function:
    id: GO:0005201
    label: extracellular matrix structural constituent
  location:
    id: GO:0031012
    label: extracellular matrix
  biological_process:
    id: GO:0030199
    label: collagen fibril organization
```

| Field | Required | Description |
|-------|----------|-------------|
| `id` | yes | Unique within module |
| `gene` | if not `complex` | `{symbol, hgnc_id}` — HGNC gene reference |
| `complex` | if not `gene` | Free-text complex name |
| `molecular_function` | no | GO term `{id, label}` — what it does |
| `location` | no | GO term `{id, label}` — where it acts |
| `biological_process` | no | GO term `{id, label}` — process it participates in |
| `substrate` | no | `{symbol, hgnc_id}` — for activities acting on a specific target (e.g., LZTR1 ubiquitinating HRAS) |
| `display_name` | no | Override label for visualization |
| `source` | no | Provenance — `{type, id}` for GO-CAM or `{type, reference}` for literature |

### Edges

Edges define causal relationships between activities using Relation Ontology (RO) terms. Direction is source → target.

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
    snippet: "SHP2 is required for RAS-ERK MAP kinase (MAPK) cascade activation, and Noonan syndrome mutants enhance ERK activation ex vivo and in mice."
```

| Field | Required | Description |
|-------|----------|-------------|
| `source` | yes | Activity ID (within this module) |
| `target` | yes | Activity ID (within this module) |
| `relation` | yes | RO term `{id, label}` |
| `eco` | yes | Evidence Code Ontology term `{id, label}` |
| `evidence` | yes | Array of evidence items (can be empty) |

Module edges use "direct" RO relations:
- `RO:0002629` — directly positively regulates
- `RO:0002630` — directly negatively regulates
- `RO:0002413` — directly provides input for

---

## Disease Files

A disease file imports modules, defines how mutations perturb them, and routes the consequences to clinical phenotypes.

### Top-Level Structure

```yaml
disease_model:
  id: ehlers_danlos_col5a1
  name: Ehlers-Danlos Syndrome, COL5A1-related
  disorder_ref: Ehlers-Danlos_Syndrome_COL5A1-related.yaml
  disease_term:
    id: MONDO:0007522
    label: Ehlers-Danlos syndrome, classic type

  has_phenotype: [...]        # Disease → phenotype annotations
  imports: [...]              # Module references
  activities: [...]           # Disease-local activities (optional)
  hypothesis_groups: [...]    # Alternative genetic etiologies
  phenotype_routes: [...]     # Tissue-specific phenotype pathways
```

| Field | Required | Description |
|-------|----------|-------------|
| `id` | yes | Unique disease model ID |
| `name` | yes | Display name |
| `disorder_ref` | yes | Cross-reference to `kb/disorders/` file |
| `disease_term` | yes | MONDO term `{id, label}` |
| `has_phenotype` | no | Phenotype classification edges |
| `imports` | yes | `[{module: module_id}]` |
| `activities` | no | Disease-local activities not in any module |
| `hypothesis_groups` | yes | Genetic etiologies |
| `phenotype_routes` | yes | Pathways to phenotypes |

### Disease-Local Activities

Some diseases need activities that aren't in any reusable module — typically transcriptional targets specific to a disease context. These use the same structure as module activities but may omit `molecular_function` and `location` when they represent higher-level abstractions.

```yaml
activities:
- id: ccnd1_upregulation
  gene:
    symbol: CCND1
    hgnc_id: HGNC:1582
  biological_process:
    id: GO:0044843
    label: cell cycle G1/S phase transition
```

Only Gorlin Syndrome currently has disease-local activities (CCND1, BCL2, MYCN, GLI3 A/R imbalance) — these are Hedgehog target genes that aren't part of the signaling module itself.

---

## Hypothesis Groups

A disease may have multiple genetic etiologies converging on the same downstream pathophysiology. Each hypothesis group represents one such etiology.

```yaml
hypothesis_groups:
- id: col5a1_haploinsufficiency
  name: COL5A1 haploinsufficiency
  frequency: "~50% of cEDS"
  description: >
    Heterozygous loss-of-function variants in COL5A1 result in haploinsufficiency
    of the alpha-1(V) collagen chain...

  perturbations: [...]        # Entry point mutations
  propagated_states: [...]    # Downstream activity perturbations
```

Noonan Syndrome has 4 hypothesis groups (PTPN11 ~50%, SOS1 ~10%, RAF1 ~5%, LZTR1 <5%), all converging on ERK hyperactivation through different entry points in the RAS-MAPK cascade.

### Perturbations

A perturbation is the entry point — how a genetic variant alters a specific module activity.

```yaml
perturbations:
- target_activity: collagen_v_assembly:col5a1_structural
  variant_class:
    id: GENO:0000134
    label: loss of function variant
  perturbed_state: decreased
  eco:
    id: ECO:0000315
    label: mutant phenotype evidence used in manual assertion
  evidence:
  - type: literature
    reference: PMID:20847697
    snippet: "In the majority of patients with molecularly characterized classic Ehlers-Danlos syndrome, the disease is caused by a mutation leading to a nonfunctional COL5A1 allele and resulting in haploinsufficiency of type V collagen."
```

Activities are referenced as `module_id:activity_id` (e.g., `collagen_v_assembly:col5a1_structural`).

| Field | Required | Description |
|-------|----------|-------------|
| `target_activity` | yes | `module_id:activity_id` reference |
| `variant_class` | yes | GENO term `{id, label}` |
| `perturbed_state` | yes | How the activity is altered (see [Controlled Vocabularies](#controlled-vocabularies)) |
| `eco` | yes | Evidence code `{id, label}` |
| `evidence` | yes | Supporting evidence |

### Propagated States

Perturbations propagate through the module graph, creating downstream activity states. Each propagated state overlays a `perturbed_state` on an existing activity.

```yaml
propagated_states:
- activity: collagen_v_assembly:colv_heterotrimer
  perturbed_state: decreased

- activity: collagen_v_assembly:heterotypic_fibril_formation
  perturbed_state: decreased
```

Propagated states are **overlays, not independent nodes** — they don't have their own `id`. Identity comes from the referenced activity. A perturbed ERK kinase is still ERK kinase.

For module-internal propagation, the causal chain is inferred from the module's edges — no `driven_by` is needed. If `col5a1_structural` is decreased and the module has an edge `col5a1_structural → colv_heterotrimer`, the decrease propagates automatically.

**Cross-boundary propagated states** (connecting a module activity to a disease-local activity) do need explicit `driven_by`, since no module edge exists:

```yaml
# From Gorlin Syndrome — GLI1 activation drives disease-local CCND1 upregulation
- activity: ccnd1_upregulation
  perturbed_state: increased
  driven_by:
  - source: hedgehog_signaling:gli1_activation
    relation: {id: RO:0002304, label: causally upstream of, positive effect}
    eco: {id: ECO:0000305, label: curator inference used in manual assertion}
    evidence: []
```

| Field | Required | Description |
|-------|----------|-------------|
| `activity` | yes | `module_id:activity_id` or disease-local `activity_id` |
| `perturbed_state` | yes | How the activity is affected |
| `driven_by` | only for cross-boundary | Explicit causal edge(s) when no module edge exists |

**Constraint**: One propagated state per activity per hypothesis (enforced by validation).

---

## Phenotype Routes

Routes connect perturbed molecular activities to clinical phenotypes through tissue-specific intermediates. They are **hypothesis-agnostic** — defined at the disease level, not within hypothesis groups. A route describes "if this activity is perturbed, here's what happens in this tissue" regardless of which upstream mutation caused the perturbation.

```yaml
phenotype_routes:
- id: joint_hypermobility_route
  name: Joint hypermobility pathway
  description: >
    Reduced collagen fibril density in ligaments and joint capsules decreases
    tensile strength, permitting excessive joint excursion.

  intermediates: [...]    # Tissue-specific molecular states
  targets: [...]          # Clinical phenotypes
```

### Intermediates

An intermediate is a tissue-specific molecular or cellular state that bridges the gap between a perturbed module activity and a clinical phenotype.

```yaml
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
      snippet: "Currently, musculoskeletal manifestations related to joint hypermobility are perceived as the most prevalent determinants of the quality of life of affected individuals."
  biological_process:
    id: GO:0030198
    label: extracellular matrix organization
  tissue:
    cell_type: {id: CL:0000057, label: fibroblast}
    anatomy: {id: UBERON:0000211, label: ligament}
```

| Field | Required | Description |
|-------|----------|-------------|
| `id` | yes | Unique within disease |
| `name` | yes | Display name |
| `perturbed_state` | yes | State of this intermediate |
| `driven_by` | yes | Causal edge(s) from upstream activity/intermediate |
| `biological_process` | no | GO term `{id, label}` |
| `tissue` | no | `{cell_type: {id, label}, anatomy: {id, label}}` using CL and UBERON terms |

The `driven_by` edges on intermediates use "causally upstream of" RO relations:
- `RO:0002304` — causally upstream of, positive effect
- `RO:0002305` — causally upstream of, negative effect

### Targets

A target is a clinical phenotype — the observable consequence grounded in HPO.

```yaml
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

| Field | Required | Description |
|-------|----------|-------------|
| `id` | yes | Unique within disease; referenced by `has_phenotype` |
| `preferred_term` | yes | Human-readable phenotype name |
| `perturbed_state` | yes | Usually `increased` (phenotype is present/elevated) |
| `term` | yes | HPO term `{id, label}` |
| `driven_by` | yes | Causal edge(s) from intermediates |

Target `driven_by` uses `RO:0003303` (causes condition) — the relation between a pathological state and a clinical phenotype.

---

## Disease Classification (has_phenotype)

The `has_phenotype` field connects the disease to its phenotype targets. This is the only **non-causal** edge in the model — it expresses classification (the disease *is characterized by* these phenotypes), not causation.

```yaml
has_phenotype:
- phenotype: joint_hypermobility
  relation: {id: RO:0002200, label: has phenotype}
  eco: {id: ECO:0000305, label: curator inference used in manual assertion}
  evidence: []
- phenotype: skin_hyperextensibility
  relation: {id: RO:0002200, label: has phenotype}
  eco: {id: ECO:0000305, label: curator inference used in manual assertion}
  evidence: []
```

The `phenotype` field references a target `id` from `phenotype_routes`. The relation direction is disease → phenotype (matching RO:0002200 semantics: "Gorlin Syndrome *has phenotype* basal cell carcinoma").

This is deliberately separate from `driven_by` because the semantic direction is opposite: `driven_by` means "what causes this node's state" (upstream → downstream), while `has_phenotype` means "disease is classified by this phenotype" (disease → phenotype).

---

## Evidence

Evidence appears on edges throughout the model: module edges, perturbation entries, `driven_by` entries on intermediates and targets. It does not appear on containers (routes, hypothesis groups, disease_model).

```yaml
evidence:
- type: literature
  reference: PMID:17143285
  snippet: "SHP2 is required for RAS-ERK MAP kinase (MAPK) cascade activation..."
```

| Field | Required | Description |
|-------|----------|-------------|
| `type` | yes | `literature`, `go_cam`, or `reactome` |
| `reference` | yes | PMID, GO-CAM model ID, or Reactome pathway ID |
| `snippet` | for literature | Exact quote from the paper's abstract |

GO-CAM and Reactome evidence reference model/pathway IDs:

```yaml
- type: go_cam
  id: "gomodel:67c10cc400009089"
- type: reactome
  id: R-HSA-5358351
```

### Evidence Codes (ECO)

Every edge carries an ECO term describing how the claim was established:

| ECO ID | Label | When to use |
|--------|-------|-------------|
| `ECO:0007669` | computational evidence used in automatic assertion | Edge derived from GO-CAM model |
| `ECO:0000304` | traceable author statement used in manual assertion | Edge grounded in specific literature |
| `ECO:0000305` | curator inference used in manual assertion | Edge inferred by domain expert |
| `ECO:0000315` | mutant phenotype evidence used in manual assertion | Perturbation supported by mutant phenotype data |

---

## Edge Types Summary

The model has four distinct edge contexts, each using different RO relations:

| Context | Location | Common Relations | Semantics |
|---------|----------|-----------------|-----------|
| Module edges | `module.edges[]` | `RO:0002629` directly positively regulates, `RO:0002630` directly negatively regulates, `RO:0002413` directly provides input for | Normal-biology molecular interactions |
| Intermediate driven_by | `phenotype_routes[].intermediates[].driven_by[]` | `RO:0002304` causally upstream of, positive effect; `RO:0002305` causally upstream of, negative effect | Activity perturbation → tissue pathology |
| Target driven_by | `phenotype_routes[].targets[].driven_by[]` | `RO:0003303` causes condition | Tissue pathology → clinical phenotype |
| has_phenotype | `disease_model.has_phenotype[]` | `RO:0002200` has phenotype | Disease classification (non-causal) |

---

## Controlled Vocabularies

### perturbed_state

| Value | Category | Description | Example |
|-------|----------|-------------|---------|
| `increased` | Quantitative | Activity elevated above normal | ERK kinase hyperactivated |
| `decreased` | Quantitative | Activity reduced below normal | COL5A1 haploinsufficient |
| `absent` | Existential | Activity completely lost | PTCH1 inhibition absent |
| `constitutively_active` | Regulatory | Always active, ignores upstream regulation | SHP2 gain-of-function |
| `substrate_accumulated` | Mechanistic | Substrate builds up due to impaired degradation | RAS accumulation from LZTR1 loss |

### Common GENO Variant Classes

| GENO ID | Label |
|---------|-------|
| `GENO:0000134` | loss of function variant |
| `GENO:0000015` | missense variant |

### Common RO Relations

| RO ID | Label | Used in |
|-------|-------|---------|
| `RO:0002629` | directly positively regulates | Module edges |
| `RO:0002630` | directly negatively regulates | Module edges |
| `RO:0002413` | directly provides input for | Module edges |
| `RO:0002304` | causally upstream of, positive effect | Intermediate driven_by, cross-boundary propagated states |
| `RO:0002305` | causally upstream of, negative effect | Intermediate driven_by |
| `RO:0003303` | causes condition | Target driven_by |
| `RO:0002200` | has phenotype | Disease has_phenotype |

---

## Design Decisions

These architectural choices were made during data model review:

1. **`has_phenotype` is separate from `driven_by`.** The disease→phenotype relationship is annotation (classification), not causation. Using `driven_by` with `RO:0002200` read backwards semantically ("BCC has phenotype Gorlin" instead of "Gorlin has phenotype BCC").

2. **Module topology is the single source of truth for module-internal edges.** Propagated states don't redeclare module edges via `driven_by` — the module already defines the connectivity. Only cross-boundary edges (module → disease-local activity) retain `driven_by` on propagated states.

3. **Propagated states are overlays, not independent nodes.** A perturbed ERK is still ERK — it doesn't need its own ID. Downstream nodes reference the activity ID, and the visualization resolves perturbed state from context.

4. **Routes are hypothesis-agnostic.** Phenotype routes describe "if this activity is perturbed, here's the tissue-specific consequence" — independent of which upstream mutation caused the perturbation. Different hypotheses may activate different subsets of routes; the visualization handles this by checking which upstream drivers are perturbed under the selected hypothesis.

5. **Evidence lives on edges, not containers.** Every evidence item is attached to a specific causal claim (an edge), not to a route or hypothesis group as ambient context.

---

## Node Types at a Glance

| Type | Has `id` | Has `driven_by` | Has `perturbed_state` | Declared in |
|------|----------|-----------------|----------------------|-------------|
| Module activity | yes | no (uses module `edges`) | no (wild-type) | `module.activities` |
| Disease activity | yes | no | no (wild-type) | `disease_model.activities` |
| Propagated state | no (refs `activity`) | optional (cross-boundary only) | yes | `hypothesis_groups[].propagated_states` |
| Intermediate | yes | yes | yes | `phenotype_routes[].intermediates` |
| Target (phenotype) | yes | yes | yes | `phenotype_routes[].targets` |
| Disease | yes | no (uses `has_phenotype`) | no | `disease_model` |
