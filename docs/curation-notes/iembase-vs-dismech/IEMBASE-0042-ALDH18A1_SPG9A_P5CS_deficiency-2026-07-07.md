# IEMbase 0042: ALDH18A1-related pyrroline-5-carboxylate synthetase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 42 |
| Nosology | 1.7.14.01 |
| Gene | ALDH18A1 |
| External IDs | OMIM:138250; OMIM:219150 |
| Generated mapping | AMBIGUOUS by `alias_exact:spg9a` |
| Candidate DisMech targets | `ALDH18A1_De_Barsy_Spectrum.yaml`; `ALDH18A1_De_Barsy_Spectrum.yaml#SPG9A` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this record as autosomal dominant ALDH18A1-related
pyrroline-5-carboxylate synthetase deficiency, explicitly tied to SPG9A. The
biochemical signal is low-to-normal plasma arginine, citrulline, ornithine, and
proline.

The clinical pattern is SPG9A-facing rather than cutis-laxa-facing. IEMbase
marks spastic paraparesis/paraplegia/tetraplegia, pyramidal signs, hypertonia,
gait disturbance, muscle weakness, muscle wasting, dysarthria, pes cavus, spinal
cord atrophy, cataract, gastroesophageal reflux, vomiting, growth retardation,
short stature, and variable intellectual disability or global developmental
delay. Cutis laxa, wrinkly skin, and joint laxity are explicitly normal in the
cached phenotype table.

## DisMech phenotype coverage

The generated ambiguity is understandable but resolvable. The parent file
`ALDH18A1_De_Barsy_Spectrum.yaml` is the correct local container, and the
`SPG9A` subtype is the best canonical target for this IEMbase record.

DisMech models ALDH18A1-related P5CS deficiency as a spectrum containing
dominant SPG9A, recessive SPG9B, and ARCL3A/De Barsy presentations. It already
captures autosomal dominant SPG9A, dominant-negative P5CS oligomer disruption,
impaired proline and ornithine biosynthesis, low plasma proline, ornithine,
citrulline, and arginine, spastic paraplegia, cataracts, gastroesophageal
reflux, preserved or milder cognition in SPG9A, and the broader spectrum
mechanisms involving antioxidant metabolism, extracellular-matrix changes, and
neurodevelopmental/corticospinal involvement.

## Concordance and completeness

Judgement: map this IEMbase record to
`ALDH18A1_De_Barsy_Spectrum.yaml#SPG9A`, with the parent spectrum retained as
context. The ambiguity is caused by the same alias matching both the file-level
spectrum and the subtype.

Concordance is high for the gene, inheritance, P5CS mechanism, amino-acid
profile, spastic paraplegia, cataract, and reflux. IEMbase adds more granular
SPG9A phenotype detail, including dysarthria, gait disturbance, pes cavus,
muscle wasting/weakness, spinal cord atrophy, vomiting, pyramidal signs, and
explicit absence of cutis laxa/wrinkly skin/joint laxity. DisMech is stronger
for mechanism and for placing SPG9A relative to SPG9B and ARCL3A.

## Curation actions

- Prefer the subtype mapping
  `ALDH18A1_De_Barsy_Spectrum.yaml#SPG9A` for this record.
- Consider adding IEMbase's granular SPG9A features to the subtype if supported:
  dysarthria, gait disturbance, pes cavus, muscle wasting/weakness, spinal cord
  atrophy, vomiting, and pyramidal signs.
- Preserve subtype boundaries: IEMbase ID 42 is not the cutis laxa/De Barsy
  presentation despite sharing ALDH18A1 and P5CS deficiency biology.
