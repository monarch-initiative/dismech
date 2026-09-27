# Computational-model curation backlog (2026-08-22)

## Executive summary

The raw absence count is not a useful work queue. On the `main` snapshot used
for this audit, the knowledge base contains 2,140 disorder files:

- 17 have one or more curated `computational_models` entries;
- 6 explicitly carry `computational_models: []`;
- 2,117 have no `computational_models` field.

The resumed curation series has eleven open, one-disorder PRs. If all merge,
28 disorders will have populated computational-model sections and 2,106 will
still have no field. Most of those 2,106 are rare disorders for which no
disease-level computational model is expected. They should not be converted
mechanically to empty lists.

The useful remaining queue is therefore the ranked, evidence-led set below.
It favors models that illuminate a named pathophysiology node, prioritizes
recent patient-specific digital twins, and prefers runnable public deposits.
It deliberately includes several model classes rather than turning the section
into an index of diagnostic machine-learning classifiers.

This report complements the execution-focused
[Computational Model Execution: State of the Art](computational-model-execution-landscape-2026-08-01.md).

## Work already in flight

| PR | Disorder | Distinctive model class |
|---|---|---|
| [#9084](https://github.com/monarch-initiative/dismech/pull/9084) | Glioblastoma, IDH-wildtype | reaction-diffusion and data-assimilation twins; multiscale ABM/RL |
| [#9087](https://github.com/monarch-initiative/dismech/pull/9087) | Advanced sleep phase syndrome | circadian ODE and physiological phase estimator |
| [#9091](https://github.com/monarch-initiative/dismech/pull/9091) | Multiple sclerosis | computational disease models |
| [#9104](https://github.com/monarch-initiative/dismech/pull/9104) | Hyperinsulinemic hypoglycemia | glucose-insulin physiology |
| [#9119](https://github.com/monarch-initiative/dismech/pull/9119) | Noonan syndrome | allele-specific signaling models |
| [#9122](https://github.com/monarch-initiative/dismech/pull/9122) | Ataxia-telangiectasia | DNA-damage/signaling models |
| [#9123](https://github.com/monarch-initiative/dismech/pull/9123) | Brugada syndrome | cardiac electrophysiology |
| [#9140](https://github.com/monarch-initiative/dismech/pull/9140) | Renal cell carcinoma | agent-based tumor model |
| [#9142](https://github.com/monarch-initiative/dismech/pull/9142) | Hepatitis C | within-host viral dynamics |
| [#9145](https://github.com/monarch-initiative/dismech/pull/9145) | Chronic myeloid leukemia | ecological ODE / treatment-response ensemble |
| [#9263](https://github.com/monarch-initiative/dismech/pull/9263) | Alzheimer disease | EEG-personalized brain digital twin |

Operational state is deliberately kept out of the table because it changes
faster than this report. As of 2026-08-22 19:11 UTC, nine approved PRs (#9087
through #9145 above) were marked ready for review and were conflict-free. #9084
remained a draft while its requested review fix was being completed; #9263 was
also awaiting re-review after requested changes.
Approved, ready, unassigned PRs become eligible for the repository's
deterministic auto-merge sweep after its three-day cooling period; drafts are
never eligible. Current state should be read from the linked PRs.

## Tier 1: curate next

These have a strong disease/model fit and a credible path to mechanistic,
repository-backed curation. Order within the tier is a judgment call.

| Priority | Disorder file | Model lead and intended value | Principal guardrail |
|---:|---|---|---|
| 1 | `Epilepsy.yaml` | Virtual Epileptic Patient / The Virtual Brain patient-specific seizure-network models; connect excitability and propagation parameters to the epilepsy mechanism chain | Separate a genuine patient-specific mechanistic twin from generic seizure classifiers |
| 2 | `Heart_Failure.yaml` | Med-Real2Sim and CircAdapt-style inverse hemodynamic twins; include pressure, flow, and contractility readouts | Confirm that the evaluated disease cohort is heart failure, not only healthy cardiac geometry |
| 3 | `Tuberculosis.yaml` | UISS-TB and other immune agent-based models with executable intervention simulations | Do not promote regulatory qualification or platform claims into clinical efficacy claims |
| 4 | `Asthma.yaml` | airway smooth-muscle, bronchoconstriction, and immune/airway multiscale models | Prefer mechanistic airway models over risk-prediction ML; verify any claimed asthma digital twin is more than a proposal |
| 5 | `Cystic_Fibrosis.yaml` | CFTR/airway-surface-liquid ion-transport ODEs and mucus-clearance models | Keep epithelial transport models distinct from organoid or animal models |
| 6 | `Chronic_Obstructive_Pulmonary_Disease.yaml` | patient-specific ventilation, airway-network, and emphysema mechanics models | Link to an actual COPD mechanism node; generic lung simulators alone are insufficient |
| 7 | `Sickle_Cell_Disease.yaml` | multiscale red-cell sickling, adhesion, and microvascular-flow simulations | State oxygenation, rheology, and vessel-geometry assumptions; avoid treating in-vitro calibration as clinical validation |
| 8 | `Duchenne_Muscular_Dystrophy.yaml` | calcium handling, energetics, and finite-element muscle mechanics models | Do not misclassify iPSC or mouse muscle systems as computational models |
| 9 | `Prostate_Adenocarcinoma.yaml` | patient-specific treatment-response and executable PI3K/AKT/mTOR/AR resistance models | Coordinate with the existing phenotype algorithm and mTOR-resistance conformance rather than duplicating them |
| 10 | `Non-Small_Cell_Lung_Cancer.yaml` | tumor-growth and immune-checkpoint treatment twins; executable Boolean/agent-based alternatives | Require subtype/cohort identity and a direct pathograph join point |
| 11 | `COVID-19.yaml` | within-host viral/immune ODE, QSP, and multiscale intervention models | Prefer models with parameter identifiability and external validation; avoid undifferentiated pandemic forecasting |
| 12 | `Chronic_Kidney_Disease.yaml` | nephron/hemodynamic and fibrosis/QSP models that complement, rather than repeat, the CKD-MBD exemplar | Keep CKD progression separate from the already-curated mineral-bone subsystem |

## Tier 2: strong candidates after focused literature and repository checks

| Disorder file | Candidate model family | Why it is second tier |
|---|---|---|
| `Amyotrophic_Lateral_Sclerosis.yaml` | motor-neuron excitability, protein-aggregation, and progression models | Many models are mutation- or subsystem-specific; the disease-level join point needs careful scoping |
| `Dilated_Cardiomyopathy.yaml` | patient-specific electromechanics and ventricular-remodeling twins | Repositories often supply generic cardiac infrastructure but not the disease parameterization |
| `Hypertrophic_Cardiomyopathy.yaml` | sarcomere-to-organ electromechanics and sudden-death risk twins | Separate mechanistic simulation from morphology/risk classifiers |
| `Essential_Hypertension.yaml` | closed-loop circulation and renal-pressure control models | Broad physiological models can be relevant without being disease-specific |
| `Osteoarthritis.yaml` | cartilage finite-element, mechanobiology, and cell-based degradation models | Public code and model-to-node evidence are uneven |
| `Rheumatoid_Arthritis.yaml` | immune QSP and synovial agent-based treatment models | Many deposits are proprietary or treatment-development platforms |
| `ER_Positive_Breast_Cancer.yaml` | endocrine-resistance Boolean/QSP and patient-specific response models | Curate the molecular subtype, not generic breast-cancer prediction |
| `HER2_Positive_Breast_Cancer.yaml` | HER2 signaling and combination-treatment models | Check that repositories preserve the exact published parameterization |
| `Triple_Negative_Breast_Cancer.yaml` | executable signaling networks and tumor-immune ABMs | High volume of ML papers, low fraction of interpretable mechanism models |
| `Metastatic_Colorectal_Cancer.yaml` | liver-metastasis growth/therapy twins and agent-based models | Primary and metastatic disease are often conflated in search results |
| `Acquired_Immunodeficiency_Syndrome.yaml` | classic within-host HIV dynamics and treatment models | Strong literature, but repository and modern reproducibility metadata need work |
| `Major_Depressive_Disorder.yaml` | neural-circuit and treatment-response models | Most available work is predictive ML; accept only models with a defensible mechanism link |
| `Schizophrenia.yaml` | cortical excitation/inhibition and dysconnection models | Heterogeneity makes disease-level fidelity claims particularly fragile |

## Explicit empty sections

The following six entries on `main` explicitly declare
`computational_models: []`:

- `ATTR_Amyloidosis.yaml`
- `Alsahan-Harris_Syndrome.yaml`
- `Aminoacylase_1_Deficiency.yaml`
- `Amyloidosis.yaml`
- `Anterior_Spinal_Artery_Syndrome.yaml`
- `BEST1-Related_Dominant_Retinopathy.yaml`

Treat these as "reviewed but no model curated," not as evidence that no model
can exist. Reopen one only when a concrete paper or repository lead appears.
The broad `Amyloidosis.yaml` entry is especially prone to subtype conflation;
a subtype-specific model belongs on the corresponding subtype entry.

## Defer and skip rules

A disorder can remain without `computational_models` when any of the following
applies:

1. No disease-specific or mechanism-specific computational model was found.
2. The only results are diagnostic/prognostic classifiers that do not illuminate
   a curated pathophysiology node.
3. A paper proposes a future digital twin but does not instantiate or evaluate one.
4. The system is an organoid, cell line, organ-chip, or animal model and therefore
   belongs under `experimental_models` or `animal_models`.
5. A generic platform is not parameterized or evaluated for the disorder.
6. Disease identity is ambiguous or a paper actually concerns a sibling subtype.
7. The source is too poorly specified to support honest provenance, limitations,
   or a model-to-mechanism link.

An inaccessible repository is not automatically disqualifying: a paper-only
model may still be curated when its equations, variables, findings, and limits
are recoverable. Conversely, a GitHub repository is not automatically relevant.

## Per-disorder completion standard

Each future PR should modify one disorder file and should, where the source
permits:

- classify the model type accurately;
- pin a repository commit or stable accession;
- record software, format, and license/reproducibility caveats;
- connect the model to exact pathophysiology or phenotype names through
  `modeled_mechanisms`;
- distinguish link-level evidence from readout-level evidence;
- represent negative results and fidelity limitations explicitly;
- run the deposited model or at least a bounded smoke test when feasible;
- use deep-research/OpenScientist output only as a lead, after disease-identity
  and reference verification;
- add a history record and regenerate `app/models/data.js` with
  `just gen-models-data` (or `uv run python -m dismech.export.models_export`).

## Reproducing the census

The snapshot counts use only top-level fields on `origin/main`:

```bash
git ls-tree -r --name-only origin/main -- kb/disorders/ | grep -c '\.yaml$'
git grep -l '^computational_models:' origin/main -- 'kb/disorders/*.yaml'
```

The second command identifies 23 files. Inspection of those fields separates
17 populated sections from 6 explicit empty lists. Open PRs were then audited
individually rather than counted from branch names.
