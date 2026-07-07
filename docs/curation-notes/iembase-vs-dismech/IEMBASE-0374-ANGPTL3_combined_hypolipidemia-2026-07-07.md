# IEMbase 0374: ANGPTL3-related angiopoietin-like 3 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 374 |
| Nosology | 15.5.1.01 |
| Gene | ANGPTL3 |
| External IDs | OMIM:605019; OMIM:604774 |
| Generated mapping | MAPPED; `Abetalipoproteinemia.yaml` |
| Candidate DisMech targets | No exact local target; `Abetalipoproteinemia.yaml` is shared hypolipidemia context only |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents ANGPTL3-related angiopoietin-like 3 deficiency, with
alternate names familial hypobetalipoproteinemia type 2 and combined familial
hypolipidemia. Inheritance is autosomal recessive.

The cached record is clinically sparse and states no clinical significance.
Biochemical rows include plasma HDL cholesterol, plasma LDL cholesterol, serum
triglyceride, and plasma Apo B. There are no treatment rows.

## DisMech phenotype coverage

The generated mapping to `Abetalipoproteinemia.yaml` is a false positive exact
mapping driven by shared hypobetalipoproteinemia identifiers or labels. Local
abetalipoproteinemia models MTTP-related failure of apoB-lipoprotein assembly,
not ANGPTL3 deficiency.

The Familial Hypercholesterolemia file discusses ANGPTL3 as a therapeutic
target through evinacumab in homozygous FH, but this is drug-target context for
LDL lowering, not a curated ANGPTL3 deficiency disease.

## Concordance and completeness

Judgement: false positive exact mapping; ANGPTL3-related combined familial
hypolipidemia is a local disease gap or scope-review item.

IEMbase and abetalipoproteinemia share low LDL, low triglyceride, low HDL, and
low Apo B biochemical directionality, but the causal mechanism differs. ANGPTL3
loss affects lipoprotein lipase and endothelial lipase inhibition, whereas the
local abetalipoproteinemia file models MTTP loss and apoB-lipoprotein export
failure.

## Curation actions

- Do not treat `Abetalipoproteinemia.yaml` as the exact target for this record.
- Create or prioritize a separate ANGPTL3 combined familial hypolipidemia entry
  if this low-LDL condition is in DisMech scope.
- Keep local FH/evinacumab ANGPTL3 content as therapeutic pathway context only.
- Review the IEMbase "no clinical significance" row before deciding disease
  scope and phenotype import.
