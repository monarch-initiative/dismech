# PhenoCAM V2 — Schema Reference

Schema file: `src/dismech/schema/phenocam/phenocam.yaml`

> **Note on required fields:** The LinkML schema enforces only four fields as `required: true`:
> `id` (identifier on all node kinds), and `subject`, `predicate`, `object` (on CausalRelation).
> Everything else is a curator convention — the validator won't reject a file that omits them,
> but they are expected for a complete model. The "Schema-req" column below marks only what
> the schema actually enforces.

---

## Root Classes

`BiologicalCausalModel` is the abstract base class shared by both file types.
It owns all node-kind collections and the `causal_relations` block.

### BiologicalCausalModel (abstract)

| Slot | Type | Notes |
|---|---|---|
| `id` | string | schema-required, identifier |
| `name` | string | |
| `description` | string | |
| `sources` | list of `Source` | provenance references |
| `molecular_entities` | list of `MolecularEntity` | |
| `molecular_activities` | list of `MolecularActivity` | |
| `cellular_processes` | list of `CellularProcess` | |
| `tissue_processes` | list of `TissueProcess` | |
| `variants` | list of `Variant` | |
| `chemical_exposures` | list of `ChemicalExposure` | |
| `environmental_factors` | list of `EnvironmentalFactor` | |
| `phenotypes` | list of `Phenotype` | |
| `modulators` | list of `Modulator` | |
| `causal_relations` | list of `CausalRelation` | |

### Module (`tree_root`)

File location: `causal_models/modules/<id>.yaml`

Inherits all slots from BiologicalCausalModel. Adds no additional slots.
Behavioural constraint: nodes carry no `quality` tags — normal biology is implicitly wild-type.

### DiseaseCourse (`tree_root`)

File location: `causal_models/diseases/<Disease>.yaml`

Inherits all slots from BiologicalCausalModel, plus:

| Slot | Type | Notes |
|---|---|---|
| `realises_disease` | `OntologyTerm` | MONDO term for the disease |
| `has_subtypes` | list of `Subtype` | clinical or molecular subtypes |
| `hypothesis_groups` | list of `HypothesisGroup` | alternative etiologies |
| `imports` | list of `ModuleImport` | modules this disease course imports |
| `has_phenotype` | list of `DiseaseHasPhenotype` | non-causal disease→phenotype annotations |
| `disorder_ref` | string | cross-reference to `kb/disorders/<filename>.yaml` |

---

## Node Kinds

### Variant

A genetic perturbation (germline or somatic) that drives the disease course.

| Attribute | Schema-req | Type / Ontology | Notes |
|---|---|---|---|
| `id` | ✅ | string | local identifier |
| `gene` | — | `GeneRef` | HGNC gene reference |
| `variant_type` | — | `OntologyTerm` | GENO or SO term (e.g. `SO:0002054 loss_of_function_variant`) |
| `hypotheses` | — | list of strings | hypothesis group IDs this variant drives |
| `description` | — | string | |

Lives in: **DiseaseCourse only**

---

### ChemicalExposure

An exogenous small molecule driving the disease (toxin, dietary load, drug-as-stressor).
Distinct from `MolecularEntity` which is an endogenous intermediate.

| Attribute | Schema-req | Type / Ontology | Notes |
|---|---|---|---|
| `id` | ✅ | string | |
| `agent` | — | `OntologyTerm` | ChEBI term |
| `hypotheses` | — | list of strings | |
| `description` | — | string | |

Lives in: **DiseaseCourse only**

---

### EnvironmentalFactor

A non-chemical environmental input (UV radiation, mechanical stress, infection).

| Attribute | Schema-req | Type / Ontology | Notes |
|---|---|---|---|
| `id` | ✅ | string | |
| `factor` | — | `OntologyTerm` | ECTO term |
| `hypotheses` | — | list of strings | |
| `description` | — | string | |

Lives in: **DiseaseCourse only**

---

### MolecularActivity

A gene product (or complex) performing a molecular function at a cellular location.

| Attribute | Schema-req | Type / Ontology | Notes |
|---|---|---|---|
| `id` | ✅ | string | |
| `gene` | — | `GeneRef` | mutually exclusive with `complex_name` |
| `complex_name` | — | string | for multi-subunit complexes (e.g. "BBSome") — mutually exclusive with `gene` |
| `molecular_function` | — | `OntologyTerm` | GO Molecular Function (GO MF) |
| `location` | — | `OntologyTerm` | GO Cellular Component or UBERON |
| `biological_process` | — | `OntologyTerm` | GO Biological Process (GO BP) |
| `quality` | — | `PerturbationQualityEnum` | absent on module nodes; set on perturbed nodes in disease files |
| `hypotheses` | — | list of strings | |
| `subtypes` | — | list of strings | |
| `sources` | — | list of `Source` | GO-CAM, Reactome, or literature provenance |
| `description` | — | string | |
| `display_name` | — | string | override label for visualization |

Lives in: **Module or DiseaseCourse**

---

### CellularProcess

