# Schema Elements Associated with NAMs

The schema elements a New Approach Methodology touches, as two trees: the fields on a `ModelMechanismLink` and the four places such a link can live. Written 2026-10-13.

```text
Disease
├── name                                         string
├── pathophysiology: [Pathophysiology]
│   ├── name ◄────────────────────────────────────────┐  string; the pathograph node
│   └── biological_scale                              │  BiologicalScaleEnum (optional)
│                                                     │  MOLECULAR | CELLULAR | TISSUE | ORGANISM
│                                                     │  compared against the link's model_scale
└── experimental_models: [ExperimentalModel]          │
    ├── name                                          │  string; the NAM
    └── modeled_mechanisms: [ModelMechanismLink]      │
        ├── target ───────────────────────────────────┤  string, required; = pathophysiology[].name
        ├── relationship                              │  ModelMechanismRelationshipEnum
        │                                             │  RECAPITULATES | PARTIALLY_RECAPITULATES |
        │                                             │  FAILS_TO_RECAPITULATE | PERTURBS | MEASURES | RESCUES
        ├── fidelity                                  │  ModelFidelityEnum
        │                                             │  HIGH | MODERATE | LOW | UNKNOWN
        ├── limitations                               │  string; the translational caveat as prose
        ├── model_scale                               │  BiologicalScaleEnum; the scale the model OBSERVES
        ├── divergences: [ModelDivergence]            │
        │   ├── divergence_type                       │  ModelDivergenceTypeEnum
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
        │   ├── name                                  │  string; the outcome measure
        │   ├── target ───────────────────────────────┘  string, required; must repeat the link's target
        │   ├── direction                                ModelReadoutDirectionEnum
        │   │                                            INCREASED | DECREASED | UNCHANGED |
        │   │                                            RESTORED | ABOLISHED | ALTERED
        │   ├── interpretation                           string
        │   ├── (phenotype_term | biomarker_term |       optional ontology grounding of the measure
        │   │    biological_processes | assays)          (HP / biomarker / GO / OBI)
        │   └── evidence: [EvidenceItem]                 layer 2: "this measurement was made"
        └── evidence: [EvidenceItem]                     layer 1: "this model is informative for this node"
            ├── reference                                PMID / DOI / …
            ├── supports                                 EvidenceItemSupportEnum
            │                                            SUPPORT | REFUTE | NO_EVIDENCE
            ├── evidence_source                          EvidenceSourceEnum (IN_VITRO for NAMs)
            ├── snippet                                  exact quote from the reference
            └── explanation                              string
```

```text
Disease
├── pathophysiology: [Pathophysiology]
│   └── name ◄──────────────────────────────────────────────┐   the pathograph node
│                                                           │
├── experimental_models: [ExperimentalModel]   NAMs         │   600 entries use it
│   ├── name                                                │
│   ├── experimental_model_type   ORGANOID | ORGAN_ON_CHIP | IPSC_DERIVED_MODEL |
│   │                             CELL_LINE | PRIMARY_CELL_CULTURE | CO_CULTURE | …
│   ├── namo_type · cell_source · culture_system · cell_types · tissue_term
│   └── modeled_mechanisms: [ModelMechanismLink] ───────────┤
│                                                           │
├── animal_models: [AnimalModel]           whole organisms  │   1,206 entries use it
│   ├── name                     (optional; recommended once linked)
│   ├── species · genotype · background · genes · alleles   │
│   ├── associated_phenotypes                               │
│   └── modeled_mechanisms: [ModelMechanismLink] ───────────┤
│                                                           │
├── computational_models: [ComputationalModel]   in silico  │   56 entries use it
│   ├── name                                                │
│   ├── model_type     BOOLEAN_NETWORK | KINETIC | AGENT_BASED | FLUX_BALANCE_ANALYSIS |
│   │                  GENOME_SCALE_METABOLIC | PHYSIOLOGICAL | DIGITAL_TWIN | MACHINE_LEARNING |
│   │                  PERTURBATION_PREDICTION | FOUNDATION_MODEL | STRUCTURAL_PREDICTION |
│   │                  MOLECULAR_DOCKING | BIOMECHANICAL
│   ├── model_id · repository_url · model_format · variables · perturbations · findings
│   └── modeled_mechanisms: [ModelMechanismLink] ───────────┤
│                                                           │
└── discussions: [Discussion]                               │
    └── proposed_experiments: [Experiment]                  │
        ├── model_systems: [ExperimentalModel]   4th home   │
        │   └── modeled_mechanisms: [ModelMechanismLink] ───┤
        └── controls: [ExperimentalControl]                 │
            └── model_systems: [ExperimentalModel]          │
                └── modeled_mechanisms ─────────────────────┘
```

ModelMechanismLink is the same class in every home:
  target · relationship · fidelity · limitations · model_scale ·
  divergences · readouts · evidence
