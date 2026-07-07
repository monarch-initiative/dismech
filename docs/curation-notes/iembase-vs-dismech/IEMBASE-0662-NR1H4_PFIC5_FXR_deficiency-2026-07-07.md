# IEMbase 0662: NR1H4-related progressive familial intrahepatic cholestasis 5

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 662 |
| Nosology | 14.8.07.02 |
| Nosology code | IEM0808 |
| Gene | NR1H4 |
| External IDs | OMIM:617049; ORPHA:69665 |
| Generated mapping | UNMAPPED; best candidate `Progressive_Familial_Heart_Block.yaml` |
| Candidate DisMech targets | Broad cholestasis and bile-acid context only; no exact NR1H4/PFIC5 target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive NR1H4-related progressive familial
intrahepatic cholestasis 5, also labeled nuclear bile-acid receptor deficiency
or farnesoid X receptor deficiency.

The clinical signal is neonatal or infantile intrahepatic cholestasis,
jaundice, and liver failure. Biochemical rows include increased bilirubin,
increased transaminases/ASAT/ALAT, normal GGT, and variable ammonia and glucose.
Hypoglycemia is represented as a possible infancy/childhood clinical feature.

## DisMech phenotype coverage

No exact NR1H4, FXR, nuclear bile-acid receptor deficiency, or PFIC5 local
target was identified.

`Inborn_Disorder_of_Bile_Acid_Synthesis.yaml` gives broad bile-acid metabolism
context for inherited cholestatic disorders, but it is built around bile-acid
synthesis and conjugation enzyme/transporter defects such as HSD3B7, AKR1D1,
CYP7B1, AMACR, CYP27A1, BAAT, and SLC27A5. It does not model NR1H4/FXR
signaling deficiency or progressive familial intrahepatic cholestasis type 5.

The generated `Progressive_Familial_Heart_Block.yaml` candidate is a lexical
false positive and should not be used.

## Concordance and completeness

Judgement: true local gap. Existing bile-acid and cholestasis context can help
orient a curator, but it is not disease-level coverage for NR1H4-related PFIC5.

The most important phenotype package to preserve is normal-GGT neonatal
cholestasis with jaundice, liver failure, increased bilirubin and
transaminases, and possible hypoglycemia/hyperammonemia.

## Curation actions

- Add a dedicated NR1H4/PFIC5 target if this record is curated into DisMech.
- Do not accept the progressive familial heart block candidate.
- Preserve normal GGT as a discriminating biochemical prompt.
- Use the bile-acid synthesis umbrella only as broad context, not as exact
  coverage.
