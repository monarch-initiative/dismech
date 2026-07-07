# IEMbase 0663: PPM1K-related branched-chain ketoacid dehydrogenase phosphatase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 663 |
| Nosology | 1.3.24.01 |
| Nosology code | IEM1109 |
| Gene | PPM1K |
| External IDs | OMIM:615135; ORPHA:268162 |
| Generated mapping | UNMAPPED; best candidate `Maple_Syrup_Urine_Disease.yaml` |
| Candidate DisMech targets | Partial umbrella coverage in `Maple_Syrup_Urine_Disease.yaml` |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents autosomal recessive PPM1K-related branched-chain ketoacid
dehydrogenase phosphatase deficiency, with alternate labels including mild
variant maple syrup urine disease.

The biochemical signal is narrowly focused: increased plasma isoleucine,
leucine, and valine from the neonatal period into adulthood. The clinical rows
state no clinical significance, which is an important mild-variant cue rather
than an absence of metabolic abnormality.

## DisMech phenotype coverage

`Maple_Syrup_Urine_Disease.yaml` covers the BCKDH pathway, elevated branched
chain amino acids, branched-chain ketoacids, alloisoleucine, and the classic
BCKDHA/BCKDHB/DBT/DLD disease spectrum. It also explicitly describes BCKDH
regulation by BCKDK and PPM1K, including PPM1K as the PP2Cm phosphatase that
dephosphorylates and activates BCKDH.

That makes the generated best candidate biologically relevant, but coverage is
not complete. The local MSUD entry does not currently expose a standalone
PPM1K-related mild MSUD subtype or disease entry, and the IEMbase row is much
milder than classic neonatal MSUD.

## Concordance and completeness

Judgement: partial false negative. `Maple_Syrup_Urine_Disease.yaml` is the right
local context, but it should not be treated as exact PPM1K disease-level
coverage without a subtype or target that captures the phosphatase defect.

The concordant core is elevated leucine, isoleucine, and valine due to impaired
regulation of the BCKDH complex. The completeness gap is the PPM1K-specific
regulatory mechanism and the mild/no-clinical-significance phenotype framing.

## Curation actions

- Link this record to MSUD pathway context, but mark disease-level coverage as
  partial.
- Consider adding a PPM1K-specific subtype or entry if DisMech needs this IEMbase
  row represented explicitly.
- Preserve the mild-variant signal and avoid importing classic MSUD crisis
  features by default.
- Preserve increased plasma leucine, isoleucine, and valine as the key
  biochemical triad.