A process primarily characterized by a cell type performing a biological process.

| Attribute | Schema-req | Type / Ontology | Notes |
|---|---|---|---|
| `id` | ✅ | string | |
| `cell_type` | — | `OntologyTerm` | Cell Ontology (CL) |
| `biological_process` | — | `OntologyTerm` | GO Biological Process (GO BP) |
| `anatomy` | — | `OntologyTerm` | UBERON — when cell is in a specific tissue context |
| `quality` | — | `PerturbationQualityEnum` | |
| `hypotheses` | — | list of strings | |
| `subtypes` | — | list of strings | |
| `sources` | — | list of `Source` | |
| `description` | — | string | |
| `display_name` | — | string | |

Lives in: **Module or DiseaseCourse**

---

### TissueProcess

A process primarily characterized by an anatomical structure.

| Attribute | Schema-req | Type / Ontology | Notes |
|---|---|---|---|
| `id` | ✅ | string | |
| `anatomy` | — | `OntologyTerm` | UBERON |
| `biological_process` | — | `OntologyTerm` | GO Biological Process (GO BP) |
| `cell_type` | — | `OntologyTerm` | CL — when a specific cell mediates the tissue-level process |
| `quality` | — | `PerturbationQualityEnum` | |
| `hypotheses` | — | list of strings | |
| `subtypes` | — | list of strings | |
| `sources` | — | list of `Source` | |
| `description` | — | string | |
| `display_name` | — | string | |

Lives in: **Module or DiseaseCourse**

---

### MolecularEntity

A biomolecule (protein, cytokine, metabolite, lipid, second messenger, ECM component)
acting as an intermediate in the causal chain — simultaneously an output of one process
and an input to another (e.g. SHH ligand, TNF-alpha).

| Attribute | Schema-req | Type / Ontology | Notes |
|---|---|---|---|
| `id` | ✅ | string | |
| `entity` | — | `OntologyTerm` | ChEBI (molecules) or PR (specific proteins) |
| `gene` | — | `GeneRef` | if the entity is a specific gene product |
| `location` | — | `OntologyTerm` | GO CC or UBERON |
| `quality` | — | `PerturbationQualityEnum` | |
| `hypotheses` | — | list of strings | |
| `subtypes` | — | list of strings | |
| `sources` | — | list of `Source` | |
| `description` | — | string | |
| `display_name` | — | string | |

Lives in: **Module or DiseaseCourse**

---

### Phenotype

A clinical observable. Connected to the disease non-causally via `has_phenotype` and
causally via `causal_relations` edges from upstream nodes.

| Attribute | Schema-req | Type / Ontology | Notes |
|---|---|---|---|
| `id` | ✅ | string | |
| `hpo_term` | — | `OntologyTerm` | HPO term |
| `hypotheses` | — | list of strings | scopes to a specific genetic etiology |
| `subtypes` | — | list of strings | |
| `description` | — | string | |
| `display_name` | — | string | |

Lives in: **DiseaseCourse only**

---

### Modulator

A therapeutic, dietary, or environmental intervention wired into the causal graph.

| Attribute | Schema-req | Type / Ontology | Notes |
|---|---|---|---|
| `id` | ✅ | string | |
| `agent` | — | `OntologyTerm` | ChEBI (specific small molecules), NCIT (drug classes/biologics), MAXO (non-pharmacological) |
| `role` | — | `ModulatorRoleEnum` | `therapeutic`, `dietary`, or `environmental` |
| `description` | — | string | |

Lives in: **DiseaseCourse only**

---

### CausalRelation

A directed causal edge between any two nodes. All causal claims live here — no edges
hidden inside node internals.

| Attribute | Schema-req | Type | Notes |
|---|---|---|---|
| `subject` | ✅ | string | id of source node (any kind) |
| `predicate` | ✅ | `OntologyTerm` | RO relation (e.g. `RO:0002630 directly negatively regulates`) |
| `object` | ✅ | string | id of target node (any kind) |
| `eco` | — | `OntologyTerm` | ECO evidence code |
| `evidence` | — | list of `EvidenceItem` | |
| `hypotheses` | — | list of strings | scopes edge to specific hypotheses |
| `subtypes` | — | list of strings | |
| `effect` | — | `ModulatorEffectEnum` | only when `subject` is a `Modulator` |

Lives in: **Module or DiseaseCourse**

---

### DiseaseHasPhenotype

Non-causal annotation linking the disease to a phenotype. Separate from `causal_relations`
which traces the mechanistic path to the phenotype.

| Attribute | Schema-req | Type | Notes |
|---|---|---|---|
| `phenotype_ref` | — | string | must match a `Phenotype.id` in `phenotypes` |
| `relation` | — | `OntologyTerm` | typically `RO:0002200 has phenotype` |
| `eco` | — | `OntologyTerm` | ECO evidence code |
| `evidence` | — | list of `EvidenceItem` | |

Lives in: **DiseaseCourse only**

---

### HypothesisGroup

An alternative etiology for the disease. Nodes and edges tagged with this id apply
only under this etiology.

