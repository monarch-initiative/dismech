# IEMbase 0320: SCARB2-related glucocerebrosidase receptor deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 320 |
| Nosology | 20.6.03.02 |
| Gene | SCARB2 |
| External IDs | OMIM:254900; ORPHA:163696 |
| Generated mapping | UNMAPPED |
| Candidate DisMech targets | Fuzzy candidate `Gaucher_Disease.yaml` rejected; broad PME context only |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase represents this as SCARB2-related glucocerebrosidase receptor
deficiency with alternate labels myoclonus-neuropathy syndrome and action
myoclonus-renal failure syndrome. The characteristic row is myoclonic
seizures. Additional clinical rows include dilated cardiomyopathy, dementia,
polyneuropathy, and renal failure.

The biochemical row is beta-D-glucosidase enzyme testing, recorded as normal in
the cached age strata. No treatment rows are present.

## DisMech phenotype coverage

The generated fuzzy candidate is `Gaucher_Disease.yaml`, but this is a false
positive. Gaucher disease is GBA1-related beta-glucocerebrosidase deficiency
with beta-glucocerebrosidase activity, chitotriosidase, glucosylsphingosine,
organomegaly, cytopenias, bone disease, and ERT/SRT treatment. IEMbase's normal
beta-D-glucosidase row is a differentiating clue, not a reason to map AMRF to
Gaucher disease.

`Progressive_Myoclonus_Epilepsy.yaml` mentions SCARB2 among rarer PME genes,
but it is not a dedicated SCARB2/AMRF target and does not cover the renal
failure syndrome as a standalone disease.

## Concordance and completeness

Judgement: true missing SCARB2/AMRF target.

The local PME umbrella provides weak context for action myoclonus and
myoclonic seizures. It is not sufficient for canonical mapping because the
IEMbase record is a SCARB2 lysosomal-membrane disease with renal failure and
polyneuropathy. Gaucher disease should be rejected despite lysosomal and
glucocerebrosidase-adjacent terminology.

## Curation actions

- Do not map this record to Gaucher disease.
- Add a standalone SCARB2/action myoclonus-renal failure syndrome target if the
  disease is prioritized.
- Preserve normal beta-D-glucosidase as a differential diagnostic detail rather
  than modeling it as Gaucher-like enzyme deficiency.
