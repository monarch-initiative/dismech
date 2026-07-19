# IEMbase 0333: MOGS/GCS1-related glucosidase 1 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 333 |
| Nosology | 18.1.2.01 |
| Gene | MOGS |
| External IDs | OMIM:606056 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | Reject `Gaucher_Disease.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents GCS1-CDG/CDG-IIb, caused by MOGS/glucosidase I deficiency.
Characteristic rows include alopecia areata, high-arched palate, abnormal
brain evoked response audiometry, burst-suppression EEG, epilepsy, facial
dysmorphism, overlapping fingers, hepatomegaly, hypokinesia, hypoplastic labia
majora, hypotonia, long eyelashes, myelinating neuropathy, respiratory failure,
short palpebral fissures, and abnormal visual evoked potentials. Additional
clinical rows include apnea, broad nose, developmental delay, gastric tube
feeding, prominent occiput, retrognathia, and short palpebral fissures.

The biochemical rows are sparse but distinctive: abnormal serum
sialotransferrins, increased urinary tetraglucoside, and decreased
immunoglobulins. No treatment rows are present.

## DisMech phenotype coverage

The Gaucher disease candidate is a lexical false positive around glucosidase
terminology. Gaucher disease is a lysosomal storage disease caused by GBA1
beta-glucocerebrosidase deficiency, with glucosylceramide/glucosylsphingosine
storage, hepatosplenomegaly, cytopenias, bone disease, and ERT/SRT treatment
logic. It is not MOGS/glucosidase I deficiency and does not cover CDG-IIb.

Other local glycosylation entries and the CDG module provide family context,
but no standalone MOGS/GCS1-CDG entry exists.

## Concordance and completeness

Judgement: true local disease gap; reject the Gaucher candidate.

IEMbase points to a distinct type II CDG with neurologic, respiratory,
craniofacial, immunologic, sensory-evoked-potential, and tetraglucoside
signals. The shared words "glucosidase" and "hepatomegaly" are not enough to
map this record to Gaucher disease.

## Curation actions

- Add a standalone MOGS/GCS1-CDG target before treating this record as mapped.
- Do not map this record to Gaucher disease or other lysosomal glucosidase
  disorders.
- Preserve urinary tetraglucoside, immunoglobulins, burst-suppression EEG,
  evoked-potential abnormalities, respiratory failure/apnea, and myelinating
  neuropathy as future-curation prompts.
