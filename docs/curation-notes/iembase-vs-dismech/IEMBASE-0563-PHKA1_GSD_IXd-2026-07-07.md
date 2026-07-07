# IEMbase 0563: PHKA1-related glycogen storage disease IXd

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 563 |
| Nosology | 3.4.13.01 |
| Gene | PHKA1 |
| External IDs | OMIM:300559; ORPHA:715 |
| Generated mapping | CANDIDATE; `Glycogen_Storage_Disease_Type_I.yaml` |
| Candidate DisMech targets | No exact PHKA1/GSD IXd target found |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents PHKA1-related muscle phosphorylase kinase deficiency, with
alternate labels glycogen storage disease type IXd and GSD-IXd. The record
lists autosomal recessive inheritance, idiopathic subtype, treatability yes,
and no treatment rows.

Biochemical rows include increased creatine kinase, decreased muscle
phosphorylase kinase, low lactate rise on forearm exercise testing, increased
muscle glycogen, normal ammonia rise, low-normal glucose, increased uric acid,
and normal-high urine myoglobin. Clinical rows include liver adenoma, second
wind, exercise intolerance, muscle cramps, muscle pain, and muscle weakness.

## DisMech phenotype coverage

The generated `Glycogen_Storage_Disease_Type_I.yaml` candidate is a false
positive. Local GSD I covers glucose-6-phosphatase or glucose-6-phosphate
transporter disease, not muscle phosphorylase kinase alpha subunit deficiency.
Existing glycogen storage disease entries provide neighborhood context, but no
exact PHKA1/GSD IXd target was found.

## Concordance and completeness

Judgement: reject `Glycogen_Storage_Disease_Type_I.yaml`; true PHKA1/GSD IXd
local gap.

IEMbase overlaps with nearby glycogen-storage myopathy entries on exercise
intolerance, cramps, pain, weakness, CK elevation, second wind, and exercise
test metabolite behavior. The gene, enzyme, tissue, and subtype identity are
not covered by the generated GSD I candidate.

IEMbase provides useful seed rows for a future PHKA1/GSD IXd entry, including
muscle phosphorylase kinase deficiency, muscle glycogen increase, forearm
exercise lactate/ammonia pattern, myoglobin, CK, uric acid, and exercise
phenotypes. The IEMbase inheritance value should be reviewed during future
curation because this record's inheritance field is a key provenance-sensitive
detail.

## Curation actions

- Reject the generated GSD I candidate as an exact mapping.
- Add PHKA1/GSD IXd to the glycogen-storage disease curation backlog.
- Preserve IEMbase enzyme, muscle glycogen, exercise-test, second-wind,
  myoglobin, CK, uric-acid, and inheritance prompts for source review.
