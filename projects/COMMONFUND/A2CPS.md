# Acute to Chronic Pain Signatures (A2CPS)

Reviewed: 2026-05-29

## Why This Is Mechanistically Valuable

A2CPS is useful because it captures the transition from an acute pain event to
chronic pain using longitudinal multimodal data. The mechanism is not simply
"pain present"; it is a time-resolved state transition involving nociceptor
activity, neuroimmune signaling, central sensitization, descending modulation,
functional impairment, and psychosocial context.

The A2CPS public data documentation describes patient-reported outcomes,
functional testing, multiple omics panels, brain imaging, and quantitative
sensory testing. The Common Fund page frames the program around objective
biomarker signatures that predict transition to chronic pain or resilience
after acute pain.

## Dismech Interpretation Pattern

Use A2CPS to convert longitudinal measurements into mechanism-stage evidence:

`surgery or injury -> peripheral nociceptive input -> neuroimmune amplification
or sensitization -> altered central pain processing -> persistent pain,
movement limitation, and fatigue`

The most important curation distinction is time: baseline risk, early acute
post-event change, transition trajectory, and chronic outcome should not be
collapsed into a single static biomarker claim.

## Concrete Implementation Plan

**Mode:** teach dismech first, benchmark later. Current external A2CPS release
materials are most useful for teaching dismech how to represent an
acute-to-chronic transition study. They are not yet enough to benchmark
prediction of chronic pain outcomes because the public release page states that
only baseline data are currently available and no post-baseline data will be
externally released before study conclusion and primary publications.

**Required datasets and access path:**

- Use the A2CPS researcher pages as the open documentation source:
  https://a2cps.org/researchers/data-releases/,
  https://a2cps.org/researchers/data-releases/about-the-data/, and
  https://a2cps.org/researchers/accessing-our-data/.
- Request controlled access through the NIMH Data Archive (NDA). A2CPS is listed
  there as "Data Center for Acute to Chronic Pain Biosignatures", project #5121;
  access requires NIH Research Auth Service login and a Data Access Request for
  the NDA permission group.
- Treat release 1.0.0 as baseline-only: demographics, psychosocial PROs,
  functional testing, QST, and brain imaging. The A2CPS documentation states
  that release 1.0.0 does not include omics or EHR data; future releases are
  expected to add plasma proteomics, lipidomics, metabolomics, exRNA, SNP array
  genotype/imputation, and EHR-derived surgical variables.
- Cohorts to track separately: total knee arthroplasty and thoracic surgery.
  Do not merge them until the surgery-type variable is explicitly modeled.

**Tools and environment:**

- NDA web portal and NDA data download tooling for controlled data; no
  patient-level files should be committed to this repo.
- Python/R environment with `pandas`, `pyarrow`, `statsmodels`,
  `scikit-learn`, and, for imaging-derived summaries, `nilearn` or `bids`
  tooling if NDA releases BIDS-like MRI derivatives.
- A local mapping table from A2CPS CRF/CDE variables to dismech concepts:
  HPO pain phenotypes where defensible, UBERON tissue/procedure context, and
  unforced free-text findings where no ontology mapping is exact.

**Curation targets:**

- Create `kb/modules/acute_to_chronic_pain_transition.yaml` with nodes for
  acute tissue injury, peripheral sensitization, QST hyperalgesia/allodynia,
  neuroimmune amplification, altered brain pain-network activity, descending
  modulation dysfunction, functional impairment, and persistent pain phenotype.
- Update `Fibromyalgia` as the chronic-pain convergence benchmark and
  `Osteoarthritis` as the TKA pain-persistence use case.
- Add focused candidate nodes to `Endometriosis`, `Sickle_Cell_Disease`, and
  `Chronic_Pancreatitis` only when the cited literature supports transition
  from recurrent nociceptive input to central sensitization.

**Code to write:**

- Add `src/dismech/commonfund/a2cps.py` to parse the public CRF/CDE data
  dictionaries into a `projects/COMMONFUND/generated/a2cps_variable_map.tsv`
  artifact, excluding patient-level data.
- Add a small report command that flags which A2CPS variables can map cleanly
  to existing dismech slots and which require schema work. Likely schema gaps:
  `IMAGING`, `QST`, `PRO`, `EHR`, and `LIPIDOMICS` dataset types.
- Add tests that assert no controlled-access records, subject IDs, or raw values
  are written under `kb/` or `projects/`.

**Graduate-student first pass:**

