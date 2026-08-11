# IEMbase 0372: APOB-related apolipoprotein B deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 372 |
| Nosology | 15.1.04.01 |
| Gene | APOB |
| External IDs | OMIM:144010; OMIM:605019; ORPHA:391665 |
| Generated mapping | MAPPED; `Abetalipoproteinemia.yaml` |
| Candidate DisMech targets | No exact local target; `Abetalipoproteinemia.yaml` is shared low-apoB context only |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents APOB-related apolipoprotein B deficiency, with alternate
names familial hypobetalipoproteinemia type 1 and normotriglyceridemic
hypobetalipoproteinemia. Inheritance is listed as autosomal recessive.

The cached record is clinically sparse. It lists hemolytic anemia and no
clinical significance, with biochemical rows for plasma HDL cholesterol, plasma
LDL cholesterol, serum triglyceride, plasma Apo B, and plasma vitamin E.
Treatment contains low-fat diet.

## DisMech phenotype coverage

The generated exact mapping to `Abetalipoproteinemia.yaml` is over-broad for a
mechanism-first DisMech target. The local abetalipoproteinemia entry models
MTTP-related failure of apoB-lipoprotein assembly and secretion. It has strong
shared phenotype context for very low LDL-C, triglycerides, Apo B, vitamin E
deficiency, fat malabsorption, and severe homozygous hypobetalipoproteinemia
presentations, but its causal gene and initiating mechanism are MTTP, not APOB.

The local `Familial_Hypercholesterolemia.yaml` entry also mentions APOB, but in
the opposite binding-defect/hypercholesterolemia direction. It is not a valid
target for APOB deficiency with low LDL.

## Concordance and completeness

Judgement: false positive exact mapping; APOB-related familial
hypobetalipoproteinemia type 1 is a local disease gap.

IEMbase and the abetalipoproteinemia file share low apoB/LDL/triglyceride and
vitamin E biology, but they diverge at the root cause: APOB deficiency versus
MTTP loss of function. The IEMbase record is also much milder in clinical rows,
including "no clinical significance," which should not be imported into the
MTTP abetalipoproteinemia target.

## Curation actions

- Do not treat `Abetalipoproteinemia.yaml` as the exact target for this record.
- Create or prioritize a separate APOB-related familial hypobetalipoproteinemia
  type 1 target if this condition is in DisMech scope.
- Use `Abetalipoproteinemia.yaml` only as shared low-apoB/vitamin E/fat
  absorption context, not as the canonical mapping.
- Review the low-fat diet and hemolytic anemia rows before importing them into
  any future APOB-specific entry.
