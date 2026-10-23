# Schema Elements Associated with NAMs

The schema elements a New Approach Methodology touches, as three trees: the fields on a `ModelMechanismLink`, the four places such a link can live, and the places an `AssayDescriptor` can be attached.

First written 2026-10-13; updated 2026-10-23 to match `src/dismech/schema/dismech.yaml`.

```text
Disease
├── name                                         string
├── pathophysiology: [Pathophysiology]
│   ├── name ◄────────────────────────────────────────┐  string; the pathograph node
│   └── biological_scale                              │  BiologicalScaleEnum (optional)
│                                                     │  MOLECULAR | CELLULAR | TISSUE | ORGANISM
│                                                     │  compared against the link's model_scale
└── experimental_models: [ExperimentalModel]          │
    ├── name                                          │  string, identifier; the NAM
    ├── experimental_model_type                       │  ExperimentalModelTypeEnum (optional)
    │                                                 │  ORGANOID | ORGAN_ON_CHIP | CELL_LINE |
    │                                                 │  IPSC_DERIVED_MODEL | PRIMARY_CELL_CULTURE |
    │                                                 │  CO_CULTURE | OTHER
    ├── description                                   │  string
    ├── namo_type                                     │  uriorcurie; the NAMO class, e.g. namo:Organoid
    ├── organism                                      │  OrganismDescriptor; the species the cells came from
    ├── tissue_term                                   │  AnatomicalEntityDescriptor (UBERON)
    ├── cell_types: [CellTypeDescriptor]              │  CL
    ├── conditions: [string]                          │  conditions or disease states represented
    ├── cell_source                                   │  string; where the cells came from
    ├── culture_system                                │  string; culture format or device
    ├── publication                                   │  PMID
    ├── findings: [Finding]                           │  key findings from the source
    ├── evidence: [EvidenceItem]                      │  recommended; same fields as the link's evidence
    ├── notes                                         │  string
    └── modeled_mechanisms: [ModelMechanismLink]      │
        ├── target ───────────────────────────────────┤  string, required; = pathophysiology[].name
        ├── relationship                              │  ModelMechanismRelationshipEnum
        │                                             │  RECAPITULATES | PARTIALLY_RECAPITULATES |
        │                                             │  FAILS_TO_RECAPITULATE | PERTURBS | MEASURES | RESCUES
        ├── description                               │  string
        ├── fidelity                                  │  ModelFidelityEnum
        │                                             │  HIGH | MODERATE | LOW | UNKNOWN
        ├── limitations                               │  string; the translational caveat as prose
        ├── model_scale                               │  BiologicalScaleEnum; the scale the model OBSERVES
        ├── divergences: [ModelDivergence]            │
        │   ├── divergence_type                       │  ModelDivergenceTypeEnum, required
        │   │                                         │  BOUNDARY_OMISSION | PROXY_QUANTITY |
        │   │                                         │  CALIBRATION_PROVENANCE | CAUSE_UNREPRESENTED |
        │   │                                         │  STRUCTURAL_IDEALIZATION | TEMPORAL_SCOPE |
        │   │                                         │  CONTESTED_ASSUMPTION | SCALE_EXTRAPOLATION |
        │   │                                         │  SPECIES_MISMATCH | POPULATION_MISMATCH | OTHER
        │   ├── materiality                           │  ModelDivergenceMaterialityEnum
        │   │                                         │  INVALIDATING | QUALIFYING | IMMATERIAL | UNKNOWN
        │   ├── description                           │  string, required; says why it applies HERE
        │   └── evidence: [EvidenceItem]              │
        ├── readouts: [ExperimentalReadout]           │
        │   ├── name                                  │  string, required; the outcome measure
        │   ├── description                           │  string
        │   ├── target ───────────────────────────────┘  string, required; must repeat the link's target
        │   │                                            (checked by tests/test_data.py)
        │   ├── direction                                ModelReadoutDirectionEnum
        │   │                                            INCREASED | DECREASED | UNCHANGED |
        │   │                                            RESTORED | ABOLISHED | ALTERED
        │   │                                            or BiomarkerReadoutDirectionEnum
        │   │                                            POSITIVE | NEGATIVE | PRESENT_ABSENT |
        │   │                                            THRESHOLD_DEPENDENT
        │   ├── interpretation                           string
        │   ├── (phenotype_term | biomarker_term |       optional ontology grounding of the measure
        │   │    biological_processes | assays)          (HP / biomarker / GO / OBI);
        │   │                                            assays is [AssayDescriptor], see the third tree
        │   ├── notes                                    string
        │   └── evidence: [EvidenceItem]                 layer 2: "this measurement was made"
        └── evidence: [EvidenceItem]                     layer 1: "this model is informative for this node"
            ├── reference                                PMID / DOI / …
            ├── reference_title                          string (recommended)
            ├── supports                                 EvidenceItemSupportEnum
            │                                            SUPPORT | REFUTE | NO_EVIDENCE
            ├── evidence_source                          EvidenceSourceEnum (IN_VITRO for NAMs)
            ├── directness                               DirectnessEnum: DIRECT | INDIRECT | UNKNOWN
            ├── quote_role                               QuoteRoleEnum: PRIMARY_RESULT | BACKGROUND |
            │                                            REVIEW_SYNTHESIS
            ├── snippet                                  exact quote from the reference
            ├── explanation                              string
            └── images: [string]                         paths to supporting figures under research/
```

