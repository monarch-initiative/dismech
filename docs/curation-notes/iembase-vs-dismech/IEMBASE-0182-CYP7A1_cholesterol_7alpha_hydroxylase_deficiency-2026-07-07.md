# IEMbase 0182: CYP7A1-related cholesterol 7alpha-hydroxylase deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 182 |
| Nosology | 14.8.1.01 |
| Gene | CYP7A1 |
| External IDs | OMIM:118455; ORPHA:209902 |
| Generated mapping | CANDIDATE; `Inborn_Disorder_of_Bile_Acid_Synthesis.yaml#BASD Type 3` |
| Candidate DisMech targets | None valid; generated BASD type 3 candidate is false |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as CYP7A1-related cholesterol 7alpha-hydroxylase
deficiency, with CYP7A1 as the alternate label. Treatability is marked
unknown.

The IEMbase signal is sparse compared with adjacent bile acid synthesis
records. The biochemical row reports adult statin-resistant hyperlipidemia as
characteristic. The clinical row reports variable adult gallstones. No
treatment rows are listed.

## DisMech phenotype coverage

No valid local CYP7A1 disease target was found. The generated candidate,
`Inborn_Disorder_of_Bile_Acid_Synthesis.yaml#BASD Type 3`, is not correct
because BASD type 3 is CYP7B1-related oxysterol 7alpha-hydroxylase deficiency.
Local CYP7A1 mentions are pathway or context mentions rather than a standalone
CYP7A1-related cholesterol 7alpha-hydroxylase deficiency entry.

## Concordance and completeness

Judgement: generated false positive; true local disease gap.

The lexical similarity between CYP7A1 cholesterol 7alpha-hydroxylase deficiency
and CYP7B1 oxysterol 7alpha-hydroxylase deficiency is misleading. IEMbase
describes an adult dyslipidemia and gallstone phenotype, not the infantile
cholestasis and later spastic paraplegia phenotype modeled under BASD type 3.

## Curation actions

- Do not map this record to BASD type 3.
- Add a future standalone CYP7A1-related cholesterol 7alpha-hydroxylase
  deficiency target if this disease is in scope.
- Seed that future entry with statin-resistant hyperlipidemia, gallstones, and
  CYP7A1/cholesterol 7alpha-hydroxylase identity.