| Attribute | Schema-req | Notes |
|---|---|---|
| `id` | ✅ | referenced by `hypotheses` fields on nodes and edges |
| `name` | — | display name |
| `frequency` | — | free text (e.g. `~85%`) |
| `description` | — | |

Lives in: **DiseaseCourse only**

---

### Subtype

A clinical or molecular subtype of the disease.

| Attribute | Schema-req | Type / Ontology | Notes |
|---|---|---|---|
| `id` | ✅ | string | referenced by `subtypes` fields on nodes and edges |
| `display_name` | — | string | |
| `mondo_term` | — | `OntologyTerm` | MONDO term if the subtype has its own identifier |
| `description` | — | string | |

Lives in: **DiseaseCourse only**

---

### ModuleImport

Declares that a DiseaseCourse imports a named Module.

| Attribute | Schema-req | Notes |
|---|---|---|
| `module` | — | module id — must match a file at `causal_models/modules/<id>.yaml` |

Lives in: **DiseaseCourse only**

---

## Supporting Types

### GeneRef

| Attribute | Schema-req | Notes |
|---|---|---|
| `symbol` | — | HGNC-approved gene symbol (e.g. `SMO`) |
| `hgnc_id` | — | lowercase `hgnc:` prefix (e.g. `hgnc:11119`) |

### OntologyTerm

| Attribute | Schema-req | Notes |
|---|---|---|
| `id` | — | CURIE (e.g. `GO:0004930`, `HP:0002671`) |
| `label` | — | canonical ontology term label — must exactly match the authoritative source |

### EvidenceItem

| Attribute | Schema-req | Notes |
|---|---|---|
| `reference` | — | CURIE (PMID:, DOI:, NCT:, ORPHA:, gomodel:, R-HSA-*) |
| `supports` | — | `EvidenceItemSupportEnum` |
| `evidence_source` | — | `EvidenceSourceEnum` |
| `snippet` | — | verbatim quote from the cited source |
| `explanation` | — | curator explanation of how the evidence supports the claim |

### Source

Provenance for a module or node.

| Attribute | Schema-req | Notes |
|---|---|---|
| `type` | — | `SourceTypeEnum` — `go_cam`, `reactome`, `wikipathways`, `literature` |
| `source_id` | — | gomodel: CURIE, R-HSA-* for Reactome, WP* for WikiPathways |
| `reference` | — | PMID or other literature CURIE |
| `source_name` | — | human-readable name of the source pathway |

---

## Enums

### PerturbationQualityEnum (PATO-bound)

Applied to nodes in disease courses. Absent on module nodes (normal biology = implicitly wild-type).

| Value | Meaning | PATO term |
|---|---|---|
| `INCREASED` | Increased activity, abundance, or level | PATO:0000573 |
| `DECREASED` | Decreased activity, abundance, or level | PATO:0000574 |
| `ABSENT` | Completely absent or null | PATO:0000462 |
| `GAIN_OF_FUNCTION` | Pathological gain of function | PATO:0001396 |
| `LOSS_OF_FUNCTION` | Pathological loss of function | PATO:0001561 |

### ModulatorEffectEnum

Set on `CausalRelation.effect` when the subject is a `Modulator`.

| Value | Meaning |
|---|---|
| `rescues_full` | Fully restores perturbed node to near-normal state |
| `rescues_partial` | Partially restores perturbed node |
| `reduces_load` | Reduces substrate or upstream load |
| `blocks_downstream` | Blocks a downstream pathological node |
| `amplifies` | Amplifies an existing perturbation |
| `none` | No net effect (null result) |

### ModulatorRoleEnum

| Value | Meaning |
|---|---|
| `therapeutic` | Drug or biologic intervention |
| `dietary` | Dietary intervention |
| `environmental` | Environmental modulation |

### EvidenceItemSupportEnum

| Value | Meaning |
|---|---|
| `SUPPORT` | Evidence directly supports the claim |
| `PARTIAL` | Evidence partially or indirectly supports |
| `REFUTE` | Evidence contradicts the claim |
| `NO_EVIDENCE` | Reference contains no relevant evidence |
| `WRONG_STATEMENT` | Claim contains a factual error |

### EvidenceSourceEnum

Classifies the study type in the cited publication — not how curation was performed.

| Value | Meaning |
|---|---|
| `HUMAN_CLINICAL` | Human patients, cohorts, case reports, clinical trials |
| `MODEL_ORGANISM` | In vivo animal data |
| `IN_VITRO` | Cell culture, organoids, biochemical assays |
| `COMPUTATIONAL` | In silico modeling, ML predictions, network inference |
| `OTHER` | Does not fit above categories |

### SourceTypeEnum

| Value | Meaning |
|---|---|
| `go_cam` | GO-CAM model (gomodel: CURIE) |
| `reactome` | Reactome pathway (R-HSA-* identifier) |
| `wikipathways` | WikiPathways pathway (WP* identifier) |
| `literature` | Primary literature (PMID reference) |
