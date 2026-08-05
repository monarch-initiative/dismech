# IEMbase 0699: NDUFA11-related NADH dehydrogenase alpha subcomplex subunit 11 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 699 |
| Nosology | 7.1.28.01 |
| Nosology code | IEM1140 |
| Gene | NDUFA11 |
| External IDs | OMIM:618236; ORPHA:2609 |
| Generated mapping | CANDIDATE to `COA3-Related_COX_Deficiency.yaml` |
| Candidate DisMech targets | Broad complex I/Leigh context only; no exact NDUFA11 target |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive NDUFA11-related NADH dehydrogenase alpha
subcomplex subunit 11 deficiency, also labeled mitochondrial complex I
deficiency, nuclear type 14.

Biochemical rows show decreased fibroblast complex I activity and increased
plasma lactate in neonatal and infantile windows. The clinical/characteristic
rows include cardiomyopathy and encephalopathy. The source's lactic-acidosis
clinical row carries a downward marker, despite the biochemical lactate row
being increased; this should be treated as a source coding anomaly rather than
evidence for decreased lactic acidosis.

## DisMech phenotype coverage

No exact NDUFA11 or MC1DN14 local target was identified.

`Leigh_Syndrome.yaml` gives broad context for complex I-related mitochondrial
encephalopathy and lactate elevation, but it does not model NDUFA11.

The generated `COA3-Related_COX_Deficiency.yaml` candidate is a complex IV
assembly-factor disorder. It shares the nuclear-type number 14 but not the gene
or respiratory-chain complex and should be rejected as exact coverage.

## Concordance and completeness

Judgement: true local gap with broad mitochondrial/Leigh overlap only.

The IEMbase record is compact and centered on an NDUFA11 complex I biochemical
defect with cardiomyopathy and encephalopathy. COA3 is a wrong-complex
number-collision candidate, not a substitute for NDUFA11/MC1DN14.

## Curation actions

- Add a dedicated NDUFA11/MC1DN14 target if curated.
- Reject COA3-related complex IV deficiency as exact coverage.
- Preserve decreased fibroblast complex I activity, increased plasma lactate,
  cardiomyopathy, encephalopathy, and the source lactic-acidosis marker anomaly.
- Use broad Leigh/mitochondrial disease context only for shared phenotype
  framing.
