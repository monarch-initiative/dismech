# Molecular Transducers of Physical Activity in Humans (MoTrPAC)

Reviewed: 2026-05-29

## Why This Is Mechanistically Valuable

MoTrPAC is valuable because exercise is a reproducible physiological
perturbation with broad disease relevance. The Common Fund describes MoTrPAC as
an effort to uncover, at the molecular level, how exercise improves and
maintains tissue and organ health. The program profiles molecular changes over
time in human tissues and uses animal studies to cover many additional tissues.

For dismech, MoTrPAC can convert exercise from a generic lifestyle treatment
into mechanism-specific evidence: which molecular transducers change, in which
tissue, after which exercise modality, and how those changes map to disease
nodes.

## Dismech Interpretation Pattern

Use MoTrPAC as an exercise perturbation atlas:

`exercise modality, dose, and time point -> molecular transducer in tissue ->
cellular adaptation -> disease mechanism node -> phenotype, biomarker, or
treatment response`

Human data should anchor clinical relevance; rat multi-tissue data should be
used for mechanism generation and cross-tissue inference, with species caveats.

## Concrete Implementation Plan

**Mode:** teach treatment-mechanism curation and benchmark perturbation
generalization. MoTrPAC can be used alone for the NOFO, so it is the best
single-program pilot for turning an intervention into dismech mechanism edits.

**Required datasets and access path:**

- Use the MoTrPAC Data Hub: https://motrpac-data.org/ and consortium site:
  https://www.motrpac.org/.
- Use Data Hub browse/download pages to select release, organism, tissue,
  exercise modality, timepoint, omics assay, and file type. Record the exact
  release and access status for every dataset.
- Treat rat endurance-training and acute-exercise multi-tissue data as
  mechanism-generation data with species caveats. Treat human blood, skeletal
  muscle, and adipose tissue data as the clinical anchor when available.
- Use MoTrPAC protocols from the consortium site to record exercise modality,
  dose, training duration, age, sex, and biospecimen timing.

**Tools and environment:**

- Python/R multi-omics environment: `pandas`, `duckdb`, `scanpy` or
  Bioconductor as needed, pathway enrichment, and time-series modeling.
- Tissue/modality-specific tools for RNA-seq, proteomics, metabolomics, or
  epigenomics only after a narrow pilot is chosen.
- Disease mapping through dismech treatment entries: exercise modality ->
  molecular transducer -> mechanism node -> expected phenotype change.

**Curation targets:**

- `Type_2_Diabetes_Mellitus` and `Obesity`: insulin resistance, mitochondrial
  function, adipose inflammation, hepatic glucose, and metabolic flexibility.
- `Coronary_Artery_Disease` and `Heart_Failure`: endothelial function,
  inflammation, cardiac stress, skeletal-muscle conditioning, and lipid biology.
- `Postural_Orthostatic_Tachycardia_Syndrome`: exercise training as a direct
  treatment mechanism for cardiovascular deconditioning and reduced preload.
- `Osteoarthritis`, `Fibromyalgia`, and `Parkinsons_Disease`: use cautiously to
  distinguish beneficial conditioning/adaptation from symptom exacerbation or
  disease-specific limitations.

**Code to write:**

- Add `src/dismech/commonfund/motrpac.py` to parse Data Hub manifests/download
  metadata into disease candidate tables with organism, tissue, exercise
  protocol, timepoint, assay, release, and access status.
- Add `scripts/motrpac_exercise_mechanism_map.py` that maps exercise-responsive
  genes/proteins/metabolites to dismech treatment mechanisms for selected
  diseases.
- Add schema-review notes for intervention dose, timepoint, exercise modality,
  species, tissue, and longitudinal treatment-response datasets.

**Graduate-student first pass:**

1. Start with one disease and one tissue: T2D/skeletal muscle is the best first
   pilot.
2. Pull MoTrPAC metadata for human muscle and rat homologous tissues, then list
   exercise modality, timepoint, assay, and available processed tables.
3. Choose 10 transducers and classify each as insulin signaling, mitochondrial
   adaptation, inflammation, vascular/endothelial effect, or nonspecific
   exercise marker before editing dismech.

## Dismech Disease and Mechanism Exemplars

