# IEMbase 0198: POR-related cytochrome P450 oxidoreductase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 198 |
| Nosology | 24.2.07.01 |
| Gene | POR |
| External IDs | OMIM:201750; ORPHA:83 |
| Generated mapping | MAPPED; `Amniotic_Band_Syndrome.yaml` |
| Candidate DisMech targets | No direct target; `Humeroradial_Synostosis.yaml` has partial Antley-Bixler/POR context |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as POR-related cytochrome P450 oxidoreductase
deficiency, with alternate labels Antley-Bixler syndrome and ABS. Treatability
is marked unknown.

The biochemical rows include normal-to-increased ACTH, normal-to-increased
17-OH-pregnenolone, neonatal elevation of 17-OH-progesterone,
neonatal androgen/androstenedione/testosterone excess followed by low-to-normal
values later, decreased ACTH-stimulated cortisol with normal baseline cortisol,
neonatal DHEA excess followed by low-to-normal values later, and increased
urinary pregnanediol. Characteristic clinical rows include femoral bowing and
fractures, midface hypoplasia, radiohumeral synostosis, and radioulnar
synostosis. Additional rows include adrenal insufficiency, ambiguous genitalia,
46,XY undervirilization, neonatal androgen excess, Antley-Bixler syndrome,
arachnodactyly, choanal atresia or stenosis, clitoral hypertrophy,
craniosynostosis, dysplastic ears, hydronephrosis, hypoplastic labia majora,
hypospadias, male genital hypoplasia, phalangeal malformations, renal
anomalies or hypoplasia, scoliosis, skeletal abnormalities, and Prader III-V
virilization in 46,XX individuals. No treatment rows are listed.

## DisMech phenotype coverage

`Amniotic_Band_Syndrome.yaml` is not a valid target. The generated exact mapping
is an acronym collision: IEMbase uses ABS for Antley-Bixler syndrome, whereas the
local file models amniotic band syndrome, a sporadic mechanical malformation
sequence. `Humeroradial_Synostosis.yaml` contains relevant partial context for
POR-related Antley-Bixler syndrome and radiohumeral synostosis, but it is an
HRS feature entry, not a canonical POR deficiency disease entry and it does not
cover the steroidogenesis phenotype in full.

## Concordance and completeness

Judgement: mapped false positive; true POR deficiency/Antley-Bixler local gap
with partial HRS context.

IEMbase describes a POR-specific mixed steroidogenesis and skeletal
malformation disorder: disordered adrenal/gonadal steroid markers, adrenal
insufficiency, genital ambiguity, craniosynostosis, midface hypoplasia,
radiohumeral/radioulnar synostosis, femoral bowing/fractures, choanal
abnormalities, and renal anomalies. Local amniotic band syndrome is unrelated;
local HRS captures only one important skeletal feature and contextual gene
association.

## Curation actions

- Do not map this record to `Amniotic_Band_Syndrome.yaml`.
- Consider a future POR-related cytochrome P450 oxidoreductase deficiency /
  Antley-Bixler syndrome entry, with `Humeroradial_Synostosis.yaml` retained as
  feature context rather than the disease target.
- Seed that future entry with ACTH-stimulated cortisol deficiency, mixed
  neonatal androgen excess and later androgen deficiency, DHEA/pregnanediol
  abnormalities, adrenal insufficiency, genital ambiguity, craniosynostosis,
  midface hypoplasia, radiohumeral/radioulnar synostosis, femoral bowing, and
  choanal/renal anomalies.