1. Read the A2CPS release and About the Data pages, then make a spreadsheet of
   variables grouped as PRO, QST, functional testing, imaging, omics, and EHR.
2. For 20 high-value variables, decide whether each is a phenotype, a mechanism
   readout, a confounder, or a dataset-level covariate.
3. Draft the pain-transition module from public documentation and literature
   first; add A2CPS dataset references only after stable NDA accessions and
   release versions are selected.

## Dismech Disease and Mechanism Exemplars

| Disease | Current or candidate mechanism | How A2CPS helps |
|---------|--------------------------------|-----------------|
| `Fibromyalgia` | Curated nodes: `Central Sensitization`, `Descending Pain Modulation Dysfunction`, `Neuroinflammation`, `Small Fiber Pathology`, `HPA Axis Dysregulation` | Use as the canonical chronic-pain mechanism graph. A2CPS can test whether post-surgical transition signatures converge on these curated mechanisms. |
| `Osteoarthritis` | Curated nodes: `Cartilage Matrix Catabolism`, `Chondrocyte Senescence`, `Synovial Macrophage-Fibroblast Crosstalk`, `Subchondral Bone Remodeling`; phenotype `Joint Pain` | A2CPS total-knee-arthroplasty data can separate structural joint mechanisms from central pain persistence after tissue repair. |
| `Chronic_Pancreatitis` | Curated nodes: `Recurrent Acinar Cell Injury`, `Pancreatic Fibrosis`, `Chronic Abdominal Pain` | A2CPS methods can inform chronic visceral pain curation even if the source cohort is surgical pain rather than pancreatitis. |
| `Endometriosis` | Curated nodes: `Ectopic Endometrial Tissue`, `Chronic Inflammation`, `Hypoxia and Angiogenesis`, phenotype `Pelvic Pain` | Candidate addition: lesion inflammation -> peripheral sensitization -> central sensitization -> chronic pelvic pain. |
| `Congenital_Insensitivity_to_Pain` | Curated nodes: `Impaired nociceptor specification`, `NGF-TRKA trophic signaling failure`, `Nav1.7 loss-of-function channelopathy`, `Loss of protective pain perception` | Mechanistic contrast case: A2CPS studies chronic pain transition; this entry anchors the opposite causal direction, failed nociception. |
| `Sickle_Cell_Disease` | Curated nodes: `Hemoglobin Polymerization`, `Red Blood Cell Sickling`, `Vaso-Occlusion`, phenotype `Pain Crises` | Candidate addition: recurrent vaso-occlusive nociceptive input -> central sensitization and chronic pain phenotype. |
| Yet to curate: post-surgical chronic pain | Candidate mechanisms: acute tissue injury -> QST hyperalgesia -> altered brain network activity -> persistent pain | A2CPS itself can motivate a mechanism module for transition from acute to chronic pain. |

## High-Value Curation Work

- Create a reusable `acute_to_chronic_pain_transition` module with nodes for
  peripheral sensitization, central sensitization, descending modulation
  dysfunction, neuroimmune amplification, and persistent pain phenotype.
- Add `datasets` to `Fibromyalgia` and `Osteoarthritis` that point to A2CPS
  data releases or portal records once stable accession-level references are
  selected.
- Add pain-transition annotations to disease entries where pain is currently a
  phenotype but not a mechanism, especially `Endometriosis`,
  `Sickle_Cell_Disease`, and `Chronic_Pancreatitis`.
- Map A2CPS quantitative sensory testing and functional measures to HPO terms
  only when the mapping is clinically defensible; otherwise record them as
  dataset findings rather than forced phenotype terms.

## Fit for RFA-RM-26-017

Best partner datasets:

- A2CPS + MoTrPAC: pain transition and exercise-responsive molecular recovery.
- A2CPS + SPARC: pain circuits and peripheral neuromodulation mechanisms.
- A2CPS + LINCS: perturbation signatures for neuroinflammatory or nociceptive
  drug candidates.
- A2CPS + Metabolomics Workbench: metabolite predictors of transition or
  resilience.

## Sources

- NIH Common Fund A2CPS: https://commonfund.nih.gov/pain
- A2CPS data releases: https://a2cps.org/researchers/data-releases/
- A2CPS About the Data: https://a2cps.org/researchers/data-releases/about-the-data/
- A2CPS data access: https://a2cps.org/researchers/accessing-our-data/
- A2CPS study details: https://a2cps.org/researchers/a2cps-study-details/