```text
Disease
├── pathophysiology: [Pathophysiology]
│   └── name ◄──────────────────────────────────────────────┐   the pathograph node
│                                                           │
├── experimental_models: [ExperimentalModel]   NAMs         │
│   ├── name                                                │
│   ├── experimental_model_type · namo_type                 │
│   ├── organism · cell_source · culture_system · cell_types · tissue_term
│   └── modeled_mechanisms: [ModelMechanismLink] ───────────┤
│                                                           │
├── animal_models: [AnimalModel]           whole organisms  │
│   ├── name                     (optional; recommended once linked)
│   ├── species · genotype · background · genes · alleles   │
│   ├── associated_phenotypes                               │
│   └── modeled_mechanisms: [ModelMechanismLink] ───────────┤
│                                                           │
├── computational_models: [ComputationalModel]   in silico  │
│   ├── name                                                │
│   ├── model_type     BOOLEAN_NETWORK | KINETIC | AGENT_BASED | FLUX_BALANCE_ANALYSIS |
│   │                  GENOME_SCALE_METABOLIC | PHYSIOLOGICAL | DIGITAL_TWIN | MACHINE_LEARNING |
│   │                  PERTURBATION_PREDICTION | FOUNDATION_MODEL | STRUCTURAL_PREDICTION |
│   │                  MOLECULAR_DOCKING | BIOMECHANICAL
│   ├── model_id · repository_url · base_model · model_software · model_format
│   ├── variables · perturbations · findings                │
│   └── modeled_mechanisms: [ModelMechanismLink] ───────────┤
│                                                           │
└── discussions: [Discussion]                               │
    └── proposed_experiments: [Experiment]                  │
        ├── model_systems: [ExperimentalModel]   4th home   │
        │   └── modeled_mechanisms: [ModelMechanismLink] ───┤
        ├── readouts: [ExperimentalReadout]                 │   the experiment's own outcome
        │                                                   │   measures, outside any link
        └── controls: [ExperimentalControl]                 │
            └── model_systems: [ExperimentalModel]          │
                └── modeled_mechanisms ─────────────────────┘
```

All three model classes also carry description · publication · evidence · notes;
experimental and computational models add findings.

ModelMechanismLink is the same class in every home:
  target · relationship · description · fidelity · limitations · model_scale ·
  divergences · readouts · evidence

## AssayDescriptor

`AssayDescriptor` names an assay: the technique used to make a measurement. It is
a leaf, never a pathograph node, and is reached only through the `assays:` slot.
Four classes carry that slot (`Pathophysiology`, `Biochemical`,
`ExperimentalReadout` and `Experiment`), which gives four routes from a
pathophysiology node to an assay. Each `(A)` below is an
`assays: [AssayDescriptor]` slot.

