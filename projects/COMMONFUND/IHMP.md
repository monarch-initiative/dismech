# Integrated Human Microbiome Project (iHMP)

Reviewed: 2026-05-29

## Why This Is Mechanistically Valuable

iHMP is more mechanistic than static microbiome catalogs because it collected
longitudinal host and microbiome multiomics for microbiome-associated
conditions. The HMP DACC page describes integrated longitudinal datasets from
three cohort studies using multiple omics technologies, including pregnancy and
preterm birth, inflammatory bowel disease, and prediabetes. PubMed/NIH
summaries describe the three dynamic conditions as pregnancy/preterm birth,
IBD, and stressors affecting individuals with prediabetes.

For dismech, iHMP is a direct time-series source for trigger, amplifier,
effector, and consequence nodes.

## Dismech Interpretation Pattern

Use iHMP to model transitions:

`baseline host-microbiome state -> perturbation or stressor -> microbial,
transcriptomic, proteomic, or metabolomic change -> host barrier, immune, or
metabolic process -> clinical transition`

The key is to preserve ordering and dynamics rather than flattening iHMP into a
single case-control biomarker list.

## Concrete Implementation Plan

**Mode:** teach transition mechanisms and benchmark temporal reasoning. iHMP is
the microbiome program best suited to teaching dismech that disease mechanisms
change over time.

**Required datasets and access path:**

- Use the iHMP DACC page: https://www.hmpdacc.org/ihmp/.
- Treat the three iHMP projects as separate data sources:
  IBDMDB for inflammatory bowel disease, MOMS-PI for pregnancy/preterm birth,
  and IPOP for prediabetes/stressor-associated transition.
- Use HMPDACC and project-specific portals where available. The iHMP marker
  publication reports raw and processed data via IBDMDB, the HMP2 DCC, and
  project manuscripts; the DACC links public data and controlled-access data
  according to IRB permissions.
- Track each file by modality: metagenome, metatranscriptome, metabolome,
  metaproteome, host transcriptome, host genetics/epigenome, cytokines,
  serology, and clinical timepoint.

**Tools and environment:**

- HUMAnN/MetaPhlAn, QIIME2 where needed, plus R/Python longitudinal modeling
  (`lme4`, `brms`, `statsmodels`, or `lifelines` depending on outcome).
- Multi-omics table integration with `pandas`, `duckdb`, and explicit
  timepoint metadata. Do not combine modalities until sample/timepoint keys are
  checked.
- For IBD, start with processed IBDMDB profiles rather than raw reads.

**Curation targets:**

- `Crohn_Disease` and `Ulcerative_Colitis`: flare/remission, microbial
  function, barrier injury, cytokine activity, and metabolite transitions.
- `Pouchitis`: use iHMP as a method/template unless a pouch-specific dataset is
  selected.
- `Type_2_Diabetes_Mellitus`: IPOP/prediabetes stressor data for
  preclinical insulin resistance, inflammatory, microbiome, and metabolite
  shifts.
- New candidate entry or module: preterm birth transition, after deciding how
  dismech should represent pregnancy outcomes.

**Code to write:**

- Add `src/dismech/commonfund/ihmp.py` to normalize iHMP project metadata into
  longitudinal manifests: participant/timepoint id placeholder, condition,
  visit, modality, body site, public/protected status, and project URL.
- Add `scripts/ihmp_transition_to_module.py` to convert curated time-resolved
  findings into draft mechanism chains with temporal qualifiers.
- Add schema-review notes for longitudinal timepoints, flare/remission state,
  and multi-omics sample linkage.

**Graduate-student first pass:**

1. Start with IBDMDB, choose Crohn disease or ulcerative colitis, and list all
   available processed modalities and timepoint fields.
2. Pick one mechanism chain, such as loss of SCFA producers -> decreased
   butyrate -> impaired colonocyte energy metabolism -> epithelial injury.
3. For each edge, record whether iHMP provides temporal support, correlation
   only, or requires independent experimental evidence.

## Dismech Disease and Mechanism Exemplars

| Disease | Current or candidate mechanism | How iHMP helps |
|---------|--------------------------------|----------------|
| `Crohn_Disease` | Curated nodes: `Microbiome Imbalance`, `Paneth Cell Autophagy Impairment`, `Antimicrobial Defense Deficiency`, `Intestinal Barrier Dysfunction`, `Macrophage Autophagy Dysfunction`, `IL-23/Th17 Axis Dysregulation` | iHMP IBDMDB can support longitudinal dysbiosis and host-response trajectories in flare, remission, and barrier injury. |
| `Ulcerative_Colitis` | Curated nodes: `Loss of Microbial Diversity`, `Loss of Keystone SCFA Producers`, `Decreased Butyrate Production`, `Impaired Colonocyte Energy Metabolism`, `NLRP3 Inflammasome-Mediated Pyroptosis` | Ideal use case for microbe -> metabolite -> colonocyte metabolism -> inflammation curation. |
| `Pouchitis` | Curated nodes: `Bacterial Dysbiosis`, `Mucosal Immune Dysregulation`, `Epithelial Barrier Dysfunction`, `NOD2 Genetic Susceptibility` | iHMP methods can guide time-resolved pouch dysbiosis and immune activation curation. |
| `Type_2_Diabetes_Mellitus` | Curated nodes: `Insulin Resistance`, `Beta Cell Dysfunction`, `Hepatic Glucose Overproduction`, `Mitochondrial Dysfunction and Oxidative Stress` | iHMP prediabetes/IPOP data can represent stressor-driven host-microbiome-metabolome transitions before overt diabetes. |
| `Preeclampsia` | Curated nodes: `Defective Trophoblast Invasion and Spiral Artery Remodeling`, `Placental Anti-Angiogenic Factor Release`, `Maternal Endothelial Dysfunction` | Candidate extension from pregnancy/preterm birth data: vaginal/maternal microbiome state -> inflammation or angiogenic imbalance -> pregnancy outcome. |
| Yet to curate: preterm birth | Candidate mechanisms: vaginal microbiome shift -> ascending inflammation -> membrane/placental inflammation -> preterm labor | iHMP pregnancy data can motivate a new dismech entry or module. |

## High-Value Curation Work

- Add iHMP-backed datasets to `Crohn_Disease`, `Ulcerative_Colitis`,
  `Pouchitis`, and `Type_2_Diabetes_Mellitus`.
- Add temporal qualifiers in notes or dataset findings: baseline, flare,
  remission, stressor, preclinical, transition, and outcome.
- For IBD entries, connect iHMP findings to the existing
  `intestinal_barrier_dysfunction` module and the current microbiome metabolic
  computational models already present in `Crohn_Disease` and
  `Ulcerative_Colitis`.
- Decide whether preterm birth should be a new disease/condition entry or a
  pregnancy-outcome project note before adding curation.

## Fit for RFA-RM-26-017

Best partner datasets:

- iHMP + HMP: longitudinal disease data plus healthy reference.
- iHMP + Metabolomics Workbench: metabolite mechanism validation.
- iHMP + exRNA: host biofluid RNA signals during microbiome transitions.
- iHMP + HuBMAP: mucosal tissue localization of host response.

## Sources

- iHMP DACC: https://www.hmpdacc.org/ihmp/
- IBDMDB: https://ibdmdb.org/
- iHMP data model: https://www.hmpdacc.org/ihmp/overview/data-model/
- NIH HMP/iHMP news release: https://www.nih.gov/news-events/news-releases/human-microbiome-project-expands-toolbox-studying-host-microbiome-interactions
- iHMP overview publication: https://pubmed.ncbi.nlm.nih.gov/31142853/