| Disease | Current or candidate mechanism | How MoTrPAC helps |
|---------|--------------------------------|-------------------|
| `Type_2_Diabetes_Mellitus` | Curated nodes: `Insulin Resistance`, `Beta Cell Dysfunction`, `Hepatic Glucose Overproduction`, `Mitochondrial Dysfunction and Oxidative Stress`, `Incretin Axis Dysfunction`; treatment includes lifestyle/exercise context | MoTrPAC can identify exercise-responsive muscle, adipose, liver, blood, and metabolite transducers that plausibly reverse insulin resistance and mitochondrial dysfunction. |
| `Obesity` | Curated nodes: `Energy Imbalance`, `Adipose Tissue Dysfunction`, `Chronic Low-Grade Inflammation`, `Hypothalamic Dysregulation`, `Adipocyte Mitochondrial Dysfunction`; treatment `Lifestyle Modification` | Use exercise signatures to refine how physical activity affects adipose inflammation, mitochondrial function, insulin resistance, and energy-balance biomarkers. |
| `Coronary_Artery_Disease` | Curated nodes: `Atherosclerotic Plaque Formation`, `Endothelial Dysfunction`, `Plaque Rupture and Thrombosis`; risk factor `Sedentary Lifestyle` | MoTrPAC can support exercise-linked endothelial, lipid, inflammatory, and vascular repair mechanisms that reduce CAD risk. |
| `Heart_Failure` | Curated nodes: `Myocardial Contractile Dysfunction`, `Neurohormonal Activation`, `Ventricular Remodeling`, `Fluid Retention` | Exercise signatures can be mapped to skeletal muscle conditioning, vascular adaptation, inflammation, and cardiac stress response mechanisms relevant to rehabilitation. |
| `Postural_Orthostatic_Tachycardia_Syndrome` | Curated nodes: `Cardiovascular Deconditioning`, `Venous Pooling and Reduced Preload`, `Compensatory Reflex Tachycardia`; treatment `Exercise Training` | This is a strong treatment-mechanism example: exercise training can be represented as a perturbation of deconditioning and autonomic compensation. |
| `Osteoarthritis` | Curated nodes: `Cartilage Matrix Catabolism`, `Chondrocyte Senescence`, `Synovial Macrophage-Fibroblast Crosstalk`, `Subchondral Bone Remodeling` | MoTrPAC can help separate beneficial muscle/metabolic effects of exercise from joint-load injury mechanisms. |
| `Fibromyalgia` | Curated nodes: `Central Sensitization`, `Descending Pain Modulation Dysfunction`, `Neuroinflammation`, `HPA Axis Dysregulation`, `Small Fiber Pathology` | Exercise-response molecular profiles can support hypotheses around fatigue, neuroimmune tone, stress-axis regulation, and graded exercise response. |
| `Parkinsons_Disease` | Curated nodes: `Dopaminergic Neuron Loss`, `Basal Ganglia Circuit Dysfunction`, `Mitochondrial Dysfunction`, `Neuroinflammation`, `Gut-Brain Axis Dysfunction` | MoTrPAC can support exercise as a systems perturbation affecting mitochondrial, inflammatory, and neuromuscular mechanisms, especially when paired with SPARC or metabolomics data. |

## High-Value Curation Work

- Add a reusable "exercise intervention -> molecular transducer -> mechanism
  node" pattern for treatment sections that currently only list lifestyle or
  physical therapy.
- Build one MoTrPAC-only pilot around `Type_2_Diabetes_Mellitus`, `Obesity`,
  `Heart_Failure`, `Coronary_Artery_Disease`, and
  `Postural_Orthostatic_Tachycardia_Syndrome`.
- Record exercise modality, tissue, time point, age/sex/body-composition
  context, and assay type when using MoTrPAC as dataset evidence.
- Use rat data to nominate mechanisms, then mark human support separately.

## Fit for RFA-RM-26-017

MoTrPAC is the special case in the NOFO: it may be used alone or with another
eligible CF dataset. Best partner datasets:

- MoTrPAC + Metabolomics Workbench: exercise-responsive metabolites.
- MoTrPAC + LINCS: compare exercise and drug perturbation signatures.
- MoTrPAC + SPARC: exercise, autonomic tone, and organ control mechanisms.
- MoTrPAC + GTEx/HuBMAP: tissue-specific expression and cell context.

## Sources

- NIH Common Fund MoTrPAC: https://commonfund.nih.gov/MolecularTransducers
- MoTrPAC Data Hub: https://motrpac-data.org/
- MoTrPAC project overview: https://motrpac-data.org/project-overview
- MoTrPAC consortium site: https://www.motrpac.org/
