# Stimulating Peripheral Activity to Relieve Conditions (SPARC)

Reviewed: 2026-05-29

## Why This Is Mechanistically Valuable

SPARC is valuable because many disease mechanisms pass through peripheral
nerves, autonomic circuits, and organ control systems, but those links are
often represented weakly in disease knowledge bases. The NIH Common Fund
describes SPARC as a program to accelerate therapeutic devices that modulate
electrical activity in nerves to improve organ function. The SPARC Portal
provides multimodal peripheral nervous system and organ datasets, anatomical
maps, tools, and models.

For dismech, SPARC can turn neuromodulation from a treatment label into a
mechanism chain: neural target -> circuit activity -> organ process -> symptom
or physiologic endpoint.

## Dismech Interpretation Pattern

Use SPARC as a nerve-organ mechanism layer:

`stimulation or lesion target -> peripheral/autonomic circuit change ->
organ-level physiology -> symptom, biomarker, or treatment response`

The strongest uses are autonomic disease, visceral pain, gastrointestinal
disease, cardiovascular control, bladder function, inflammatory reflexes, and
bioelectronic medicine interventions.

## Concrete Implementation Plan

**Mode:** teach treatment-mechanism curation and benchmark nerve-organ
interpretation. SPARC should teach dismech how to represent neuromodulation as
an anatomical target, circuit effect, organ response, and phenotype endpoint.

**Required datasets and access path:**

- Use the SPARC Portal: https://sparc.science/ and documentation:
  https://docs.sparc.science/docs/sparc-portal-overview.
- Use the public-dataset access docs:
  https://docs.sparc.science/docs/accessing-public-datasets. The docs describe
  in-browser download for smaller datasets and AWS S3 access for larger
  current-version public datasets.
- Use SPARC maps and tools for anatomical context:
  https://sparc.science/tools-and-resources and the portal's scaffold/viewer
  workflows.
- For each dataset, record organ, species, nerve/branch, stimulation or lesion
  context, assay, file format, dataset version, DOI if present, and download
  route.

**Tools and environment:**

- Portal UI first; AWS CLI for larger public datasets; Pennsieve/SPARC metadata
  tools where the dataset exposes Pennsieve identifiers.
- Python/R for physiologic time series, imaging, and metadata tables; Neurodata
  Without Borders tooling if datasets are NWB.
- Ontology mapping to UBERON/CL/MAXO/NCIT plus an anatomical nerve-organ
  crosswalk for treatment mechanism targets.

**Curation targets:**

- `Postural_Orthostatic_Tachycardia_Syndrome` and
  `Autoimmune_Autonomic_Ganglionopathy`: autonomic target-to-organ control.
- `Irritable_Bowel_Syndrome` and `Chronic_Pancreatitis`: visceral afferent,
  enteric, vagal, and pain-amplification mechanisms.
- `Epilepsy` and `Dravet_syndrome`: vagus nerve stimulation as a treatment
  mechanism while keeping central seizure mechanisms separate.
- `Heart_Failure` and `Essential_Hypertension`: autonomic modulation of heart,
  vasculature, kidney, and baroreflex/renal sympathetic pathways.

**Code to write:**

- Add `src/dismech/commonfund/sparc.py` to harvest dataset metadata by organ,
  nerve, species, assay, version, DOI, file format, and access route.
- Add `scripts/sparc_neuromodulation_targets.py` to produce treatment
  mechanism templates: intervention, anatomical target, nerve branch, organ,
  expected physiologic endpoint, and dismech pathophysiology node.
- Add schema-review notes for stimulation parameters, nerve branch, organ
  endpoint, and device/treatment mechanism fields.

**Graduate-student first pass:**

1. Pick one organ-control problem: POTS/vascular tone, IBS/gut motility,
   epilepsy/VNS, heart failure/autonomic balance, or hypertension/renal nerve.
2. Find 5 SPARC datasets with relevant organ and nerve context. Record dataset
   DOI/version and whether download is browser or S3.
3. Draft one neuromodulation treatment mechanism in dismech form: target,
   circuit effect, organ physiology, symptom/endpoint, and caveat.

## Dismech Disease and Mechanism Exemplars