```text
Disease
├── pathophysiology: [Pathophysiology]
│   ├── name ◄────────────────────────────────────────────────┐  the pathograph node
│   ├── biological_scale · cell_types · biological_processes …│
│   └── assays: [AssayDescriptor] ─────────────────────► (A)  │  route 1: directly on the node
│                                                             │
├── biochemical: [Biochemical]                                │
│   ├── name · biomarker_term · loinc_term · reference_ranges │
│   ├── assays: [AssayDescriptor] ─────────────────────► (A)  │  route 2: the assay that measures the marker
│   └── readouts: [BiomarkerReadout]                          │
│       ├── target ───────────────────────────────────────────┤  bare name = pathophysiology[].name
│       └── relationship · direction · endpoint_context       │
│                                                             │
├── experimental_models | animal_models | computational_models│
│   └── modeled_mechanisms: [ModelMechanismLink]              │
│       ├── target ───────────────────────────────────────────┤  bare name
│       └── readouts: [ExperimentalReadout]                   │
│           ├── target ───────────────────────────────────────┤  must repeat the link's target
│           ├── phenotype_term | biomarker_term | biological_processes
│           └── assays: [AssayDescriptor] ─────────────► (A)  │  route 3: how a model's readout was measured
│                                                             │
└── discussions: [Discussion]                                 │
    ├── attaches_to ──────────────────────────────────────────┤  "pathophysiology#<name>"
    └── proposed_experiments: [Experiment]                    │
        ├── would_support / would_refute ─────────────────────┤  "pathophysiology#<name>"
        ├── assays: [AssayDescriptor] ─────────────────► (A)  │  route 4a: the experiment's assays
        ├── readouts: [ExperimentalReadout]                   │
        │   ├── target ───────────────────────────────────────┘  "pathophysiology#<name>"
        │   └── assays: [AssayDescriptor] ─────────────► (A)     route 4b: how this readout is measured
        └── model_systems: [ExperimentalModel]
            └── modeled_mechanisms → readouts → assays ─► (A)    route 3 again, inside a proposal

(A) AssayDescriptor   is_a Descriptor
    ├── preferred_term        string; the assay's name
    ├── description           string
    ├── term                  optional {id, label}
    │                         bound to the AssayTerm dynamic enum:
    │                         reachable_from OBI:0000070 "assay" (rdfs:subClassOf, indirect)
    └── modifier · located_in · laterality · spatial_extent · onset · temporality ·
        clinical_course · severity · qualifiers
                              inherited from Descriptor; rarely meaningful for an assay
```

The schema also defines a class named `Assay`, with only `name` and
`description`. No slot uses it as a range and no class inherits from it, so it
plays no part in the routes above; `AssayDescriptor` is the class that carries
assays.

The `target` slots on `BiomarkerReadout` and `ModelMechanismLink` take the node's
bare `name`; the slots under `discussions` take `pathophysiology#<name>`.

An assay and an experimental model record different things. A
`ModelMechanismLink` names a model system and states how it relates to the node
(relationship, fidelity, caveats, evidence). An assay names a measurement
technique and makes no claim about the node. The two meet at route 3: "this
model shows X at this node, measured by assay Y".

Use in `kb/`, counted 2026-10-23:

| Route | Slot path | Objects | Files | Assay entries | With an OBI `term:` |
|---|---|---|---|---|---|
| 4b | `discussions[].proposed_experiments[].readouts[].assays` | 301 | 82 | 534 | 0 |
| 4a | `discussions[].proposed_experiments[].assays` | 17 | 6 | 60 | 0 |
| 2 | `biochemical[].assays` | 6 | 4 | 7 | 0 |
| 1 | `pathophysiology[].assays` | 1 | 1 | 2 | 0 |
| 3 | model-link `readouts[].assays` | 0 | 0 | 0 | 0 |

- Nearly all assays describe how a proposed experiment would measure something.
  Route 3, which would record how a curated model's readout was measured, is
  unused.
- No assay is bound to an OBI term. OBI has no adapter in
  `conf/oak_config.yaml` and no `cache/enums/` membership file, so a binding
  cannot be validated yet. Ground a readout with GO `biological_processes` in
  the meantime.
- The global `assays` slot has no description, and its only example value,
  `Elevated Blood Glucose`, is a result rather than an assay. The one
  pathophysiology node using route 1, `Hyperglycemia` in
  `kb/disorders/Type_I_Diabetes.yaml`, follows that example; its two values
  duplicate markers the entry already lists under `biochemical:`.
