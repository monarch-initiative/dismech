# IEMbase 0007: GCH1-related GTP cyclohydrolase I deficiency, autosomal dominant

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 7 |
| Nosology | 21.1.03.01 |
| Gene | GCH1 |
| External IDs | OMIM:600225 |
| Generated mapping | UNMAPPED; weak candidate `Dopa-Responsive Dystonia` score 0.762 |
| Likely DisMech targets | `kb/disorders/Autosomal_Dominant_Dopa_Responsive_Dystonia.yaml`; umbrella `kb/disorders/Dopa_Responsive_Dystonia.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

Characteristic clinical features are diurnal fluctuation, dystonia,
hypokinesia, parkinsonism, and rigidity. Additional features include
bradykinesia, dyskinesia, dysphagia, hypertonia, hypotonia, pes equinovarus,
scoliosis, spasticity, increased tendon reflexes, and tremor.

Biochemical entries include phenylalanine, CSF 5-HIAA and homovanillic acid,
phenylalanine loading, and CSF biopterin/neopterin. Treatment is levodopa.

## DisMech phenotype coverage

The generated crosswalk is a false negative. DisMech has a specific
`Autosomal Dominant Dopa-Responsive Dystonia` entry with GCH1 genetics,
autosomal dominant inheritance, BH4 cofactor limitation, childhood dystonia,
diurnal fluctuation, parkinsonism, and low-dose levodopa response. The broader
`Dopa-Responsive Dystonia` umbrella also captures limb/focal dystonia,
parkinsonism, gait disturbance, decreased CSF homovanillic acid, transient
hyperphenylalaninemia, and levodopa therapy.

## Concordance and completeness

Judgement: mapping false negative; phenotype concordance is high once the
specific AD-DRD entry is selected.

IEMbase has some orthopedic or pyramidal/motor secondary terms not explicit in
the local entry, including pes equinovarus, scoliosis, spasticity, and increased
tendon reflexes. DisMech has stronger mechanism and treatment modeling than the
IEMbase row.

## Curation actions

- Add synonyms such as Segawa disease, GTPCH-DRD, and GTP cyclohydrolase I
  deficiency autosomal dominant to the local target or mapping normalization.
- Prefer the specific `Autosomal Dominant Dopa-Responsive Dystonia` entry as
  the canonical crosswalk target, with the umbrella as parent context.
- Consider secondary musculoskeletal/pyramidal features only with supporting
  phenotype evidence.