| Disease | Current or candidate mechanism | How SPARC helps |
|---------|--------------------------------|-----------------|
| `Postural_Orthostatic_Tachycardia_Syndrome` | Curated nodes: `Sympathetic Denervation`, `Venous Pooling and Reduced Preload`, `Compensatory Reflex Tachycardia`, `Excessive Sympathetic Activation`, `Cardiovascular Deconditioning`; treatment `Exercise Training` | SPARC can provide nerve-organ context for sympathetic vascular control, orthostatic compensation, and candidate neuromodulatory interventions. |
| `Autoimmune_Autonomic_Ganglionopathy` | Curated nodes: `Ganglionic Acetylcholine Receptor Autoantibodies`, `Antibody-Mediated Ganglionic Acetylcholine Receptor Dysfunction`, `Postganglionic Sympathetic and Parasympathetic Failure` | A direct autonomic circuit example: map ganglionic receptor dysfunction to multi-organ sympathetic and parasympathetic failure. |
| `Irritable_Bowel_Syndrome` | Curated nodes: `Visceral Hypersensitivity`, `Gut Dysmotility`, `Gut-Brain Axis Dysfunction`, `Intestinal Barrier Dysfunction`, `Immune Activation and Mast Cell Degranulation` | SPARC can add enteric, vagal, and visceral afferent anatomy to pain and motility mechanisms. |
| `Chronic_Pancreatitis` | Curated nodes: `Recurrent Acinar Cell Injury`, `Pancreatic Fibrosis`, `Chronic Abdominal Pain` | Use SPARC to distinguish tissue injury/fibrosis mechanisms from pancreatic sensory and autonomic pain-amplification mechanisms. |
| `Epilepsy` | Curated nodes: `Neuronal Hyperexcitability`, `Network Hyperexcitability`, `Neuroinflammation and Gliosis`; treatments include `Vagus Nerve Stimulation` and `Deep Brain Stimulation` | SPARC can support the peripheral vagal component of seizure-modulating treatments, while central mechanisms stay in the epilepsy graph. |
| `Dravet_syndrome` | Curated nodes: `SCN1A Gene Mutation`, `Neuronal Hyperexcitability`, `Astrocyte Dysregulation`; treatment `Vagus Nerve Stimulation (VNS)` | A rare-disease treatment-mechanism example for mapping VNS to seizure-network modulation. |
| `Heart_Failure` | Curated nodes: `Myocardial Contractile Dysfunction`, `Neurohormonal Activation`, `Ventricular Remodeling`, `Fluid Retention` | SPARC can add autonomic control and vagal/sympathetic modulation context to cardiac function and remodeling. |
| `Essential_Hypertension` | Curated nodes: `Vascular Resistance`, `Renin-Angiotensin-Aldosterone System Dysregulation`, `Sympathetic Nervous System Overactivity`, `Immune and Inflammatory Activation` | Use SPARC to interpret renal, baroreflex, and sympathetic neuromodulation strategies for blood pressure control. |

## High-Value Curation Work

- Add a treatment-mechanism pattern for neuromodulation: anatomical target,
  nerve branch, organ, stimulation parameters when known, target mechanism, and
  measurable endpoint.
- Prioritize entries that already have autonomic or neural-circuit nodes:
  `Postural_Orthostatic_Tachycardia_Syndrome`,
  `Autoimmune_Autonomic_Ganglionopathy`, `Irritable_Bowel_Syndrome`,
  `Epilepsy`, `Dravet_syndrome`, `Heart_Failure`, and
  `Essential_Hypertension`.
- Add MAXO/NCIT intervention terms for VNS, DBS, autonomic modulation, and
  implanted or noninvasive stimulation where ontology coverage exists.
- Pair SPARC data with dismech mechanism graphs only when the anatomical target
  and disease-relevant organ physiology are explicit.

## Fit for RFA-RM-26-017

Best partner datasets:

- SPARC + MoTrPAC: exercise, autonomic tone, and organ physiology.
- SPARC + LINCS/IDG: bioelectronic versus pharmacologic modulation of the same
  disease node.
- SPARC + HuBMAP: organ cell context for nerve-organ endpoints.
- SPARC + A2CPS: chronic pain transition and neural modulation.

## Sources

- NIH Common Fund SPARC: https://commonfund.nih.gov/sparc
- SPARC Portal: https://sparc.science/
- SPARC Portal overview: https://docs.sparc.science/docs/sparc-portal-overview
- SPARC public dataset access: https://docs.sparc.science/docs/accessing-public-datasets
- SPARC tools/resources: https://sparc.science/tools-and-resources
- SPARC health relevance: https://commonfund.nih.gov/sparc/public
