# Schema Elements Associated with NAMs

The schema elements a New Approach Methodology touches, as two trees: the fields on a `ModelMechanismLink`, and the four places such a link can live.

First written 2026-10-13; updated 2026-10-22 to match `src/dismech/schema/dismech.yaml`.

```text
Disease
├── name                                         string
├── pathophysiology: [Pathophysiology]
│   ├── name ◄────────────────────────────────────────┐  string; the pathograph node
│   └── biological_scale                              │  BiologicalScaleEnum (optional)
│                                                     │  MOLECULAR | CELLULAR | TISSUE | ORGANISM
│                                                     │  compared against the link's model_scale
└── experimental_models: [ExperimentalModel]          │
    ├── name                                          │  string, required; the NAM
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
        │   │    biological_processes | assays)          (HP / biomarker / GO / OBI)
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
            └── explanation                              string
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
