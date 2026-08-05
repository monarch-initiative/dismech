# IEMbase 0561: ALPL-related hypophosphatasia

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 561 |
| Nosology | 21.6.03.01 |
| Gene | ALPL |
| External IDs | OMIM:241500; ORPHA:436 |
| Generated mapping | MAPPED; `Hypophosphatasia.yaml` |
| Candidate DisMech targets | `Hypophosphatasia.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents ALPL-related tissue-nonspecific alkaline phosphatase
deficiency, with alternate labels congenital hypophosphatasia,
phosphoethanolaminuria, and HOPS. The record lists autosomal dominant and
autosomal recessive inheritance, idiopathic subtype, unknown treatability, and
an asfotase alfa enzyme-replacement treatment row.

Biochemical rows include increased urinary phosphoethanolamine, increased
plasma pyridoxal phosphate, very low plasma alkaline phosphatase, normal-high
to high plasma calcium, and low-normal to low plasma phosphate. Clinical rows
include dentine hypoplasia, premature dentition exfoliation, respiratory
failure, taurodontism, and thin dentinal walls. Characteristic rows include
seizures and skeletal hypomineralization.

## DisMech phenotype coverage

`Hypophosphatasia.yaml` is the correct local target. The entry models ALPL
loss of function, tissue-nonspecific alkaline phosphatase deficiency, reduced
alkaline phosphatase and pyrophosphatase activity, accumulation of inorganic
pyrophosphate, pyridoxal phosphate, and phosphoethanolamine, impaired
hydroxyapatite formation, and decreased bone mineralization. It also covers
dominant and recessive inheritance across severity levels and asfotase alfa
enzyme replacement.

## Concordance and completeness

Judgement: correct high-concordance mapping to `Hypophosphatasia.yaml`.

IEMbase and DisMech agree on ALPL identity, mixed dominant/recessive
inheritance, low alkaline phosphatase, elevated PLP and PEA, mineralization
failure, skeletal hypomineralization, dental involvement, seizures, and
asfotase alfa treatment. DisMech is stronger for the pyrophosphate-mediated
bone-mineralization mechanism and severity-spectrum framing.

IEMbase adds review prompts for calcium and phosphate directionality,
respiratory failure, taurodontism, dentine hypoplasia, premature dentition
exfoliation, and thin dentinal walls.

## Curation actions

- Keep this record mapped to `Hypophosphatasia.yaml`.
- Consider source-checking IEMbase dental subfeatures, respiratory failure,
  calcium/phosphate rows, and seizure framing for possible local additions.
- Keep asfotase alfa linked to pediatric-onset or severe disease context where
  evidence supports that scope.
