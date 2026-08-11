# IEMbase 0748: ACSL4-related long-chain fatty acid-CoA ligase 4 deficiency

## Scope

| Field | Value |
|---|---|
| IEMbase ID | 748 |
| Nosology | 14.1.01.02 |
| Nosology code | IEM0655 |
| Gene | ACSL4 |
| External IDs | OMIM:300387; ORPHA:86818 |
| Generated mapping | UNMAPPED; weak candidate `VLCAD_Deficiency.yaml` |
| Candidate DisMech targets | None exact |
| Review date | 2026-07-07 |

## IEMbase phenotype signal

IEMbase labels this X-linked record as ACSL4-related long-chain fatty
acid-CoA ligase 4 deficiency, with alternate name X-linked mental retardation
63. The cached signal is sparse but specific: decreased enzyme activity in
fibroblasts and white blood cells in adulthood, and characteristic intellectual
disability in adolescent and adult age bands.

## DisMech phenotype coverage

No exact ACSL4 / X-linked intellectual disability 63 entry is present locally.
`Wilsons_Disease.yaml` mentions ACSL4 only as pathway context for ferroptosis;
it is not ACSL4-related disease coverage.

The generated `VLCAD_Deficiency.yaml` candidate is a false positive. VLCAD
deficiency is an ACADVL long-chain fatty acid beta-oxidation disorder with a
different gene, inheritance context, biochemical mechanism, and clinical
presentation.

## Concordance and completeness

Judgement: true local gap.

The IEMbase record is concise and mainly establishes disease identity,
X-linked inheritance, reduced ACSL4 activity, and intellectual disability. That
is enough to distinguish it from fatty acid oxidation disorders such as VLCAD.

## Curation actions

- Add a distinct ACSL4 / X-linked intellectual disability 63 target if this
  disease is brought into DisMech.
- Reject `VLCAD_Deficiency.yaml` as exact or partial identity coverage.
- Preserve the enzyme-activity evidence separately from phenotype assertions.
